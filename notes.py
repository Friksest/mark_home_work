from os import system
## notes application

# add new note
# show all notes
# delete note

# * timer

notes = [
    {"text": "table 1, 2 soups"},
    {"text": "bill to table 2"},
    {"text": "call mom"},
] 


def clear():
    system("clear")

def showNotes(pnotes):
    for note in pnotes:
        print(f"{note['text']}")

def addNote(pnotes):
    text = input("Enter text: ")
    
    # HM1: 
    #   ask the user if he wants it on a specific position
    position = input("Add in end (yes / no): >")
    if position == "yes":
        pnotes.append( {"text": text} )
    elif position == "no":
        idx = int(input("Specify possition nuber: ")) -1
        pnotes.insert( idx, {"text": text} )

def deleteNote(pnotes):
    idx = int(input("which one: ")) -1
    pnotes.pop(idx)
    
#clear()
showNotes(notes)
addNote(notes)
print()
showNotes(notes)
# deleteNote(notes)
# clear()
# showNotes(notes)