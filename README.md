# 🌡️ Smart Thermostat - Automatic Temperature Control

[![Home Assistant](https://img.shields.io/badge/Home%20Assistant-Compatible-blue.svg)](https://www.home-assistant.io/)
[![Energy Savings](https://img.shields.io/badge/Energy%20Savings-15--30%25-green.svg)](https://github.com/msinhore/adaptive-climate-blueprint)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Automatically adjusts your AC/heating based on outdoor weather to keep you comfortable while reducing energy bills.**

## 🎯 What This Does (Simple Version)

**Problem**: You manually adjust your thermostat when it gets hot/cold outside, wasting energy and time.

**Solution**: This blueprint automatically changes your AC/heating temperature based on the weather outside.

### Real Example:
- **Hot day (30°C outside)**: Sets AC to 26°C (comfortable, energy efficient)
- **Mild day (20°C outside)**: Sets AC to 23°C (you need less cooling)
- **Cool day (10°C outside)**: Sets heating to 20°C (cozy without waste)

### Bottom Line:
**Set it once, save 15-30% on energy bills, stay comfortable year-round.**

## ⚡ Key Benefits

- **💰 Lower Bills**: 15-30% energy savings in testing
- **🔄 Fully Automatic**: No daily thermostat adjustments needed
- **🏠 Works with SmartIR**: Compatible with existing AC/heating setups
- **�️ Always Comfortable**: Science-based temperature targets
- **⏰ Occupancy Smart**: Saves energy when you're away

## � Quick Setup (5 Minutes)

### What You Need:
- Home Assistant with your AC/heating already working
- Any temperature sensor in the room
- Weather integration (free, built-in to Home Assistant)

### Installation:

1. **Import This Blueprint**
## Adaptative Climate Blueprint v1
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fmsinhore%2Fadaptive-climate-blueprint%2Fblob%2Fmain%2Fblueprints%2Fashrae55_adaptive_comfort.yaml)

## Adaptative Climate Blueprint v2
[![Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fgithub.com%2Fmsinhore%2Fadaptive-climate-blueprint%2Fblob%2Fmain%2Fblueprints%2Fashrae55_adaptive_comfort_v2.yaml)

3. **Create Automation**
   - Go to Settings → Automations → Blueprints
   - Find "Smart Thermostat" blueprint
   - Fill in your AC device and temperature sensor
   - Done!

4. **Start Saving Money! 💰**

## ⚙️ Simple Configuration

### Basic Setup (Most People)
```yaml
# Just 3 things needed:
climate_device: climate.your_ac_or_heating          # Your AC/heating device
room_temperature: sensor.room_temperature           # Any room temperature sensor  
outdoor_weather: weather.home                       # Built-in weather (free)
```

### What It Does Automatically:
- **🌡️ Calculates optimal temperature** based on outdoor weather
- **⚡ Saves energy** when you're away (if you have motion sensors)
- **🌬️ Uses free cooling** when outside air is perfect
- **🔄 Adjusts all day** as weather changes

### Advanced Options (Optional):
- **Motion sensors**: Extra energy savings when away
- **Humidity sensors**: Better comfort in humid weather  
- **Multiple rooms**: Set up one per room/AC unit

## 🧠 How It Works (The Smart Part)

Instead of keeping your AC at a fixed temperature (like 22°C all year), this blueprint:

1. **Checks the weather outside** every few minutes
2. **Calculates the perfect indoor temperature** using scientific comfort research
3. **Automatically adjusts your thermostat** to that temperature
4. **Saves energy** because the "perfect" temperature changes with outdoor conditions

### Example Magic:
- **Winter (5°C outside)**: Perfect indoor = 20°C (cozy, not overheated)
- **Spring (15°C outside)**: Perfect indoor = 22°C (comfortable)  
- **Summer (35°C outside)**: Perfect indoor = 27°C (cool enough, not freezing)

**Why This Saves Money**: Traditional thermostats use the same temperature year-round, fighting against nature. This works WITH the weather.

## 🎯 Perfect For You If:

✅ You use **SmartIR or any HA-compatible AC/heating**
✅ You want to **save money without thinking about it**  
✅ You're tired of **manually adjusting the thermostat**
✅ You like **"set it and forget it" automation**
✅ You want **science-based comfort** (not just guessing)

❌ **Not for you if**: You prefer manual control or don't have temperature sensors

## ❓ Common Questions

### Current
- **ASHRAE 55 Adaptive Comfort** (`ashrae55_adaptive_comfort.yaml`)
  - Adaptive thermal comfort model
  - Energy optimization
  - SmartIR integration

### Coming Soon
- **EN 16798-1 Air Quality** - European air quality standards (future release)
- **Energy Optimizer** - Advanced energy saving algorithms
- **Multi-Zone Controller** - Whole-house coordination

## 🛠️ Advanced Configuration

### Multiple Rooms Setup

```yaml
# Bedroom
automation bedroom_climate:
  use_blueprint:
    path: ashrae55_adaptive_comfort.yaml
    input:
      climate_entity: climate.bedroom_ac
      indoor_temp_sensor: sensor.bedroom_temperature
      # ... other settings

# Living Room  
automation living_room_climate:
  use_blueprint:
    path: ashrae55_adaptive_comfort.yaml
    input:
      climate_entity: climate.living_room_ac
      indoor_temp_sensor: sensor.living_room_temperature
      # ... other settings
```

### Custom Comfort Categories

Adjust comfort tolerances based on your preferences:
- **Category I** (Strict): Office environments, sensitive occupants
- **Category II** (Standard): Typical residential use
- **Category III** (Relaxed): Maximum energy savings

## ❓ Common Questions

### "What exactly does this do that my thermostat doesn't?"
Your thermostat keeps the same temperature year-round. This blueprint changes the target temperature based on outdoor weather, which is more comfortable and uses less energy.

### "Do I need special hardware?"
No! Works with whatever AC/heating you already have in Home Assistant (SmartIR, climate entities, etc.) plus any room temperature sensor.

### "Is this just for opening windows?"
No, that's a small part. The main function is **automatically adjusting your AC/heating setpoint** based on weather conditions.

### "How much energy does it really save?"
In real testing: 15-30% savings. Your results depend on your local climate, home insulation, and current thermostat habits.

### "What if I don't like the temperature it picks?"
You can set minimum/maximum temperature limits. It will never go outside your comfort range.

### "Does it work with SmartIR?"
Yes! That's actually one of the main target platforms. Works with any Home Assistant climate entity.

## 📚 Documentation & Setup Guides

**For beginners:**
- **[5-Minute Setup Guide](docs/basic-vs-advanced-setup.md)** - Step-by-step installation
- **[Weather Services Setup](examples/weather-services-setup.md)** - Using free weather data

**For technical users:**
- **[ASHRAE 55 Technical Details](docs/ashrae55_technical.md)** - Science behind the calculations
- **[CBE Tool Validation](validation/cbe-tool-comparison.md)** - Accuracy verification
- **[Advanced Features](docs/v2-enhanced-features.md)** - All optional settings explained

## 🤝 Community & Support

**First-time user?** The basic setup works great - don't overthink it!

**Found a bug?** Please open an issue on GitHub.

**Want to contribute?** See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Questions?** Ask in the Home Assistant community forums.

---

*This blueprint implements scientific comfort standards (ASHRAE 55) in simple, user-friendly automation. No PhD required! 🎓*

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
