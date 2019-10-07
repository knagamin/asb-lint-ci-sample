from setuptools import setup, find_packages

setup(name="myasblintrules",
      packages=find_packages(include=['rules', 'rules.*']),
#      package_dir = {'': 'rules'}
    
     )
