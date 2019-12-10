import PySimpleGUI as sg
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from json import loads

cred = credentials.Certificate('cohesive-keel-160802-firebase-adminsdk-n4i9f-a4cc4d9f57.json')
firebase_admin.initialize_app(cred, {'databaseURL': 'https://cohesive-keel-160802.firebaseio.com/'})
pokeDb = db.reference("pokemon")
sg.change_look_and_feel('Light Blue 3') # GUI color

def Create(pokeHeight, pokeId, pokeImgUrl, pokeName, pokeNum, pokeType, pokeWeakness, pokeWeight):
    pokeId = int(pokeId) # need to convert string to int for searches to work
    pokeNum = int(pokeNum) # need to convert string to int for searches to work
    tempPokemon={
                        "height" : pokeHeight,
                        "id" : pokeId,
                        "img" : pokeImgUrl,
                        "name" : pokeName,
                        "num" : pokeNum,
                        "type" : [ pokeType ],
                        "weaknesses" : [ pokeWeakness ],
                        "weight" : pokeWeight
                }
    print("")
    print(tempPokemon)
    try:
        lastKey = (next(iter(pokeDb.order_by_key().limit_to_last(1).get()))) # lastKey is used to find the last ID number and convert to string for newly added entry
        lastKey = int(lastKey)+1
        pokeNum = str(lastKey)
        pokeDb.child(pokeNum).set(tempPokemon)
        print("Entry successfully added!")
    except:
        print("Error entering new item.")

def Read(pokeHeight, pokeId, pokeImgUrl, pokeName, pokeNum, pokeType, pokeWeakness, pokeWeight): # finds by child ID
    try:
        print("")
        if pokeName:
            pokemon = pokeDb.order_by_child("name").equal_to(pokeName).get()
        if pokeNum:
            pokemon = pokeDb.order_by_child("num").equal_to(int(pokeNum)).get()
        if pokeId:
            pokemon = pokeDb.order_by_child("id").equal_to(int(pokeId)).get()
        print(pokemon)
    except:
        print("Not in DB")

def Update(pokeHeight, pokeId, pokeImgUrl, pokeName, pokeNum, pokeType, pokeWeakness, pokeWeight):
    pokeId = int(pokeId) # need to convert string to int for searches to work
    pokeNum = int(pokeNum) # need to convert string to int for searches to work
    tempPokemon={
                        "height" : pokeHeight,
                        "id" : pokeId,
                        "img" : pokeImgUrl,
                        "name" : pokeName,
                        "num" : pokeNum,
                        "type" : [ pokeType ],
                        "weaknesses" : [ pokeWeakness ],
                        "weight" : pokeWeight
                }
    try:
        print("")
        if pokeName:
            pokemon = pokeDb.order_by_child("name").equal_to(pokeName).get()
            currKey = (next(iter(pokemon)))
            pokeDb.child(currKey).set(tempPokemon)
        if pokeNum:
            pokemon = pokeDb.order_by_child("num").equal_to(int(pokeNum)).get()
            currKey = (next(iter(pokemon)))
            pokeDb.child(currKey).set(tempPokemon)
        if pokeId:
            pokemon = pokeDb.order_by_child("id").equal_to(int(pokeId)).get()  
            currKey = (next(iter(pokemon)))
            pokeDb.child(currKey).set(tempPokemon)
        print(pokemon)
        print("Record has been sucessfully updated.")
    except:
        print("There was an error updating this entry.")

def Delete(pokeHeight, pokeId, pokeImgUrl, pokeName, pokeNum, pokeType, pokeWeakness, pokeWeight):
    try:
        print("")
        if pokeName:
            pokemon = pokeDb.order_by_child("name").equal_to(pokeName).get()
            currKey = (next(iter(pokemon)))
        if pokeNum:
            pokemon = pokeDb.order_by_child("num").equal_to(int(pokeNum)).get()
            currKey = (next(iter(pokemon)))
        if pokeId:
            pokemon = pokeDb.order_by_child("id").equal_to(int(pokeId)).get()  
            currKey = (next(iter(pokemon)))
        print(pokemon)
        pokeDb.child(currKey).delete()
        print("Record deleted successfully.")      
    except:
        print("Delete failed")


dispatch_dictionary = {'Create':Create, 'Read':Read, 'Update':Update, 'Delete':Delete}

layout = [
        [sg.Text("Searches currently supported: Name, Number, ID")],
        [sg.Button('Create'), sg.Button('Read'), sg.Button('Update'), sg.Button('Delete')],
        [sg.Text('Enter height: ', auto_size_text=True)],[sg.InputText()],
        [sg.Text('Enter ID: ', auto_size_text=True)],[sg.InputText()],
        [sg.Text('Enter IMG URL: ', auto_size_text=True)],[sg.InputText()],
        [sg.Text('Enter Name: ', auto_size_text=True)],[sg.InputText()],
        [sg.Text('Enter num: ', auto_size_text=True)],[sg.InputText()],
        [sg.Text('Enter Type: ', auto_size_text=True)],[sg.InputText()],
        [sg.Text('Enter weaknesses: ', auto_size_text=True)],[sg.InputText()],
        [sg.Text('Enter weight: ', auto_size_text=True)],[sg.InputText()],
        [sg.Output(size=(88, 20))], 
        [sg.Quit()]
          ]
window = sg.Window('Simple GUI for Firebase database administration using Python', layout)


while True:
    event, values = window.read()
    if event in ('Quit', None):
        break
    if event in dispatch_dictionary:
        func_to_call = dispatch_dictionary[event]

        pokeHeight = values[0]
        pokeId = values[1] 
        pokeImgUrl = values[2]
        pokeName = values[3]
        pokeNum = values[4]  
        pokeType = values[5]
        pokeWeakness = values[6]
        pokeWeight = values[7]

        func_to_call(pokeHeight, pokeId, pokeImgUrl, pokeName, pokeNum, pokeType, pokeWeakness, pokeWeight)
    else:
        print('Event {} not in dispatch dictionary'.format(event))
window.close()