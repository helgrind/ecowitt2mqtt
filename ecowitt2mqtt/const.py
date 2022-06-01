"""Define package constants."""
import logging

from ecowitt2mqtt.helpers.typing import UnitSystemType

LOGGER = logging.getLogger(__package__)

# Configuration keys:
CONF_BATTERY_CONFIG = "battery_config"
CONF_CONFIG = "config"
CONF_ENDPOINT = "endpoint"
CONF_HASS_DISCOVERY = "hass_discovery"
CONF_HASS_DISCOVERY_PREFIX = "hass_discovery_prefix"
CONF_HASS_ENTITY_ID_PREFIX = "hass_entity_id_prefix"
CONF_INPUT_UNIT_SYSTEM = "input_unit_system"
CONF_MQTT_BROKER = "mqtt_broker"
CONF_MQTT_PASSWORD = "mqtt_password"
CONF_MQTT_PORT = "mqtt_port"
CONF_MQTT_TOPIC = "mqtt_topic"
CONF_MQTT_USERNAME = "mqtt_username"
CONF_OUTPUT_UNIT_SYSTEM = "output_unit_system"
CONF_PORT = "port"
CONF_RAW_DATA = "raw_data"
CONF_VERBOSE = "verbose"

# Data points (glob):
DATA_POINT_GLOB_BAROM = "barom"
DATA_POINT_GLOB_BATT = "batt"
DATA_POINT_GLOB_BATT_BINARY = "batt_binary"
DATA_POINT_GLOB_GUST = "gust"
DATA_POINT_GLOB_HUMIDITY = "humidity"
DATA_POINT_GLOB_MOISTURE = "moisture"
DATA_POINT_GLOB_RAIN = "rain"
DATA_POINT_GLOB_TEMP = "temp"
DATA_POINT_GLOB_WIND = "wind"

# Data points (specific):
DATA_POINT_CO2 = "co2"
DATA_POINT_DEWPOINT = "dewpoint"
DATA_POINT_FEELSLIKE = "feelslike"
DATA_POINT_HEATINDEX = "heatindex"
DATA_POINT_HUMIDITY = "humidity"
DATA_POINT_LIGHTNING = "lightning"
DATA_POINT_LIGHTNING_NUM = "lightning_num"
DATA_POINT_LIGHTNING_TIME = "lightning_time"
DATA_POINT_PM25 = "pm25"
DATA_POINT_PM25_24H = "pm25_24h"
DATA_POINT_SOLARRADIATION = "solarradiation"
DATA_POINT_SOLARRADIATION_LUX = "solarradiation_lux"
DATA_POINT_SOLARRADIATION_PERCEIVED = "solarradiation_perceived"
DATA_POINT_TEMPF = "tempf"
DATA_POINT_UV = "uv"
DATA_POINT_WINDCHILL = "windchill"
DATA_POINT_WINDDIR = "winddir"
DATA_POINT_WINDSPEEDMPH = "windspeedmph"

# Environment variables:
ENV_BATTERY_CONFIG = "ECOWITT2MQTT_BATTERY_CONFIG"
ENV_CONFIG = "ECOWITT2MQTT_CONFIG"
ENV_ENDPOINT = "ECOWITT2MQTT_ENDPOINT"
ENV_HASS_DISCOVERY = "ECOWITT2MQTT_HASS_DISCOVERY"
ENV_HASS_DISCOVERY_PREFIX = "ECOWITT2MQTT_HASS_DISCOVERY_PREFIX"
ENV_HASS_ENTITY_ID_PREFIX = "ECOWITT2MQTT_HASS_ENTITY_ID_PREFIX"
ENV_INPUT_UNIT_SYSTEM = "ECOWITT2MQTT_INPUT_UNIT_SYSTEM"
ENV_MQTT_BROKER = "ECOWITT2MQTT_MQTT_BROKER"
ENV_MQTT_PASSWORD = "ECOWITT2MQTT_MQTT_PASSWORD"
ENV_MQTT_PORT = "ECOWITT2MQTT_MQTT_PORT"
ENV_MQTT_TOPIC = "ECOWITT2MQTT_MQTT_TOPIC"
ENV_MQTT_USERNAME = "ECOWITT2MQTT_MQTT_USERNAME"
ENV_OUTPUT_UNIT_SYSTEM = "ECOWITT2MQTT_OUTPUT_UNIT_SYSTEM"
ENV_PORT = "ECOWITT2MQTT_PORT"
ENV_RAW_DATA = "ECOWITT2MQTT_RAW_DATA"
ENV_VERBOSE = "ECOWITT2MQTT_VERBOSE"

# Legacy environment variables that will be deprecated at some point:
LEGACY_ENV_ENDPOINT = "ENDPOINT"
LEGACY_ENV_HASS_DISCOVERY = "HASS_DISCOVERY"
LEGACY_ENV_HASS_DISCOVERY_PREFIX = "HASS_DISCOVERY_PREFIX"
LEGACY_ENV_HASS_ENTITY_ID_PREFIX = "HASS_ENTITY_ID_PREFIX"
LEGACY_ENV_INPUT_UNIT_SYSTEM = "INPUT_UNIT_SYSTEM"
LEGACY_ENV_LOG_LEVEL = "LOG_LEVEL"
LEGACY_ENV_MQTT_BROKER = "MQTT_BROKER"
LEGACY_ENV_MQTT_PASSWORD = "MQTT_PASSWORD"
LEGACY_ENV_MQTT_PORT = "MQTT_PORT"
LEGACY_ENV_MQTT_TOPIC = "MQTT_TOPIC"
LEGACY_ENV_MQTT_USERNAME = "MQTT_USERNAME"
LEGACY_ENV_OUTPUT_UNIT_SYSTEM = "OUTPUT_UNIT_SYSTEM"
LEGACY_ENV_PORT = "PORT"
LEGACY_ENV_RAW_DATA = "RAW_DATA"

# Unit systems:
UNIT_SYSTEM_IMPERIAL: UnitSystemType = "imperial"
UNIT_SYSTEM_METRIC: UnitSystemType = "metric"
