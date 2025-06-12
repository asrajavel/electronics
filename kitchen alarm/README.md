# Kitchen Alarm V1

A simple Raspberry Pi Pico-based kitchen timer.

## Features
- 10-minute countdown timer
- TM1637 4-digit display
- Audio alerts with buzzer

## Pin Connections
- Display:
  - CLK: Pin 26
  - DIO: Pin 27
- Buzzer: Pin 15

## Usage
1. Power on the device
2. Timer starts counting down from 10 minutes
3. When timer reaches zero, 'done' is displayed
4. Triple beep sounds every 10 seconds for 10 minutes 