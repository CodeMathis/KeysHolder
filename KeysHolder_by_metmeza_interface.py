#import
try:
    import keyboard
    import ast
    import csv
    from tkinter import *
    from tkinter import ttk
    from tkinter import messagebox
    import mouse
except ModuleNotFoundError:
    print("Please note that you might have a problem with the keyboard, mouse and tkinter module",
          "in your version of python, if so, type 7 for help.")

#fenêtre
window = Tk()

#personnalisation
window.title("Morpion")
window.resizable(width = True, height = True)
window.minsize(400,300)
window.iconbitmap("")
window.config(background="#17202A")

#setup  
stop_and_start_key = ""
keys_list = []
current_save = 0
    
possible_keys = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*',
        '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
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
        'f15','help','home','page up',
        'f4','end','f2','page down','f1','left',
        'right','down', 'up','enter','ctrl','alt',
        'ctrl+v','ctrl+c','ctrl+x','ctrl+a']

possible_click = ['left click','middle click','right click']
real_click = ['left','middle','right']

#input keys (1)
def action_listeCombo_keys(event):
    keys_list.append(listeCombo_keys.get())
    keys_list_text.config(state=NORMAL)
    keys_list_text.insert(END, "'"+listeCombo_keys.get()+"' => ")
    keys_list_text.config(state=DISABLED)
listeCombo_keys = ttk.Combobox(window, values=possible_keys, width=12)
listeCombo_keys.bind("<<ComboboxSelected>>", action_listeCombo_keys)
keys_list_text=Text(window, width=30, height=15)
keys_list_text.config(state=DISABLED)

#keys to activate/desactivate
def action_stop_and_start_key(event):
    global stop_and_start_key
    stop_and_start_key = Combobox_stop_and_start_key.get()
Combobox_stop_and_start_key = ttk.Combobox(window, values=possible_keys, width=12)
Combobox_stop_and_start_key.bind("<<ComboboxSelected>>", action_stop_and_start_key)

#keys holder
def holder(stat_holder=True, compteur_holder=(-1)): #-1 important pour première éxecution
    global state, compteur_holder_vrai
    #global et stat important car il peut y avoir plusieurs iterations en meme temps et sa permet de toutes les arreter
    state = stat_holder
    compteur_holder_vrai = compteur_holder
    
    if keys_list != [] and stop_and_start_key != "" and state == True: 
        if compteur_holder_vrai == -1: # s'éxecute qu'une fois au lancement de "holder" pour update l'interface et les opérations a faire une seule fois
            compteur_holder_vrai = 0
            b_hold.config(text = " Stop holder ", command=lambda: holder(False), bg = "#c2c2c2")
            listeCombo_keys.config(state=DISABLED)
            Combobox_stop_and_start_key.config(state=DISABLED)
            b_spam.config(state=DISABLED)
            b_deleter_last.config(state=DISABLED)
            b_deleter_save.config(state=DISABLED)
            b_loader.config(state=DISABLED)
            e_spam.config(state=DISABLED)
            
        
        if keyboard.is_pressed(stop_and_start_key) == True and compteur_holder_vrai == 1:
            for keys in keys_list : #release all the keys
                if keys in possible_keys:
                    keyboard.release(keys)
                elif keys in possible_click:
                    mouse.release(button=real_click[possible_click.index(keys)])
            compteur_holder_vrai = 0
            
        elif keyboard.is_pressed(stop_and_start_key) == True or compteur_holder_vrai == 1:
            if compteur_holder_vrai < 1:
                compteur_holder_vrai += 1
            for keys in keys_list :
                if keys in possible_keys:
                    keyboard.press(keys)
                elif keys in possible_click:
                    mouse.press(button=real_click[possible_click.index(keys)])
                    
        return window.after(100, lambda: holder(state,compteur_holder_vrai))

    elif state == False:
        listeCombo_keys.config(state=NORMAL)
        Combobox_stop_and_start_key.config(state=NORMAL)
        b_spam.config(state=NORMAL)
        b_hold.configure(text=" Start holder ", font= ('Helvetica 20 bold', 15), bg="white", command=lambda: window.after(100, holder))
        b_deleter_last.config(state=NORMAL)
        b_deleter_save.config(state=NORMAL)
        b_loader.config(state=NORMAL)
        e_spam.config(state=NORMAL)
    
    else:
        return messagebox.showerror("INPUT ERROR", "Choose keys to press and the activation key before starting.")     

b_hold = Button(window, text=" Start holder ", font= ('Helvetica 20 bold', 15), bg="white", command=lambda: window.after(100, holder))

