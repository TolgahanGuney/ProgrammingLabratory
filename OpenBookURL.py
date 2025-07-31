import webbrowser

availableBooks = [
    {
        "title": "Medea",
        "author": "Euripides",
        "url": "https://en.wikisource.org/wiki/Tragedies_of_Euripides_(Way)/Medea",
        "quantity": 5
    },
    {
        "title": "Madame Bovary",
        "author": "Gustave Flaubert",
        "url": "https://en.wikisource.org/wiki/Madame_Bovary_(Marx-Aveling_translation)",
        "quantity": 5
    },
    {
        "title": "Les Misérables",
        "author": "Victor Hugo",
        "url": "https://en.wikisource.org/wiki/Les_Mis%C3%A9rables/Volume_1/Book_First/Chapter_1",
        "quantity": 5
    },
    {
        "title": "Notre-Dame de Paris",
        "author": "Victor Hugo",
        "url": "https://en.wikisource.org/wiki/Notre-Dame_de_Paris_(Hapgood)",
        "quantity": 5
    }
]

booksThatCanBeAdded = [
    {
        "title": "The Princess of Cleves",
        "author": "Madame de La Fayette",
        "url": "https://en.wikisource.org/wiki/The_Princess_of_Cleves",
        "quantity": None
    },
    {
        "title": "Antigone",
        "author": "Sophocles",
        "url": "https://en.wikisource.org/wiki/Sophocles,_the_Seven_Plays_in_English_verse/Antigone",
        "quantity": None
    },
    {
        "title": "Socrates",
        "author": "Voltaire",
        "url": "https://en.wikisource.org/wiki/Socrates_(Voltaire)/Dramatis_Person%C3%A6",
        "quantity": None
    }
]



def readBook():
    print("Available books:")
    for index, bookInfo in enumerate(availableBooks):
        print(f"\n{index}. {bookInfo.get("title")} by {bookInfo.get("author")}")
    print(f"\n{index+1}. Return to main page")
    bookChoice = input("\nEnter the index of the book you want to read: ")
    if bookChoice == str(index+1):
        main()
    elif int(bookChoice) in range(index+1):
        for i in range (len(availableBooks)):
            if bookChoice == str(i):
                webbrowser.open(availableBooks[i].get("url"))
                print("you have been redirected to book URL")
        userImput = input("Do you want to read a new book?\n\n0. yes\n\n1. return to main menu\n")
        if userImput == "0":
            readBook()
        elif userImput == "1":
            main()
        else:
            raise ValueError("please enter a valid value (either 0 or 1)")
    else:
        raise ValueError("Please input a valid index")

def addBook():
    print("Books that can be added: ")
    for index, bookName in enumerate(booksThatCanBeAdded):
        print(f"\n{index}. {bookName.get("title")} by {bookName.get("author")}")
    print(f"\n{index+1}. Add a new book")
    print(f"\n{index+2}. Return to main page")
    newBook = input("\nEnter the index of the book you want to add: ")
    if newBook == str(index+2):
        main()

    elif int(newBook) in range(index+1):
        addQuantity = input("Enter the quantity of the book you want to add: ")
        booksThatCanBeAdded[index].update({"quantity": int(addQuantity)})

        for i in range(len(availableBooks)):
            if newBook == str(i):
                availableBooks.append(booksThatCanBeAdded[i])
                booksThatCanBeAdded.remove(booksThatCanBeAdded[i])
                print("")
                main()
                break

    elif newBook == str(index + 1):
        newTitle = input("Enter the title of the new book: ")
        for i in range(len(availableBooks)):
            if availableBooks[i].get("title") == newTitle:
                print(f"{newTitle} is already in the list of available books.")
                addBook()
                break
                
        newAuthor = input("Enter the author of the new book: ")
        newUrl = input("Enter the URL of the new book: ")
        newQuantity = input("Enter the quantity of the new book: ")

        for i in range(len(availableBooks)):
            if availableBooks[i].get("title") == newTitle:
                print(f"This URL is already in the list of available books.")
                addBook()
                break

        booksThatCanBeAdded.append({"title": newTitle, "author": newAuthor, "url": newUrl, "quantity": newQuantity})
        print(f"\n{newQuantity} copies of {newTitle} by {newAuthor} have been added to the list.")
        main()
    else:
        print("please inter a valide input")
        addBook()


def removeBook():
    print("Available books:")
    for index, bookInfo in enumerate(availableBooks):
        print(f"\n{index}. {bookInfo.get('title')} by {bookInfo.get('author')}")
    print(f"\n{index+1}. Return ot the main page")
    book = input("\nEnter the index of the book you want to remove: ")
    if book == str(index+1):
        main()
    quantityRemoved = input("Enter the quantity that you want to remove")

    for i in range (len(availableBooks)):
        if book == str(i):
            removedBook = availableBooks[i]
            remainingQuantity = removedBook.get("quantity") - int(quantityRemoved)
            if remainingQuantity == 0:
                availableBooks.remove(removedBook)
                booksThatCanBeAdded.append(removedBook)
                print(f"{removedBook.get('title')} by {removedBook.get('author')} has been removed entierly from the available books.")
                main()
                break
            elif remainingQuantity > 0:
                removedBook.update({"quantity": remainingQuantity})
                print(f"The quantity of {removedBook.get("title")} is now of {remainingQuantity}")
                main()
                break
            elif remainingQuantity < 0: 
                print("a book's quantity can not hold a negative number, try again")
                removeBook()
                break
def main():
    print("\nWecome to the book managment area!")
    print("Which action do you want to do?\n")
    print("0. Read a book\n")
    print("1. add a book to the available books\n") # You can make this option only available for the admin
    print("2. remove a book from the available books\n") # You can make this option only available for the admin
    choice = input("Please input the index action that you want to do: ")
    if choice == "0":
        readBook()
    elif choice == "1":
        addBook()
    elif choice== "2":
        removeBook()
main()
