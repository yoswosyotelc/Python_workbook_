# # @#$!@#$@!#$upwork### << ///Oct_2023..??>> @ @#$@%#!@%!Saving??@!#$@!#$@!#$!@#$@!#$@
# # !!!!! don't stay at one part for more than 1 weekds...!!!!
# # !!!!! proceed as you go through by commenting .. for furhter refirinement..


# #1. Write a Python script to display the various Date Time formats - Go to the editor

# import time
# import datetime
# print("Current date and time: " , datetime.datetime.now())
# print("Current year: ", datetime.date.today().strftime("%Y"))
# print("Month of year: ", datetime.date.today().strftime("%B"))
# print("Week number of the year: ", datetime.date.today().strftime("%W"))
# print("Weekday of the week: ", datetime.date.today().strftime("%w"))
# print("Day of year: ", datetime.date.today().strftime("%j"))
# print("Day of the month : ", datetime.date.today().strftime("%d"))
# print("Day of week: ", datetime.date.today().strftime("%A"))

# #2. Write a Python program to determine whether a given year is a leap year. Go to the editor

# def leap_year(y):
    # if y % 400 == 0:
        # return True
    # if y % 100 == 0:
        # return False
    # if y % 4 == 0:
        # return True
    # else:
        # return False
# print(leap_year(1900))
# print(leap_year(2004))

# #3. Write a Python program to convert a string to datetime. Go to the editor

# from datetime import datetime
# date_object = datetime.strptime('Jul 1 2014 2:43PM', '%b %d %Y %I:%M%p')
# print(date_object)

# #4. Write a Python program to get the current time in Python. Go to the editor

# import datetime
# print(datetime.datetime.now().time())

# #5. Write a Python program to subtract five days from current date. Go to the editor

# from datetime import date, timedelta
# dt = date.today() - timedelta(5)
# print('Current Date :',date.today())
# print('5 days before Current Date :',dt)

# #6. Write a Python program to convert unix timestamp string to readable date. Go to the editor

# import datetime
# print(
    # datetime.datetime.fromtimestamp(
        # int("1284105682")
    # ).strftime('%Y-%m-%d %H:%M:%S')
# )

# #7. Write a Python program to print yesterday, today, tomorrow. Go to the editor

# import datetime 
# today = datetime.date.today()
# yesterday = today - datetime.timedelta(days = 1)
# tomorrow = today + datetime.timedelta(days = 1) 
# print('Yesterday : ',yesterday)
# print('Today : ',today)
# print('Tomorrow : ',tomorrow)

# #8. Write a Python program to convert the date to datetime (midnight of the date) in Python. Go to the editor

# from datetime import date
# from datetime import datetime
# dt = date.today()
# print(datetime.combine(dt, datetime.min.time()))

# #9. Write a Python program to print next 5 days starting from today. Go to the editor

# import datetime
# base = datetime.datetime.today()
# for x in range(0, 5):
      # print(base + datetime.timedelta(days=x))
	  
# #10. Write a Python program to add 5 seconds with the current time. Go to the editor

# import datetime
# x= datetime.datetime.now()
# y = x + datetime.timedelta(0,5)
# print(x.time())
# print(y.time())

# #11. Write a Python program to convert Year/Month/Day to Day of Year in Python. Go to the editor

# import datetime
# today = datetime.datetime.now()
# day_of_year = (today - datetime.datetime(today.year, 1, 1)).days + 1
# print(day_of_year)

# #12. Write a Python program to get current time in milliseconds in Python Go to the editor

# import time
# milli_sec = int(round(time.time() * 1000))
# print(milli_sec)

# #13. Write a Python program to get week number. Go to the editor

# import datetime
# print(datetime.date(2015, 6, 16).isocalendar()[1])

# #14. Write a Python program to find the date of the first Monday of a given week. Go to the editor

# import time
# print(time.asctime(time.strptime('2015 50 1', '%Y %W %w')))

# #15. Write a Python program to select all the Sundays of a specified year. Go to the editor

# from datetime import date, timedelta

# def all_sundays(year):
# # January 1st of the given year
       # dt = date(year, 1, 1)
# # First Sunday of the given year       
       # dt += timedelta(days = 6 - dt.weekday())  
       # while dt.year == year:
          # yield dt
          # dt += timedelta(days = 7)
          
# for s in all_sundays(2020):
   # print(s)
   
# #16. Write a Python program to add year(s) with a given date and display the new date. Go to the editor

# import datetime
# from datetime import date
# def addYears(d, years):
    # try:
# #Return same day of the current year        
        # return d.replace(year = d.year + years)
    # except ValueError:
