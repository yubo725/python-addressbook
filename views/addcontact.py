# coding: utf-8
from Tkinter import *
from person import Person
from dbutil import DBUtils
import tkMessageBox

class AddContactView(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent;
		self.tabtitle="添加联系人"
		self.initUI()

	def initUI(self):
		PAD_X = 5
		PAD_Y = 10

		frame1 = Frame(self)
		frame1.pack(fill=X)
		Label(frame1, text="姓名：").pack(side=LEFT, padx=PAD_X, pady=PAD_Y)
		self.nameEntry = Entry(frame1)
		self.nameEntry.pack(side=LEFT, fill=X, expand=True, padx=PAD_X, pady=PAD_Y)

		frame2 = Frame(self)
		frame2.pack(fill=X)
		Label(frame2, text="电话：").pack(side=LEFT, padx=PAD_X, pady=PAD_Y)
		self.phoneEntry = Entry(frame2)
		self.phoneEntry.pack(side=LEFT, fill=X, expand=True, padx=PAD_X, pady=PAD_Y)

		frame3 = Frame(self)
		frame3.pack(fill=X)
		Label(frame3, text="住址：").pack(side=LEFT, padx=PAD_X, pady=PAD_Y)
		self.addrEntry = Entry(frame3)
		self.addrEntry.pack(side=LEFT, fill=X, expand=True, padx=PAD_X, pady=PAD_Y)

		Button(self, text="添加", command=self.addContact).pack(side=BOTTOM, fill=X, expand=True, padx=50, pady=PAD_Y)

		self.pack(ipadx=20, ipady=20)

	def addContact(self):
		name = self.nameEntry.get()
		phone = self.phoneEntry.get()
		addr = self.addrEntry.get()
		person = Person(name, phone, addr)
		dbUtils = DBUtils()
		if dbUtils.add_record(person):
			tkMessageBox.showinfo('提示', '添加联系人成功')
			self.nameEntry.delete(0, len(name))
			self.phoneEntry.delete(0, len(phone))
			self.addrEntry.delete(0, len(addr))
		else:
			tkMessageBox.showerror('提示', '添加联系人失败')