#!/usr/bin/env python3
# ============================================================
# PCD 点云 → 2D 占据栅格地图转换 (坡度感知)
# 输入: FAST-LIO 保存的 PCD 点云地图
# 输出: map.pgm + map.yaml (Nav2 map_server 标准格式)
#
# 原理: 把点云投影到 XY 平面, 每格记录 z 范围;
#       计算坡度(高度突变), 坡度 > max_slope_deg 的格子标为障碍(黑);
#       平地/缓坡标可通行(白), 无数据标未知(灰)。
#
# 用法: python3 pcd_to_map.py input.pcd output_dir [分辨率m] [坡度度]
# ============================================================
import sys
import os
import math
import struct
import numpy as np

def read_pcd(path):
    """读取 PCD (支持 ascii 和 binary) 返回 Nx3 点云数组"""
    with open(path, 'rb') as f:
        header = []
        while True:
            line = f.readline().decode('utf-8', errors='ignore').strip()
            header.append(line)
            if line.startswith('DATA'):
                break
        data_type = header[-1].split()[1]
        fields = []
        for l in header:
            if l.startswith('FIELDS'):
                fields = l.split()[1:]
        # 找到 x y z 的索引
        xi = fields.index('x') if 'x' in fields else 0
        yi = fields.index('y') if 'y' in fields else 1
        zi = fields.index('z') if 'z' in fields else 2
        nfields = len(fields)
        # 读数据
        if data_type == 'ascii':
            data = np.loadtxt(f)
        else:  # binary / binary_compressed
            raw = f.read()
            if data_type == 'binary_compressed':
                import lzf
                raw = lzf.decompress(raw, len(raw)*10)
            # binary: 每点 nfields 个 float32
            arr = np.frombuffer(raw, dtype=np.float32)
            arr = arr.reshape(-1, nfields)
            data = arr
        pts = data[:, [xi, yi, zi]].astype(np.float32)
        return pts

def pcd_to_map(pcd_path, out_dir, resolution=0.1, max_slope_deg=25.0, z_min=-1.0, z_max=2.0):
    """核心转换"""
    os.makedirs(out_dir, exist_ok=True)
    print(f"读取 {pcd_path} ...")
    pts = read_pcd(pcd_path)
    print(f"点云点数: {len(pts)}")

    # 过滤 z 范围(地面附近到车顶高度)
    mask = (pts[:, 2] >= z_min) & (pts[:, 2] <= z_max)
    pts = pts[mask]
    print(f"z 过滤后: {len(pts)} 点")

    # 确定地图范围
    x_min, x_max = pts[:, 0].min(), pts[:, 0].max()
    y_min, y_max = pts[:, 1].min(), pts[:, 1].max()
    print(f"范围: x[{x_min:.1f},{x_max:.1f}] y[{y_min:.1f},{y_max:.1f}]")

    cols = int(math.ceil((x_max - x_min) / resolution))
    rows = int(math.ceil((y_max - y_min) / resolution))
    print(f"地图: {cols}x{rows} 格 @ {resolution}m")

    # 高度图(每格最高z) + 最低z
    z_high = np.full((rows, cols), -np.inf, dtype=np.float32)
    z_low = np.full((rows, cols), np.inf, dtype=np.float32)
    has_data = np.zeros((rows, cols), dtype=bool)

    for x, y, z in pts:
        c = int((x - x_min) / resolution)
        r = int((y - y_min) / resolution)
        if 0 <= c < cols and 0 <= r < rows:
            if z > z_high[r, c]: z_high[r, c] = z
            if z < z_low[r, c]: z_low[r, c] = z
            has_data[r, c] = True

    # 坡度判定: 与 8 邻域的高度差 / 水平距离
    max_slope = math.tan(math.radians(max_slope_deg))
    # 占据栅格: 0=可通行, 100=障碍, -1=未知
    grid = np.full((rows, cols), -1, dtype=np.int8)  # 默认未知

    for r in range(rows):
        for c in range(cols):
            if not has_data[r, c]:
                continue
            # 该格高度范围
            h_range = z_high[r, c] - z_low[r, c]
            # 与邻域最大坡度
            max_s = 0.0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0: continue
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < rows and 0 <= cc < cols and has_data[rr, cc]:
                        dist = math.hypot(dr * resolution, dc * resolution)
                        s = abs(z_high[rr, cc] - z_high[r, c]) / dist
                        if s > max_s: max_s = s
            if max_s > max_slope or h_range > 0.5:
                grid[r, c] = 100   # 陡坡/高障碍 → 占据(黑)
            else:
                grid[r, c] = 0     # 平地/缓坡 → 可通行(白)

    # 写 PGM (0=黑障碍, 254=白可通行, 205=灰未知)
    pgm = np.full((rows, cols), 205, dtype=np.uint8)  # 未知灰
    pgm[grid == 100] = 0    # 障碍黑
    pgm[grid == 0] = 254    # 可通行白

    pgm_path = os.path.join(out_dir, 'map.pgm')
    # PGM 头部 + 数据
    with open(pgm_path, 'wb') as f:
        f.write(f"P5\n{cols} {rows}\n255\n".encode())
        f.write(pgm.tobytes())

    # 写 YAML (Nav2 map_server 格式)
    yaml_path = os.path.join(out_dir, 'map.yaml')
    with open(yaml_path, 'w') as f:
        f.write("image: map.pgm\n")
        f.write("resolution: {}\n".format(resolution))
        f.write(f"origin: [{x_min}, {y_min}, 0.0]\n")
        f.write("negate: 0\n")
        f.write("occupied_thresh: 0.65\n")
        f.write("free_thresh: 0.196\n")

    print(f"✅ 完成!")
    print(f"  {pgm_path}")
    print(f"  {yaml_path}")
    print(f"  地图尺寸: {cols}x{rows}, 分辨率 {resolution}m, 原点 ({x_min:.2f}, {y_min:.2f})")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("用法: python3 pcd_to_map.py input.pcd output_dir [分辨率] [坡度度]")
        sys.exit(1)
    pcd = sys.argv[1]
    out = sys.argv[2]
    res = float(sys.argv[3]) if len(sys.argv) > 3 else 0.1
    slope = float(sys.argv[4]) if len(sys.argv) > 4 else 25.0
    pcd_to_map(pcd, out, res, slope)
