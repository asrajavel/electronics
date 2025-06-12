# Kitchen Alarm with Two Timer Options

## Changes Made
- Added option button support (GPIO 12) for selecting timer duration
- Added 3-second window at start to select between 5 and 10 minute timers
- If button is pressed during selection window: 10-minute timer
- If no button press: 5-minute timer (default)
- Display shows 'SEL' during selection, then selected time, and 'done' at completion
- Removed unnecessary delays for faster operation 