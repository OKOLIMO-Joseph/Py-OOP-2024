# Example 1: Library System
class Book:
    def __inti__(self, title, author, pages, genre, volume):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.volume = volume

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f"{self.title} has been deleted")

    #Method to get chapter
    def get_chapter(self,chapter):
        return f"{self.title} - chapter{chapter}"

    #Method to get author
    def get_author(self):
        return f"{self.title} is written by {self.author}"

#Create a book object of the titile: The Moon Also Sets
book1 = Book('The Moon Also Sets', 'John Doe', 300, 'Fiction', 1)
book2 = Book('The Art of Racing in te Rain', 'Garth Stanley', 600, 'Fiction', 2)
book3 = Book('No More Mr. Nice Guy', 'Robert L', 200, 'Self-help', 3)
book4 = Book('First Blood', 'David Morrale', 400, 'Action', 1)

#Print author of book1
print(book1.get_author)
priny(book2.get_chapter(4))