title = input("Enter a book title: ")
author = input("Enter the author's name: ")
pub_year = int(input("Enter the year that the book was published: "))
pages = int(input("Enter the number of pages in the book: \n"))
age = 2019 - pub_year
if age < 10:
    print("This book is younger than ten years old.\n")
else:
    print("This book is at least ten years old.\n")
if pages < 100:
    print("This book is a short book.")
elif pages > 100 and pages < 300:
    print("This book is an average book.")
else:
    print("This book is a long book.")
