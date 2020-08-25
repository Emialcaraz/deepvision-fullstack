# Fullstack Challenge
This project is under development. We are working in progress.

## Technical Details

### Uvicorn

**Uvicorn** is a lightning-fast "ASGI" server.

It runs asynchronous Python web code in a single process.

### Gunicorn

You can use **Gunicorn** to manage Uvicorn and run multiple of these concurrent processes.

That way, you get the best of concurrency and parallelism.

### FastAPI

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+.

### ElasticSearch
We use the Official low-level client for Elasticsearch. Its goal is to provide common ground for all Elasticsearch-related code in Python.

### Interactive API docs

Now you can go to <a href="http://0.0.0.0:5000/docs" target="_blank">http://0.0.0.0:5000/docs</a> or <a href="http://127.0.0.1:5000/docs" target="_blank">http://127.0.0.1:5000/docs</a> (or equivalent, using your Docker host).

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" target="_blank">Swagger UI</a>):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Alternative API docs

And you can also go to <a href="http://0.0.0.0/redoc" target="_blank">http://0.0.0.0/redoc</a> or <a href="http://127.0.0.1/redoc" target="_blank">http://127.0.0.1/redoc</a>(or equivalent, using your Docker host).

You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" target="_blank">ReDoc</a>):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## Dependencies and packages

All dependencies are in requirements.txt

## API authentication.

Our API uses https://jwt.io/ for encrypt the payload and brings Bearer Authentication.
There is and endpoint called /token that brings this token from OAuth2 Authentication.

Default Username and Password:

- ubuntu debian

##  Command Line Interface (CLI) 

Typer is a library for building <abbr title="command line interface, programs executed from a terminal">CLI</abbr> applications that users will **love using** and developers will **love creating**. Based on Python 3.6+ type hints.

The key features are:

* **Intuitive to write**: Great editor support. <abbr title="also known as auto-complete, autocompletion, IntelliSense">Completion</abbr> everywhere. Less time debugging. Designed to be easy to use and learn. Less time reading docs.
* **Easy to use**: It's easy to use for the final users. Automatic help, and automatic completion for all shells.
* **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* **Start simple**: The simplest example adds only 2 lines of code to your app: **1 import, 1 function call**.
* **Grow large**: Grow in complexity as much as you want, create arbitrarily complex trees of commands and groups of subcommands, with options and arguments.

We use Typer https://typer.tiangolo.com/ that allows to fill data in a database.

Commands:

- ``` updateDB(namefile: str, index: str): ``` 

- ``` getFromDB(namefile: str, index: str): ``` 

## Front End

Node-RED is a programming tool for wiring together hardware devices, APIs and online services in new and interesting ways.
You will see Node-RED in <a href="http://127.0.0.1:1880" target="_blank"> localhost:1880</a>

# Getting Started

- ``` sudo docker-compose build ``` 

- This is for elasticsearch-py ``` sudo sysctl -w vm.max_map_count=262144 ```
- ``` sudo docker-compose up ```
- <a href="http://0.0.0.0:5000/docs" target="_blank"> localhost:5000/docs</a> to test REST API
- User: ubuntu password: debian for OAuth2


# Challenge Notes
It provides a browser-based editor that makes it easy to wire together flows using the wide range of nodes in the palette that can be deployed to its runtime in a single-click.
For this challenge we will be working on one of our product's output, in charge of reporting traffic anomalies.
Given the JSON file with a list of events generated by the Vehicle Recognition AI module. You have to build a microservice that provides:

- A  command line interface (CLI) that allows you to fill in a database.
- Create an REST API with two GET endpoints:
  - **/api/anomalies:** returns a list of all the generated anomalies.
  - **/api/anomalies/csvfile:** returns a CSV file with the following stats, grouped by date and time:
    - Count of objects that crossed the **checkpoint_name** named *countingLine*
    - Count of each type of anomaly.

    Columns:
      - Date
      - Day of Week
      - Hour
      - Camera
      - Car Count
      - Bus Count
      - Motorbike Count
      - Truck Count
      - Bicycle Count
      - Person Count
      - Traffic Congestion
      - Queue Clearing
      - Wrong Way
      - Unsafe Lane Entry
      - Stalled Car
      - Illegal Turn
      - Jay Walking

- Develop the frontend in NodeRed:
  - Create a view with a paged table that consumes from the endpoint **/api/anomalies**.

    Columns: 
      - Date
      - Day of Week
      - Hour
      - Camera
      - Instance
      - Anomalies
  
  - Add a download button to the previous view that allows you to download the stats through the **/api/anomalies/csvfile** endpoint.

Notes:

- You can choose NodeJS or any Python Web Framework to develop the REST API.
  - Based on our current stack you can use the following Python libraries (optional):
    - [typer](https://typer.tiangolo.com/) or pyCLI for CLI development.
    - [fastAPI](https://fastapi.tiangolo.com/) for API REST development.
    - [elasticsearch](https://elasticsearch-py.readthedocs.io/en/master/) to manage elasticsearch db.
- You can choose any kind of database to persist the data.


You will deliver the code in a public repository at www.github.com.
The proposed solution must use Docker
The repo must include a `README.md` file with all the instalation instructions, along with the corresponding Dockerfiles.


Plus:

- Docker compose.
- Swagger.
- API authentication.
