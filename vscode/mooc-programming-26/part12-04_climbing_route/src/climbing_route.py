class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution herer:

def sort_by_length(routes: list) -> list:
    def odered_by_length(route: ClimbingRoute):
        return route.length
    return sorted(routes, key=odered_by_length, reverse=True)

def sort_by_difficulty(routes: list) -> list:
    def odered_by_difficulty(route: ClimbingRoute):
        return (route.grade, route.length)
    return sorted(routes, key=odered_by_difficulty, reverse=True)   

if __name__ == "__main__":
    r1 = ClimbingRoute("Small steps", 13, "6A+")
    r2 = ClimbingRoute("Edge", 38, "6A+")
    r3 = ClimbingRoute("Bukowski", 9, "6A+")
    reply = sort_by_difficulty([r1, r2, r3])

    for route in reply:
        print(route)