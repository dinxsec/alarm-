import datetime
from playsound import playsound
alarmHour = int(input("enter Hour:  "))
alarmMin = int(input("enter Minutes:  "))
alarmAm = input("am / pm: ")

if alarmAm=="pm":
    alarmHour+=12

    while true:
        if alarmHour==datetime.datetime.now().hour and alarmMin==datetime.data.now().minute:
            print("playing...")
            playsound("")
            break
