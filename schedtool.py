"""
This script will be used for building out the Digital Support schedule.
"""
from calendar import Calendar
import datetime
import json

MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
YEAR = 2025

class tournament(object):
    def __init__(self, name, id, startDate, endDate) -> None:
        self.name = name
        self.id = id
        self.start_date = startDate
        self.end_date = endDate
        self.url = tournament.buildURL(name, id)
        self.activeState = self.isActive()
        print("active state = " + str(self.activeState))
    
    def isActive(self) -> bool:
        curDay = datetime.date.today()
        curWeek = curDay.isocalendar().week
        print(curWeek)
        print()

        if (self.start_date.isocalendar().week or self.end_date.isocalendar().week) == curWeek:
            return True
        return False

    def buildURL(name, id):
        nameHolder = []
        for char in name:
            if char != " ":
                nameHolder.append(char)
            else:
                nameHolder.append("-")
        formatted_name = "".join(nameHolder)
         #test print - print(formatted_name)



class employee(object):
    pass

def insertTournament(tourn):
    pass

def main():
    # create calendar instance to build out months and weeks with.
    cal = Calendar()
    months = dict.fromkeys(MONTHS)
    testTourn = tournament("The Sentry Test", "R2024054", datetime.date(2025, 8, 23), datetime.date(2025, 8, 30))

    # loop to build out calendar

    for month in MONTHS:
        months[month] = cal.monthdatescalendar(YEAR, MONTHS.index(month) + 1)
    
    #print(months)
    
    """
    Calendar is built out for current YEAR. Now need to collect tournament data from source file or API call and parse it.
    Once tournament data is collected and parsed, loop through all tournaments and insert them into the calendar.
    """
    
    try:
        with open('r_schedule_2025', 'r') as fStream:
            data = json.load(fStream)
            # Need to check to ensure data is properly captured (isinstance)
            # Then need to traverse through the json data and build out tournament objects.
            # Once the tournament object is created, add it into the tournaments list for storage.
            

    

if __name__ == "__main__":
    main()
