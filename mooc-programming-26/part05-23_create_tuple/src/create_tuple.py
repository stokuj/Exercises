def create_tuple(x: int, y: int, z: int) -> tuple:
    sum_ = x + y + z
    return (min(x, y, z), max(x, y, z), sum_)



if __name__ == "__main__":
    print(create_tuple(5, 3, -1))