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

### 4. Testing & Debugging

**Check if helper is updating:**
- Go to **Developer Tools** → **States**
- Find your helper entity (e.g., `input_number.adaptive_climate_prev_temp_sala`)
- Value should update every time the automation runs (every 10 minutes or when temperature changes)

**Test detection:**
- **Winter Test**: Open window while heating is on → should detect temperature drop
- **Summer Test**: Open window while cooling is on → should detect temperature rise
- **Check Logs**: Look for these messages in **Settings** → **System** → **Logs**:
  - `"Window/door open detected!"` - Detection triggered
  - `"Updated previous temperature helper"` - Helper state updated
  - `"Adaptive Climate - State Update"` - Debug information

### 5. Troubleshooting

**Detection not working?**
1. ✅ **Helper exists**: Check if `input_number.adaptive_climate_prev_temp_[room]` exists in **Developer Tools** → **States**
2. ✅ **Helper updating**: Value should change every 10 minutes when automation runs
3. ✅ **Blueprint configured**: Helper selected in "Previous Temperature Helper" parameter
4. ✅ **Temperature sensor working**: Current indoor temperature updating correctly
5. ✅ **Threshold appropriate**: Default 2.0°C might be too sensitive or not sensitive enough
6. ✅ **Debug logs**: Look for "Updated previous temperature helper" messages

**Helper not updating?**
- 🔄 **Reload automation**: Settings → Automations → Find your automation → ⋮ → Reload
- 🔄 **Restart Home Assistant**: Sometimes needed after blueprint changes
- 📝 **Check automation trace**: Go to automation → Run actions → View trace

**False positives?**
- 📈 **Increase threshold**: Try 2.5°C or 3.0°C instead of 2.0°C
- ⏱️ **Sensor placement**: Avoid sensors near windows, heat sources, or direct sunlight
- 📊 **Check sensor stability**: Some sensors have natural fluctuations

**Helper value stuck?**
- 🔧 **Manually update**: Developer Tools → Services → `input_number.set_value`
- 📋 **Entity ID**: `input_number.adaptive_climate_prev_temp_[room]`
- � **Value**: Current room temperature

**No detection messages in logs?**
- 🔍 **Enable automation traces**: Settings → Automations → Your automation → Enable tracing
- � **Check conditions**: Temperature change ≥ threshold AND helper configured AND detection enabled
- ⚡ **Manual trigger**: Test automation manually with current conditions

### 6. Understanding the Debug Logs

When the automation runs, you'll see these log messages:

**State Update Log:**
```
Updated previous temperature helper: input_number.adaptive_climate_prev_temp_sala = 22.5°C
(was 22.3°C, change: 0.2°C)
Window detection: ON (threshold: 2.0°C)
```

**What this means:**
- 🌡️ **Current temperature**: 22.5°C (stored for next run)
- 📊 **Previous temperature**: 22.3°C (from last run)
- 📈 **Temperature change**: 0.2°C absolute difference
- ⚙️ **Detection status**: ON with 2.0°C threshold
- ❌ **No detection**: 0.2°C < 2.0°C threshold

**Detection Triggered Log:**
```
Window/door open detected! HVAC paused for 15 minutes.
Temperature change: 2.8°C in 5 minutes.
Indoor: 19.2°C (was 22.0°C), Outdoor: 15.0°C.
```

**What this means:**
- 🚪 **Detection triggered**: Temperature change exceeded threshold
- 📉 **Change amount**: 2.8°C drop (22.0°C → 19.2°C)
- ⏰ **Time frame**: Change detected within window
- ❄️ **Context**: Outdoor cooler (15.0°C) suggests window opening
- ⏸️ **HVAC paused**: For configured duration (15 minutes)

---

💡 **Pro Tip**: Create one helper per room if you have multiple Adaptive Climate automations!
