from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description  = f.read()

setup(
    name='QL1D',
    version='0.2.0',
    packages=find_packages(),
    install_requires=[
        'numpy>=2.4.4'
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)
