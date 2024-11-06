from setuptools import setup, find_packages

# Utility function to read the requirements.txt file
def parse_requirements(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line and not line.startswith('#')]

description = None
with open("README.md", "r") as file:
    description = file.read().splitlines()[1]

setup(
    name='mi_py_sql',               # Replace with your package's name
    version='0.1.0',
    packages=find_packages(),        # Automatically find sub
    #install_requires=["setuptools", "git+https://github.com/MichaelMueller/mi_py_test_lib.git"],#parse_requirements('requirements.txt'),
    author='Michael Mueller',
    author_email='michaelmuelleronline@gmx.de',
    description=description,
    url='https://github.com/MichaelMueller/mi_py_sql_lib.git',  # Link to your repository
)
