import psutil

battery = psutil.sensors_battery()

if battery is not None:
    print(f"Battery Percentage: {battery.percent}%")
    print(f"Power plugged in: {battery.power_plugged}")


    def convertTime(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)
    
    print(f"Battery remaining time: ", convertTime(battery.seceleft))

else:
    print("No battery information available")
