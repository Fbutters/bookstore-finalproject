'''
Bookstore Program
Frances Butters
v2.0
5/6/22
'''

import tkinter as tk
from tkinter import *
from tkinter import ttk
root = Tk()


def select():   #First window, users click whether they are a Child, Teen, or a Adult
    global agelabel
    selectWindow = Toplevel()
    selectWindow.title('Age')
    selectWindow.geometry('400x150')
    
    
    ageLabel = Label(selectWindow, text = 'Please click which Age you are :',
               font=('Times', '18', 'bold')).pack()
    age1 = Button(selectWindow, text="Child", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [childGenre(),selectWindow.destroy()])
    age1.pack()
    
    age2 = Button(selectWindow, text="Teen", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [teenGenre(),selectWindow.destroy()])
    age2.pack()
    
    age3 = Button(selectWindow, text="Adult", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [adultGenre(),selectWindow.destroy()])
    age3.pack()
    
    #After users choose one of the three options, it leads them to the second window

def childGenre():   #Window where the user clicks Child, the user then chooses whether they want Romance, Adventure, or Mystery
    global cdgenrelabel
    childWindow = Toplevel()
    childWindow.title('Child Books')
    childWindow.geometry('400x150')
    
    cdgenreLabel = Label(childWindow, text = 'Please click a Genre :',
               font=('Times', '18', 'bold')).pack()
    #Adventure button for the Child Window  
    child1 = Button(childWindow, text='Adventure', bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [childAdventure(),childWindow.destroy()])
    child1.pack()
    #Romance button for the Child Window
    child2 = Button(childWindow, text='Romance', bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [childRomance(),childWindow.destroy()])
    child2.pack()
    #Mystery button for the Child Window
    child3 = Button(childWindow, text='Mystery', bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [childMystery(),childWindow.destroy()])
    child3.pack()
    
    #After user chooses a Genre, it showcases the list of books and their prices
    
