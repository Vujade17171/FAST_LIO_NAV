#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to nav2_msgs__msg__CollisionMonitorState
/// Action type for robot in Collision Monitor

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CollisionMonitorState {

    // This member is not documented.
    #[allow(missing_docs)]
    pub action_type: u8,

    /// Name of triggered polygon
    pub polygon_name: std::string::String,

}

impl CollisionMonitorState {
    /// No action
    pub const DO_NOTHING: u8 = 0;

    /// Stop the robot
    pub const STOP: u8 = 1;

    /// Slowdown in percentage from current operating speed
    pub const SLOWDOWN: u8 = 2;

    /// Keep constant time interval before collision
    pub const APPROACH: u8 = 3;

    /// Sets a limit of velocities if pts in range
    pub const LIMIT: u8 = 4;

}


impl Default for CollisionMonitorState {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::CollisionMonitorState::default())
  }
}

impl rosidl_runtime_rs::Message for CollisionMonitorState {
  type RmwMsg = super::msg::rmw::CollisionMonitorState;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        action_type: msg.action_type,
        polygon_name: msg.polygon_name.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      action_type: msg.action_type,
        polygon_name: msg.polygon_name.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      action_type: msg.action_type,
      polygon_name: msg.polygon_name.to_string(),
    }
  }
}


// Corresponds to nav2_msgs__msg__CollisionDetectorState
/// Name of configured polygons

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CollisionDetectorState {

    // This member is not documented.
    #[allow(missing_docs)]
    pub polygons: Vec<std::string::String>,

    /// List of detections for each polygon
    pub detections: Vec<bool>,

}



impl Default for CollisionDetectorState {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::CollisionDetectorState::default())
  }
}

impl rosidl_runtime_rs::Message for CollisionDetectorState {
  type RmwMsg = super::msg::rmw::CollisionDetectorState;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        polygons: msg.polygons
          .into_iter()
          .map(|elem| elem.as_str().into())
          .collect(),
        detections: msg.detections.into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        polygons: msg.polygons
          .iter()
          .map(|elem| elem.as_str().into())
          .collect(),
        detections: msg.detections.as_slice().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      polygons: msg.polygons
          .into_iter()
          .map(|elem| elem.to_string())
          .collect(),
      detections: msg.detections
          .into_iter()
          .collect(),
    }
  }
}


// Corresponds to nav2_msgs__msg__Costmap
/// This represents a 2-D grid map, in which each cell has an associated cost

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Costmap {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,

    /// MetaData for the map
    pub metadata: super::msg::CostmapMetaData,

    /// The cost data, in row-major order, starting with (0,0).
    pub data: Vec<u8>,

}



impl Default for Costmap {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::Costmap::default())
  }
}

impl rosidl_runtime_rs::Message for Costmap {
  type RmwMsg = super::msg::rmw::Costmap;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        metadata: super::msg::CostmapMetaData::into_rmw_message(std::borrow::Cow::Owned(msg.metadata)).into_owned(),
        data: msg.data.into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
        metadata: super::msg::CostmapMetaData::into_rmw_message(std::borrow::Cow::Borrowed(&msg.metadata)).into_owned(),
        data: msg.data.as_slice().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      metadata: super::msg::CostmapMetaData::from_rmw_message(msg.metadata),
      data: msg.data
          .into_iter()
          .collect(),
    }
  }
}


// Corresponds to nav2_msgs__msg__CostmapMetaData
/// This hold basic information about the characteristics of the Costmap

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CostmapMetaData {
    /// The time at which the static map was loaded
    pub map_load_time: builtin_interfaces::msg::Time,

    /// The time of the last update to costmap
    pub update_time: builtin_interfaces::msg::Time,

    /// The corresponding layer name
    pub layer: std::string::String,

    /// The map resolution
    pub resolution: f32,

    /// Number of cells in the horizontal direction
    pub size_x: u32,

    /// Number of cells in the vertical direction
    pub size_y: u32,

    /// The origin of the costmap [m, m, rad].
    /// This is the real-world pose of the cell (0,0) in the map.
    pub origin: geometry_msgs::msg::Pose,

}



