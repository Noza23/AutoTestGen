# AutoTestGen

[![LMU: Munich](https://img.shields.io/badge/LMU-Munich-009440.svg)](https://www.en.statistik.uni-muenchen.de/index.html)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

AutoTestGen uses Large Language Models (OpenAI chat completion model endpoints) to analyze code segments and autonomously generate unit tests.
It was developed as part of the **Practical Applications for Large Language Models** seminar at LMU Munich under the guidance and supervision of Martin Binder.

## Prerequisites

Before you can use this application, make sure you have the following prerequisites installed on your system:

1. **Docker**: Ensure that you have Docker installed. You can download and install Docker from [Docker's official website](https://www.docker.com/get-started).

2. **Python 3.9+ Docker Image**: This application requires any Docker image containing Python version 3.9 or higher. It is required to provide an isolated environment and avoid executing potentially malicious code generated by the LLM on your local machine.
If you don't have your custom image already do the following:

- Use provided [Dockerfile](./Dockerfile) to build a custom image, which additionally installs *coverage* package used in the application for measuring python code coverage. You are free to add other packages which the project you want to test requires. To build the image, run the following command: 
    ```sh
    docker build -t auto-test-gen:latest .
    ```

## Installation
To get started with this application, follow these simple installation steps:
```sh
# Clone the repository
git clone git@github.com:LMU-Seminar-LLMs/AutoTestGen.git

# Change into the project directory
cd AutoTestGen

# Install the AutoTestGen package
pip install .

# Run the application
autotestgen
```

## Usage



