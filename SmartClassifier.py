brain = {
    "Python": ["Python", "Script", "Code", "Automate"],
    "Ai": ["Neural", "Intelligence", "Data", "Robot", "Machine"],
    "History": ["History", "Ancient", "War", "Century"]
}
brain = {k.lower(): [w.lower() for w in v] for k, v in brain.items()}
def guess_catagory(title):
    title_clean = title.strip().lower()
    
    for catagory, keywords in brain.items():
        for word in keywords:
            if word in title_clean:
                return catagory
    return "Unknown"

test_title = input("Enter any title here: ")
prediction = guess_catagory(test_title)
print(f"I think the category is: {prediction}")

# text = "a war between iran and israel"
# print(text.strip().upper())