impl Default for CostmapMetaData {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::CostmapMetaData::default())
  }
}

impl rosidl_runtime_rs::Message for CostmapMetaData {
  type RmwMsg = super::msg::rmw::CostmapMetaData;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        map_load_time: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Owned(msg.map_load_time)).into_owned(),
        update_time: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Owned(msg.update_time)).into_owned(),
        layer: msg.layer.as_str().into(),
        resolution: msg.resolution,
        size_x: msg.size_x,
        size_y: msg.size_y,
        origin: geometry_msgs::msg::Pose::into_rmw_message(std::borrow::Cow::Owned(msg.origin)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        map_load_time: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Borrowed(&msg.map_load_time)).into_owned(),
        update_time: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Borrowed(&msg.update_time)).into_owned(),
        layer: msg.layer.as_str().into(),
      resolution: msg.resolution,
      size_x: msg.size_x,
      size_y: msg.size_y,
        origin: geometry_msgs::msg::Pose::into_rmw_message(std::borrow::Cow::Borrowed(&msg.origin)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      map_load_time: builtin_interfaces::msg::Time::from_rmw_message(msg.map_load_time),
      update_time: builtin_interfaces::msg::Time::from_rmw_message(msg.update_time),
      layer: msg.layer.to_string(),
      resolution: msg.resolution,
      size_x: msg.size_x,
      size_y: msg.size_y,
      origin: geometry_msgs::msg::Pose::from_rmw_message(msg.origin),
    }
  }
}


// Corresponds to nav2_msgs__msg__CostmapUpdate
/// Update msg for Costmap containing the modified part of Costmap

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CostmapUpdate {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub x: u32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub y: u32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub size_x: u32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub size_y: u32,

    /// The cost data, in row-major order, starting with (x,y) from 0-255 in Costmap format rather than OccupancyGrid 0-100.
    pub data: Vec<u8>,

}



impl Default for CostmapUpdate {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::CostmapUpdate::default())
  }
}

impl rosidl_runtime_rs::Message for CostmapUpdate {
  type RmwMsg = super::msg::rmw::CostmapUpdate;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        x: msg.x,
        y: msg.y,
        size_x: msg.size_x,
        size_y: msg.size_y,
        data: msg.data.into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      x: msg.x,
      y: msg.y,
      size_x: msg.size_x,
      size_y: msg.size_y,
        data: msg.data.as_slice().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      x: msg.x,
      y: msg.y,
      size_x: msg.size_x,
      size_y: msg.size_y,
      data: msg.data
          .into_iter()
          .collect(),
    }
  }
}


// Corresponds to nav2_msgs__msg__CostmapFilterInfo

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CostmapFilterInfo {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,

    /// Type of plugin used (keepout filter, speed limit in m/s, speed limit in percent, etc...)
    /// 0: keepout/lanes filter
    /// 1: speed limit filter in % of maximum speed
    /// 2: speed limit filter in absolute values (m/s)
    pub type_: u8,

    /// Name of filter mask topic
    pub filter_mask_topic: std::string::String,

    /// Multiplier base offset and multiplier coefficient for conversion of OccGrid.
    /// Used to convert OccupancyGrid data values to filter space values.
    /// data -> into some other number space:
    /// space = data * multiplier + base
    pub base: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub multiplier: f32,

}



impl Default for CostmapFilterInfo {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::CostmapFilterInfo::default())
  }
}

impl rosidl_runtime_rs::Message for CostmapFilterInfo {
  type RmwMsg = super::msg::rmw::CostmapFilterInfo;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        type_: msg.type_,
        filter_mask_topic: msg.filter_mask_topic.as_str().into(),
        base: msg.base,
        multiplier: msg.multiplier,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      type_: msg.type_,
        filter_mask_topic: msg.filter_mask_topic.as_str().into(),
      base: msg.base,
      multiplier: msg.multiplier,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      type_: msg.type_,
      filter_mask_topic: msg.filter_mask_topic.to_string(),
      base: msg.base,
      multiplier: msg.multiplier,
    }
  }
}


