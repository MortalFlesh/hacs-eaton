"""Sensor platform for eaton integration."""

from .const import DEFAULT_NAME, DOMAIN, ICON, SENSOR
from .entity import EatonIntegrationEntity


async def async_setup_entry(hass, entry, async_add_devices):
    """Setup sensor platform."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_devices([EatonIntegrationSensor(coordinator, entry)])


class EatonIntegrationSensor(EatonIntegrationEntity):
    """integration Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def native_value(self):
        """Return the native value of the sensor."""
        return "value:42"

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON
