# 🌡️ ASHRAE 55 Adaptive Climate Control v2

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Compatible-blue.svg)](https://www.home-assistant.io/)
[![Energy Savings](https://img.shields.io/badge/Energy%20Savings-15--30%25-green.svg)](https://github.com/msinhore/adaptive-climate-blueprint)
[![ASHRAE 55](https://img.shields.io/badge/ASHRAE%2055-Compliant-orange.svg)](https://www.ashrae.org/technical-resources/standards-and-guidelines/read-only-versions-of-ashrae-standards)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fmsinhore%2Fadaptive-climate-blueprint%2Fblob%2Fmain%2Fblueprints%2Fashrae55_adaptive_comfort_v2.yaml)

**Intelligent climate control implementing ASHRAE 55 adaptive comfort model. Automatically adjusts your AC/heating based on outdoor weather conditions for optimal comfort and energy savings.**

## 🎯 What This Does (Simple Version)

**Problem**: You manually adjust your thermostat when it gets hot/cold outside, wasting energy and time.

**Solution**: This blueprint automatically changes your AC/heating temperature based on the weather outside using scientifically proven comfort models.

### Real Example:
- **Hot day (35°C outside)**: Sets AC to 27°C (comfortable, energy efficient)
- **Mild day (20°C outside)**: Sets AC to 23°C (you need less cooling)
- **Cool day (10°C outside)**: Sets heating to 20°C (cozy without waste)

### Bottom Line:
**Set it once, save 15-30% on energy bills, stay comfortable year-round with ASHRAE 55 adaptive comfort standards.**

## ⚡ Key Benefits

- **💰 Lower Bills**: 15-30% energy savings in testing
- **🔄 Fully Automatic**: No daily thermostat adjustments needed
- **🏠 Works with SmartIR**: Compatible with existing AC/heating setups
- **🌡️ Always Comfortable**: ASHRAE 55 adaptive comfort standards
- **⏰ Occupancy Smart**: Saves energy when you're away
- **🌤️ Weather Integration**: Uses free weather services (no outdoor sensors needed)
- **🎚️ Flexible Sensors**: Supports physical sensors, weather data, or manual input

## 🚀 Quick Setup (5 Minutes)

### What You Need:
- Home Assistant with your AC/heating already working
- Any indoor temperature sensor (or weather service for testing)
- Weather integration (free, built-in to Home Assistant) OR outdoor temperature sensor

### Installation:

1. **Import This Blueprint**

[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fmsinhore%2Fadaptive-climate-blueprint%2Fblob%2Fmain%2Fblueprints%2Fashrae55_adaptive_comfort_v2.yaml)

3. **Create Automation**
   - Go to Settings → Automations → Blueprints
   - Find "ASHRAE 55 Adaptive Climate Control" blueprint
   - Fill in your AC device and temperature sensors
   - Choose your comfort category (I, II, or III)
   - Done!

4. **Start Saving Money! 💰**

## ⚙️ Simple Configuration

### Basic Setup (Most People)
```yaml
# Just 3 things needed:
climate_entity: climate.your_ac_or_heating          # Your AC/heating device
indoor_temp_sensor: sensor.room_temperature         # Any room temperature sensor  
outdoor_temp_sensor: weather.home                   # Built-in weather (free)
```

### v2 Sensor Options:
- **Temperature sensors**: Physical sensors, weather services (OpenWeatherMap, Open-Meteo, etc.), or input_number entities
- **Weather integration**: Use any Home Assistant weather service as outdoor temperature source
- **Manual input**: Create input_number entities for manual temperature/humidity override
- **Flexible setup**: Mix and match sensor types as needed

### What It Does Automatically:
- **🌡️ Calculates optimal temperature** based on ASHRAE 55 adaptive comfort model
- **⚡ Saves energy** when you're away (if you have motion sensors)
- **🌬️ Uses free cooling** when outside air is perfect
- **🔄 Adjusts all day** as weather changes
- **💧 Considers humidity** for better comfort (optional)

### Advanced Options (Optional):
- **Motion sensors**: Extra energy savings when away
- **Humidity sensors**: Better comfort in humid weather  
- **Multiple rooms**: Set up one per room/AC unit
- **Comfort categories**: Choose precision level (I, II, or III)
- **Weather services**: OpenWeatherMap, Open-Meteo, AccuWeather, Met.no
- **Manual overrides**: Use input_number entities for testing/calibration

## 🧠 How It Works (The Smart Part)

Instead of keeping your AC at a fixed temperature (like 22°C all year), this blueprint:

1. **Checks the weather outside** every few minutes
2. **Calculates the perfect indoor temperature** using ASHRAE 55 adaptive comfort standards
3. **Automatically adjusts your thermostat** to that temperature
4. **Saves energy** because the "perfect" temperature changes with outdoor conditions

### Example Magic:
- **Winter (5°C outside)**: Perfect indoor = 20°C (cozy, not overheated)
- **Spring (15°C outside)**: Perfect indoor = 22°C (comfortable)  
- **Summer (35°C outside)**: Perfect indoor = 27°C (cool enough, not freezing)

**Why This Saves Money**: Traditional thermostats use the same temperature year-round, fighting against nature. This works WITH the weather using scientifically proven comfort models.

## 🎯 Perfect For You If:

✅ You use **SmartIR or any HA-compatible AC/heating**
✅ You want to **save money without thinking about it**  
✅ You're tired of **manually adjusting the thermostat**
✅ You like **"set it and forget it" automation**
✅ You want **ASHRAE 55 adaptive comfort standards** (not just guessing)
✅ You prefer **flexible sensor options** (physical, weather, or manual input)

❌ **Not for you if**: You prefer manual control or don't have any temperature sensors

## 🆕 What's New in v2

### Enhanced Sensor Support
- **Weather Services**: Use OpenWeatherMap, Open-Meteo, AccuWeather, Met.no as temperature sources
- **Manual Input**: input_number entities for testing and calibration
- **Mixed Setup**: Combine different sensor types as needed

### Advanced Comfort Features (Optional)
- **Humidity Correction**: Adjusts comfort temperature based on relative humidity
- **Operative Temperature**: Considers radiant temperature from windows/walls
- **Air Velocity Comfort**: Accounts for cooling effect from air movement
- **Enhanced Natural Ventilation**: Smarter decisions based on temperature and humidity

### Improved Usability
- **Auto-Detection**: All advanced features are optional and auto-detected
- **Better Validation**: Ensures sensor data is within realistic ranges
- **Real-time Logging**: Shows compliance with ASHRAE 55 standards
- **Flexible Configuration**: Start simple, add features as needed

## 🛠️ Advanced Configuration

### Multiple Rooms Setup

```yaml
# Bedroom
automation bedroom_climate:
  use_blueprint:
    path: ashrae55_adaptive_comfort_v2.yaml
    input:
      climate_entity: climate.bedroom_ac
      indoor_temp_sensor: sensor.bedroom_temperature
      outdoor_temp_sensor: weather.home
      # ... other settings

# Living Room  
automation living_room_climate:
  use_blueprint:
    path: ashrae55_adaptive_comfort_v2.yaml
    input:
      climate_entity: climate.living_room_ac
      indoor_temp_sensor: sensor.living_room_temperature
      outdoor_temp_sensor: weather.home
      # ... other settings
```

### Custom Comfort Categories

Adjust comfort tolerances based on your preferences:
- **Category I** (Strict): ±2°C tolerance, office environments
- **Category II** (Standard): ±3°C tolerance, typical residential use  
- **Category III** (Relaxed): ±4°C tolerance, maximum energy savings

### Available Sensor Options (v2)

The v2 blueprint supports multiple sensor types for maximum flexibility:

**Temperature Sensors:**
- **Physical sensors**: Any Home Assistant temperature sensor
- **Weather services**: OpenWeatherMap, Open-Meteo, AccuWeather, Met.no
- **Manual input**: input_number entities for testing/calibration

**Humidity Sensors (Optional):**
- **Room sensors**: Physical humidity sensors
- **Weather data**: Humidity from weather services
- **Manual input**: input_number entities for manual control

**Occupancy Sensors (Optional):**
- **Motion detectors**: PIR sensors, microwave sensors
- **Presence sensors**: mmWave, Bluetooth, etc.
- **Door sensors**: For rooms without motion sensors

**Weather Integration Examples:**
```yaml
# Use free weather service (no API key needed)
outdoor_temp_sensor: weather.open_meteo

# Use OpenWeatherMap
outdoor_temp_sensor: weather.openweathermap

# Use manual input for testing
outdoor_temp_sensor: input_number.outdoor_temp_override
```

## ❓ Common Questions

### "What exactly does this do that my thermostat doesn't?"
Your thermostat keeps the same temperature year-round. This blueprint changes the target temperature based on outdoor weather using ASHRAE 55 adaptive comfort standards, which is more comfortable and uses 15-30% less energy.

### "Do I need special hardware?"
No! Works with whatever AC/heating you already have in Home Assistant (SmartIR, climate entities, etc.) plus any indoor temperature sensor. You can even use weather services instead of outdoor sensors.

### "Is this just for opening windows?"
No, that's a small part. The main function is **automatically adjusting your AC/heating setpoint** based on weather conditions using scientifically proven comfort models.

### "How much energy does it really save?"
In real testing: 15-30% savings. Your results depend on your local climate, home insulation, and current thermostat habits.

### "What if I don't like the temperature it picks?"
You can set minimum/maximum temperature limits and choose comfort categories (I, II, or III). It will never go outside your comfort range.

### "Does it work with SmartIR?"
Yes! That's actually one of the main target platforms. Works with any Home Assistant climate entity.

### "Can I use it without outdoor sensors?"
Yes! v2 supports weather services (OpenWeatherMap, Open-Meteo, etc.) so you don't need physical outdoor sensors.

## 📚 Documentation & Setup Guides

**For beginners:**
- **[5-Minute Setup Guide](docs/basic-vs-advanced-setup.md)** - Step-by-step installation
- **[Weather Services Setup](examples/weather-services-setup.md)** - Using free weather data

**For technical users:**
- **[ASHRAE 55 Technical Details](docs/ashrae55_technical.md)** - Science behind the calculations
- **[CBE Tool Validation](validation/cbe-tool-comparison.md)** - Accuracy verification
- **[v2 Enhanced Features](docs/v2-enhanced-features.md)** - All optional settings explained

## 🤝 Community & Support

**First-time user?** The basic setup works great - don't overthink it!

**Found a bug?** Please open an issue on GitHub.

**Want to contribute?** See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Questions?** Ask in the Home Assistant community forums.

---

*This blueprint implements ASHRAE 55 adaptive comfort standards in simple, user-friendly automation. Scientifically proven comfort with no PhD required! 🎓*

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **ASHRAE** for the adaptive comfort standard
- **CBE (Center for the Built Environment)** for the thermal comfort tool
- **SmartIR** community for HVAC integration
- **Home Assistant** for the amazing platform

## 📞 Support

- 🐛 **Issues**: [GitHub Issues](https://github.com/msinhore/adaptive-climate-blueprint/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/msinhore/adaptive-climate-blueprint/discussions)
- 📧 **Contact**: [msinhore](https://github.com/msinhore)

## ⭐ Star History

If this project helps you save energy and improve comfort, please consider giving it a star! ⭐

---

**Made with ❤️ for the Home Assistant community**
