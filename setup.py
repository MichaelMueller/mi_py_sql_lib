from setuptools import setup, find_packages

# Utility function to read the requirements.txt file
def parse_requirements():
    with open("requirements.txt", "r") as file:
        return [line.strip() for line in file if line and not line.startswith('#')]

def parse_description_from_readme() -> str:
    with open("README.md", "r") as file:
        return file.read().splitlines()[1]

setup(
    name='mi_py_sql',               # Replace with your package's name
    version='0.1.1',
    packages=find_packages(),        # Automatically find sub
    install_requires=parse_requirements(),
    author='Michael Mueller',
    author_email='michaelmuelleronline@gmx.de',
    description=parse_description_from_readme(),
    url='https://github.com/MichaelMueller/mi_py_sql_lib.git',  # Link to your repository
)
