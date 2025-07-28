class Shelf: 
    def __init__(self ,genre, availableCapacity, shelfID):
        self.__shelfID = shelfID
        self.__genre = genre
        self.__availableCapacity = availableCapacity
        self.__booksInThisShelf = {}
    
    def addBookToShelf(self, title, count):
        if not isinstance(title, str):
            raise Exception("Error: enter the title as string")
        if not isinstance(count, int):
            raise Exception("Error: enter a the count as a int")
        
        if self.__availableCapacity - count >= 0:
            if not title in self.__booksInThisShelf:
                self.__booksInThisShelf.update({title: count})
                self.__availableCapacity -= count
                print(f"{count} of {title} were added to the self {self.__shelfID}")
            else:
                print(f"{title} is already available in the shelf {self.__shelfID}")
        else:
            raise Exception("Insufficient shelf capacity") # should I do a print here instead of raise exception?
        

    def removeBookFromShelf(self, title, count):

        if not isinstance(title, str):
            raise Exception("Error: enter the title as string")
        if not isinstance(count, int):
            raise Exception("Error: enter a the count as a int")
        
        if title in self.__booksInThisShelf:
            if self.__booksInThisShelf.get(title) - count > 0:
                newCount = self.__booksInThisShelf.get(title) - count
                self.__booksInThisShelf.update({title: newCount})
                self.__availableCapacity += count
                print(f"{count} units of {title} were removed from shelf {self.__shelfID}\n{newCount} of {title} are still available")

            elif self.__booksInThisShelf.get(title) - count == 0:
                self.__booksInThisShelf.pop(title)
                self.__availableCapacity += count
                print(f"{title} was removed from this shelf")

            elif self.__booksInThisShelf.get(title) - count < 0: # making sure that the count of each book does not go below 0
                print(f"{self.__booksInThisShelf.get(title)} are available still available")

            else:
                raise Exception("Error: Invalide input")
        else:
            raise Exception(f"{title} is not available in the shelf {self.__shelfID}")
        
    
    def get_booksInThisShelf(self):

        if self.__booksInThisShelf == {}:
            print(f"shelf {self.shelfID} is empty")

        else:
            print(f"Books avaiblable in shelf {self.__shelfID}")
            for book in self.__booksInThisShelf:
                print(f" - {book}, {self.__booksInThisShelf.get(book)} units")

    
    def checkAvailability(self, title):
            
            if title in self.__booksInThisShelf:
                print(f"{self.__booksInThisShelf.get(title)} units of {title} are available")

            else:
                print(f"{title} in not available")
    def getGenre(self):
        return self.__genre

    # def getBookPDF(): a function that will get the bookPDF from the database

shelf1 = Shelf("tolga", 100, "08925032")
shelf1.addBookToShelf("le prince", 10)
shelf1.addBookToShelf("la peste", 10)
shelf1.addBookToShelf("Harry Potter 1", 10)
shelf1.addBookToShelf("Peau noir masque blanc", 10)
shelf1.addBookToShelf("le capital", 10)
print(shelf1.get_booksInThisShelf())
print("\n") 
print(shelf1.checkAvailability("la peste"))
# shelf1.removeBookFromShelf("le prince", 3)
# print(f"Available Capacity: {shelf1.availableCapacity}")
# print(shelf1.get_booksInThisShelf())
