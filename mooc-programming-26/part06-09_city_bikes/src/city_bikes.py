# tee ratkaisu tänne
import math

def get_station_data(filename: str) -> dict:
    with open(filename) as file:
                        # (0, 1)           # 2    #3      # 4           # 5          # 6
        stations = {}   # [[localisation], [FID], [name], [total_slot], [operative], [id]]
        next(file)
        for line in file:
            parts = line.split(';')
            longitude = float(parts[0])
            latitude = float(parts[1])
            station_name = parts[3]
            stations[station_name] = (longitude, latitude)
            
    return stations

def distance(stations: dict, station1: str, station2: str) -> float:
    longitude1, latitude1 = stations[station1]
    longitude2, latitude2 = stations[station2]
    
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km
    
def greatest_distance(stations: dict) -> tuple:
    max_distance = 0
    max_station_name1 = ''
    max_station_name2 = ''
    
    for station1 in stations:
        for station2 in stations:
            current_distance = distance(stations,station1, station2)
            if current_distance > max_distance:
                max_distance = current_distance
                max_station_name1 = station1
                max_station_name2 = station2
    return (max_station_name1, max_station_name2, max_distance)             
                
    
if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)