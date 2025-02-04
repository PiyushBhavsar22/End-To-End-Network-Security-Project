from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]: #This will return list of requirements
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt", "r") as file: # Read lines from file
            lines=file.readlines() # Process each line
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!= '-e .': # Ignore empty lines and e .
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("No requirements.txt file found")
    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author="Piyush Bhavsar",
    author_email="piyushproject.main@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)    


