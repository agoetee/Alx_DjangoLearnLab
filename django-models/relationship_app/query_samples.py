from .models import Author, Book, Library, Librarian

# Add Author objects
chinua = Author.objects.create(name="Chinua Achebe")
chinua.save()
ama = Author.objects.create(name="Ama Ata Aidoo")
ama.save()

#Add Book objects
things = Book.objects.create(title="Things Fall Apart", author=chinua) 
dilemma = Book.objects.create(title="Dilemma of a Ghost", author=ama) 
things.save()
dilemma.save()

# Get books by one author
Book.objects.get(author=ama) 
Book.objects.get(author=chinua) 

# List all books
Book.objects.all()

# Create Library Instance
balme = Library.objects.create(name='balme')
balme.save()

# Add books to Library
balme.books.add(things, dilemma)

# List all books in Library
balme.books.all()
Library.objects.get(name=balme)

# Add Librarian
agyim = Librarian.objects.create(name='Agyim Taala', library=balme)
agyim.save()

#Retrieve a Libryrian for a library
agyim.library