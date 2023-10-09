# Uses an official Python runtime as a base image
FROM python:3.9

# Setting the working directory inside the container to ' /app'
WORKDIR /BMICalculator

#Copies the contents of the current directory (including the Flask app and any necessary files) into the container's /app directory
COPY . /BMICalculator/

#Installing any needed python packages specified in requirements.txt
RUN pip install -r requirements.txt

#Exposing or making port: 80 available to the world outside this container. Port 80 is the default port for Flask Applications.
EXPOSE 80

#Run the basefile bmicalculator.py when the container launches. 
CMD ["python", "./BMICalculator.py"]

# nOW, TO BUILD THE DOCKER IMAGES, IN TERMINAL WE PASS COMMAND: "docker build -t itsmeruan/bmi-calculator:0.0.1.RELEASE .
#" HERE -t is to give a tag and here i mentioned myusername/appname and version as needed. the last "." defines that the docker file based on which the given image name should be created and available in the current directory which is docker file.


