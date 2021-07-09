
import time
import winsound as ws
import datetime as dt

print("Alarm using Python..")

def myAlarm():   
    a = time.localtime()
    a = dt.datetime.fromtimestamp(time.mktime(a))
    time_a = input("Enter Time in format  %Y/%m/%d  %H:%M:%S ie.(2016/11/11 12:20:21)")
    alarmTime = dt.datetime.strptime(time_a,"%Y/%m/%d  %H:%M:%S")

    time.sleep(abs(alarmTime.minute - a.minute)*60)

    print(alarmTime.minute - a.minute,a,alarmTime)
    
    ws.Beep(3000,4000)
  
myAlarm()