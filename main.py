from log import Log

def format1_task5(log):
    for key, value in log.items():
        print('{} {} km'.format(key, value))

def format2_task5(log):
    for key, value in log.items():
        print('{}: {}km'.format(key, value))

def print_task7(driving_log):
    for entry in driving_log['entries']:
        print("{}\t{}.\t{}\t{} km\t{}.\t{}\t{} km".format(
            entry['person_id'],
            entry['start']['day'],
            entry['start']['time'],
            entry['start']['odometer'],
            entry['end']['day'],
            entry['end']['time'],
            entry['end']['odometer']))

lines = [
    
    '5 07:30 CEG300 590 30580 0',
    '5 14:16 CEG300 590 30656 1',
    '5 17:00 CEG300 534 30656 0',
    '5 19:03 CEG300 534 30784 1' 
]

log1 = Log(lines)
print(log1)

with open('autok.txt') as f:
    lines2 = f.readlines()
    log2 = Log(lines2)
"""
print(log2)

print(log2.findlastcar1())

print(log2.findentriesbyday('6'))

print(log2.findinboundentriesbylastdayofmonth())

print(log2.plates_unique())

print(log2.plates_lastoutboundentriesbyendofmonth())

print(log2.findCarsNotInGarageOnEndOfMonth())

result_task5 = log2.find_distance_in_month_by_plate1()
 
format1_task5(result_task5)
format2_task5(result_task5)
print(log2.find_max_distance_by_plate_and_person())
"""

result = log2.create_driving_log_by_plate('CEG300')
print(result)

print(print_task7(result))