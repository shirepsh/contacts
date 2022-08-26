"""menu - V
load - make the file into a string V
add - the 1 ooption in the menu, add a new contact V
print - the 2 option in the menu, print all contacts V
search - the 3 option in the menu, search for a contacf V
delete - the 4 option in the menu, delete a contact V
exit - the 5 optin in the menu, exit from the program - a loop V
dump - return into a file again V"""

import json
contacts =[] 
"""we create an ampty list in order to fill it"""

def menu (): 
    """we print the menu for the user and ask him to choose an option"""
    print ("a - add a new contact")
    print ("p - print all contacts")
    print ("s - search for a contact")
    print ("d - delete a contact")
    print ("x - exit from contacts")
    user_selction = input("select an option:")
    print(f"you selcted : {user_selction}")
    return user_selction

def load (): 
    """a function that load the file into a string list (in order to make changes as add/delete contacts)"""
    global contacts
    with open ("Prog1.json", "r+") as file:
        contacts = json.load(file)

def printAllContacts (): 
    """a function that print all the contacts"""
    print (contacts)

def addNewContact (): 
    """a function that add a new contact"""
    name = input("enter a name:")
    cell = input("enter a cell:")
    list_to_add = {"name": name, "cell": cell}
    contacts.append (list_to_add)
    # print (contacts)

def search_a_contact (): 
    """a function that serach for a specific contact"""
    name_2_search = input ("write a name you want to search:")
    for item in contacts:
        if item['name'] == name_2_search:
            print (f"found- name {item['name']}, cell {item['cell']}")
            return
    print (f"not found {name_2_search}")

def delete_a_contact (): 
    """a function that serach for a specific contact and delete him"""
    name_2_search = input ("write a name you want to delete:")
    for item in contacts:
        if item['name'] == name_2_search:
            print (f"delete- name {item['name']}, cell {item['cell']}")
            contacts.remove(item)
            print(contacts)
            return
    print (f"not found {name_2_search}")

def save():
     """save the data into a file again"""
     with open ("prog1.json" , "w") as file:
         json.dump (contacts, file)

def main(): 
    """organize the function to run due to the order"""
    load()
    user_selection = menu()
    while user_selection != "x":
        if user_selection == "a" :addNewContact ()
        if user_selection == "p" :printAllContacts ()
        if user_selection == "s" :search_a_contact()
        if user_selection == "d" :delete_a_contact()
        user_selection = menu()
    save()    

if __name__ == "__main__":
    main()


