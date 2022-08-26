"""
helper file that contain all the function that used for the script
"""
import json
def menu ():
    """
    a finction that show to the user all his options
    """
    print ("a - add a new contact")
    print ("p - print all contacts")
    print ("s - search for a contact")
    print ("d - delete a contact")
    print ("x - exit from contacts")
    user_selction = input("select an option:")
    print(f"you selcted : {user_selction}")
    return user_selction

def load (fileName):
    """
    a function that load the contact of a file, from file into a python object (list),
     in order to make changes in the prog.
    """
    with open (fileName, "r+") as file:
        return json.load(file)  #return the value, when we call the func we will give an arry that fill the value returned

def printAllContacts (array):
    """
    a function that print all the content that in the array
    """
    print (array)

def addNewContact (array):
    """
    a finction that add an contact into a list , with the keys name and cell.
    """
    name = input("enter a name:")
    cell = input("enter a cell:")
    list_to_add = {"name": name, "cell": cell}
    array.append (list_to_add)
    # print (contacts)

def search_a_contact (array): 
    """
    a function that looking for a contact due to the key 'name' and print his details
    """
    name_2_search = input ("write a name you want to search:")
    for item in array:
        if item['name'] == name_2_search:
            print (f"found- name {item['name']}, cell {item['cell']}")
            return
    print (f"not found {name_2_search}")

def delete_a_contact (array):
    """
    a function that looking for a contact due to the key 'name' and delete his details
    """
    name_2_search = input ("write a name you want to delete:")
    for item in array:
        if item['name'] == name_2_search:
            print (f"delete- name {item['name']}, cell {item['cell']}")
            array.remove(item)
            print(array)
            return
    print (f"not found {name_2_search}")

def save(fileName , array):
    """
    a function that return the list into a json file again
    """
    with open (fileName , "w") as file:
        json.dump (array, file)
