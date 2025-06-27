# Contributing to Adaptive Climate Blueprint

Thank you for your interest in contributing to the Adaptive Climate Blueprint project! 

## 🚀 Getting Started

### Prerequisites
- Home Assistant Core 2023.4+
- Basic understanding of YAML and Home Assistant automations
- Knowledge of ASHRAE 55 standards (helpful but not required)

### Development Environment
1. Fork the repository
2. Clone your fork locally
3. Create a Home Assistant test environment
4. Test your changes thoroughly

## 🛠️ Types of Contributions

### Blueprint Improvements
- Enhanced comfort algorithms
- Better energy optimization
- New sensor integrations
- Performance improvements

### New Blueprints
- EN 16798-1 implementation (future release)
- Multi-zone controllers
- Advanced energy algorithms

### Documentation
- README improvements
- Example configurations
- Troubleshooting guides
- Translation support

### Bug Fixes
- Automation issues
- Template errors
- Compatibility problems

## 📋 Development Guidelines

### Code Standards
- Follow Home Assistant blueprint conventions
- Use clear, descriptive variable names
- Comment complex logic
- Maintain YAML formatting consistency

### Testing Requirements
- Test with multiple climate platforms (SmartIR, Generic Thermostat, etc.)
- Verify with different sensor types
- Test edge cases (sensor unavailable, extreme temperatures)
- Validate energy savings claims

### Documentation Standards
- Update README.md for new features
- Include configuration examples
- Document breaking changes
- Add technical explanations for algorithms

## 🔄 Pull Request Process

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Implement your feature/fix
   - Test thoroughly
   - Update documentation

3. **Commit Guidelines**
   ```bash
   git commit -m "feat: add natural ventilation optimization"
   git commit -m "fix: handle sensor unavailable state"
   git commit -m "docs: update SmartIR integration example"
   ```

4. **Submit Pull Request**
   - Clear description of changes
   - Link to related issues
   - Include testing details
   - Update changelog if needed

## 🧪 Testing Checklist

### Functional Testing
- [ ] Blueprint installs correctly
- [ ] All input parameters work
- [ ] Automation triggers properly
- [ ] Climate entity responds correctly
- [ ] Comfort calculations are accurate
- [ ] Energy saving features work
- [ ] Natural ventilation detection works
- [ ] Occupancy awareness functions

### Compatibility Testing
- [ ] SmartIR integration
- [ ] Generic Thermostat platform
- [ ] Various temperature sensors
- [ ] Different occupancy sensors
- [ ] Multiple Home Assistant versions

### Edge Case Testing
- [ ] Sensor unavailable/unknown states
- [ ] Extreme temperature values
- [ ] Network connectivity issues
- [ ] Rapid temperature changes
- [ ] Clock changes (DST)

## 📊 Performance Guidelines

### Efficiency Targets
- Automation execution time < 1 second
- Memory usage minimal
- CPU impact negligible
- Network requests optimized

### Energy Validation
- Document testing methodology
- Provide before/after data
- Include seasonal variations
- Consider different climate zones

## 🌍 Internationalization

### Temperature Units
- Support both Celsius and Fahrenheit
- Provide conversion utilities
- Test with different unit systems

### Regional Standards
- ASHRAE 55 (North America) - ✅ Implemented
- EN 16798-1 (Europe) - 🔄 Future release
- JIS A 1956 (Japan) - 🔄 Future release
- Other regional standards welcome

## 📞 Getting Help

### Communication Channels
- **Issues**: Technical problems and bug reports
- **Discussions**: Questions and feature requests
- **Pull Requests**: Code contributions
- **Email**: Direct contact for sensitive issues

### Response Times
- Issues: 1-3 business days
- Pull Requests: 3-7 business days
- Discussions: 1-5 business days

## 🏆 Recognition

Contributors will be:
- Listed in README acknowledgments
- Credited in release notes
- Invited to maintainer team (for significant contributions)

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You

Every contribution helps make this project better for the entire Home Assistant community!