# #If not same day, it will return other, i.e.  February 29 to March 1 etc.        
        # return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

# print(addYears(datetime.date(2015,1,1), -1))
# print(addYears(datetime.date(2015,1,1), 0))
# print(addYears(datetime.date(2015,1,1), 2))
# print(addYears(datetime.date(2000,2,29),1))

# #17. Write a Python program to drop microseconds from datetime. Go to the editor

# import datetime
# dt = datetime.datetime.today().replace(microsecond=0)
# print()
# print(dt)
# print()

# #18. Write a Python program to get days between two dates. Go to the editor

# from datetime import date
# a = date(2000,2,28)
# b = date(2001,2,28)
# print(b-a)

# #19. Write a Python program to get the date of the last Tuesday. Go to the editor

# from datetime import date
# from datetime import timedelta
# today = date.today()
# offset = (today.weekday() - 1) % 7
# last_tuesday = today - timedelta(days=offset)
# print(last_tuesday)

# #20. Write a Python program to test the third Tuesday of a month. Go to the editor

# from datetime import datetime 
# def is_third_tuesday(s):
    # d = datetime.strptime(s, '%b %d, %Y')
    # return d.weekday() == 1 and 14 < d.day < 22

# print(is_third_tuesday('Jun 23, 2015')) #False
# print(is_third_tuesday('Jun 16, 2015')) #True 
# print(is_third_tuesday('Jul 21, 2015')) #False

# #21. Write a Python program to get the last day of a specified year and month. Go to the editor

# import calendar
# year = 2015
# month = 2
# print(calendar.monthrange(year, month)[1])

# #22. Write a Python program to get the number of days of a given month and year. Go to the editor

# from calendar import monthrange
# year = 2016
# month = 2
# print(monthrange(year, month))

# #23. Write a Python program to add a month with a specified date. Go to the editor

# from datetime import date, timedelta
# import calendar
# start_date = date(2014, 12, 25)
# days_in_month = calendar.monthrange(start_date.year, start_date.month)[1]
# print(start_date + timedelta(days=days_in_month))

# #24. Write a Python program to count the number of Monday of the 1st day of the month from 2015 to 2016. Go to the editor

# import datetime
# from datetime import datetime
# monday1 = 0
# months = range(1,13)
# for year in range(2015, 2017):
    # for month in months:
        # if datetime(year, month, 1).weekday() == 0:
            # monday1 += 1
# print(monday1)

# #25. Write a Python program to print a string five times, delay three seconds. Go to the editor

# import time 
# x=0
# print("\nw3resource will print five  times, delay for three seconds.")
# while x<5:
    # print("w3resource")
    # time.sleep(3)
    # x=x+1
	
# #26. Write a Python program calculates the date six months from the current date using the datetime module. Go to the editor

# import datetime
# print((datetime.date.today() + datetime.timedelta(6*365/12)).isoformat())

# #27. Write a Python program to create 12 fixed dates from a specified date over a given period. The difference between two dates will be 20. Go to the editor

# import datetime
# def every_20_days(date):
    # print('Starting Date: {d}'.format(d=date))
    # print("Next 12 days :")
    # for _ in range(12):
        # date=date+datetime.timedelta(days=20)
        # print('{d}'.format(d=date))

# dt = datetime.date(2016,8,1)
# every_20_days(dt)

# #28. Write a Python program to get the dates 30 days before and after from the current date. Go to the editor

# from datetime import date, timedelta

# current_date = date.today().isoformat()   
# days_before = (date.today()-timedelta(days=30)).isoformat()
# days_after = (date.today()+timedelta(days=30)).isoformat()  

# print("\nCurrent Date: ",current_date)
# print("30 days before current date: ",days_before)
# print("30 days after current date : ",days_after)

# #29. Write a Python program to get the GMT and local current time. Go to the editor


# from time import gmtime, strftime
# import time
# print("\nGMT: "+time.strftime("%a, %d %b %Y %I:%M:%S %p %Z", time.gmtime()))
# print("Local: "+strftime("%a, %d %b %Y %I:%M:%S %p %Z\n"))


# #30. Write a Python program to convert a date to the timestamp. Go to the editor

# import time
# import datetime
# now = datetime.datetime.now()
# print()
# print(time.mktime(now.timetuple()))
# print()

# #31. Write a Python program to convert a string date to the timestamp. Go to the editor

# import time
# import datetime
# s = "01/10/2016"
# print()
# print(time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple()))
# print()

# #32. Write a Python program to calculate a number of days between two dates. Go to the editor

