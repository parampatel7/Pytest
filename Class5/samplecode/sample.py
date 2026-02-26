import json

#Read:
#https://docs.pytest.org/en/stable/reference/reference.html#std-fixture
#Saving dictionary as a json object at given filepath
def save_dict(_dict, filepath):
        json.dump(_dict, open(filepath, 'w'))
        print("saved")