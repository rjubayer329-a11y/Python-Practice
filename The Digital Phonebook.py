# dict = {
#     "name" : {
#         "number" : 654654
#     }
# }
# user_input = int(input())
# dict["name"]["number"]=user_input
# print(dict["name"]["number"])

phonebook = {}
status = True
while status:
    entered_name = input("Enter a name: ")
    entered_num = int(input("Enter his/her number: "))
    phonebook[entered_name] = entered_num
    asking_for_quit = input("Do you want to add more? (yes/no): ")
    if asking_for_quit == "no":
        status = False
    else:
        pass
asking_for_data = input("Who do you want to look up?: ")
if asking_for_data in phonebook:
    print(f"Name: {asking_for_data}")
    print("Number:", phonebook[asking_for_data])
else:
    print("Sorry! the name entered is not available")