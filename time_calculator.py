def add_time(start, duration, day_of_the_week="off"):
  dayofweek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
  timeofday = ""
  hours = ""
  minutes = ""
  day = ""
  daycount = 0

  timearray = start.split()
  timeofday = timearray[1]

  splitstarttime = timearray[0].split(":")
  starthour = int(splitstarttime[0])
  startmin = int(splitstarttime[1])

  splitduration = duration.split(":")
  durationhour = int(splitduration[0])
  durationmin = int(splitduration[1])

  #add all of the minutes together
  minutes = startmin + durationmin
  while(minutes>=60):
    minutes-=60
    starthour+=1
  if(minutes<10):
        minutes = '0' + str(minutes)
  if(starthour==12):
      if (timeofday=='AM'):
        timeofday='PM'
      elif (timeofday=='PM'):
        timeofday='AM'
        daycount+=1
  elif(starthour==13):
    starthour-=12

  while(durationhour>0):
    starthour+=1
    durationhour-=1
    if(starthour==12):
      if (timeofday=='AM'):
        timeofday='PM'
      elif (timeofday=='PM'):
        timeofday='AM'
        daycount+=1
    elif(starthour==13):
      starthour-=12


  hours = starthour

  #figure out time of the week
  if not (day_of_the_week=='off'):
    day = day_of_the_week
    day = day.capitalize()
    day_index = dayofweek.index(day)
    day_index+=daycount
    while(day_index>len(dayofweek)-1):
      day_index-=7
    dayresult = dayofweek[day_index]

    newtime = str(hours) + ":" + str(minutes) + " " + timeofday + ", " + dayresult
    if (daycount==1):
      newtime = str(hours) + ":" + str(minutes) + " " + timeofday + ", " + dayresult + " (next day)"
    elif(daycount>1):
      newtime = str(hours) + ":" + str(minutes) + " " + timeofday + ", " + dayresult + " (" + str(daycount) + " days later)"

    return newtime


  newtime = str(hours) + ":" + str(minutes) + " " + timeofday
  if (daycount==1):
    newtime = str(hours) + ":" + str(minutes) + " " + timeofday + " (next day)"
  elif(daycount>1):
    newtime = str(hours) + ":" + str(minutes) + " " + timeofday + " (" + str(daycount) + " days later)"

  return newtime
