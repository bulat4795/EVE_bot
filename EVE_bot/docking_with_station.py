from playback import initializePyAutoGUI, countdownTimer, playActions
from time  import sleep
import pyautogui
import os

def main():
    
    initializePyAutoGUI()
    countdownTimer()
    
    docking_with_station()
    
def get_spaceship_position():
    
    script_dir = os.path.dirname(__file__)
    
    image_path = os.path.join(script_dir, 'screen_images', 'screenshot_1.png')
    screen_analizing_1  = pyautogui.locateOnScreen(image_path, confidence=0.9)
    
    image_path = os.path.join(script_dir, 'screen_images', 'screenshot_2.png')
    screen_analizing_2  = pyautogui.locateOnScreen(image_path, confidence=0.9)
    
    return screen_analizing_1, screen_analizing_2

def docking_with_station():
    
    #Check if the player is at the station every 60 seconds
    #If the player is in space, dock with the nearest station
    #If it is not possible to determine the position of the player three times, the program ends
    repeat_number = 1
    while True:
        spaceship_position = get_spaceship_position()
        if spaceship_position[0]:
            print("Player is on station.")
            repeat_number = 1
            sleep(60)
        elif spaceship_position[1]:
            print("Player is in space. Docking with the nearest station.")
            if spaceship_position[1][1] == 257:
                playActions('select_station_from_list_1.json')
            elif spaceship_position[1][1] == 276:
                playActions('select_station_from_list_2.json')
            elif spaceship_position[1][1] == 295:
                playActions('select_station_from_list_3.json')
            else:
                print("Unable to select station.")
            sleep(3)
            playActions('docking_with_station.json')
            repeat_number = 1
            sleep(60)
        else:
            if repeat_number < 4:
                print("Unable to determine the position of the player.")
                print("Re-determining the position of player number {}.".format(repeat_number))
                repeat_number +=  1
                sleep(20)
            else:
                print("Failed to determine the position of the player.")
                break

if __name__ == '__main__':
    main()