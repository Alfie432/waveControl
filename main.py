import serial
import pyautogui
import time

# --- CONFIGURATION ---
SERIAL_PORT = '/dev/cu.usbmodem1201' 
BAUD_RATE = 9600

try:
    arduino = serial.Serial(port=SERIAL_PORT, baudrate=BAUD_RATE, timeout=.1)
    time.sleep(2) # Allow time for Serial handshake
    print("Connection established!")
except Exception as e:
    print(f"Connection Error: {e}")
    print("Tip: Make sure the Arduino Serial Monitor is CLOSED.")
    exit()

# --- KEY SETUP ---
print("\n--- WaveControl Setup ---")
print("Enter the shortcut: (Examples: 'command+c', 'space', 'shift+alt+s')")
user_input = input("Enter keys: ").lower().strip()
key_list = user_input.split('+')


threshold = 10 # If the user is 10cm away from sensor, trigger action, can be changed

# --- THE MAIN LOOP ---
print(f"\nSystem Active. Triggering '{user_input}' when hand is close.")

last_trigger = 0
cooldown = 1.5 # Wait 1.5 seconds between triggers to avoid double-firing

try:
    while True:
        line = arduino.readline().decode('ascii').strip()
        
        if line.isdigit():
            distance = int(line)
            now = time.time()
            
            if 0 < distance <= threshold:
                # Make sure 1.5s has passed so the shortcut only runs once
                if (now - last_trigger) > cooldown:
                    print(f"Triggered: {key_list}")
                    
                    try:
                        # Handle both single keys and combinations
                        if len(key_list) > 1:
                            pyautogui.hotkey(*key_list)
                        else:
                            pyautogui.press(key_list[0])
                    except Exception as key_err:
                        print(f"Invalid key combination: {key_err}")
                        
                    last_trigger = now
except KeyboardInterrupt:
    print("\nStopping WaveControl... Goodbye!")
    arduino.close()