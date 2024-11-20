from setuptools import find_packages, setup
from typing import List


def get_requirements(filename:str)->List[str]:
    """Return a list of requirements from a file.

    The file is expected to have one requirement per line.
    
    Parameters
    ----------
    filename : str
        The name of the file to read the requirements from.

    Returns
    -------
    list
        A list of requirements.
    """
    with open(filename) as f:
        req = f.read().splitlines()

    if "-e ." in req:
        req.remove("-e .")

    return req


setup(
    name='End to End Ml Project',
    packages=find_packages(),
    version='0.0.1',
    author='Overowser',
    author_email="ben-ghali@hotmail.com",
    install_requires=get_requirements('requirements.txt')
)