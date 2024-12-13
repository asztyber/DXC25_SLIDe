# Use a specific Ubuntu version
FROM ubuntu:22.04

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC

# Update the system and install Python 3.11 and pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.11 \
    python3.11-venv \
    python3.11-distutils \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.11 as the default Python
RUN ln -sf /usr/bin/python3.11 /usr/bin/python && \
    ln -sf /usr/bin/pip3 /usr/bin/pip

# Set up a virtual environment and install dependencies
WORKDIR /app
COPY requirements.txt /app/
RUN python3.11 -m venv /venv && \
    /venv/bin/pip install --no-cache-dir -r requirements.txt

# Set the PATH to use the virtual environment
ENV PATH="/venv/bin:$PATH"

# Copy the current directory contents into the container
COPY . .


# Set the entry point to Python
ENTRYPOINT ["python"]
