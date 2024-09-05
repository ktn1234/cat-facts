from time import sleep
from .services import CatFacts

def get_cat_facts_task(fail = False):
    response = CatFacts.get_fact()
    cat_fact = response['fact']
    sleep(5) # Simulate
    if fail:
        raise Exception('Failed to get cat fact')
    return cat_fact