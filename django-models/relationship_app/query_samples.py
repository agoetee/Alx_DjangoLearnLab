# >>> chinua = Author.objects.create(name="Chinua Achebe")
# >>> chinua.save()
# >>> ama = Author.objects.create(name="Ama Ata Aidoo")
# >>> ama.save()
# >>> things = Book.objects.create(title="Things Fall Apart", author=1)
# things = Book.objects.create(title="Things Fall Apart", author=chinua) 
# >>> dilemma = Book.objects.create(title="Dilemma of a Ghost", author=ama) 
# >>> things.save()
# >>> dilemma.save()
# >>> Book.objects.get(author=ama) 
# <Book: Dilemma of a Ghost>
# >>> Book.objects.get(author=chinua) 
# <Book: Things Fall Apart>
# >>>