// Corresponds to nav2_msgs__msg__SpeedLimit

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SpeedLimit {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,

    /// Setting speed limit in percentage if true or in absolute values in false case
    pub percentage: bool,

    /// Maximum allowed speed (in percent of maximum robot speed or in m/s depending
    /// on "percentage" value). When no-limit it is set to 0.0
    pub speed_limit: f64,

}



impl Default for SpeedLimit {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::SpeedLimit::default())
  }
}

impl rosidl_runtime_rs::Message for SpeedLimit {
  type RmwMsg = super::msg::rmw::SpeedLimit;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        percentage: msg.percentage,
        speed_limit: msg.speed_limit,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      percentage: msg.percentage,
      speed_limit: msg.speed_limit,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      percentage: msg.percentage,
      speed_limit: msg.speed_limit,
    }
  }
}


// Corresponds to nav2_msgs__msg__VoxelGrid

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct VoxelGrid {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub data: Vec<u32>,


    // This member is not documented.
    #[allow(missing_docs)]
    pub origin: geometry_msgs::msg::Point32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub resolutions: geometry_msgs::msg::Vector3,


    // This member is not documented.
    #[allow(missing_docs)]
    pub size_x: u32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub size_y: u32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub size_z: u32,

}



impl Default for VoxelGrid {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::VoxelGrid::default())
  }
}

impl rosidl_runtime_rs::Message for VoxelGrid {
  type RmwMsg = super::msg::rmw::VoxelGrid;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        data: msg.data.into(),
        origin: geometry_msgs::msg::Point32::into_rmw_message(std::borrow::Cow::Owned(msg.origin)).into_owned(),
        resolutions: geometry_msgs::msg::Vector3::into_rmw_message(std::borrow::Cow::Owned(msg.resolutions)).into_owned(),
        size_x: msg.size_x,
        size_y: msg.size_y,
        size_z: msg.size_z,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
        data: msg.data.as_slice().into(),
        origin: geometry_msgs::msg::Point32::into_rmw_message(std::borrow::Cow::Borrowed(&msg.origin)).into_owned(),
        resolutions: geometry_msgs::msg::Vector3::into_rmw_message(std::borrow::Cow::Borrowed(&msg.resolutions)).into_owned(),
      size_x: msg.size_x,
      size_y: msg.size_y,
      size_z: msg.size_z,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      data: msg.data
          .into_iter()
          .collect(),
      origin: geometry_msgs::msg::Point32::from_rmw_message(msg.origin),
      resolutions: geometry_msgs::msg::Vector3::from_rmw_message(msg.resolutions),
      size_x: msg.size_x,
      size_y: msg.size_y,
      size_z: msg.size_z,
    }
  }
}


// Corresponds to nav2_msgs__msg__BehaviorTreeStatusChange

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct BehaviorTreeStatusChange {
    /// internal behavior tree event timestamp. Typically this is wall clock time
    pub timestamp: builtin_interfaces::msg::Time,


    // This member is not documented.
    #[allow(missing_docs)]
    pub node_name: std::string::String,

    /// unique ID for this node
    pub uid: u16,

    /// IDLE, RUNNING, SUCCESS or FAILURE
    pub previous_status: std::string::String,

    /// IDLE, RUNNING, SUCCESS or FAILURE
    pub current_status: std::string::String,

}



impl Default for BehaviorTreeStatusChange {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::BehaviorTreeStatusChange::default())
  }
}

