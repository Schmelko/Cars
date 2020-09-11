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
    
    def findinboundentriesbylastdayofmonth(self):
         return [str(entry.plate) for entry in self.entries if entry.day == '30' and entry.direction == '1']

    def plates_unique(self):
        return set(entry.plate for entry in self.entries)

    def plates_lastoutboundentriesbyendofmonth(self):
        i = len(self.entries)-1
        last_entry = self.entries[i]
        return set(last_entry.plate for last_entry in self.entries if last_entry.direction !='1')
    
    def findDirectionOnEndOfMonthByPlate(self, plate):
        entries = tuple(entry for entry in self.entries if entry.plate == plate)
        lastEntry = entries[-1]
        return lastEntry.direction
    
    def findCarsNotInGarageOnEndOfMonth(self):
        plates = self.plates_unique()
        directionsByPlate = {plate:self.findDirectionOnEndOfMonthByPlate(plate) for plate in plates}
        result = tuple(plate for plate, direction in directionsByPlate.items() if direction == '0')
        return result