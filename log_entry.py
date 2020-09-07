class LogEntry:
    '''One log entry.'''

    def __init__(self, line):
        raw = line.split()
        self.day, self.time, self.plate, self.person_id, self.odometer, self.direction = raw
    
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
        