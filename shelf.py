class shelf: 
    def __init__(self ,genre, availableCapacity, shelfID):
        self.shelfID = shelfID
        self.genre = genre
        self.availableCapacity = availableCapacity
        self.booksInThisShelf = []
    
    def addBookToShelf(self, title, count):

        if self.availableCapacity - count >= 0:
            # didn't find a good way to attach an int to each title in the booksInThisShelf list
            self.booksInThisShelf.append(title)
            self.availableCapacity -= count
            print(f"{count} of {title} were removed from the self")
        else:
            raise Exception("Insufficient shelf capacity") # should I do a print here instead of raise exception?

    def removeBookFromShelf(self, title, count):
        if title in self.booksInThisShelf:
            # didn't find a good way to attach an int to each title in the booksInThisShelf list
            self.booksInThisShelf.remove(title)
            self.availableCapacity += count
            print(f"{title} was removed from this shelf")
        else:
            raise Exception("This book is not present in this shelf")
    
    def get_booksInThisShelf(self):
        if self.booksInThisShelf == []:
            print(f"shelf {self.shelfID} is empty")
        else:
            print(f"Books avaiblable in shelf {self.shelfID}")
            for book in self.booksInThisShelf:
                print(f" - {book}")
    
    def checkAvailability(self, title):
            if title in self.booksInThisShelf:
                print(f"{title} is available")
            else:
                print(f"{title} in not available")

    # def getBookPDF(): a function that will get the bookPDF from the database

shelf1 = shelf("fantasy", 10, "08925032")
shelf1.addBookToShelf("le prince", 10)
print(f"Available Capacity: {shelf1.availableCapacity}")
print(shelf1.get_booksInThisShelf())
