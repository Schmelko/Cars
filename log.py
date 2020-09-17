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
        return [entry for entry in self.entries if entry.day == day]
    
    def findinboundentriesbylastdayofmonth(self):
         return [str(entry.plate) for entry in self.entries if entry.day == '30' and entry.direction == '1']

    def plates_unique(self):
        return set(entry.plate for entry in self.entries)

    def persons_unique(self):
        return set(entry.person_id for entry in self.entries)
    
    def findDirectionOnEndOfMonthByPlate(self, plate):
        entries = tuple(entry for entry in self.entries if entry.plate == plate)
        lastEntry = entries[-1]
        return lastEntry.direction
    
    def findCarsNotInGarageOnEndOfMonth(self):
        directionsByPlate = {plate:self.findDirectionOnEndOfMonthByPlate(plate) for plate in self.plates_unique()}
        return tuple(plate for plate, direction in directionsByPlate.items() if direction == 0)
    
    def find_distance_in_month_by_plate1(self):
        distances = dict()
        for plate in self.plates_unique():
            entries = tuple(entry for entry in self.entries if entry.plate == plate)
            first, last = entries[0].odometer, entries[-1].odometer
            distances[plate] = last - first
        
        return distances

    def find_distance_in_month_by_plate2(self):
        return {plate: self.calculate_distance_by_plate(plate) for plate in self.plates_unique()}
        
    def calculate_distance_by_plate(self, plate):
        entries = tuple(entry for entry in self.entries if entry.plate == plate)
        first, last = entries[0].odometer, entries[-1].odometer
        return last - first

    def find_max_distance_by_plate_and_person(self):
        distances = dict()
        for plate in self.plates_unique():
            for person_id in self.persons_unique():
                entries = tuple(entry for entry in self.entries if entry.plate == plate and entry.person_id == person_id)
                if entries:
                    distances[plate, person_id] = self.calculate_max_distance(entries)

        person_id, distance = 1, float('-inf')
        for key, value in distances.items():
            if value > distance:
                person_id, distance = key[1], value

        return person_id, distance

    def calculate_max_distance(self, entries):
        if len(entries) < 2:
            return float('-inf')
        if entries[0].direction == 1:
            entries = entries[1:]
        if entries[-1].direction == 0:
            entries = entries[:-2]
        if len(entries) < 2:
            return float('-inf')
        
        distances = self.calculate_distances(entries)
        return max(distances)

    def calculate_distances(self, entries):
        distances = []
        while len(entries) >= 2:
            distances.append(entries[1].odometer - entries[0].odometer)
            entries = entries[2:]

        return tuple(distances)
