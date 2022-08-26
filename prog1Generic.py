"""menu - V
load - make the file into a string V
add - the 1 ooption in the menu, add a new contact V
print - the 2 option in the menu, print all contacts V
search - the 3 option in the menu, search for a contacf V
delete - the 4 option in the menu, delete a contact V
exit - the 5 optin in the menu, exit from the program
dump - return into a file again"""

from fileinput import filename
from helper_prog1_generic import *



def main():
     """a function that call all the functions due to the order"""
filename = "prog1.json"
contacts =[]
contacts = load(filename)
user_selection = menu()
while user_selection != "x":
    if user_selection == "a" :addNewContact (contacts)
    if user_selection == "p" :printAllContacts (contacts)
    if user_selection == "s" :search_a_contact(contacts)
    if user_selection == "d" :delete_a_contact(contacts)
    user_selection = menu()
save()    

if __name__ == "__main__":
    main()


