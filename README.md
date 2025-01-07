# DDS File Sharing Application

This application is a CLI tool for sharing files over a Local Area Network (LAN) using the Data Distribution Service (DDS) protocol. It provides two main functionalities:

1. **Publish**: Distribute files across the network.
2. **Subscribe**: Retrieve published files to a local directory.

## Features
- Lightweight and efficient file sharing using DDS.
- Command-line interface for simplicity and flexibility.

## Getting Started

### Prerequisites
- Python 3.6 or later.
- Git for cloning the repository.
- Access to the python package registry via pip.

### Installation
1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/johnathaningle/cyclonedds-experiments.git
   cd cyclonedds-experiments
   ```
2. Install required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Publisher
To publish a file over the network:
```bash
python ./publisher.py
```

#### Subscriber
To subscribe and retrieve a file:
```bash
python ./subscriber.py "filename.ext" "C:/outputdir"
```
- Replace `filename.ext` with the name of the file you want to retrieve.
- Replace `C:/outputdir` with the path to the directory where you want the file saved.

### Example
1. Start the publisher on one machine:
   ```bash
   python ./publisher.py
   ```
2. On another machine, subscribe to the file:
   ```bash
   python ./subscriber.py "example.txt" "./downloads"
   ```

## Continuous Integration and Deployment (CI/CD)
This project uses GitLab CI/CD for automated builds and testing. You can view the pipeline status here:
[GitLab CI/CD Pipeline](https://gitlab.com/tangomonstor/cyclonedds-experiments/)

[![GitLab CI/CD Status](https://gitlab.com/tangomonstor/cyclonedds-experiments/badges/master/pipeline.svg)](https://gitlab.com/tangomonstor/cyclonedds-experiments/-/pipelines)

## Repository Links
- **Development Repository (GitHub):** [GitHub - cyclonedds-experiments](https://github.com/johnathaningle/cyclonedds-experiments)
- **CI/CD Pipeline (GitLab):** [GitLab - cyclonedds-experiments](https://gitlab.com/tangomonstor/cyclonedds-experiments/)



