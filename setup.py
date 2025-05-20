from setuptools import setup,find_packages
from pathlib import Path
import sys

#to remove -e . as text from the text file

hyphen_e_dot = "-e ."
#create a function to get the requirements from the text file
def get_requirements(file: str) -> list[str]:
    """
    The above function returns the list of libraries installed in the text file.
    """
    requirements_list: list[str]= []    #list out the requirements
    with open(file) as f:   #  open the text file 
         file_lines: list[str] = f.readlines() # load each line of the text file a library
         requirements_list = [req.replace("\n", "") for req in file_lines] #separate end of the lines with empty space
         if hyphen_e_dot in requirements_list:
             requirements_list.remove(hyphen_e_dot)
    return requirements_list  # provide the required list



setup(
    name = "End to end Predictive ML project",
    version = "0.0.1",
    author = "Sylvan",
    authors_email ="sylvaneurons@gmail.com",
    packages = find_packages(),
    install_requirements =get_requirements("requirements.txt"),  #called the function to get the text file

)