impl rosidl_runtime_rs::Message for BehaviorTreeStatusChange {
  type RmwMsg = super::msg::rmw::BehaviorTreeStatusChange;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        timestamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Owned(msg.timestamp)).into_owned(),
        node_name: msg.node_name.as_str().into(),
        uid: msg.uid,
        previous_status: msg.previous_status.as_str().into(),
        current_status: msg.current_status.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        timestamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Borrowed(&msg.timestamp)).into_owned(),
        node_name: msg.node_name.as_str().into(),
      uid: msg.uid,
        previous_status: msg.previous_status.as_str().into(),
        current_status: msg.current_status.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      timestamp: builtin_interfaces::msg::Time::from_rmw_message(msg.timestamp),
      node_name: msg.node_name.to_string(),
      uid: msg.uid,
      previous_status: msg.previous_status.to_string(),
      current_status: msg.current_status.to_string(),
    }
  }
}


// Corresponds to nav2_msgs__msg__BehaviorTreeLog

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct BehaviorTreeLog {
    /// ROS time that this log message was sent.
    pub timestamp: builtin_interfaces::msg::Time,


    // This member is not documented.
    #[allow(missing_docs)]
    pub event_log: Vec<super::msg::BehaviorTreeStatusChange>,

}



impl Default for BehaviorTreeLog {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::BehaviorTreeLog::default())
  }
}

impl rosidl_runtime_rs::Message for BehaviorTreeLog {
  type RmwMsg = super::msg::rmw::BehaviorTreeLog;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        timestamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Owned(msg.timestamp)).into_owned(),
        event_log: msg.event_log
          .into_iter()
          .map(|elem| super::msg::BehaviorTreeStatusChange::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        timestamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Borrowed(&msg.timestamp)).into_owned(),
        event_log: msg.event_log
          .iter()
          .map(|elem| super::msg::BehaviorTreeStatusChange::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      timestamp: builtin_interfaces::msg::Time::from_rmw_message(msg.timestamp),
      event_log: msg.event_log
          .into_iter()
          .map(super::msg::BehaviorTreeStatusChange::from_rmw_message)
          .collect(),
    }
  }
}


// Corresponds to nav2_msgs__msg__CriticsStats
/// Critics statistics message

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CriticsStats {

    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::Time,


    // This member is not documented.
    #[allow(missing_docs)]
    pub critics: Vec<std::string::String>,


    // This member is not documented.
    #[allow(missing_docs)]
    pub changed: Vec<bool>,


    // This member is not documented.
    #[allow(missing_docs)]
    pub costs_sum: Vec<f32>,

}



impl Default for CriticsStats {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::CriticsStats::default())
  }
}

impl rosidl_runtime_rs::Message for CriticsStats {
  type RmwMsg = super::msg::rmw::CriticsStats;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        stamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Owned(msg.stamp)).into_owned(),
        critics: msg.critics
          .into_iter()
          .map(|elem| elem.as_str().into())
          .collect(),
        changed: msg.changed.into(),
        costs_sum: msg.costs_sum.into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        stamp: builtin_interfaces::msg::Time::into_rmw_message(std::borrow::Cow::Borrowed(&msg.stamp)).into_owned(),
        critics: msg.critics
          .iter()
          .map(|elem| elem.as_str().into())
          .collect(),
        changed: msg.changed.as_slice().into(),
        costs_sum: msg.costs_sum.as_slice().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      stamp: builtin_interfaces::msg::Time::from_rmw_message(msg.stamp),
      critics: msg.critics
          .into_iter()
          .map(|elem| elem.to_string())
          .collect(),
      changed: msg.changed
          .into_iter()
          .collect(),
      costs_sum: msg.costs_sum
          .into_iter()
          .collect(),
    }
  }
}


// Corresponds to nav2_msgs__msg__Particle
/// This represents an individual particle with weight produced by a particle filter

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Particle {

    // This member is not documented.
    #[allow(missing_docs)]
    pub pose: geometry_msgs::msg::Pose,


    // This member is not documented.
    #[allow(missing_docs)]
    pub weight: f64,

}



impl Default for Particle {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::Particle::default())
  }
}

