from setuptools import setup

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="dvc_with_ML_experiment",
    version= "0.0.1",
    author= "AAZZIOUI",
    description= "A small package for dvc ML demo",
    long_description= long_description,
    long_description_content_type = "text/markdown",
    url= "https://github.com/AAZZIOUI/dvc_ml",
    packages=["src"],
    license= "GNU",
    python_requires= ">=3.7",
    install_requires= [
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)