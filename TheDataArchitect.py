library = {
    "AI":["Superintelligence", "life 3.0", "How an AI can be a teacher like Gimini"],
    "Python":["Automate the boring stuff"],
    "History": ["The history of Bangladesh"]
}
library = {k.capitalize(): v for k, v in library.items()}
def add_book(catagory, title):
    if catagory in library:
        if title not in library[catagory]:
            library[catagory].append(title)
            print(f"Added {title} to {catagory}")
        else:
            print("We already have this book!")
    else:
        library[catagory] = [title]
        print("A new book is added")
    
def show_book():
    print("------------------------------------")
    for catagory in library:
        for title in library[catagory]:
            print(f"{catagory} -> {title}")
    print("------------------------------------")
input1 = input("What's your book catagory?: ").strip().capitalize()
input2 = input("What's the title of the book?: ").strip().capitalize()
add_book(input1, input2)
show_book()