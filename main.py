# coding: utf-8
from Tkinter import *
from ttk import * 
from views.contactlist import ContactListView
from views.addcontact import AddContactView
from views.searchcontact import SearchContactView

root = Tk()

notebook = Notebook(root)

contactListView = ContactListView(root)
notebook.add(contactListView, text=contactListView.tabtitle)

addContactView = AddContactView(root)
notebook.add(addContactView, text=addContactView.tabtitle)

searchContactView = SearchContactView(root)
notebook.add(searchContactView, text=searchContactView.tabtitle)

notebook.pack(fill=BOTH, expand=True, padx=1, pady=1)

def handleTabChange(e):
	contactListView.refresh()

notebook.bind('<<NotebookTabChanged>>', handleTabChange)

root.geometry('400x300+600+300')
root.resizable(width=False, height=False)
root.title('python简易通讯录')
root.mainloop()