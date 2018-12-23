'''
Authored by dbot_5 12-22-2018 14:00 IST

'''

import stackapps
import oxford_dict 
import wolfram_math 
import wikipedia_engine 
import star_push 
import flippy
from datetime import datetime
from os import system

def initialize():
    system('clear')
    print("Zarvis 0.0.1\n\n")    
    print("Enter the application you want to invoke: \n1. Voice Assistant\n2. Stack Apps Query Engine\n3. Oxford Dictionary Engine\n4. Mathematics Engine\n5. Wikipedia Engine\n6. Star push (Game) \n7. Flippy (Game)\n8. Tic-tac-toe (Game)")
    print ("Enter your choice (integer 1 to 9), Enter q to exit")
    user_input = input(str(datetime.time(datetime.now()))+ '>>')
    return user_input

while True:
    user_input = initialize()
    if user_input == '1':
        system('./sdk-folder/sdk-build/SampleApp/src/SampleApp sdk-folder/sdk-build/Integration/AlexaClientSDKConfig.json')
    elif user_input == '2':
        stackapps.stack_apps_api()
    elif user_input == '3':
        oxford_dict.oxford()
    elif user_input == '4':
        wolfram_math.wolfram_math_api()
    elif user_input == '5':
        wikipedia_engine.wikipedia_api()
    elif user_input == '6':
        star_push.play()
    elif user_input == '7':
        flippy.play()
    elif user_input == '8':
        system('./tictactoe')
    elif user_input == 'q':
        break
    else:
        print("Invalid input, Try again")
    char = input("Press any key to continue!!")    
