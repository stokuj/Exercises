# Write your solution here
from datetime import *

day = int(input('Day: '))
month = int(input('Month: '))
year = int(input('Year: '))

born = datetime(year, month, day)
reference = datetime(1999, 12, 31)
diff = reference-born

if diff.days > 0:
    print(f'You were {diff.days} days old on the eve of the new millennium.')
else:
    print(f'You weren\'t born yet on the eve of the new millennium.')