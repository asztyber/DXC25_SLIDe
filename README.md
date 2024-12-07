# Competition Setup Guide

This guide will walk you through setting up and running the competition environment using Docker on both Ubuntu and Windows. The repository contains a Dockerfile, a Python class interface, and an evaluation script to ensure consistent evaluation for all participants.

## Prerequisites
- [Docker](https://docs.docker.com/get-docker/) installed on your machine (instructions provided below).
- Git installed to clone the repository.

### Docker Installation

#### Ubuntu
1. **Update your system**:
   ```bash
   sudo apt update
   ```

2. **Install Docker**:
   ```bash
   sudo apt install docker.io
   ```

3. **Start and Enable Docker**:
   ```bash
   sudo systemctl start docker
   sudo systemctl enable docker
   ```

4. **Add your user to the Docker group** (optional, for running Docker without `sudo`):
   ```bash
   sudo usermod -aG docker $USER
   ```
   After this, log out and log back in for changes to take effect.

#### Windows
1. **Download Docker Desktop** from [Docker's official website](https://www.docker.com/products/docker-desktop).
2. **Install Docker Desktop** and follow the on-screen instructions.
3. **Enable WSL2 Integration** (recommended):
   - Open Docker Desktop settings.
   - Navigate to "Resources" > "WSL Integration" and enable integration for your desired WSL2 distributions.
4. **Verify Installation**:
   Open PowerShell or Command Prompt and run:
   ```powershell
   docker --version
   ```

## Repository Setup
1. **Clone the Repository**:
   ```bash
   git clone git@github.com:asztyber/DXCdockerDummyExample.git
   cd DXCdockerDummyExample
   ```

2. **Files Overview**:
   - `Dockerfile`: Defines the Docker image for the competition.
   - `base_class.py`: The base class interface for participants.
   - `evaluation_script.py`: The script used to evaluate participant submissions.
   - `requirements.txt`: Contains required Python packages.

## Running the Environment

### Build the Docker Image

In the directory where the Dockerfile is located, build the Docker image:

```bash
docker build -t competition_env .
```

### Running the Evaluation

To run the evaluation, mount the current directory and specify input and output files.

#### Ubuntu
```bash
docker run -v "$(pwd):/app" --network none competition_env evaluation_script.py input.txt output.txt
```

#### Windows (PowerShell)
```powershell
docker run -v "${PWD}:/app" --network none competition_env evaluation_script.py input.txt output.txt
```

By using --network none, the container will be completely isolated from the network, ensuring it cannot connect to the internet or any external network.

### Input and Output
- **Input File**: `input.txt` (must be placed in the current directory).
- **Output File**: After running the command, `output.txt` will be created in the same directory.

## Participants' Instructions
1. **Implement the Class**:
   - Use `base_class.py` as a reference.
   - Implement your solution in a new Python file (e.g., `participant_processor.py`).
2. **Requirements**:
   - If your solution requires additional Python libraries, list them in `requirements.txt`.

## Example Participant Implementation
Here is an example implementation of the class:

```python
# participant_processor.py
from base_class import BaseProcessor

class ParticipantProcessor(BaseProcessor):
    def process_input(self, input_data: str) -> str:
        # Example: Convert the input data to uppercase
        return input_data.upper()
```


