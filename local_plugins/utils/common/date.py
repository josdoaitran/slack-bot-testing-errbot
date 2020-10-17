import datetime

def current_date():
    currentDT = datetime.datetime.now()
    return currentDT.strftime("%H%M%S")

def time_stamp():
    currentDT = datetime.datetime.now()
    return currentDT.strftime("%y-%m-%d")
