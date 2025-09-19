'''
 the setup.py file is an essential component of a Python project, used for packaging and distributing the project. It typically contains metadata about the
 project, such as its name, version, author, and 
 dependencies. The setup.py file is executed using the 
 Python interpreter to install the package and its dependencies.
 used by steuptools or distutils to facilitate the packaging process.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements() -> List[str]:
    """"
    thiss function will return the list of requirements
    """

    requirement_lst:List[str] = []  
    try:
        with open("requirements.txt", "r") as file:
            # read the lines from the file
            lines = file.readlines()
            #process  each line 
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e aswell
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Rushikesh",
    author_email="rushikeshukhade@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)