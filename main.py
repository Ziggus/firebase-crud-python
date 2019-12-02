from tkinter import *
from tkinter import messagebox
#import firebase_admin
#from firebase_admin import credentials
#
#cred = credentials.Certificate("cohesive-keel-160802-firebase-adminsdk-n4i9f-4f18c45b35.json")
#firebase_admin.initialize_app(cred)
#print('test')

pokeDB = db.reference()

def createFunc():  
    #createWin = Toplevel(root)
    #display = Label(createWin, text="Update this for user info")
    #display.pack() 
    newPokemon = pokeDB.child('pokemon').push(
    {
    'name' : 'Test Pokemon', 
    'type' : "Test Type"
    }) # test entry for Create function - this will be updated via user input with tkinter later

def readFunc():  
    result = pokeDB.order_by_child('ID').limit_to_last(5).get() # this will be changed to read by user input
    print(result)

def updateFunc():  
    print("update function")
    newPokemon.update({'since' : 1799}) # this will be changed to find the correct record to update and new changes with the user input 

def deleteFunc():  
    pokeDB.newPokemon(key).remove()

# ----------------------------------------------------- GUI -----------------------------------------------------
# commented out while testing functions
"""
root = Tk()  
root.geometry('210x420') 
root.title('Python Firebase GUI')

createButton = Button(root,
	text = 'Create',
	command = createFunc,
    height = 1, 
    width = 6) 
createButton.pack()

readButton = Button(root,
	text = 'Read',
	command = readFunc,
    height = 1, 
    width = 6)   
readButton.pack()   

updateButton = Button(root,
	text = 'Update',
	command = updateFunc,
    height = 1, 
    width = 6)  
updateButton.pack()   

deleteButton = Button(root,
	text = 'Delete',
	command = deleteFunc,
    height = 1, 
    width = 6) 
deleteButton.pack()  



root.mainloop()
"""
# ----------------------------------------------------- GUI -----------------------------------------------------