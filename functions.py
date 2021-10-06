import datetime

def greet():
    #Get current time
    dt = datetime.datetime.now()
    
    if dt.hour <= 11:
        greeting = "morning!"
    elif dt.hour <= 17:
        greeting = "afternoon!"
    else:
        greeting = "night"
        
    print(f"Hello, good {greeting}.")
    
    
greet()