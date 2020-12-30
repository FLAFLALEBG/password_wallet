import string
from random import randint, choice
from tkinter import *

def password_generator():

    def generate_password():
        password_min = 6
        password_max = 12
        all_chars = string.printable

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)


    background = '#BFBFBF'
    window = Tk()
    window.title("Génrateur de mot de passe")
    window.geometry("900x800")
    window.minsize(450, 600)
    window.config(background='#BFBFBF')
    # window.iconbitmap("logo.ico")

    # création de la frame principale
    frame = Frame(window, bg='#BFBFBF')
    
    # ajout image
    #width = 300
    #height = 300
    #image = PhotoImage(file="unknown.gif").zoom(35).subsample(32)
    #canvas = Canvas(frame, width=width, height=height, bg='#BFBFBF', bd=0)
    #canvas.create_image(width/2, height/2, image=image)
    #canvas.grid(row=0)

    # créer une sous boite
    right_frame = Frame(frame, bg=background)

    label_title = Label(right_frame, text="Bienvenue sur le générateur de mot de passe", font=("Arial", 20), bg='#BFBFBF')
    label_title.pack()

    # création d'un champs
    password_entry = Entry(right_frame, font=("Arial", 20), bg='#BFBFBF')
    password_entry.pack()

    # création du boutton -> générateur de mots de passe
    generate_button = Button(window, text="Générer", font=("Arial", 20), bg='#BFBFBF', command=generate_password)
    generate_button.pack(side=BOTTOM, expand=True, fill=X)

    # on place la sous boite à droite de la principale
    right_frame.grid(row=0, column=2, sticky=W)

    # affichage de la frame
    frame.pack(expand=YES)

    # création barre de menu
    menu_bar = Menu(window)
    # création du menu
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Nouveau", command=generate_password())
    file_menu.add_command(label="Quitter", command=window.quit)
    menu_bar.add_cascade(label="Fichier ", menu=file_menu)
    # ajout de la bar sur la fenetre "window"
    window.config(menu=menu_bar)
    
    # affichage de la fenetre
    window.mainloop()