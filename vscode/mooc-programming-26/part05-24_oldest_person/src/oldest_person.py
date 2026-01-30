def oldest_person(people: list) -> str:
    
    oldest_name = people[0][0]
    min_year = people[0][1]
    for person in people:
        name, year = person[0], person[1]
        if min_year > year:
            min_year = year
            oldest_name = name
    
    return oldest_name
    
# p1 = ("Adam", 1977)
# p2 = ("Ellen", 1985)
# p3 = ("Mary", 1953)
# p4 = ("Ernest", 1997)
# people = [p1, p2, p3, p4]
# print(oldest_person(people))