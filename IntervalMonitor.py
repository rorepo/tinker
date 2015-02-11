from datetime import datetime, timedelta


#check whether current time in monitoring range
def timeToMonitor(startTime,endTime):
	strDateFormat = '%Y %m %d %H:%M'
	currentDateTime = datetime.now()
	#currentDateTime = datetime.strptime('2012 03 01 03:59', strDateFormat)
	currentDay = currentDateTime.day
	currentMonth = currentDateTime.month
	currentYear = currentDateTime.year
	currentHour = currentDateTime.hour

	#if start hour is am
	if int(startTime[:3]) < int(endTime[:3]):
		startDateString = str(currentYear) + ' ' + str(currentMonth) + ' ' + str(currentDay) + startTime
		startDateTime = datetime.strptime(startDateString, strDateFormat)
		endDateString = str(currentYear) + ' ' + str(currentMonth) + ' ' + str(currentDay) + endTime
		endDateTime = datetime.strptime(endDateString, strDateFormat)
	#elseif curr hour is am
	elif int(startTime[:3]) > currentHour:
		testNowString = str(currentYear) + ' ' + str(currentMonth) + ' ' + str(currentDay) + ' ' + '{:0>2d}'.format(currentHour) + ':00'
		testNow = datetime.strptime(testNowString, strDateFormat)
		testNow -= timedelta(hours=currentHour+1)
		testNowYear = testNow.year
		testNowMonth = testNow.month
		testNowDay = testNow.day
		startDateString = str(testNowYear) + ' ' + str(testNowMonth) + ' ' + str(testNowDay) + startTime
		startDateTime = datetime.strptime(startDateString, strDateFormat)
		endDateString = str(currentYear) + ' ' + str(currentMonth) + ' ' + str(currentDay) + endTime
		endDateTime = datetime.strptime(endDateString, strDateFormat)
	#curr hour must be pm, after start hour
	else:
		startDateString = str(currentYear) + ' ' + str(currentMonth) + ' ' + str(currentDay) + startTime
		startDateTime = datetime.strptime(startDateString, strDateFormat)
		startTimeValue = int(startTime[:3])
		testEndTime = startDateTime + timedelta(hours=25-startTimeValue)
		endYear = testEndTime.year
		endMonth = testEndTime.month
		endDay = testEndTime.day
		endDateString = str(endYear) + ' ' + str(endMonth) + ' ' + str(endDay) + endTime
		endDateTime = datetime.strptime(endDateString, strDateFormat)

        if startDateTime <= currentDateTime <= endDateTime:
                return True
        else:
                return False