# import datetime
# from datetime import date
# def differ_days(date1, date2):

    # a = date1
    # b = date2
    # return (a-b).days
# print()
# print(differ_days((date(2016,10,12)), date(2015,12,10)))
# print(differ_days((date(2016,3,23)), date(2017,12,10)))
# print()

# #33. Write a Python program to calculate no of days between two datetimes. Go to the editor

# import datetime
# from datetime import datetime

# def differ_days(date1, date2):
    # a = date1
    # b = date2
    # return (a-b).days
# print()
# print(differ_days((datetime(2016,10,12,0,0,0)), datetime(2015,12,10,0,0,0)))
# print(differ_days((datetime(2016,10,12,0,0,0)), datetime(2015,12,10,23,59,59)))
# print()

# #34. Write a Python program to display the date and time in a human-friendly string. Go to the editor

# import time
# print()
# print(time.ctime())
# print()

# #35. Write a Python program to convert a date to Unix timestamp. Go to the editor

# import datetime
# import time
# dt = datetime.datetime(2016, 2, 25, 23, 23)
# print()
# print("Unix Timestamp: ",(time.mktime(dt.timetuple())))
# print()

# #36. Write a Python program to calculate two date difference in seconds. Go to the editor

# from datetime import datetime, time
# def date_diff_in_Seconds(dt2, dt1):
  # timedelta = dt2 - dt1
  # return timedelta.days * 24 * 3600 + timedelta.seconds
# #Specified date
# date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')
# #Current date
# date2 = datetime.now()
# print("\n%d seconds" %(date_diff_in_Seconds(date2, date1)))
# print()

# #37. Write a Python program to convert two date difference in days, hours, minutes, seconds. Go to the editor

# from datetime import datetime, time

# def date_diff_in_seconds(dt2, dt1):
  # timedelta = dt2 - dt1
  # return timedelta.days * 24 * 3600 + timedelta.seconds

# def dhms_from_seconds(seconds):
	# minutes, seconds = divmod(seconds, 60)
	# hours, minutes = divmod(minutes, 60)
	# days, hours = divmod(hours, 24)
	# return (days, hours, minutes, seconds)

# #Specified date
# date1 = datetime.strptime('2015-01-01 01:00:00', '%Y-%m-%d %H:%M:%S')

# #Current date
# date2 = datetime.now()

# print("\n%d days, %d hours, %d minutes, %d seconds" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))
# print()

# #38. Write a Python program to get last modified information of a file. Go to the editor

# import os, time
# def last_modified_fileinfo(filepath):
	
	# filestat = os.stat(filepath)
	# date = time.localtime((filestat.st_mtime))

	# # Extract year, month and day from the date
	# year = date[0]
	# month = date[1]
	# day = date[2]
	# # Extract hour, minute, second
	# hour = date[3]
	# minute = date[4]
	# second = date[5]
	
	# # Year
	# strYear = str(year)[0:]

	# # Month
	# if (month <=9):
	    # strMonth = '0' + str(month)
	# else:
	    # strMonth = str(month)

	# # Date
	# if (day <=9):
	    # strDay = '0' + str(day)
	# else:
	    # strDay = str(day)

	# return (strYear+"-"+strMonth+"-"+strDay+" "+str(hour)+":"+str(minute)+":"+str(second))
# print()
# print(last_modified_fileinfo('test.txt'))
# print()

# #39. Write a Python program to calculate an age in year. Go to the editor

# from datetime import date

# def calculate_age(dtob):
    # today = date.today()
    # return today.year - dtob.year - ((today.month, today.day) < (dtob.month, dtob.day))
# print()
# print(calculate_age(date(2006,10,12)))
# print(calculate_age(date(1989,1,12)))
# print()

# #40. Write a Python program to get the current date time information. Go to the editor

# import time
# import datetime

# print()
# print("Time in seconds since the epoch: %s" %time.time())
# print("Current date and time: " , datetime.datetime.now())
# print("Alternate date and time: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))
# print("Current year: ", datetime.date.today().strftime("%Y"))
# print("Month of year: ", datetime.date.today().strftime("%B"))
# print("Week number of the year: ", datetime.date.today().strftime("%W"))
# print("Weekday of the week: ", datetime.date.today().strftime("%w"))
# print("Day of year: ", datetime.date.today().strftime("%j"))
# print("Day of the month : ", datetime.date.today().strftime("%d"))
# print("Day of week: ", datetime.date.today().strftime("%A"))
# print()

# #41. Write a python program to generate a date and time as a string. Go to the editor

