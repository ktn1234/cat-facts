import requests

class CatFacts:
    base_url = 'https://catfact.ninja'

    @staticmethod
    def get_fact() -> str:
        response = requests.get(f'{CatFacts.base_url}/fact')
        if response.status_code != 200:
            return 'Could not fetch a random cat fact. Please try again later.'
        
        return response.json()
    
    
    @staticmethod
    def get_facts() -> str:
        response = requests.get(f'{CatFacts.base_url}/facts?limit=1000')
        if response.status_code != 200:
            return 'Could not fetch cat facts. Please try again later.'
        
        return response.json()
    
    @staticmethod
    def get_breeds() -> str:
        response = requests.get(f'{CatFacts.base_url}/breeds?limit=1000')
        if response.status_code != 200:
            return 'Could not fetch cat breeds. Please try again later.'
        
        return response.json()