impl rosidl_runtime_rs::Message for Particle {
  type RmwMsg = super::msg::rmw::Particle;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        pose: geometry_msgs::msg::Pose::into_rmw_message(std::borrow::Cow::Owned(msg.pose)).into_owned(),
        weight: msg.weight,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        pose: geometry_msgs::msg::Pose::into_rmw_message(std::borrow::Cow::Borrowed(&msg.pose)).into_owned(),
      weight: msg.weight,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      pose: geometry_msgs::msg::Pose::from_rmw_message(msg.pose),
      weight: msg.weight,
    }
  }
}


// Corresponds to nav2_msgs__msg__ParticleCloud
/// This represents a particle cloud containing particle poses and weights

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ParticleCloud {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,

    /// Array of particles in the cloud
    pub particles: Vec<super::msg::Particle>,

}



impl Default for ParticleCloud {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::ParticleCloud::default())
  }
}

impl rosidl_runtime_rs::Message for ParticleCloud {
  type RmwMsg = super::msg::rmw::ParticleCloud;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        particles: msg.particles
          .into_iter()
          .map(|elem| super::msg::Particle::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
        particles: msg.particles
          .iter()
          .map(|elem| super::msg::Particle::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      particles: msg.particles
          .into_iter()
          .map(super::msg::Particle::from_rmw_message)
          .collect(),
    }
  }
}


// Corresponds to nav2_msgs__msg__WaypointStatus
/// Waypoint state for multi-goal navigation or waypoint following

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct WaypointStatus {

    // This member is not documented.
    #[allow(missing_docs)]
    pub waypoint_status: u8,


    // This member is not documented.
    #[allow(missing_docs)]
    pub waypoint_index: u32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub waypoint_pose: geometry_msgs::msg::PoseStamped,


    // This member is not documented.
    #[allow(missing_docs)]
    pub error_code: u16,


    // This member is not documented.
    #[allow(missing_docs)]
    pub error_msg: std::string::String,

}

impl WaypointStatus {
    /// Waypoint is not processed or processing
    pub const PENDING: u8 = 0;

    /// Waypoint is completed
    pub const COMPLETED: u8 = 1;

    /// Waypoint is skipped
    pub const SKIPPED: u8 = 2;

    /// Waypoint is failed
    pub const FAILED: u8 = 3;

}


impl Default for WaypointStatus {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::WaypointStatus::default())
  }
}

impl rosidl_runtime_rs::Message for WaypointStatus {
  type RmwMsg = super::msg::rmw::WaypointStatus;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        waypoint_status: msg.waypoint_status,
        waypoint_index: msg.waypoint_index,
        waypoint_pose: geometry_msgs::msg::PoseStamped::into_rmw_message(std::borrow::Cow::Owned(msg.waypoint_pose)).into_owned(),
        error_code: msg.error_code,
        error_msg: msg.error_msg.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      waypoint_status: msg.waypoint_status,
      waypoint_index: msg.waypoint_index,
        waypoint_pose: geometry_msgs::msg::PoseStamped::into_rmw_message(std::borrow::Cow::Borrowed(&msg.waypoint_pose)).into_owned(),
      error_code: msg.error_code,
        error_msg: msg.error_msg.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      waypoint_status: msg.waypoint_status,
      waypoint_index: msg.waypoint_index,
      waypoint_pose: geometry_msgs::msg::PoseStamped::from_rmw_message(msg.waypoint_pose),
      error_code: msg.error_code,
      error_msg: msg.error_msg.to_string(),
    }
  }
}


// Corresponds to nav2_msgs__msg__Route

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Route {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub route_cost: f32,

    /// ordered set of nodes of the route
    pub nodes: Vec<super::msg::RouteNode>,

    /// ordered set of edges that connect nodes
    pub edges: Vec<super::msg::RouteEdge>,

}



impl Default for Route {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::Route::default())
  }
}

