from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="StayPredictorOps",
    version="0.1",
    author="Sahil Rahate",
    author_email="sahilrahate567@gmail.com",
    packages=find_packages(),
    install_requires = requirements,
)