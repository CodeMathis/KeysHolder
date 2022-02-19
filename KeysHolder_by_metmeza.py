#setup
import time

try:
    import keyboard
    import mouse
except ModuleNotFoundError:
    print("Please note that you might have a problem with the keyboard and the mouse module",
          "in your version of python, if so, type 7 for help.")   
          
state_loop = "on"
keys_list = []
try:
    with open('data.txt') as f:
        keys_list_from_file = f.readlines()
        keys_list = ast.literal_eval(keys_list_from_file[0])
except:
    keys_list = []
    
possible_keys = ['\t', '\n', '\r', ' ', '!', '"', '#',
        '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
        '/', '0', '1', '2', '3', '4', '5', '6', '7',
        '8', '9', ':', ';', '<', '=', '>', '?', '@', '[',
        '\\', ']', '^', '_', '`',
        'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~\n',
        'return','tab','space','delete','escape',
        'command','shift','capslock','option','control',
        'right shift','right option','right control','function',
        'f17','volume up','volume down','mute','f18',
        'f19','f20','f5','f6','f7','f3','f8',
        'f9','f11','f13','f16','f14','f10','f12',
        'f15','help','home','page up','forward delete',
        'f4','end','f2','page down','f1','left',
        'right','down', 'up',]

possible_click = ['left click','middle click','right click']
real_click = ['left','middle','right']

def print_keys_list(keys_list):
    print("Currently using the keys ",end=": ")
    for key in range(len(keys_list)):
        print("'",keys_list[key],"'",end=" ; ")
    print("\n")



