# 🧪 Testing & Validation

This directory contains test configurations and validation tools for the Adaptive Climate Blueprint.

## 📁 Test Structure

- `validation_sensors.yaml` - Test sensors for blueprint validation
- `test_scenarios.yaml` - Various test scenarios and edge cases
- `energy_validation.yaml` - Energy savings validation setup
- `comfort_validation.yaml` - Comfort calculations validation

## 🎯 Testing Approach

### Unit Testing
- Individual template calculations
- Comfort zone boundary conditions
- Energy optimization logic

### Integration Testing
- Blueprint automation execution
- SmartIR platform compatibility
- Sensor integration validation

### Performance Testing
- Energy savings measurement
- Comfort satisfaction tracking
- System responsiveness

## 🔧 Test Environment Setup

### Prerequisites
- Home Assistant test instance
- Mock sensors for testing
- SmartIR test device (optional)
- Energy monitoring sensors

### Test Data Sources
- Synthetic temperature data
- Historical weather data
- Occupancy simulation patterns
- Energy usage baselines

## 📊 Validation Metrics

### Comfort Validation
- ASHRAE 55 compliance checking
- Comfort zone accuracy
- Adaptive temperature calculations

### Energy Validation
- Baseline vs optimized consumption
- Peak demand reduction
- HVAC runtime optimization

### Performance Validation
- Automation execution time
- Memory usage monitoring
- Network request optimization

## 🚀 Running Tests

### Manual Testing
1. Install test configuration
2. Configure mock sensors
3. Run through test scenarios
4. Validate results

### Automated Testing
- Use Home Assistant testing framework
- Continuous integration setup
- Regression testing suite

## 📞 Reporting Issues

When testing reveals issues:
1. Document test scenario
2. Include relevant logs
3. Provide configuration details
4. Submit GitHub issue with test results
