import json
library = {
    "AI":["Superintelligence", "life 3.0", "How an AI can be a teacher like Gimini"],
    "Python":["Automate the boring stuff"],
    "History": ["The history of Bangladesh"]
}
brain = {
    "Python": ["Python", "Script", "Code", "Automate"],
    "Ai": ["Neural", "Intelligence", "Data", "Robot", "Machine"],
    "History": ["History", "Ancient", "War", "Century"]
}
brain = {k.lower(): [w.lower() for w in v] for k, v in brain.items()}
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
    print("\n" + "-"*30)
    for catagory, books in library.items():
        print(f"[{catagory.upper()}]")
        for title in books:
            print(f" > {title}")
    print("-"*30 + "\n")

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

def guess_catagory(title):
    title_clean = title.strip().lower()
    
    for catagory, keywords in brain.items():
        for word in keywords:
            if word in title_clean:
                return catagory
    return "Unknown"

load_data()
user_title = input("Enter the title of the book: ")
prediction = guess_catagory(user_title)
if prediction != "Unknown":
    print(f"🤖 Your book catagory might be {prediction}")
    confermation = input("Do you want to conferm this catagory?: ").lower()
    if confermation == "yes":
        final_cat = prediction
    else:
        final_cat = input("So, please enter the catagory: ")
else:
    print("🤖 I'm not sure about the catagory of this book!")
    final_cat = input("Please enter the catagory of this book: ")
add_book(final_cat, user_title)
show_book()
save_data()