#keys spammer
def spammer(delay_between_press, stat_holder=True, compteur_holder=(-1)): #-1 important pour première éxecution
    global state, compteur_holder_vrai
    #global et stat important car il peut y avoir plusieurs iterations en meme temps et sa permet de toutes les arreter
    state = stat_holder
    compteur_holder_vrai = compteur_holder

    try :
        delay_between_press = int(delay_between_press)
        if delay_between_press > 0:
            pass
        else:
            delay_between_press = False
    except:
        delay_between_press = False
        
    if keys_list != [] and stop_and_start_key != "" and state == True and type(delay_between_press) == int: 
        if compteur_holder_vrai == -1: # s'éxecute qu'une fois au lancement de "holder" pour update l'interface et les opérations a faire une seule fois
            compteur_holder_vrai = 0
            b_spam.config(text = "Stop spammer", command=lambda: spammer(False), bg = "#c2c2c2")
            listeCombo_keys.config(state=DISABLED)
            Combobox_stop_and_start_key.config(state=DISABLED)
            b_spam.config(state=DISABLED)
            b_deleter_last.config(state=DISABLED)
            b_deleter_save.config(state=DISABLED)
            b_loader.config(state=DISABLED)
            e_spam.config(state=DISABLED)
            
        
        if keyboard.is_pressed(stop_and_start_key) == True and compteur_holder_vrai == 1:
            for keys in keys_list : #release all the keys
                if keys in possible_keys:
                    keyboard.release(keys)
                elif keys in possible_click:
                    mouse.release(button=real_click[possible_click.index(keys)])
            compteur_holder_vrai = 0
            
        elif keyboard.is_pressed(stop_and_start_key) == True or compteur_holder_vrai == 1:
            if compteur_holder_vrai < 1:
                compteur_holder_vrai += 1
            for keys in keys_list :
                if keys in possible_keys:
                    keyboard.press_and_release(keys)
                elif keys in possible_click:
                    mouse.click(button=real_click[possible_click.index(keys)])
                    
        return window.after(delay_between_press, lambda: spammer(delay_between_press, state, compteur_holder_vrai))

    elif state == False:
        listeCombo_keys.config(state=NORMAL)
        Combobox_stop_and_start_key.config(state=NORMAL)
        b_spam.config(state=NORMAL)
        b_spam.configure(text="Start spammer", font= ('Helvetica 20 bold', 15), bg="white", command=lambda: window.after(100, lambda: spammer(e_spam.get())))
        b_deleter_last.config(state=NORMAL)
        b_deleter_save.config(state=NORMAL)
        b_loader.config(state=NORMAL)
        e_spam.config(state=NORMAL)
    
    else:
        return messagebox.showerror("INPUT ERROR", "Choose keys to press, delay above 0, and the activation key before starting.")
        
b_spam = Button(window, text="Start spammer", font= ('Helvetica 20 bold', 15), bg="white", command=lambda: window.after(100, lambda: spammer(e_spam.get())))
e_spam = Entry(bd =5)
e_how_many_spam = Entry(bd =5)

#keys saver
def save(name_of_save):
    if keys_list != [] and name_of_save != "":
        with open('data.txt', 'a') as f:
            f.writelines(str(str({name_of_save:keys_list}).strip("''")).strip('""'))
            f.writelines("\n")
        name_saved_keys, list_of_save = loader_keys() 
        b_loader.config(values=name_saved_keys)
        e_saver.delete(0, END)
    else:
        return messagebox.showerror("INPUT ERROR", "Choose keys and a file name before saving.")
    
b_saver = Button(window, text=" Save keys ", font= ('Helvetica 20 bold', 15), bg="white", command=lambda: save(e_saver.get()))
e_saver = Entry(bd =5)

#load save
def loader_keys():
    name_saved_keys = []
    list_of_save = []
    with open('data.txt') as f:
        keys_list_from_file = f.readlines()
        for value in keys_list_from_file:
            list_of_save.append(ast.literal_eval(value.strip('""')))
    for i in list_of_save:
        key, value = list(i.items())[0]
        name_saved_keys.append(key)
    return name_saved_keys, list_of_save
    
def action_loader_keys(event):
    global keys_list, keys_list_text, current_save
    name_saved_keys, list_of_save = loader_keys() 
    for i in list_of_save:
        key, value = list(i.items())[0]
        if b_loader.get() == key:
            current_save = i
            keys_list = value

    keys_list_text.config(state=NORMAL)
    keys_list_text.delete("1.0","end")
    keys_list_text.config(state=DISABLED)
    for i in keys_list:
        keys_list_text.config(state=NORMAL)
        keys_list_text.insert(END, "'"+i+"' => ")
        keys_list_text.config(state=DISABLED)

name_saved_keys, list_of_save = loader_keys() 
b_loader = ttk.Combobox(window, values=name_saved_keys, width=12)
b_loader.bind("<<ComboboxSelected>>", action_loader_keys)

#keys deleter
def erase_last_keys():
    global keys_list, keys_list_text
    if keys_list != []:
        keys_list.pop()
        keys_list_text.config(state=NORMAL)
        keys_list_text.delete("1.0","end")
        keys_list_text.config(state=DISABLED)
        for i in keys_list:
            keys_list_text.config(state=NORMAL)
            keys_list_text.insert(END, "'"+i+"' => ")
            keys_list_text.config(state=DISABLED)
        
