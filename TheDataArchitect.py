import json
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

def save_data():
    with open("libraryData.json", "w") as file:
        json.dump(library, file)
        print("Data seved to the voult✅")

def load_data():
    global library
    try:
        with open("libraryData.json", "r") as file:
            library = json.load(file)
            print("The file has loaded✅")
    except FileNotFoundError:
        print("We couldn't find the file!")
load_data()
input1 = input("What's your book catagory?: ").strip().capitalize()
input2 = input("What's the title of the book?: ").strip().capitalize()
add_book(input1, input2)
show_book()
save_data()