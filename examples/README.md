# 🏠 SmartIR Integration Examples

This directory contains practical examples of integrating the Adaptive Climate Blueprint with SmartIR and other climate platforms.

## 📁 Example Files

- `smartir_basic.yaml` - Basic SmartIR setup
- `smartir_advanced.yaml` - Advanced multi-room configuration
- `generic_thermostat.yaml` - Generic thermostat integration
- `multi_zone.yaml` - Whole-house coordination
- `energy_optimized.yaml` - Maximum energy savings setup

## 🔧 Basic Setup Process

1. **Install SmartIR** (if using SmartIR devices)
2. **Configure your climate entity**
3. **Set up temperature sensors**
4. **Import the blueprint**
5. **Create automation from blueprint**
6. **Customize settings**

## 📊 Sensor Requirements

### Required Sensors
- **Indoor Temperature**: Room temperature sensor
- **Outdoor Temperature**: Weather station or external sensor

### Optional Sensors
- **Occupancy**: Motion/presence detection
- **Humidity**: For advanced comfort calculations
- **Air Quality**: For ventilation decisions

## ⚙️ Platform Compatibility

### Tested Platforms
- ✅ SmartIR (IR climate devices)
- ✅ Generic Thermostat
- ✅ Climate Template
- ✅ Ecobee
- ✅ Nest
- ✅ Tado

### Sensor Compatibility
- ✅ ESPHome temperature sensors
- ✅ Zigbee temperature sensors (Xiaomi, etc.)
- ✅ Z-Wave temperature sensors
- ✅ Weather integrations (OpenWeatherMap, etc.)
- ✅ Local weather stations

## 🎯 Performance Tips

### Optimization
- Use local sensors when possible
- Set appropriate update intervals
- Consider multiple zones for large homes
- Monitor energy usage for validation

### Troubleshooting
- Check sensor availability
- Verify temperature units (°C/°F)
- Ensure climate entity responds to commands
- Review automation logs

## 📞 Support

If you have questions about these examples or need help with integration, please:
- Check the main README.md
- Search existing GitHub issues
- Create a new discussion for questions
- Report bugs as GitHub issues