# import datetime
# # Current time
# now = datetime.datetime.now()
# # Make a note of the date and time in a string
# # Date and time in string : 2016-11-05 11:24:24 PM
# datestr = "# In string: " + now.strftime("%Y-%m-%d %H:%M:%S %p") + "\n"
# print()
# print(datestr)
# print()

# #42. Write a Python program to display formatted text output of a month and start weeks on Sunday. Go to the editor

# import calendar
# cal = calendar.TextCalendar(calendar.SUNDAY)
# print('First Month - 2022')
# print(cal.prmonth(2022, 1))

# #43. Write a Python program to print a 3-column calendar for an entire year. Go to the editor

# import calendar
# cal = calendar.TextCalendar(calendar.SUNDAY)
# # year: 2022, column width: 2, lines per week: 1 
# # number of spaces between month columns: 1
# # 3: no. of months per column.
# print(cal.formatyear(2022, 2, 1, 1, 3))

# #44. Write a Python program to display a calendar for a locale. Go to the editor

# import calendar
# cal = calendar.LocaleTextCalendar(locale='en_AU.utf8')
# print(cal.prmonth(2025, 9))

# #45. Write a Python program to get the current week. Go to the editor

# import datetime
# Jan1st = datetime.date(2017,10,12)
# year,week_num,day_of_week = Jan1st.isocalendar() # DOW = day of week
# print()
# print("Year %d, Week Number %d, Day of the Week %d" %(year,week_num, day_of_week))
# print()

# #46. Write a Python program to create an HTML calendar with data for a specific year and month. Go to the editor

# import calendar
# htmlcal = calendar.HTMLCalendar(calendar.MONDAY)
# print(htmlcal.formatmonth(2020, 12))

# #47. Write a Python program display a list of the dates for the 2nd Saturday of every month for a given year. Go to the editor

# import calendar
# # Show every month
# for month in range(1, 13):
    # cal = calendar.monthcalendar(2020, month)
    # first_week  = cal[0]
    # second_week = cal[1]
    # third_week  = cal[2]

    # # If a Saturday presents in the first week, the second Saturday
    # # is in the second week.  Otherwise, the second Saturday must 
    # # be in the third week.
    
    # if first_week[calendar.SATURDAY]:
        # holi_day = second_week[calendar.SATURDAY]
    # else:
        # holi_day = third_week[calendar.SATURDAY]

    # print('%3s: %2s' % (calendar.month_abbr[month], holi_day))
	
# #48. Write a Python program to display a simple, formatted calendar of a given year and month. Go to the editor

# import calendar
# print('Print a calendar for a year and month:')
# month = int(input('Month (mm): '))
# year = int(input('Year (yyyy): '))
# print('\n')
 
# calendar.setfirstweekday(calendar.SUNDAY)
# cal = calendar.monthcalendar(year, month)
 
# if len(str(month)) == 1:
    # month = '0%s' % month
 
# # Header
# print('|++++++ %s-%s +++++|' % (month, year))
# print('|Su Mo Tu We Th Fr Sa|')
# print('|--------------------|')
 
# # display calendar
# border = '|'
# for week in cal:
    # line = border

      
    # for day in week:
        # if day == 0:
      # # 3 spaces for blank days       
         # line += '   ' 
        # elif len(str(day)) == 1:
            # line += ' %d ' % day
        # else:
         # line += '%d ' % day
    # # remove space in last column
    # line = line[0:len(line) - 1]  
    # line += border
    # print(line)
 
# print('|--------------------|\n')

# #49. Write a Python program to convert a string into datetime Go to the editor

# from datetime import datetime

# date_obj = datetime.strptime('May 12 2016  2:25AM', '%b %d %Y %I:%M%p')
# print()
# print(date_obj)
# print()

# #50. Write a Python program to get a list of dates between two dates. Go to the editor

# from datetime import timedelta, date

# def daterange(date1, date2):
    # for n in range(int ((date2 - date1).days)+1):
        # yield date1 + timedelta(n)

# start_dt = date(2015, 12, 20)
# end_dt = date(2016, 1, 11)
# for dt in daterange(start_dt, end_dt):
    # print(dt.strftime("%Y-%m-%d"))
	
# #51. Write a Python program to generate RFC 3339 timestamp. Go to the editor

# from datetime import datetime, timezone
# local_time = datetime.now(timezone.utc).astimezone()
# print()
# print(local_time.isoformat())
# print()

# #52. Write a Python program to get the first and last second. Go to the editor

# import datetime
# print("First Second: ", datetime.time.min)
# print("Last Second: ", datetime.time.max)

# #

# #

# #

# #

# #

# #