def childAdventure():   #Window where the user clicks which book they want to buy
    global cdaelabel
    AdventureWindow = Toplevel()
    AdventureWindow.title('Child Adventure Books')
    AdventureWindow.geometry('400x150')
    
    cdaeLabel = Label(AdventureWindow, text = 'Please click a Book :',
               font=('Times', '18', 'bold')).pack()
    #First Child Adventure Book title and price
    adventure1 = Button(AdventureWindow, text="Benny's Adventure Team  15.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),AdventureWindow.destroy()])
    adventure1.pack()
    #Second Child Adventure Book title and price
    adventure2 = Button(AdventureWindow, text="Anna and the Golden Comb	 19.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),AdventureWindow.destroy()])
    adventure2.pack()
    #Third Child Adventure Book title and price
    adventure3 = Button(AdventureWindow, text="The Dragon Who Couldn't Fly	24.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),AdventureWindow.destroy()])
    adventure3.pack()
    
    #After user choose a book and its price, it takes them to the end of the website
    
def childRomance():     #Window where the user clicks which book they want to buy
    global cdrelabel
    RomanceWindow = Toplevel()
    RomanceWindow.title('Child Romance Books')
    RomanceWindow.geometry('400x150')
    
    cdreLabel = Label(RomanceWindow, text = 'Please click a Book :',
               font=('Times', '18', 'bold')).pack()
    #First Child Romance Book title and price
    romance1 = Button(RomanceWindow, text="Valentine Confession  15.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),RomanceWindow.destroy()])
    romance1.pack()
    #Second Child Romance Book title and price
    romance2 = Button(RomanceWindow, text="Romantic Letters  19.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),RomanceWindow.destroy()])
    romance2.pack()
    #Third Child Romance Book title and price
    romance3 = Button(RomanceWindow, text="Everlasting Joy  24.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),RomanceWindow.destroy()])
    romance3.pack()
    
    #After user choose a book and its price, it takes them to the end of the website
   
    
def childMystery():     #Window where the user clicks which book they want to buy
    global cdmylabel
    MysteryWindow = Toplevel()
    MysteryWindow.title('Child Mystery Books')
    MysteryWindow.geometry('400x150')
    
    cdmyLabel = Label(MysteryWindow, text = 'Please click a Book :',
               font=('Times', '18', 'bold')).pack()
    #First Child Mystery Book title and price
    mystery1 = Button(MysteryWindow, text="The Missing Backpack  15.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),MysteryWindow.destroy()])
    mystery1.pack()
    #Second Child Mystery Book title and price
    mystery2 = Button(MysteryWindow, text="Dixie's Gone Missing  19.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'), command = lambda: [end(),MysteryWindow.destroy()])
    mystery2.pack()
    #Third Child Mystery Book title and price
    mystery3 = Button(MysteryWindow, text="The Empty Lunchbox  24.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),MysteryWindow.destroy()])
    mystery3.pack()
    
    #After user choose a book and its price, it takes them to the end of the website


def teenGenre():     #Window where the user clicks Teen, the user then chooses whether they want Romance, Adventure, or Mystery
    global tngenrelabel
    teenWindow = Toplevel()
    teenWindow.title('Teen Books')
    teenWindow.geometry('400x150')
    
    tngenreLabel = Label(teenWindow, text = 'Please click a Genre :',
               font=('Times', '18', 'bold')).pack()
       
    teen1 = Button(teenWindow, text='Adventure', bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [teenAdventure(),teenWindow.destroy()])
    teen1.pack()
    
    teen2 = Button(teenWindow, text='Romance', bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [teenRomance(),teenWindow.destroy()])
    teen2.pack()
    
    teen3 = Button(teenWindow, text='Mystery', bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [teenMystery(),teenWindow.destroy()])
    teen3.pack()
    
    #After user chooses a Genre, it showcases the list of books and their prices
    
def teenAdventure():    #Window where the user clicks which book they want to buy
    global tnaelabel
    AdventureWindow = Toplevel()
    AdventureWindow.title('Teen Adventure Books')
    AdventureWindow.geometry('400x150')
    
    tnaeLabel = Label(AdventureWindow, text = 'Please click a Book :',
               font=('Times', '18', 'bold')).pack()
    
    adventure1 = Button(AdventureWindow, text="The Broken Wand  15.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),AdventureWindow.destroy()])
    adventure1.pack()
    
    adventure2 = Button(AdventureWindow, text="Journey to the Jade Pavilion  19.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),AdventureWindow.destroy()])
    adventure2.pack()
    
    adventure3 = Button(AdventureWindow, text="The Vanquished Pixie  24.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),AdventureWindow.destroy()])
    adventure3.pack()
    
    #After user choose a book and its price, it takes them to the end of the website
    
def teenRomance():  #Window where the user clicks which book they want to buy
    global tnrelabel
    RomanceWindow = Toplevel()
    RomanceWindow.title('Teen Romance Books')
    RomanceWindow.geometry('400x150')
    
    tnreLabel = Label(RomanceWindow, text = 'Please click a Book :',
               font=('Times', '18', 'bold')).pack()
    
    romance1 = Button(RomanceWindow, text="Letters to a Vampire Queen  15.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),RomanceWindow.destroy()])
    romance1.pack()
    
    romance2 = Button(RomanceWindow, text="The Widow in Yellow  19.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),RomanceWindow.destroy()])
    romance2.pack()
    
    romance3 = Button(RomanceWindow, text="A Summer to Forget  24.99 ", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),RomanceWindow.destroy()])
    romance3.pack()
    
    #After user choose a book and its price, it takes them to the end of the website
   
    
def teenMystery():  #Window where the user clicks which book they want to buy
    global tnmylabel
    MysteryWindow = Toplevel()
    MysteryWindow.title('Teen Mystery Books')
    MysteryWindow.geometry('400x150')
    
    tnmyLabel = Label(MysteryWindow, text = 'Please click a Book :',
               font=('Times', '18', 'bold')).pack()
    
    mystery1 = Button(MysteryWindow, text="The Empty Wallet  15.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),MysteryWindow.destroy()])
    mystery1.pack()
    
    mystery2 = Button(MysteryWindow, text="Final Curtain Call 19.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),MysteryWindow.destroy()])
    mystery2.pack()
    
    mystery3 = Button(MysteryWindow, text="Dead 24/7  24.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),MysteryWindow.destroy()])
    mystery3.pack()
    
    #After user choose a book and its price, it takes them to the end of the website


def adultGenre():   #Window where the user clicks Adult, the user then chooses whether they want Romance, Adventure, or Mystery
    global atgenrelabel
    adultWindow = Toplevel()
    adultWindow.title('Adult Books')
    adultWindow.geometry('400x150')
    
    atgenreLabel = Label(adultWindow, text = 'Please click a Genre :',
               font=('Times', '18', 'bold')).pack()
       
    adult1 = Button(adultWindow, text='Adventure', bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [adultAdventure(),adultWindow.destroy()])
    adult1.pack()
    
    adult2 = Button(adultWindow, text='Romance', bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [adultRomance(),adultWindow.destroy()])
    adult2.pack()
    
    adult3 = Button(adultWindow, text='Mystery', bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [adultMystery(),adultWindow.destroy()])
    adult3.pack()
    
    #After user chooses a Genre, it showcases the list of books and their prices
    
    
def adultAdventure():   #Window where the user clicks which book they want to buy
    global ataelabel
    AdventureWindow = Toplevel()
    AdventureWindow.title('Adult Adventure Books')
    AdventureWindow.geometry('400x150')
    
    ataeLabel = Label(AdventureWindow, text = 'Please click a Book :',
               font=('Times', '18', 'bold')).pack()
    
    adventure1 = Button(AdventureWindow, text="Tales of a Dead Earl  15.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),AdventureWindow.destroy()])
    adventure1.pack()
    
    adventure2 = Button(AdventureWindow, text="Journey to Pearl Peak 19.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),AdventureWindow.destroy()])
    adventure2.pack()
    
    adventure3 = Button(AdventureWindow, text="Hell Hath No Fury  24.99 ", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),AdventureWindow.destroy()])
    adventure3.pack()
    
     #After user choose a book and its price, it takes them to the end of the website
    
def adultRomance():     #Window where the user clicks which book they want to buy
    global atrelabel
    RomanceWindow = Toplevel()
    RomanceWindow.title('Adult Romance Books')
    RomanceWindow.geometry('400x150')
    
    atreLabel = Label(RomanceWindow, text = 'Please click a Book :',
               font=('Times', '18', 'bold')).pack()
    
    romance1 = Button(RomanceWindow, text="A Snowy Kiss  15.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),RomanceWindow.destroy()])
    romance1.pack()
    
    romance2 = Button(RomanceWindow, text="The Lonely Heart  19.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),RomanceWindow.destroy()])
    romance2.pack()
    
    romance3 = Button(RomanceWindow, text="The Nanny who Vanished  24.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),RomanceWindow.destroy()])
    romance3.pack()
    
    #After user choose a book and its price, it takes them to the end of the website
   
    
def adultMystery():     #Window where the user clicks which book they want to buy
    global atmylabel
    MysteryWindow = Toplevel()
    MysteryWindow.title('Teen Mystery Books')
    MysteryWindow.geometry('400x150')
    
    atmyLabel = Label(MysteryWindow, text = 'Please click a Book :',
               font=('Times', '18', 'bold')).pack()
    
    mystery1 = Button(MysteryWindow, text="The Ballroom Massacre  15.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),MysteryWindow.destroy()])
    mystery1.pack()
    
    mystery2 = Button(MysteryWindow, text="Murder on Pearl Avenue  19.99", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),MysteryWindow.destroy()])
    mystery2.pack()
    
    mystery3 = Button(MysteryWindow, text="The Nanny who Vanished  24.99 ", bg='White', fg='Black',
                              font=('Times', '12', 'bold'),command = lambda: [end(),MysteryWindow.destroy()])
    mystery3.pack()
    
    #After user choose a book and its price, it takes them to the end of the website 
   

def end():  #The last window which thanks you for your purchase
    global endlabel
    endWindow = Toplevel()
    endWindow.title('Thank you for your purchase')
    endWindow.geometry('400x450')
    
    endlabel = Label(endWindow, text = "Thank you for your Purchase!", font=("Times", "18", "bold")).pack()
    
    books=PhotoImage(file="books.png")
    logo=Label(endWindow, image=books).pack()
    
    end = Button(endWindow, text='Exit', bg='White', fg='Black', font=('Times', '12', 'bold'), command = lambda: root.destroy())
    end.pack() #button that ends program
    
    endWindow.mainloop()
    
    

root.title('Bookstore')
root.geometry('500x395')

#the first window 
welcome = Label(root, 
      text='Welcome to the Bookstore',
      font=("Times", "24", "bold")
      ).pack()

books=PhotoImage(file="openbook.png")
logo=Label(root, image=books).pack()

#button that starts program
btn = Button(root, text='Enter', bg='White', fg='Black',
                              font=('Times', '12', 'bold'), command=lambda: [select(), root.withdraw()])
btn.pack()

root.mainloop()
