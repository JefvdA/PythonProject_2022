import json
import os
import random


FIRSTNAMES_JSON = "assets/first-names.json"
LASTNAMES_JSON = "assets/last-names.json"

DIRNAME = os.path.dirname(__file__)
FIRSTNAMES_JSON_PATH = os.path.join(DIRNAME, FIRSTNAMES_JSON)
LASTNAMES_JSON_PATH = os.path.join(DIRNAME, LASTNAMES_JSON)


def generate_firstname():
    # 5493 possible firstnames
    firstnames = []
    with open(FIRSTNAMES_JSON_PATH) as json_file: 
        firstnames = json.load(json_file)
    return random.choice(firstnames)

def generate_lastname():
    # 88798 possible lastnames
    lastnames = []
    with open(LASTNAMES_JSON_PATH) as json_file: 
        lastnames = json.load(json_file)
    return random.choice(lastnames)

def generate_name():
    # With the 5493 firstnames and 88798 lastnames -> 5493*88798 = 487.767.414 possible combinations
    firstnames = []
    lastnames = []
    with open(FIRSTNAMES_JSON_PATH) as json_file: 
        firstnames = json.load(json_file)
    with open(LASTNAMES_JSON_PATH) as json_file:
        lastnames = json.load(json_file)

    return random.choice(firstnames) + " " + random.choice(lastnames)

def generate_names(amount):
    # With the 5493 firstnames and 88798 lastnames -> 5493*88798 = 487.767.414 possible combinations
    firstnames = []
    lastnames = []
    with open(FIRSTNAMES_JSON_PATH) as json_file: 
        firstnames = json.load(json_file)
    with open(LASTNAMES_JSON_PATH) as json_file:
        lastnames = json.load(json_file)
    
    # Generate names with the data read from the JSON files
    names = []
    for i in range(amount):
        firstname = random.choice(firstnames)
        lastname = random.choice(lastnames)
        names.append(firstname + " " + lastname)
    return names
            