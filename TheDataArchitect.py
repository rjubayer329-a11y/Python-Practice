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
        print(f"Catagory {catagory} not found!")
    
    for catagory in library:
        for title in library[catagory]:
            print(f"{catagory} -> {title}")

input1 = input("What's your book catagory?: ").strip().capitalize()
input2 = input("What's the titel of the book?: ").strip().capitalize()
add_book(input1, input2)