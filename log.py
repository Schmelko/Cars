from log_entry import LogEntry

class Log:
    
    def __init__(self, lines):
        self.entries = [LogEntry(line) for line in lines]

    def __str__(self):
        return "{} entries in log".format(len(self.entries))

    def findlastcar1(self):
        index = len(self.entries) - 1
        last_entry = self.entries[index]
        return last_entry.day, last_entry.time, last_entry.plate

    def findentriesbyday(self, day):
        return [str(entry) for entry in self.entries if entry.day == day]
    
    def findinboundentriesbylastdayofmonth(self, day):
         return [str(entry.plate) for entry in self.entries if entry.day == day and entry.direction == '1']

    def plates_unique(self):
        return [set(entry.plate for entry in self.entries)]

    

 
