from functools import lru_cache
FIVE_NAMES = [ "VAISHNAVI" , "OM" ,"RAM"]

AGES = [19,18,16]

MAP_NAMES_TO_AGES = dict(zip(FIVE_NAMES, AGES))

def average_age():
    return sum(AGES) / len(AGES)

def fibonacci():
    if n== 0:
        return 0
    elif n== 1:
        return 1
    else:   
        return fibonacci(n-1) + fibonacci(n-2)
    
@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n== 0:
        return 0
    elif n== 1:
        return 1
    else:   
        return fibonacci_memo(n-1) + fibonacci_memo(n-2)
    
LAST_NAMES = ["VAISHNAVI", "OM", "RAM"]
