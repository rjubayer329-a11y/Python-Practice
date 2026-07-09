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

library = {k.capitalize(): v for k, v in library.items()}
def add_book(catagory, title):
    cat_clean = catagory.strip().capitalize()
    if cat_clean in library:
        if title not in library[cat_clean]:
            library[cat_clean].append(title)
            print(f"Added {title} to {cat_clean}")
        else:
            print("We already have this book!")
    else:
        library[cat_clean] = [title]
        print("A new book is added")
    
def show_book():
    print("\n" + "-"*30)
    for catagory, books in library.items():
        print(f"[{catagory.upper()}]")
        for title in books:
            print(f" > {title}")
    print("-"*30)

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
                return catagory.lower()
    return "Unknown"

def teach_brain(catagory, title):
    cat_lower = catagory.lower()
    words = title.lower().split()

    skip_words = ["the", "a", "an", "and", "of", "in", "to", "for", "with", "on", "at", "by", "is"]

    if cat_lower not in brain:
        brain[cat_lower] = []

    for word in words:
        word = word.strip(".,!?\"'")
        if word not in skip_words and len(word) > 2:
            if word not in brain[cat_lower]:
                brain[cat_lower].append(word)
                print(f"Brain updated: Learned that keyword '{word}' impliles '{catagory}'")

def brain_data_save():
    with open("brain_data.json", "w") as file:
        json.dump(brain, file)
        print("Data seved to the brain✅")

def brain_data_load():
    global brain
    try:
        with open("brain_data.json", "r") as file:
            brain = json.load(file)
            print("The brain file has loaded✅")
    except FileNotFoundError:
        print("We couldn't find the brain data file")
        brain = {k.lower(): [w.lower() for w in v] for k, v in brain.items()}
        brain_data_save()

load_data()
brain_data_load()

user_title = input("Enter the title of the book: ").strip()
prediction = guess_catagory(user_title)

if prediction != "Unknown":
    print(f"🤖 Your book catagory might be {prediction}")
    confermation = input("Do you want to conferm this catagory?: ").lower()
    if confermation == "yes":
        final_cat = prediction
        teach_brain(final_cat, user_title)
    else:
        final_cat = input("So, please enter the catagory: ")
        #Teach the brain because user corrected it!
        teach_brain(final_cat, user_title)
else:
    print("🤖 I'm not sure about the catagory of this book!")
    final_cat = input("Please enter the catagory of this book: ")
    #Teach the brain because it was Unknown!
    teach_brain(final_cat, user_title)
add_book(final_cat, user_title)
show_book()
save_data()
brain_data_save()