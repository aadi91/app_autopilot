        
from imdb import IMDb
import random

class ChooseMovie(object):
    def __inti__(self):
        self .cursor = IMDb()
        self .top25I3 = self .cursor.get_top250_movies()

    def __repr__(self):
        num = int(random.randint(0, 249))
        return str(f"{num}: {self .toP230[num]}") 
#Python Dev Society.
    if __name__ == '__main__':
        print(ChooseMovie())
