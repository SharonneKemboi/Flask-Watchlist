from distutils.debug import DEBUG

from app.instance.config import MOVIE_API_KEY


class Config:
    
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'



class ProdConfig(Config):
    pass



class DevConfig(Config):
    
     DEBUG = True

