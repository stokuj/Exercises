# Write your solution here:

class Series():
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []
        self.avg_grade = 0
        
    def __str__(self):
        about = f"{self.title} ({self.seasons} seasons)\n" 
        about = about + 'genres: ' + ", ".join(self.genres)
        
        if len(self.ratings) == 0:
            about += '\nno ratings'
        else:
            about += '\n' + f'{len(self.ratings)} ratings, average {self.avg_grade:.1f} points'
            
        return about

    def rate(self, n: int):
        self.ratings.append(n)
        self.avg_grade = sum(self.ratings)/len(self.ratings)
        
def minimum_grade(rating: float, series_list: list) -> list:
    return [series for series in series_list if series.avg_grade >= rating ]
        

def includes_genre(genre: str, series_list: list) -> list:
    return [series for series in series_list if genre in series.genres]

if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)