# Release Notes - Recent Improvements

## After some feedbacks, I made some adjustments

### 🔧 Recent Updates (June 2025)

**Major Improvements:**

1. **Intelligent HVAC Mode Selection** (commit a2e8989)
   - Fixed issue where all AC units were stuck in auto mode
   - Implemented smart mode selection based on outdoor vs indoor temperature
   - Added natural ventilation opportunities for energy savings
   - Expanded outdoor temperature range to 40°C with ASHRAE 55 compliance

2. **Enhanced Occupancy Sensor Support** (commit b065361)
   - Made occupancy sensor truly optional (no longer required in triggers)
   - Fixed conditional logic for better automation reliability
   - Improved energy saving behavior when rooms are unoccupied

3. **GitHub Workflow Fixes** (commit d937dbb)
   - Updated validation tests to work with Home Assistant blueprint format
   - Fixed file path references from v1 to v2 blueprint
   - Improved security scanning to avoid false positives on documentation
   - Simplified YAML validation for better CI/CD reliability

### 🏠 What This Means for Users:

- **Better Climate Control**: Your air conditioners will now properly switch between heating, cooling, and fan modes based on intelligent temperature analysis
- **Energy Savings**: Enhanced natural ventilation detection and occupancy-aware control
- **More Reliable**: Occupancy sensors are now truly optional and won't cause automation failures
- **Extended Range**: Works correctly even in very hot climates (up to 40°C outdoor temperature)

### 📊 Key Features Now Working:

✅ Adaptive comfort zone calculation (ASHRAE 55 compliant)  
✅ Intelligent HVAC mode selection  
✅ Optional occupancy sensing  
✅ Natural ventilation opportunities  
✅ Extended temperature range support  
✅ Smart state management (prevents unnecessary AC commands)  

### 🔄 Migration Notes:

If you're using the previous version, the new blueprint maintains full backward compatibility. Simply update to `ashrae55_adaptive_comfort_v2.yaml` and your existing configurations will continue to work with the improved logic.

---

*These improvements were made based on user feedback and testing in real-world scenarios. Thank you to the community for helping make this blueprint better!*
