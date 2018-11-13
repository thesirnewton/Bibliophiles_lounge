"""
A simple application to keep record of books we've read at the bibliphile's lounge
It takes in the Book title, Author, Date it was read, and moderator

Will improve on it pole pole
"""
from time import gmtime, strftime 
class Bibliophiles_Lounge():

	def __init__(self, Book_title, Book_Author, Review_Date):
		self.Book_title = Book_title
		self.Book_Author = Book_Author
		self.Review_Date = Review_Date
		#self.Name = Name

	def __repr__(self):
		return f"Our current BOTW is {self.Book_title} by {self.Book_Author}."

	def Moderator(self, first, last):
		self.first = first
		self.last = last
		return f"{self.first} {self.last} will lead the discussion"

	def Title(self):
		return f"We're curently reading {self.Book_title}"

	def Author(self):
		return f"The {self.Book_title} author is {self.Book_Author}"

	def Date(self):
		return f"The discussion of  {self.Book_title} will be on {self.Review_Date}"

	def Members(self, new_members):
		self.members = 150
		self.new_members = new_members
		if self.new_members:
			self.members += new_members
			return self.members

		return f"we are {self.members} in number"





#book1 = Bibliophiles_Lounge("Mocking bird", "Harper Lee", "10/12/2018". "")
book2 = Bibliophiles_Lounge("Deep Work", "Cal Newport", "15/30/2018")
# print(book2)
# mod = book2.Moderator("Kanini", "Mbugua")
# print(mod)
# print(book2)
# print(book2.Date())
# print(book2.Members())

new =book2.Members(10)
new2 = book2.Members(5)
print(new)
print(new2)