# coding: utf-8
from Tkinter import *
from dbutil import DBUtils
import tkMessageBox

class SearchContactView(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent;
		self.tabtitle="查找联系人"
		self.initUI()

	def initUI(self):
		frame1 = Frame(self)
		frame1.pack(fill=X)

		self.searchEntry = Entry(frame1)
		self.searchEntry.pack(side=LEFT, expand=False)
		Button(frame1, text="根据姓名搜索", command=self.search).pack(side=LEFT)

		self.listbox = Listbox(self)

	def search(self):
		keyword = self.searchEntry.get()
		dbUtils = DBUtils()
		list = dbUtils.search(keyword)
		if len(list) == 0:
			tkMessageBox.showinfo('提示', '没有搜索到相关记录')
		else:
			size = self.listbox.size()
			self.listbox.delete(0, size)
			for person in list:
				self.listbox.insert(END, '%s %s %s' % (person.name, person.phone, person.addr))
			self.listbox.pack(fill=BOTH, expand=True)