import tm1637
import machine
from machine import ADC
from machine import Pin
import time
from utime import sleep, ticks_ms
from machine import PWM

# This needs to be set, for adc 3 to work, for measuring battery.
adcpin = machine.Pin(29, machine.Pin.IN)

# Initialize components
adc = ADC(3)
mydisplay = tm1637.TM1637(clk=Pin(20), dio=Pin(21), brightness=0)
buzzer = Pin(11, Pin.OUT)
option_button = Pin(15, Pin.IN, Pin.PULL_UP)  # Button connected to GPIO 15 with internal pull-up

# Conversion factor for ADC to voltage (multiplied by 2)
conversion_factor = 3.3 / 65535 * 3  # 3.3V / max ADC value (65535) multiplied by 3

def check_button_press():
    """
    Wait for 3 seconds to see if the button is pressed.
    Returns True if button was pressed, False otherwise.
    """
    start_time = ticks_ms()
    while ticks_ms() - start_time < 3000:  # 3 seconds
        if option_button.value() == 0:  # Button is pressed (active low)
            return True
        sleep(0.01)
    return False

def read_average_adc(num_samples=10):
    total = 0
    for _ in range(num_samples):
        total += adc.read_u16()
        sleep(0.01)  # Small delay between samples (10ms)
    return total // num_samples  # Integer division


# Display battery voltage as a percentage
def display_voltage():
    # lithium ion Voltage limits
    V_MIN = 3.2
    V_MAX = 4.2

    raw = read_average_adc(20)  # Read the raw ADC value (0-65535)
    voltage = raw * conversion_factor  # Convert to voltage (0 to 3.3V range)

    # Cap the voltage at the maximum limit of 4.2V
    if voltage > V_MAX:
        voltage = V_MAX

    # Calculate the percentage (scaled between 0 and 100)
    voltage_percentage = (voltage - V_MIN) / (V_MAX - V_MIN) * 100

    # Ensure the voltage is within bounds (0-100%)
    voltage_percentage = max(0, min(100, voltage_percentage))

    print("Battery Voltage: {:.2f} V ({:.0f}%)".format(voltage, voltage_percentage))  # Print voltage and percentage
    mydisplay.number(int(voltage_percentage))  # Show the percentage on display
    
    # Check for button press during voltage display
    start_time = ticks_ms()
    while ticks_ms() - start_time < 3000:  # 3 seconds
        if option_button.value() == 0:  # Button is pressed (active low)
            return True
        sleep(0.01)
    return False

# Count-up timer function
def countup_timer(total_time):  # total_time in seconds
    elapsed_time = 0

    while elapsed_time <= total_time:
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        mydisplay.numbers(minutes, seconds)
        sleep(1)  # Delay for 1 second
        elapsed_time += 1

# Generic buzzer function
def control_buzzer(beep_duration=0.2, beep_interval=0.2, repeat_count=1):
    """
    Control the buzzer with customizable beep duration, interval, and repeat count.

    :param beep_duration: Duration of each beep in seconds.
    :param beep_interval: Interval between beeps in seconds.
    :param repeat_count: Number of beeps to repeat.
    """
    for _ in range(repeat_count):
        buzzer.value(1)  # Turn buzzer on
        sleep(beep_duration)
        buzzer.value(0)  # Turn buzzer off
        sleep(beep_interval)


# Beep functions using the generic buzzer function
def beep_buzzer_short():
    control_buzzer(beep_duration=0.2, beep_interval=0.2, repeat_count=1)


def beep_buzzer_once():
    control_buzzer(beep_duration=0.2, beep_interval=0.2, repeat_count=1)


def beep_buzzer_thrice():
    control_buzzer(beep_duration=0.8, beep_interval=0.4, repeat_count=3)


def beep_buzzer_thrice_every_10_seconds():
    for _ in range(60):  # 60 times = 10 minutes
        beep_buzzer_thrice()
        sleep(10)


def handle_time_selection(use_10_minutes):
    """
    Handle the time selection display and beeping.
    Returns the total time in seconds.
    """
    if use_10_minutes:
        mydisplay.number(10)
        beep_buzzer_short()  # beep for 10 minutes
        sleep(.5)
        return 600  # 10 minutes
    else:
        mydisplay.number(5)
        sleep(.5)
        return 300  # 5 minutes


# Main execution sequence
if __name__ == "__main__":
    mydisplay.show('8888')
    
    beep_buzzer_short()  # Initial beep

    # Check if button was pressed during voltage display
    use_10_minutes = display_voltage()  # Display the battery voltage percentage and handle selection
    
    # Handle time selection and get total time
    total_time = handle_time_selection(use_10_minutes)
    
    countup_timer(total_time)  # Start the countdown timer with selected duration

    beep_buzzer_thrice_every_10_seconds()  # Beep thrice every 10 seconds
