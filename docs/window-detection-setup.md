# Window/Door Detection Setup Guide

## Quick Setup for Window/Door Detection

### 1. Create Input Number Helper

For window/door detection to work properly, you need to create an `input_number` helper to store the previous temperature:

1. Go to **Settings** → **Devices & Services** → **Helpers**
2. Click **"+ CREATE HELPER"**
3. Select **"Number"**
4. Configure:
   - **Name**: `Adaptive Climate Previous Temperature - [Room Name]`
   - **Entity ID**: `input_number.adaptive_climate_prev_temp_[room]` (e.g., `input_number.adaptive_climate_prev_temp_sala`)
   - **Minimum**: `5`
   - **Maximum**: `40`
   - **Step**: `0.1`
   - **Unit**: `°C`
   - **Icon**: `mdi:thermometer`

### 2. Configure Blueprint

When creating/editing your Adaptive Climate automation:

1. Find **"Previous Temperature Helper (Optional)"** parameter
2. Select the helper you just created
3. Ensure **"Window/Door Open Detection"** is enabled
4. Set appropriate **"Temperature Change Threshold"** (default: 2.0°C)

### 3. How It Works

- 🌡️ **Temperature Tracking**: Helper stores the previous indoor temperature
- 📊 **Change Detection**: Compares current vs previous temperature
- ⚡ **Trigger Logic**: If absolute change ≥ threshold → window/door detected
- ⏸️ **HVAC Pause**: Automatically pauses heating/cooling for configured duration
- 🔄 **Auto Resume**: HVAC resumes after pause period

### 4. Testing

- **Winter Test**: Open window while heating is on → should detect temperature drop
- **Summer Test**: Open window while cooling is on → should detect temperature rise
- **Check Logs**: Look for "Window/door open detected!" messages in Home Assistant logs

### 5. Troubleshooting

**Detection not working?**
- ✅ Ensure helper is created and selected in blueprint
- ✅ Check temperature sensor is updating correctly
- ✅ Verify threshold is appropriate for your environment
- ✅ Look at logbook for detection messages

**False positives?**
- 📈 Increase temperature change threshold (try 2.5°C or 3.0°C)
- ⏱️ Check sensor placement - avoid direct sun/heat sources

**No helper option?**
- 🔧 Create the input_number helper first
- 🔄 Reload blueprint or restart Home Assistant
- 📝 Check helper entity ID matches pattern

---

💡 **Pro Tip**: Create one helper per room if you have multiple Adaptive Climate automations!
