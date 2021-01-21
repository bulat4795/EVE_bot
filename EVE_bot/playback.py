import pyautogui
from time import sleep
import json
import os


#def main():
    
#    initializePyAutoGUI()
#    countdownTimer()
#    playActions('new.json')

def initializePyAutoGUI():
    # Initialized PyAutoGUI
    # https://pyautogui.readthedocs.io/en/latest/introduction.html
    # When fail-safe mode is True, moving the mouse to the upper-left corner will abort your program.
    pyautogui.FAILSAFE = True

def countdownTimer():
    # Countdown timer
    print("Starting", end="", flush=True)
    for i in range(0, 5):
        print(".", end="", flush=True)
        sleep(1)
    print("Go")

def playActions(filename):
    script_dir = os.path.dirname(__file__)
    filepath = os.path.join(script_dir, 'recordings', filename)
    with open(filepath, 'r') as jsonfile:
        
        data = json.load(jsonfile)
        
        for index, action in enumerate(data):
            if action['button'] == 'Key.esc':
                break
            
            if action['type'] == 'keyDown':
                key = convertKey(action['button'])
                pyautogui.keyDown(key)
            elif action['type'] == 'keyUp':
                key = convertKey(action['button'])
                pyautogui.keyUp(key)
            elif action['type'] == 'click':
                pyautogui.click(action['possition'][0], action['possition'][1], duration = 0.25)
            
            try:
                next_action = data[index + 1]
            except IndexError:
                break
            elapsed_time = next_action['time'] - action['time']
            if elapsed_time >= 0:
                sleep(elapsed_time)
            else:
                raise Exception('Unexpected action ordering.')

def convertKey(button):
    
    PYNPUT_SPECIAL_CASE_MAP = {
        'alt_l': 'altleft',
        'alt_r': 'altright',
        'alt_gr': 'altright',
        'caps_lock': 'capslock',
        'ctrl_l': 'ctrlleft',
        'ctrl_r': 'ctrlright',
        'page_down': 'pagedown',
        'page_up': 'pageup',
        'shift_l': 'shiftleft',
        'shift_r': 'shiftright',
        'num_lock': 'numlock',
        'print_screen': 'printscreen',
        'scroll_lock': 'scrolllock',
    }
    
    cleaned_key = button.replace('Key.', '')
    
    if cleaned_key in PYNPUT_SPECIAL_CASE_MAP:
        return PYNPUT_SPECIAL_CASE_MAP[cleaned_key]
    
    return cleaned_key

#if __name__ == '__main__':
#    main()