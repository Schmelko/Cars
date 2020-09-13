class LogEntry:
    '''One log entry.'''

    def __init__(self, line):
        raw = line.split()
        self.day = int(raw[0])
        self.time = raw[1]
        self.plate = raw[2]
        self.person_id = int(raw[3])
        self.odometer = int(raw[4])
        self.direction = int(raw[5])
  
    def __str__(self):
        format = "Day: {} Time: {} Plate: {} Person ID: {} Odometer: {} Direction: {}"
        direction = {'0': 'Outbound', '1': 'Inbound'}[self.direction]
        return format.format(
            self.day, 
            self.time, 
            self.plate, 
            self.person_id, 
            self.odometer, 
            direction)
    
    def __eq__(self, other):
        return (self.day == other.day 
            and self.time == other.time 
            and self.plate == other.plate 
            and self.person_id == other.person_id 
            and self.odometer == other.odometer 
            and self.direction == other.direction)
        