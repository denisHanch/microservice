# First microservice

This microservice is a simple API, which returns price of 1 BTC in EUR and CZK

__Build image command:__

`docker build -t IMAGE_NAME .`

__Run container command:__

`docker run -d --name CONTAINER_NAME -p 80:80 IMAGE_NAME`

Go to http://127.0.0.1/btc_info to test the endpoint