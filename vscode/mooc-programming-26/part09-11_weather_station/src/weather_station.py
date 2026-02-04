# WRITE YOUR SOLUTION HERE:

class WeatherStation:
    def __init__(self, name: str):
        self.__name = name
        self.__obserwations = []
    
        
    def add_observation(self, observation: str):
        self.__obserwations.append(observation)
    
    def latest_observation(self) -> str:
        index = len(self.__obserwations)
        if index == 0:
            return ""
        return self.__obserwations[index-1]
    
    def number_of_observations(self) -> int:
        return len(self.__obserwations)
    
    def __str__(self):
        return f'{self.__name}, {self.number_of_observations()} observations'
    
    
if __name__ == "__main__": 
    station = WeatherStation("Houston")
    station.add_observation("Rain 10mm")
    station.add_observation("Sunny")
    print(station.latest_observation())

    station.add_observation("Thunderstorm")
    print(station.latest_observation())

    print(station.number_of_observations())
    print(station)