impl rosidl_runtime_rs::Message for Route {
  type RmwMsg = super::msg::rmw::Route;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        route_cost: msg.route_cost,
        nodes: msg.nodes
          .into_iter()
          .map(|elem| super::msg::RouteNode::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
        edges: msg.edges
          .into_iter()
          .map(|elem| super::msg::RouteEdge::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      route_cost: msg.route_cost,
        nodes: msg.nodes
          .iter()
          .map(|elem| super::msg::RouteNode::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
        edges: msg.edges
          .iter()
          .map(|elem| super::msg::RouteEdge::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      route_cost: msg.route_cost,
      nodes: msg.nodes
          .into_iter()
          .map(super::msg::RouteNode::from_rmw_message)
          .collect(),
      edges: msg.edges
          .into_iter()
          .map(super::msg::RouteEdge::from_rmw_message)
          .collect(),
    }
  }
}


// Corresponds to nav2_msgs__msg__RouteNode

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct RouteNode {

    // This member is not documented.
    #[allow(missing_docs)]
    pub nodeid: u16,


    // This member is not documented.
    #[allow(missing_docs)]
    pub position: geometry_msgs::msg::Point,

}



impl Default for RouteNode {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::RouteNode::default())
  }
}

impl rosidl_runtime_rs::Message for RouteNode {
  type RmwMsg = super::msg::rmw::RouteNode;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        nodeid: msg.nodeid,
        position: geometry_msgs::msg::Point::into_rmw_message(std::borrow::Cow::Owned(msg.position)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      nodeid: msg.nodeid,
        position: geometry_msgs::msg::Point::into_rmw_message(std::borrow::Cow::Borrowed(&msg.position)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      nodeid: msg.nodeid,
      position: geometry_msgs::msg::Point::from_rmw_message(msg.position),
    }
  }
}


// Corresponds to nav2_msgs__msg__RouteEdge

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct RouteEdge {

    // This member is not documented.
    #[allow(missing_docs)]
    pub edgeid: u16,


    // This member is not documented.
    #[allow(missing_docs)]
    pub start: geometry_msgs::msg::Point,


    // This member is not documented.
    #[allow(missing_docs)]
    pub end: geometry_msgs::msg::Point,

}



impl Default for RouteEdge {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::RouteEdge::default())
  }
}

impl rosidl_runtime_rs::Message for RouteEdge {
  type RmwMsg = super::msg::rmw::RouteEdge;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        edgeid: msg.edgeid,
        start: geometry_msgs::msg::Point::into_rmw_message(std::borrow::Cow::Owned(msg.start)).into_owned(),
        end: geometry_msgs::msg::Point::into_rmw_message(std::borrow::Cow::Owned(msg.end)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      edgeid: msg.edgeid,
        start: geometry_msgs::msg::Point::into_rmw_message(std::borrow::Cow::Borrowed(&msg.start)).into_owned(),
        end: geometry_msgs::msg::Point::into_rmw_message(std::borrow::Cow::Borrowed(&msg.end)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      edgeid: msg.edgeid,
      start: geometry_msgs::msg::Point::from_rmw_message(msg.start),
      end: geometry_msgs::msg::Point::from_rmw_message(msg.end),
    }
  }
}


// Corresponds to nav2_msgs__msg__EdgeCost
/// Edge cost to use with nav2_msgs/srv/DynamicEdges to adjust route edge costs

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct EdgeCost {

    // This member is not documented.
    #[allow(missing_docs)]
    pub edgeid: u16,


    // This member is not documented.
    #[allow(missing_docs)]
    pub cost: f32,

}



impl Default for EdgeCost {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::EdgeCost::default())
  }
}

impl rosidl_runtime_rs::Message for EdgeCost {
  type RmwMsg = super::msg::rmw::EdgeCost;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        edgeid: msg.edgeid,
        cost: msg.cost,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      edgeid: msg.edgeid,
      cost: msg.cost,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      edgeid: msg.edgeid,
      cost: msg.cost,
    }
  }
}


