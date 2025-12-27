from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    """
    this function will return th elist of requirements 

    """
    requirements_list =[]
    try:
        with open('requirements.txt','r') as file:
            #read lines from file
            lines = file.readlines()
            #process the lines
            for line in lines:
                requirement = line.strip()
                #ignore the empty line and -e .
                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    
    except FileNotFoundError:
        print("requirements.txt not found ")

    return requirements_list

setup(
    name = "network_security",
    version = "0.0.1",
    author = "Rushi",
    author_email = "rushi@example.com",
    packages = find_packages(),
    install_requires = get_requirements()
)