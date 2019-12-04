from datetime import datetime
from dateCalculator import nextDate, getDate
class Task(object):
	"""docstring for Task"""
	id = 0
	def __init__(self, text, deadLine, importance):
		super(Task, self).__init__()
		self.id = Task.id + 1
		Task.id += 1
		self.text = text
		self.importance = importance
		self.createdDateTime = datetime.today()
		self.deadLine = nextDate(deadLine)

	def getTask(self):
		return "{}  deadline: {} created: {} importance: {}".format(self.text,getDate(self.deadLine), getDate(self.createdDateTime), self.importance)


	def sortByImportance(mylist):
		length = len(mylist)

		for i in range(length-1):
			swapped = False
			for j in range(length-1-i):
				if mylist[j].importance < mylist[j+1].importance:
					swapped = True
					mylist[j] , mylist[j+1] =mylist[j+1], mylist[j]
			if not swapped: break #stop iteration if the collection is sorted.
		return mylist

	def sortById(mylist):
		length = len(mylist)

		for i in range(length-1):
			swapped = False
			for j in range(length-1-i):
				if mylist[j].id > mylist[j+1].id:
					swapped = True
					mylist[j] , mylist[j+1] =mylist[j+1], mylist[j]
			if not swapped: break #stop iteration if the collection is sorted.
		return mylist