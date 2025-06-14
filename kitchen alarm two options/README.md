# Kitchen Alarm with Two Timer Options

## Changes Made
- Added option button support for selecting timer duration
- Added 3-second window at start to select between 5 and 10 minute timers
- If button is pressed during selection window: 10-minute timer
- If no button press: 5-minute timer (default)
- Display shows 'SEL' during selection, then selected time, and 'done' at completion
- Removed unnecessary delays for faster operation 

## Setup using vscode/cursor

1. Install mpremote:
```bash
python3 -m pip install mpremote
```

2. Add mpremote to PATH (needed on macOS):
```bash
# Temporary (for current session only):
export PATH=$PATH:/Users/$USER/Library/Python/3.9/bin
```

3. Copy code to Pico:
```bash
# List files on Pico
mpremote ls

# Copy main.py to Pico
mpremote cp main.py :main.py

# Open REPL
mpremote repl
# To exit REPL: 
# - Press Ctrl+C to interrupt any running program
# - Then press Ctrl+X to exit the REPL
# Note: Ctrl+D will soft reset and run main.py

# Run files
mpremote run "kitchen alarm two options/main.py"  # Run local file
# Note: Program will run continuously until stopped with Ctrl+C - but somehow keeps running on pico
```