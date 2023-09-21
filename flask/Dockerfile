# Use the official Python image as a parent image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port your application will run on
EXPOSE 5000


# Command to run the application
CMD ["flask", "run", "--host=0.0.0.0"]
