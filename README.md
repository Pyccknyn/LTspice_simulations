# LTspice Simulations Portfolio

A collection of circuit models and analyses performed in LTspice, demonstrating practical skills in schematic capture, simulation setup, and performance optimization.

---

## Table of Contents

- [Overview](#overview)
- [Simulations](#simulations)
  - [Buck Converter Analysis](#buck-converter-analysis)
  - [Operational Amplifier Circuits](#operational-amplifier-circuits)
  - [Comparator Circuits](#comparator-circuits)
- [Skills Demonstrated](#skills-demonstrated)
- [License](#license)
- [Author](#author)

---

## Overview

This repository contains LTspice `.asc` schematics and simulation setups developed for both academic projects and personal experimentation. Each simulation focuses on a different aspect of circuit analysis, from switch-mode power conversion to high-speed analog behavior and digital-like comparator action.

---

## Simulations

### Buck Converter Analysis

- **Objective:** Design and analyze a synchronous buck converter with PWM control.
- **Simulations:**
  - Transient analysis of startup, steady-state switching waveforms, and load-step response
  - `.step` parameter sweeps of duty cycle, inductor value, and load resistance to evaluate output ripple and efficiency

### Operational Amplifier Circuits

- **Objective:** Implement and characterize inverting and non-inverting amplifier topologies.
- **Simulations:**
  - AC Bode plots for active high-pass and low-pass filter variants
  - Transient step response to measure slew rate, settling time, and overshoot
  - Worst case runs with `.step` and `.tran` directives to assess gain tolerance

### Comparator Circuits

- **Objective:** Model a fast comparator with hysteresis (Schmitt trigger) characteristics.
- **Simulations:**
  - Transient analysis of input step transitions to measure propagation delay and switching thresholds
  - Parameter sweep of positive feedback resistor values to tune hysteresis window
  - Behavioral source for programmable reference voltage and noise injection

---

## Skills Demonstrated

- Schematic capture and hierarchical design in LTspice  
- AC, DC, transient, noise, parametric (`.step`), and Monte Carlo simulations  
- Behavioral source (`B`-element) modeling for custom waveform generation  
- Interpretation of time-domain and frequency-domain results  
- Component optimization for performance, stability, and tolerance robustness  
- Technical documentation and result reporting  

---

## License

This project is licensed under the **GNU General Public License v3.0**. See [LICENSE](LICENSE) for details.

---

## Author

**Kacper Łucki**  
