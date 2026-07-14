import json

class DataArchitect:
    def __init__(self):
            self.brain = {
                "Python": ["Python", "Script", "Code", "Automate"],
                "Ai": ["Neural", "Intelligence", "Data", "Robot", "Machine"],
                "History": ["History", "Ancient", "War", "Century"]
            }
            self.library = {
                "AI":["Superintelligence", "life 3.0", "How an AI can be a teacher like Gimini"],
                "Python":["Automate the boring stuff"],
                "History": ["The history of Bangladesh"]
            }
    
    def load_data(self):
        try:
            with open("libraryData.json", "r") as file:
                self.library = json.load(file)
                print("The file has loaded✅")
        except FileNotFoundError:
            print("We couldn't find the file!")
            self.library = {k.capitalize(): v for k, v in self.library.items()}
            self.save_data()

    def brain_data_load(self):
        try:
            with open("brain_data.json", "r") as file:
                self.brain = json.load(file)
                print("The brain file has loaded✅")
        except FileNotFoundError:
            print("We couldn't find the brain data file")
            self.brain = {k.lower(): [w.lower() for w in v] for k, v in self.brain.items()}
            self.brain_data_save()
    
    def add_book(self, catagory, title):
        cat_clean = catagory.strip().capitalize()
        if cat_clean in self.library:
            if title not in self.library[cat_clean]:
                self.library[cat_clean].append(title)
                print(f"Added {title} to {cat_clean}")
            else:
                print("We already have this book!")
        else:
            self.library[cat_clean] = [title]
            print("A new book is added")
        
    def show_book(self):
        print("\n" + "-"*30)
        for catagory, books in self.library.items():
            print(f"[{catagory.upper()}]")
            for title in books:
                print(f" > {title}")
        print("-"*30)

    def save_data(self):
        with open("libraryData.json", "w") as file:
            json.dump(self.library, file)
            print("Data seved to the voult✅")



    def guess_catagory(self, title):
        title_clean = title.strip().lower()
        
        for catagory, keywords in self.brain.items():
            for word in keywords:
                if word in title_clean:
                    return catagory.lower()
        return "Unknown"

    def teach_brain(self, catagory, title):
        cat_lower = catagory.lower()
        words = title.lower().split()

        skip_words = ["the", "a", "an", "and", "of", "in", "to", "for", "with", "on", "at", "by", "is"]

        if cat_lower not in self.brain:
            self.brain[cat_lower] = []

        for word in words:
            word = word.strip(".,!?\"'")
            if word not in skip_words and len(word) > 2:
                if word not in self.brain[cat_lower]:
                    self.brain[cat_lower].append(word)
                    print(f"Brain updated: Learned that keyword '{word}' impliles '{catagory}'")

    # We can delete keyword through this function:
    def prune_brain(self):
        print(f"Your dictionary:\n")
        for category, keywords in self.brain.items():
            print(f"[{category.upper()}]")
            for keyword in keywords:
                print(f" > {keyword}")
        deletion_title = input("Enter the title you want to delete: ").strip().lower()
        deletion_catagory = input("Enter the catagory where the title from: ").strip().lower()
        if deletion_catagory in self.brain:
            if deletion_title in self.brain[deletion_catagory]:
                self.brain[deletion_catagory].remove(deletion_title)
                print("The keyword deleted successfully✅")
                self.brain_data_save()
            else:
                print("The title is not in the category!❌")
        else:
            print("The category is not in your brain file❌")

    def brain_data_save(self):
        with open("brain_data.json", "w") as file:
            json.dump(self.brain, file)
            print("Data seved to the brain✅")





architect = DataArchitect()
architect.load_data()
architect.brain_data_load()

#applying the prune_brain() function
asking_for_deletion = input("Do you want to delete any keyword from your brain file: ")
if asking_for_deletion == "yes":
    architect.prune_brain()
else:
    pass

user_title = input("Enter the title of the book: ").strip()
prediction = architect.guess_catagory(user_title)

if prediction != "Unknown":
    print(f"🤖 Your book catagory might be {prediction}")
    confermation = input("Do you want to conferm this catagory?: ").lower()
    if confermation == "yes":
        final_cat = prediction
        architect.teach_brain(final_cat, user_title)
    else:
        final_cat = input("So, please enter the catagory: ")
        #Teach the brain because user corrected it!
        architect.teach_brain(final_cat, user_title)
else:
    print("🤖 I'm not sure about the catagory of this book!")
    final_cat = input("Please enter the catagory of this book: ")
    #Teach the brain because it was Unknown!
    architect.teach_brain(final_cat, user_title)
architect.add_book(final_cat, user_title)
architect.show_book()
architect.save_data()
architect.brain_data_save()