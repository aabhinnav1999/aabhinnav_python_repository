import datetime

def gives_date():
    return datetime.datetime.now().date()

def gives_time():
    return str(datetime.datetime.now().time())[0:8]