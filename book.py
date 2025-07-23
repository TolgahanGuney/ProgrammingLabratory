class book:
    # I need to take off many of hte varibales out of the constructor's arguments as they are not needed to creat a new book object
    def __init__(self, title, author, bookId, dateOfAcquisition, language, series, genre, price, yearOfPublication):
        self.title = title
        self.author = author
        self.bookId = bookId
        self.dateOfAcquisition =  dateOfAcquisition
        self.language = language
        self.series = series
        self.genre = genre
        self.rating = None
        self.ratingList = []
        self.bookStatus = None
        self.price = price
        self.yearOfPublication = yearOfPublication
    
    def CalculateAvgRating(self):
        sum = 0
        for i in self.ratingList:
            sum += i
        self.rating = sum/len(self.ratingList)
    
    def rateBook(self, newRating):
        if not isinstance(newRating, int):
            raise Exception("input error: pleas input an integer: ")
        
        if not 0 < newRating <= 5:
            raise Exception("input error: pleas input an integer between 1 and 5: ")

        self.ratingList.append(newRating)
        print(f"Thank you for rating {self.title}")
        self.CalculateAvgRating()
    def buyBook(self):
        self.bookStatus = "Sold"  # for it would be better to creat a updateBookStatus() function 
                                  # that will have a list of predetermined status that 
                                  # a book can have. this would disable of possiblity of having someone 
                                  # set the book statu to a value that is accepted

        print(f"The book {self.title} by {self.author} is bought!") #Update the satus of the book in our futur database
    # def loanBook():
    
laPeste = book("lapest", "Albert Camus", None, None, None, None, None, None, None)
laPeste.rateBook(3)
laPeste.rateBook(5)
print(laPeste.rating)
print(laPeste.ratingList)












        