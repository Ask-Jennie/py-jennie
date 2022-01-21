import os

def check_if_angular_project(directory):
    search_files = [
        "angular.json", "karma.conf.js",
        "package.json"
    ]
    print ("Checking Project Type Directory for ", directory)
    is_angular = True
    for file in search_files:
        if not os.path.isfile(directory + file):
            is_angular = False

    return is_angular
