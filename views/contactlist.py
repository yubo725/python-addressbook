# coding: utf-8
from Tkinter import *
from dbutil import DBUtils

class ContactListView(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent
		self.tabtitle = "联系人列表"
		self.initUI()

	def initUI(self):
		self.dbUtils = DBUtils()
		list = self.dbUtils.get_all_records()
		self.listbox = Listbox(self)
		for person in list:
			self.listbox.insert(END, '%s %s %s' % (person.name, person.phone, person.addr))
		self.listbox.pack(fill=BOTH, expand=True)

	def refresh(self):
		size = self.listbox.size()
		self.listbox.delete(0, size)
		list = self.dbUtils.get_all_records()
		for person in list:
			self.listbox.insert(END, '%s %s %s' % (person.name, person.phone, person.addr))
		self.listbox.pack(fill=BOTH, expand=True)

