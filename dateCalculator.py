from datetime import datetime, timedelta

def nextDate(day):
	today = datetime.today()
	days = timedelta(days=day)
	return today+days

def getDate(mydate):
	return datetime.strftime(mydate, '%d.%m.%y')