def erase_save():
    global keys_list, keys_list_text, name_saved_keys, list_of_save
    with open("data.txt", "r") as f:
        lines = f.readlines()
    with open("data.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != str(current_save):
                f.write(line)
    keys_list_text.config(state=NORMAL)
    keys_list_text.delete("1.0","end")
    keys_list_text.config(state=DISABLED)
    keys_list = []
    name_saved_keys, list_of_save = loader_keys() 
    b_loader.config(values=name_saved_keys)
        
b_deleter_last = Button(window, text=" Delete last ", font= ('Helvetica 20 bold', 15), bg="white", command=lambda: erase_last_keys())
b_deleter_save = Button(window, text=" Delete save ", font= ('Helvetica 20 bold', 15), bg="white", command=lambda: erase_save())

#menu help
def help_menu():
    messagebox.showinfo("Information", """1 - Why doesn't this work using the .py file?

-Requirement : PLEASE download the keyboard, mouse and tkinter modules if you are using the .py file!
To download them you need to type in a cmd : 'pip install keyboard' and/or 'pip install mouse' and/or 'pip install tk'.
-Note : 1) This modules may not work in python updates above or under 3.9.13 that we are using.
2) If you can't download this modules it may be because you haven't pip installed.
3) The 'time' and 'ast' modules are normally pre-installed in python.

2 - Is there copyrights?

-© 2022 Metmeza and Universivil, Mozilla Public License 2.0
""")
        
my_menu = Menu(window)
window.config(menu=my_menu)
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Help", command=help_menu)
options_menu.add_command(label="Exit", command=window.destroy)


#affichage
def affichage_tout():
    #inputs
    keys_list_text.pack(side = LEFT, fill=BOTH, expand = TRUE)
    Label(window, text= " Inputs : ", font= ('Helvetica 20 bold', 15), background="#17202A", fg="white").pack(side = TOP, expand = TRUE, pady = 5)
    listeCombo_keys.pack(side = TOP, expand = TRUE, pady = 5)
    sep = ttk.Separator(window,orient='horizontal').pack(fill='x')

    #activation key
    Label(window, text= " Activation key : ", font= ('Helvetica 20 bold', 15), background="#17202A", fg="white").pack(side = TOP, expand = TRUE, pady = 5)
    Combobox_stop_and_start_key.pack(side = TOP, expand = TRUE, pady = 5)
    sep = ttk.Separator(window,orient='horizontal').pack(fill='x')

    #holder
    b_hold.pack(side = TOP, expand = TRUE, pady = 5)
    sep = ttk.Separator(window,orient='horizontal').pack(fill='x')

    #spammer
    spam_value = Label(text="Delay (in ms) :", font= ('Helvetica 20 bold', 15), background="#17202A", fg="white").pack( side = TOP, padx = 5, pady = 5, expand = TRUE)
    e_spam.pack(side = TOP, expand = TRUE, pady = 5)
    spam_value = Label(text="how many press :", font= ('Helvetica 20 bold', 15), background="#17202A", fg="white").pack( side = TOP, padx = 5, expand = TRUE)
    e_how_many_spam.pack(side = TOP, expand = TRUE, pady = 5)
    spam_value = Label(text="(nothing = infinit)", font= ('Helvetica 20 bold', 12), background="#17202A", fg="gray").pack( side = TOP, padx = 5, expand = TRUE)
    b_spam.pack(side = TOP, expand = TRUE, padx = 5, pady = 5)
    sep = ttk.Separator(window,orient='horizontal').pack(fill='x')

    #save keys
    save_name = Label(text="Save name :", font= ('Helvetica 20 bold', 15), background="#17202A", fg="white").pack( side = TOP, padx = 5, pady = 5, expand = TRUE)
    e_saver.pack(side = TOP, expand = TRUE, pady = 5)
    b_saver.pack(side = TOP, expand = TRUE, padx = 5, pady = 5)
    sep = ttk.Separator(window,orient='horizontal').pack(fill='x')

    #load save
    load_save_name = Label(text="Load save :", font= ('Helvetica 20 bold', 15), background="#17202A", fg="white").pack( side = TOP, padx = 5, pady = 5, expand = TRUE)
    b_loader.pack(side = TOP, expand = TRUE, pady = 5)
    sep = ttk.Separator(window,orient='horizontal').pack(fill='x')

    #delete save and last
    b_deleter_last.pack(side = TOP, expand = TRUE, pady = 5)
    b_deleter_save.pack(side = TOP, expand = TRUE, pady = 5)
    sep = ttk.Separator(window,orient='horizontal').pack(fill='x')
    
affichage_tout()  
window.mainloop()


#© 2022 Metmeza and Universivil, Mozilla Public License 2.0.
