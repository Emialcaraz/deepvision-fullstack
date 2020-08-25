from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.routes import views
from app.core import auth
import typer  # typerCli
from indexer.indexer import db  # db class

app = FastAPI()

appTyper = typer.Typer()

# Set all CORS enabled origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(views.router)


# si hay error de elasticsearch utilizar
# sudo sysctl -w vm.max_map_count=262144


# updateDB from CLI
@appTyper.command()
def updateDB(namefile: str, index: str):
    try:
        with open({namefile}) as raw_data:
            json_docs = json.loads(raw_data.read())
            for json_doc in json_docs:
                my_id = json_doc.pop('_id', None)
                db.index({index}, json.dumps(json_doc))
                return db.search('{index}')
    except ValueError as error:
        print("Error type:", type(error))
        return 500


# getFromDB CLI
@appTyper.command()
def getFromDB(index: str):
    try:
        return db.search({index})
    except Exception:
        return 500
