

def max_customers(arrivals, departures):
    events = []
    for time in arrivals:
        events.append((time, 1))
    for time in departures:
        events.append((time, 2))
    events.sort()
    
    counter = 0
    result = 0
    for event in events:
        if event[1] == 1:
            counter += 1
        else:
            counter -= 1
        result = max(result, counter)
    return result


arrivals = [6, 3, 6, 1, 2]
departues = [8, 7, 9, 5, 8]
print(max_customers(arrivals, departues))