from setuptools import find_packages,setup
from typing import List

hypen_e_dot ='-e .'  # we craete a constant for this because we use this in req.txt to trigger the setup file
def get_requirements(file_path:str)->List[str]:# you give the file name as file_path which is string and return output as list 
	'''The function will return list of requirements'''
			
	requiremts = []
			
	with open(file_path) as file_obj:
		requirements = file_obj.readlines()  # while using readlines \n is also read so we replace it with empty string
		requirements = [req.replace('\n','') for req in requirements]

		# but donot want the '-e .' also to be listed there in the requiremts lisz

		if hypen_e_dot in requirements:
			requirements.remove(hypen_e_dot)
	return requirements

# This is the basic setup
setup(
name= 'mlproject',
version = '0.0.1',
author= 'rajalakshmi',
author_email= 'rajalakshmibharath22@gmail.com',
packages= find_packages(),
install_requires= get_requirements('requirements.txt')
)