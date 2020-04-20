from setuptools import setup, find_packages

setup(
    name='Eskom_Predict',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='ESKOM predict',
    long_description=open('README.md').read(),
    install_requires=['numpy','pandas'],
    url='https://github.com/Xenaschke/Eskom_Predict.git',
    author='Team 3'
    )
