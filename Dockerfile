# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# copy the content of the local src directory to the working directory
COPY ./src ./src

# install dependencies
RUN pip install -r requirements.txt

# command to run on container start
#CMD [ "python", "./app.py" ] 
CMD ["uvicorn", "src.app:app", "--host", "0.0.0.0", "--port", "80"]