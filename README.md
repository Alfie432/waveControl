# WaveControl

WaveControl is a touchless gesture-based interface that allows users to trigger custom keyboard macros and shortcuts using ultrasonic distance sensing. By bridging an Arduino-based hardware layer with a Python-level automation script, WaveControl enables hands-free interaction with various software applications.

---

## System Overview

The system operates via a continuous feedback loop:
1.  **Hardware Layer**: An HC-SR04 Ultrasonic Sensor connected to an Arduino Uno measures the distance of an object (e.g., a hand).
2.  **Communication Layer**: Data is transmitted via Serial (UART) over USB to a host computer.
3.  **Application Layer**: A Python script processes the incoming distance data, applies a debouncing cooldown, and triggers specified hotkeys using the PyAutoGUI library.

---

## Hardware Requirements

* Arduino Uno (or compatible microcontroller)
* HC-SR04 Ultrasonic Sensor
* Jumper Wires

### Wiring Diagram

<Add here>



---

## Installation

### 1. Hardware Setup
Upload the provided `.ino` file to your Arduino using the Arduino IDE or the VS Code Arduino extension.

### 2. Software Setup
Ensure you have Python 3.x installed. It is recommended to use a virtual environment.

```bash
# Activate your virtual environment
source .venv/bin/activate

# Install dependencies
pip install -r software/requirements.txt
