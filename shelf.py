class shelf: 
    def __init__(self ,genre, availableCapacity, shelfID):
        self.shelfID = shelfID
        self.genre = genre
        self.availableCapacity = availableCapacity
        self.booksInThisShelf = {}
    
    def addBookToShelf(self, title, count):

        if self.availableCapacity - count >= 0:
            if not title in self.booksInThisShelf:
                self.booksInThisShelf.update({title: count})
                self.availableCapacity -= count
                print(f"{count} of {title} were added to the self {self.shelfID}")
            else:
                print(f"{title} is already available in the shelf {self.shelfID}")
        else:
            raise Exception("Insufficient shelf capacity") # should I do a print here instead of raise exception?

    def removeBookFromShelf(self, title, count):
        if title in self.booksInThisShelf:
            if self.booksInThisShelf.get(title) - count > 0:
                newCount = self.booksInThisShelf.get(title) - count
                self.booksInThisShelf.update({title: newCount})
                self.availableCapacity += count
                print(f"{count} units of {title} were removed from shelf {self.shelfID}\n{newCount} of {title} are still available")

            elif self.booksInThisShelf.get(title) - count == 0:
                self.booksInThisShelf.pop(title)
                self.availableCapacity += count
                print(f"{title} was removed from this shelf")

            elif self.booksInThisShelf.get(title) - count < 0: # making sure that the count of each book does not go below 0
                print(f"{self.booksInThisShelf.get(title)} are available still available")

            else:
                raise Exception("Error")
        else:
            raise Exception(f"Book not available in the shelf {self.shelfID}")
    
    def get_booksInThisShelf(self):
        if self.booksInThisShelf == []:
            print(f"shelf {self.shelfID} is empty")

        else:
            print(f"Books avaiblable in shelf {self.shelfID}")
            for book in self.booksInThisShelf:
                print(f" - {book}, {self.booksInThisShelf.get(book)} units")
    
    def checkAvailability(self, title):
            if title in self.booksInThisShelf:
                print(f"{self.booksInThisShelf.get(title)} units of {title} are available")

            else:
                print(f"{title} in not available")

    # def getBookPDF(): a function that will get the bookPDF from the database

shelf1 = shelf("fantasy", 100, "08925032")
shelf1.addBookToShelf("le prince", 10)
shelf1.removeBookFromShelf("le prince", 3)
print(f"Available Capacity: {shelf1.availableCapacity}")
print(shelf1.get_booksInThisShelf())
