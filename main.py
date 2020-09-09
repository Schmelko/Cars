from log import Log

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

print(log2)

print(log2.findlastcar1())

print(log2.findentriesbyday('6'))

print(log2.findinboundentriesbylastdayofmonth('30'))

print(log2.plates_unique())

