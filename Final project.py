'''
Bookstore Program for
Final Project
'''
from tkinter import* 

def Book_Store(age,genre):
    answer= age,genre
    return answer
    
def main ():
    myEnd = input('Welcome to the Bookstore: Please enter YES to continue or NO to end services: ')
    myEnd.upper()
    while myEnd!= 'NO':
        Age = input('Please enter "Kid", "Teen", or "Adult" for what person you are: ')
        Genre = input('Please enter "Romance", "Mystery", or "Adventure" for what book genre you want: ') 

        if Age == 'Adult':
            if Genre == 'Romance':
                f = open('Adult Romance Books.txt', 'r')
                content = f.read()
                print(content)
                f.close()
            elif Genre == 'Mystery':
                f = open('Adult Mystery Books.txt', 'r')
                content = f.read()
                print(content)
                f.close()
            elif Genre == 'Adventure':
                f = open('Adult Adventure Books.txt', 'r')
                content = f.read()
                print(content)
                f.close()
        elif Age == 'Teen':
            if Genre == 'Romance':
                f = open('Teen Romance Books.txt', 'r')
                content = f.read()
                print(content)
                f.close()
            elif Genre == 'Mystery':
                f = open('Teen Mystery Books.txt', 'r')
                content = f.read()
                print(content)
                f.close()
            elif Genre == 'Adventure':
                f = open('Teen Adventure Books.txt', 'r')
                content = f.read()
                print(content)
                f.close()
        elif Age == 'Kid':
            if Genre == 'Romance':
                f = open('Kid Romance Books.txt', 'r')
                content = f.read()
                print(content)
                f.close()
            elif Genre == 'Mystery':
                f = open('Kid Mystery Books.txt', 'r')
                content = f.read()
                print(content)
                f.close()
            elif Genre == 'Adventure':
                f = open('Kid Adventure Books.txt', 'r')
                content = f.read()
                print(content)
                f.close()
            
        book_choice = input("Enter books title: ")
        book_price = input ("Enter books price: ")
        print ('Thank you for purchasing ' + book_choice + ', your total is ' + book_price )
       
        myEnd = input('Welcome to the Bookstore: YES to continue or NO to end services: ')
        myEnd.upper()

main ()


