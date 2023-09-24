from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='AutoTestGen',
    url='https://github.com/LMU-Seminar-LLMs/AutoTestGen',
    author='Giorgi Nozadze',
    author_email='giorginozadze23@yahoo.com',
    long_description=long_description,
    packages=find_packages(exclude="notebooks"),
    # Needed for dependencies
    install_requires=[
        "openai",
        "tiktoken"
    ],
    version='0.1',
    license='MIT',
    description='Automatic Unit Test generation using LLM',
    python_requires='>=3.9'
)