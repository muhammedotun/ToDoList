from MyList import MyList
from Task import Task

class main():
	#definations
	deadLineRutin = 1
	deadLineHomeWork = 7
	rutin = MyList('rutin')
	homeWork = MyList('home work')
	#definations

	#create task and add
	rutin.mylist.append(Task("take a shower", deadLineRutin, 8))
	rutin.mylist.append(Task("take a coffe", deadLineRutin, 5))
	rutin.mylist.append(Task("have breakfast", deadLineRutin, 10))

	homeWork.mylist.append(Task("data stracture", deadLineHomeWork, 9))
	homeWork.mylist.append(Task("system programming", deadLineHomeWork, 10))
	homeWork.mylist.append(Task("database management systems", deadLineHomeWork, 7))

	#create task and add

	#definations functions

	def printToDoList(mylist):
		for task in mylist.mylist:
			print(task.getTask())
	#definations functions

	printToDoList(homeWork)

"""
	example

	#print ToDoList
	printToDoList(rutin)
	#print ToDoList

	#sort list
	Task.sortByImportance(rutin.mylist)
	#sort list
	print()
	print("sorted list\n")
	#sort list

	#print ToDoList
	printToDoList(rutin)
	#print ToDoList
	print("\n")
	#print ToDoList
	printToDoList(homeWork)
	#print ToDoList
	Task.sortByImportance(homeWork.mylist)
	print("\n")
	printToDoList(homeWork)

	example

"""
if __name__ == '__main__':
	main()