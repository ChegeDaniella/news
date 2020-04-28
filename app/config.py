#general configuration parent class
class Config:
    '''
    general configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?country=us&apiKey={}'
    TOP_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    

#production configuration child class
class ProdConfig(Config):
    '''
    production configuration child class
    '''
    pass

#developmnet configuration child class
class DevConfig(Config):
    '''
    developmnet configuration child class
    '''
    
    DEBUG = True