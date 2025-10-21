from esphome.core import Lambda
from esphome.const import (
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_HUMIDITY,
    DEVICE_CLASS_VOLTAGE,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_VOLUME_FLOW_RATE,
    STATE_CLASS_TOTAL_INCREASING,
    STATE_CLASS_NONE,
    STATE_CLASS_MEASUREMENT,
    UNIT_AMPERE,
    UNIT_CELSIUS,
    UNIT_WATT,
    UNIT_KILOWATT_HOURS,
    UNIT_EMPTY,
    UNIT_PERCENT,
    UNIT_VOLT,
    CONF_ENTITY_CATEGORY,
    CONF_UNIT_OF_MEASUREMENT,
    CONF_DEVICE_CLASS,
    ENTITY_CATEGORY_DIAGNOSTIC,
    ENTITY_CATEGORY_NONE,
    CONF_STATE_CLASS,
    CONF_DELTA,
    CONF_ICON,
    CONF_ACCURACY_DECIMALS,
    CONF_DEFAULTS,
    CONF_FILTERS,
    CONF_LAMBDA,
    CONF_MULTIPLY,
    ICON_COUNTER,
    ICON_EMPTY,    
    ICON_THERMOMETER,
    ICON_FLASH
)
from .const import *

ICON_ALERT = "mdi:alert"
ICON_HUMIDITY = "mdi:water-percent"
ICON_FLOW = "mdi:water-circle"
UNIT_LITRES_PER_MIN = "L/min"

def sensor_defaults(
    unit_of_measurement = UNIT_EMPTY,
    icon = ICON_EMPTY,
    accuracy_decimals = 0,
    device_class = DEVICE_CLASS_EMPTY,
    state_class = STATE_CLASS_NONE,
    entity_category = ENTITY_CATEGORY_NONE,
    filters=[]
):
    return lambda: {
        CONF_UNIT_OF_MEASUREMENT: unit_of_measurement,
        CONF_ICON: icon,
        CONF_ACCURACY_DECIMALS: accuracy_decimals,
        CONF_DEVICE_CLASS: device_class,
        CONF_STATE_CLASS: state_class,
        CONF_ENTITY_CATEGORY: entity_category,
        CONF_FILTERS: filters
    }

def temp_sensor_defaults():
    return sensor_defaults(
        UNIT_CELSIUS, 
        ICON_THERMOMETER, 
        1, 
        DEVICE_CLASS_TEMPERATURE, 
        STATE_CLASS_MEASUREMENT,
        ENTITY_CATEGORY_NONE,
        [{CONF_LAMBDA: Lambda("return (int16_t)x;")}, {CONF_MULTIPLY: 0.1}]        
    )

sensors = {
    0x24FC: {
        NASA_LABEL: "LVAR_NM_OUT_SENSOR_VOLTAGE",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: sensor_defaults(
            unit_of_measurement=UNIT_VOLT,
            icon=ICON_FLASH,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
            state_class=STATE_CLASS_MEASUREMENT        
        )
    },
    0x4038: {
        NASA_LABEL: "ENUM_IN_STATE_HUMIDITY_PERCENT",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: sensor_defaults(
            unit_of_measurement=UNIT_PERCENT,
            icon=ICON_HUMIDITY,
            device_class=DEVICE_CLASS_HUMIDITY,
            state_class=STATE_CLASS_MEASUREMENT
        )
    },
    0x4067: {
        NASA_LABEL: "ENUM_IN_3WAY_VALVE",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: sensor_defaults()
    },
    0x4069: {
        NASA_LABEL: "ENUM_IN_THERMOSTAT1",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: sensor_defaults()
    },
    0x406A: {
        NASA_LABEL: "ENUM_IN_THERMOSTAT2",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: sensor_defaults()
    },
    0x408A: {
        NASA_LABEL: "ENUM_IN_2WAY_VALVE",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: sensor_defaults()
    },
    0x4236: {
        NASA_LABEL: "VAR_IN_TEMP_WATER_IN_F ",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: temp_sensor_defaults()
    },     
    0x4237: {
        NASA_LABEL: "VAR_IN_TEMP_WATER_TANK_F",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: temp_sensor_defaults()
    },
    0x4238: {
        NASA_LABEL: "VAR_IN_TEMP_WATER_OUT_F",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: temp_sensor_defaults()
    },   
    0x4203: {
        NASA_LABEL: "VAR_IN_TEMP_ROOM_F",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: temp_sensor_defaults()
    },
    0x42D4: {
        NASA_LABEL: "VAR_IN_TEMP_ZONE2_F",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: temp_sensor_defaults()
    },
    0x42E9: {
        NASA_LABEL: "VAR_IN_FLOW_SENSOR_CALC",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: sensor_defaults(
            unit_of_measurement=UNIT_LITRES_PER_MIN,
            icon=ICON_FLOW,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLUME_FLOW_RATE,
            state_class=STATE_CLASS_MEASUREMENT,
            filters=[{CONF_MULTIPLY: 0.1}]
        )
    },
    0x4426: {
        NASA_LABEL: "LVAR_IN_4426",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS:sensor_defaults(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_FLASH,
            accuracy_decimals=1, 
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_MEASUREMENT,
            filters=[{CONF_LAMBDA: Lambda("return (int16_t)x;")}] 
        )
    },    
    0x4427: {
        NASA_LABEL: "LVAR_IN_4427",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS:sensor_defaults(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            icon=ICON_COUNTER,
            accuracy_decimals=3, 
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
            filters=[{CONF_MULTIPLY: 0.001}]
        )
    },
    0x8204: {
        NASA_LABEL: "VAR_OUT_SENSOR_AIROUT",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: temp_sensor_defaults()
    },
    0x8217: {
        NASA_LABEL: "VAR_OUT_SENSOR_CT1",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: sensor_defaults(
            unit_of_measurement=UNIT_AMPERE,
            accuracy_decimals=2,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
            filters=[{CONF_MULTIPLY: 0.1}]
        )
    },
    0x8235: {
        NASA_LABEL: "VAR_OUT_ERROR_CODE",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: sensor_defaults(
            accuracy_decimals=0,
            icon=ICON_ALERT,
            entity_category=ENTITY_CATEGORY_DIAGNOSTIC,
            filters=[{CONF_DELTA: 1}]
        )
    },
    0x8413: {
        NASA_LABEL: "LVAR_OUT_CONTROL_WATTMETER_1W_1MIN_SUM",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: sensor_defaults(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_FLASH,
            accuracy_decimals=1, 
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT            
        )        
    },
    0x8414: {
        NASA_LABEL: "LVAR_OUT_CONTROL_WATTMETER_ALL_UNIT_ACCUM",
        NASA_MODE: CONTROLLER_MODE_STATUS,
        CONF_DEFAULTS: sensor_defaults(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            icon=ICON_COUNTER,
            accuracy_decimals=3, 
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
            filters=[{CONF_MULTIPLY: 0.001}]
        )
    }
}
