class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_name(self):
        return self.name

    def change_name(self, newname):
        print("Name updating from %s to %s..." % (self.name, newname))
        self.name = newname
        print("Name is now %s" % (self.name))

    def get_email(self):
        return self.email

    def change_email(self, address):
        print("E-mail address for %s updating from %s to %s..." % (self.name, self.email, address))
        self.email = address
        print("E-mail address is now %s" % (self.email))

    def __repr__(self):
        info = "User: %s; E-Mail: %s; Number of Books Read: %s;" %(str(self.name), str(self.email), str(len(self.books)))
        return info

    def read_book(self, book, rating = None):
        self.books[book] = rating
        
    def get_average_rating(self):
        avg = 0

        for book in self.books:
            if self.books[book] == None:
                continue
            else:
                avg += self.books[book]

        avg = avg/(len(self.books))

        return avg

    def get_book_list(self):
        return self.books

    def __eq__(self, other_user):
        if other_user.get_email().upper() == self.get_email().upper() and other_user.get_name().upper() == self.get_name().upper():
            return True
        else:
            return False

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __eq__(self, other_book):
        if self.isbn == other_book.get_isbn() and self.title == other_book.get_title():
            return True
        else:
            return False

    def __repr__(self):
        info = "Book: %s; ISBN: %s;" %(self.title, str(self.isbn))
        return info

    def get_isbn(self):
        return self.isbn

    def get_title(self):
        return self.title

    def set_isbn(self, isbn):
        print("Updating ISBN from %s to %s..." % (str(self.isbn), str(isbn)))
        self.isbn = isbn
        print("ISBN updated to %s." % (str(self.isbn)))

    def add_rating(self, rating):
        if rating == None:
            self.ratings.append(rating)
            return

        else:
            rating = float(rating)

            if rating >= 0 and rating <= 4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def get_ratings_list(self):
        return self.ratings

    def get_average_rating(self):
        avg = 0

        for rating in self.ratings:
            if rating != None:
                avg += rating

        if len(self.ratings) < 1:
            avg = avg/1
        else:
            avg = avg/len(self.ratings)

        return avg

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, isbn, author):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return author

    def __repr__(self):
        info = "%s by %s" % (self.title, self.author)
        return info

class Non_Fiction(Book):
    def __init__(self, title, isbn, subject, level):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):

        if self.level[0].upper() == "A" or self.level[0].upper() == "E" or self.level[0].upper() == "I" or self.level[0].upper() == "O" or self.level[0].upper() == "U":
            info = "%s, an %s level manual on %s" % (self.title, self.level, self.subject)
        else:
            info = "%s, a %s level manual on %s" % (self.title, self.level, self.subject)
        return info

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        for book in self.books:
            if isbn == book.get_isbn():
                print("A Book with this ISBN already exists!")
                return
        
        book = Book(title, isbn)
        
        return book

    def create_novel(self, title, author, isbn):
        for book in self.books:
            if isbn == book.get_isbn():
                print("A Book with this ISBN already exists!")
                return
    
        book = Fiction(title, isbn, author)
        return book

    def create_non_fiction(self, title, subject, level, isbn):
        for book in self.books:
            if isbn == book.get_isbn():
                print("A Book with this ISBN already exists!")
                return
    
        book = Non_Fiction(title, isbn, subject, level)
        return book

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            
        else:
            print("No user with email %s!" % (email))
            return

        if book not in self.books:
            self.books[book] = 1
        else:
            self.books[book] += 1
            
    def add_user(self, name, email, user_books=None):
        if email in self.users.keys():
            print("User already exists!")
            return 

        else:
            self.users[email] = User(name, email)

        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for bookkey in self.books.keys():
            print(bookkey)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def highest_rated_book(self): #modified to account for ties by returning a list, original in comments...
        '''
        top_rating = 0

        for book in self.books.keys():
            if book.get_average_rating() > top_rating:
                top_rating = book.get_average_rating()
                champ = book

        return champ
        '''
        
        top_rating = 0
        champs = []

        for book in self.books.keys(): 
            if book.get_average_rating() > top_rating:
                top_rating = book.get_average_rating()
                champs = []
                champs.append(book)
            elif book.get_average_rating() == top_rating:
                champs.append(book)

        return champs

    def get_most_read_book(self): #modified to account for ties by returning a list, original in comments...
        '''
        readnum = 0

        for book in self.books:
            print(self.books[book], readnum)
            if self.books[book] > readnum:
                readnum = self.books[book]
                champ = book

        return champ
        '''
        
        readnum = 0
        champs = []
        
        for book in self.books:            
            if self.books[book] > readnum:
                readnum = self.books[book]
                champs = []
                champs.append(book)
            elif self.books[book] == readnum:
                champs.append(book)
                
        return champs        
        
    def most_positive_user(self): #modified to account for ties by returning a list, original in comments...
        '''
        most_positive_rating = 0
        most_positive_user = None
        
        for user in self.users.values():
            if user.get_average_rating() > most_positive_rating:
                most_positive_rating = user.get_average_rating()
                most_positive_user = user
                
        return most_positive_user
        '''
        
        most_positive_rating = 0
        most_positive_users = []
        
        for user in self.users.values():
            if user.get_average_rating() > most_positive_rating:
                most_positive_rating = user.get_average_rating()
                most_positive_users = []
                most_positive_users.append(user)
            elif user.get_average_rating() == most_positive_rating:
                most_positive_users.append(user)
                
        return most_positive_users