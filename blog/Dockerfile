# Use an official Python runtime as a parent image
FROM ubuntu:bionic

RUN apt-get update

RUN apt-get install -y ca-certificates \
                       python3-all-dev \
                       postgresql-server-dev-all python3-venv

RUN python3 -m venv /venv

ENV PATH="/venv/bin:$PATH"

COPY requirements.txt /tmp/requirements.txt

RUN pip install -U pip wheel

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r /tmp/requirements.txt

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY blog /app

# Make port 80 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python3", "manage.py", "runserver"]

ENV PYTHONUNBUFFERED 1

runserver 0.0.0.0:8000
