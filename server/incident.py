import json


def open_file(filename):
    """Read JSON file content as UTF8 encoding."""
    with open(filename, encoding='utf-8') as json_file:
        return json.load(json_file)


def get_dog_info():
    """Return a list of all reported coordinates."""
    data = open_file('incidents.json')
    dog_info = []
    for i in data['data']:
        dog_info.append(i)
    return dog_info

 



    