// Corresponds to nav2_msgs__msg__TrackingFeedback
/// Real-time tracking error for Nav2 controller

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct TrackingFeedback {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,

    /// The sign of the position tracking error indicates which side of the path the robot is on
    /// Positive sign indicates the robot is to the left of the path, negative to the right
    pub position_tracking_error: f32,

    /// The sign of the heading tracking error indicates the angular difference between
    /// the robot's heading and the path.
    /// Positive sign means the robot heading is rotated to the right of the path direction,
    /// negative sign means it is rotated to the left.
    pub heading_tracking_error: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub current_path_index: u32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub robot_pose: geometry_msgs::msg::PoseStamped,


    // This member is not documented.
    #[allow(missing_docs)]
    pub distance_to_goal: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub speed: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub remaining_path_length: f32,

}



impl Default for TrackingFeedback {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::TrackingFeedback::default())
  }
}

impl rosidl_runtime_rs::Message for TrackingFeedback {
  type RmwMsg = super::msg::rmw::TrackingFeedback;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        position_tracking_error: msg.position_tracking_error,
        heading_tracking_error: msg.heading_tracking_error,
        current_path_index: msg.current_path_index,
        robot_pose: geometry_msgs::msg::PoseStamped::into_rmw_message(std::borrow::Cow::Owned(msg.robot_pose)).into_owned(),
        distance_to_goal: msg.distance_to_goal,
        speed: msg.speed,
        remaining_path_length: msg.remaining_path_length,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      position_tracking_error: msg.position_tracking_error,
      heading_tracking_error: msg.heading_tracking_error,
      current_path_index: msg.current_path_index,
        robot_pose: geometry_msgs::msg::PoseStamped::into_rmw_message(std::borrow::Cow::Borrowed(&msg.robot_pose)).into_owned(),
      distance_to_goal: msg.distance_to_goal,
      speed: msg.speed,
      remaining_path_length: msg.remaining_path_length,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      position_tracking_error: msg.position_tracking_error,
      heading_tracking_error: msg.heading_tracking_error,
      current_path_index: msg.current_path_index,
      robot_pose: geometry_msgs::msg::PoseStamped::from_rmw_message(msg.robot_pose),
      distance_to_goal: msg.distance_to_goal,
      speed: msg.speed,
      remaining_path_length: msg.remaining_path_length,
    }
  }
}


// Corresponds to nav2_msgs__msg__PolygonObject

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct PolygonObject {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub uuid: unique_identifier_msgs::msg::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub points: Vec<geometry_msgs::msg::Point32>,


    // This member is not documented.
    #[allow(missing_docs)]
    pub closed: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub value: i8,

}



impl Default for PolygonObject {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::PolygonObject::default())
  }
}

impl rosidl_runtime_rs::Message for PolygonObject {
  type RmwMsg = super::msg::rmw::PolygonObject;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        uuid: unique_identifier_msgs::msg::UUID::into_rmw_message(std::borrow::Cow::Owned(msg.uuid)).into_owned(),
        points: msg.points
          .into_iter()
          .map(|elem| geometry_msgs::msg::Point32::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
        closed: msg.closed,
        value: msg.value,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
        uuid: unique_identifier_msgs::msg::UUID::into_rmw_message(std::borrow::Cow::Borrowed(&msg.uuid)).into_owned(),
        points: msg.points
          .iter()
          .map(|elem| geometry_msgs::msg::Point32::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      closed: msg.closed,
      value: msg.value,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      uuid: unique_identifier_msgs::msg::UUID::from_rmw_message(msg.uuid),
      points: msg.points
          .into_iter()
          .map(geometry_msgs::msg::Point32::from_rmw_message)
          .collect(),
      closed: msg.closed,
      value: msg.value,
    }
  }
}


// Corresponds to nav2_msgs__msg__CircleObject

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct CircleObject {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub uuid: unique_identifier_msgs::msg::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub center: geometry_msgs::msg::Point32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub radius: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub fill: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub value: i8,

}



impl Default for CircleObject {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::CircleObject::default())
  }
}