#main loop
while state_loop == "on":
    
    #displayed text
    print("\n---------- Keys Holder by metmeza ----------\n\n",
          "1 - Set up the keys\n",
          "2 - AutoHolder\n",
          "3 - AutoSpammer\n",
          "4 - Save your keys setup\n",
          "5 - Check the keys you've added\n",
          "6 - Erase current or saved keys\n",
          "7 - Help\n",
          "8 - Stop the program\n")
    try:
        user_input = int(input("Enter a number : "))
    except ValueError:
        user_input = 0

    #user choice execution
    if user_input == 1 :
        try:
            number_of_keys = int(input("How many keys do you want to hold ? "))
        except:
            number_of_keys = 69
            
        if type(number_of_keys) == int and number_of_keys < 10 :
            for every_key in range(number_of_keys):
                valid_key_name = False
                while valid_key_name == False:
                    keys_name = input("What is the "+str(every_key+1)+" key you want to be hold : ")
                    if keys_name in keys_list:
                        print("\nPLEASE, do not put the same input twice.")
                        print_keys_list(keys_list)
                    elif keys_name in possible_keys and keys_name not in keys_list: # add good inputs to the main list
                        valid_key_name = True
                        keys_list.append(keys_name)
                    elif keys_name in possible_click and keys_name not in keys_list: # add good inputs to the main list
                        valid_key_name = True
                        keys_list.append(keys_name)
                    else:
                        print("\nWrong name, all the possible keyboard input name are :\n",possible_keys,"\nAnd for the mouse :\n",possible_click)
            print("\nKeys added successfully")
        elif type(number_of_keys) != int or number_of_keys > 10 :
            print("\nPlease use numbers that are under 10 for the good of your device")

    elif user_input == 2 :
        if keys_list != [] :
            stop_and_start_key = input("Which keys you want to use to activate/desactivate holding "+str(keys_list)+" ?\nAnswer : ")
            if stop_and_start_key in possible_keys:
                print("When ready, press",stop_and_start_key,"to start")
                keyboard.wait(stop_and_start_key) #wait until the key is pressed
                print("When finished, press",stop_and_start_key,"to stop")
                time.sleep(0.5) #Wait in case of missclick
                while keyboard.is_pressed(stop_and_start_key) == False: #Hold all the keys until 'stop_and_start_key' is pressed again
                    time.sleep(0.1)
                    for keys in keys_list :
                        if keys in possible_keys:
                            keyboard.press(keys)
                        elif keys in possible_click:
                            mouse.press(button=real_click[possible_click.index(keys)])
                for keys in keys_list : #release all the keys
                    if keys in possible_keys:
                        keyboard.release(keys)
                    elif keys in possible_click:
                        mouse.release(button=real_click[possible_click.index(keys)])
            else:
                print("Wrong name, all the possible input name are :\n",possible_keys,"\n")
        else:
            print("\nPLEASE set up the keys before this.")
            
    elif user_input == 3 :
        if keys_list != [] :
            stop_and_start_key = input("Which keys you want to use to activate/desactivate spamming "+str(keys_list)+" ?\nAnswer : ")
            if stop_and_start_key in possible_keys:
                try:
                    speed_of_the_spam = float(input("At what speed you want to spam ? (max 0.01 = 92 cps)\nAnswer : "))
                except:
                    speed_of_the_spam = 0
                if speed_of_the_spam >= 0.01 and speed_of_the_spam <= 100 :
                    print("When ready, press",stop_and_start_key,"to start")
                    keyboard.wait(stop_and_start_key) #wait until the key is pressed
                    print("When finished, press",stop_and_start_key,"to stop (if the speed is too fast you need to spam)")
                    time.sleep(0.5) #Wait in case of missclick
                    while keyboard.is_pressed(stop_and_start_key) == False: #Hold all the keys until 'stop_and_start_key' is pressed again
                        time.sleep(speed_of_the_spam)
                        for keys in keys_list :
                            if keys in possible_keys:
                                keyboard.press_and_release(keys)
                            elif keys in possible_click:
                                mouse.click(button=real_click[possible_click.index(keys)])
                else:
                    print("\nPlease use numbers that are between 0.01 and 100 for the good of your device")
            else:
                print("\nWrong name, all the possible input name are :\n",possible_keys,"\n")
        else:
            print("\nPLEASE set up the keys before this.")

    elif user_input == 4 :
        if keys_list != []:
            with open('data.txt', 'w') as f:
                f.write(str(keys_list).strip("''"))
            print("\nKeys saved successfully")
        else:
            print("\nPLEASE set up the keys before this.")

    elif user_input == 5 :
        if keys_list == []:
            print("\nNo keys have been added")
        else:
            print_keys_list(keys_list)

    elif user_input == 6 :
        try:
            user_choice_to_erase = int(input("\nDo you want to erase : \n 1- Current keys \n 2- Saved keys \n 3- Both \nAnswer : "))
        except:
            user_choice_to_erase = 69
        if user_choice_to_erase == 1 :
            keys_list = []
            print("\nCurrent keys erased successfully")
        elif user_choice_to_erase == 2 :
            with open('data.txt', 'w') as f:
                pass
            print("\nSaved keys erased successfully")
        elif user_choice_to_erase == 3 :
            keys_list = []
            with open('data.txt', 'w') as f:
                pass
            print("\nSaved and Current keys erased successfully")
        else:
            print("\nPlease use the numbers 1 or 3")

    elif user_input == 7 :
        try:
            what_help = int(input("\nWhat information do you need ?\n 1 - What keys can be used?\n 2 - Why doesn't this work using the .py file?\nAnswer : "))
        except:
            what_help = 69
        if what_help == 1 :
            print("\n-All the possible input names for the keys are :\n",possible_keys,"\nAnd for the mouse :\n",possible_click)
        elif what_help == 2 :
            print("\n-Requirement : PLEASE download the keyboard and mouse modules if you are using the .py file ",
                  "!\nTo download it you need to type in a cmd : 'pip install keyboard' and/or 'pip install mouse'.",
                  "\n-Note : 1) This modules may not work in python updates above or under 3.9.10 that we are using.\n2) If",
                  "you can't download this modules it may be because you haven't pip installed.\n3) The",
                  "'time' and 'ast' modules are normally pre-installed in python.")
        else:
            print("\nPLEASE use numbers between 1 and 2.")
    
    elif user_input == 8 :
        state_loop = "off"

    #if user_input is wrong
    elif user_input > 8 or user_input < 1 :
        print("\nYou need to answer with a number between 1 and 8")
  
        
#© 2022 Metmeza and Universivil, Mozilla Public License 2.0.
