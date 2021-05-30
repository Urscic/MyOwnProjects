import tkinter


"""
WSTĘP
"""

#okienko
root=tkinter.Tk()

#wymiary okna
root.geometry("950x700")

#tekst --> label(x, "x")
root.geometry("950x700")

title=tkinter.Label(root, text="gra")
#wyświetl tekst
title.pack()

#przycisk
def b1podnies():
    print("podniesiesz jak napiszemy")
b1=tkinter.Button(root, text="Podnieś", command=b1podnies)
b1.pack()

def b2upusc():
    print("upuścisz jak napiszemy")
b2=tkinter.Button(root, text="Upuść", command=b2upusc, width=10, bg="red", fg="white")
b2.pack(side=tkinter.RIGHT) #umiejscowienie przycisku
#bg=kolor pzycisku, fg=kolor tekstu

def b3dzialanie(event):
    print("Wcisnąłeś przycisk 3!")
b3=tkinter.Button(root, text="Działanie") #BIND ZAMIAST COMMAND=!!!--> argumen event dla def
#bind ZDARZENIA
b3.bind("<Button-3>", b3dzialanie)#<Button-1>=lewy myszy,<Button-3>=prawy myszy
b3.pack()
b3.place(x=0,y=0)
#żeby okienko było otwarte
def okienko(event):
    print("klikasz w okienko")
root.bind("<Button-3>", okienko) #UAGA, BĘDZIE DZIAŁAĆ DLA INNYCH PRZYCISKÓW
root.mainloop()
"""
OBSŁUGA ZDARZEŃ, BIND I COMMAND
"""
# root=tkinter.Tk()
# root.geometry("950x700")
# title=tkinter.Label(root, text="gra")
# title.pack()
# # inna funkcja dla dla kliknięcia prawym i lewym
# def b1prawy(event):
#     print("prawy")
# def b1lewy(event):
#     print("lewy")
# b1=tkinter.Button(root, text="wielofunkcyjny B1")
# b1.pack()
# b1.bind("<Button-1>", b1lewy)
# b1.bind("<Button-3>", b1prawy)
# root.mainloop()

"""
IKONY I GRAFIKI, CANVAS --> from PIL import Image, ImageTk
Image.open("ścieżka i nazwa.rozszerzenie")
"""
# from PIL import Image, ImageTk
# root=tkinter.Tk()
# root.geometry("950x700")
#
# zdjecie1=Image.open("blok1.png") #musisz nadpisać zdjęcie!!!
# zdjecie1=zdjecie1.resize((100,150), Image.ANTIALIAS) #zmiana rozmiaru
# ikonka=ImageTk.PhotoImage(zdjecie1) #konwertowanie na coś znośćnego dla tk --> nowa nazwa wymagana
# tkinter.Label(root,image=ikonka).pack()
#
# canvas=tkinter.Canvas(root,width=300, height=400, bg="blue")
# canvas.pack()
# canvas.create_image(30,15, anchor=tkinter.NW, image=ikonka)
#
# root.mainloop()
"""
MENU
"""
# import tkinter
# root=tkinter.Tk()
# root.geometry("480x480")
#
# def show():
#     print("Smyraj mnie po brzuszku")
#
# glowneMenu=tkinter.Menu()
# root.config(menu=glowneMenu)
# #potrzebujess zakładek
# fileMenu=tkinter.Menu(glowneMenu) #przekazujesz do głównego
# glowneMenu.add_cascade(label="File", menu=fileMenu) #rozwija się kaskadowo
# fileMenu.add_command(label="New File1")
# fileMenu.add_command(label="New File2")
# fileMenu.add_separator()
# fileMenu.add_command(label="Show me sth", command=show)
#
# editMenu=tkinter.Menu(glowneMenu)
# glowneMenu.add_cascade(label="Edit", menu=editMenu)
# editMenu.add_command(label="Edit file1")
# editMenu.add_command(label="X")
#
# podMenu=tkinter.Menu(editMenu)
# editMenu.add_cascade(label="Z/Y", menu=podMenu)
# podMenu.add_command(label="Z")
#
# root.mainloop()