impl rosidl_runtime_rs::Message for CircleObject {
  type RmwMsg = super::msg::rmw::CircleObject;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        uuid: unique_identifier_msgs::msg::UUID::into_rmw_message(std::borrow::Cow::Owned(msg.uuid)).into_owned(),
        center: geometry_msgs::msg::Point32::into_rmw_message(std::borrow::Cow::Owned(msg.center)).into_owned(),
        radius: msg.radius,
        fill: msg.fill,
        value: msg.value,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
        uuid: unique_identifier_msgs::msg::UUID::into_rmw_message(std::borrow::Cow::Borrowed(&msg.uuid)).into_owned(),
        center: geometry_msgs::msg::Point32::into_rmw_message(std::borrow::Cow::Borrowed(&msg.center)).into_owned(),
      radius: msg.radius,
      fill: msg.fill,
      value: msg.value,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      uuid: unique_identifier_msgs::msg::UUID::from_rmw_message(msg.uuid),
      center: geometry_msgs::msg::Point32::from_rmw_message(msg.center),
      radius: msg.radius,
      fill: msg.fill,
      value: msg.value,
    }
  }
}


// Corresponds to nav2_msgs__msg__ExclusionZoneDescription
/// Description of an exclusion zone for the collision monitor / detector.
/// Used by the AddExclusionZone service to add zones at runtime.

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ExclusionZoneDescription {
    /// Unique name within the source
    pub zone_name: std::string::String,

    /// "polygon" or "circle"
    pub type_: std::string::String,

    /// TF frame the zone is anchored to (empty = base_frame_id)
    pub frame_id: std::string::String,

    /// Polygon vertices in frame_id (ignored for circle)
    pub points: Vec<geometry_msgs::msg::Point32>,

    /// Circle radius in metres (ignored for polygon)
    pub radius: f64,

    /// Lower z-bound in base frame (default: -DBL_MAX)
    pub min_height: f64,

    /// Upper z-bound in base frame (default: +DBL_MAX)
    pub max_height: f64,

    /// Whether zone is active on creation
    pub enabled: bool,

    /// Whether to publish the zone polygon for rviz
    pub visualize: bool,

    /// Extra staleness allowance (seconds)
    pub frame_hold_timeout: f64,

}



impl Default for ExclusionZoneDescription {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::ExclusionZoneDescription::default())
  }
}

impl rosidl_runtime_rs::Message for ExclusionZoneDescription {
  type RmwMsg = super::msg::rmw::ExclusionZoneDescription;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        zone_name: msg.zone_name.as_str().into(),
        type_: msg.type_.as_str().into(),
        frame_id: msg.frame_id.as_str().into(),
        points: msg.points
          .into_iter()
          .map(|elem| geometry_msgs::msg::Point32::into_rmw_message(std::borrow::Cow::Owned(elem)).into_owned())
          .collect(),
        radius: msg.radius,
        min_height: msg.min_height,
        max_height: msg.max_height,
        enabled: msg.enabled,
        visualize: msg.visualize,
        frame_hold_timeout: msg.frame_hold_timeout,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        zone_name: msg.zone_name.as_str().into(),
        type_: msg.type_.as_str().into(),
        frame_id: msg.frame_id.as_str().into(),
        points: msg.points
          .iter()
          .map(|elem| geometry_msgs::msg::Point32::into_rmw_message(std::borrow::Cow::Borrowed(elem)).into_owned())
          .collect(),
      radius: msg.radius,
      min_height: msg.min_height,
      max_height: msg.max_height,
      enabled: msg.enabled,
      visualize: msg.visualize,
      frame_hold_timeout: msg.frame_hold_timeout,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      zone_name: msg.zone_name.to_string(),
      type_: msg.type_.to_string(),
      frame_id: msg.frame_id.to_string(),
      points: msg.points
          .into_iter()
          .map(geometry_msgs::msg::Point32::from_rmw_message)
          .collect(),
      radius: msg.radius,
      min_height: msg.min_height,
      max_height: msg.max_height,
      enabled: msg.enabled,
      visualize: msg.visualize,
      frame_hold_timeout: msg.frame_hold_timeout,
    }
  }
}


