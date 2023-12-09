from fastapi import FastAPI, Path

app = FastAPI()

# musisz pobrac informacje o kontenerach z bazy danych or sth
DUMMY_CONTAINERS = [
    {"container_id": 1, "container_name": "container1", "container_blocks": 3},
    {"container_id": 2, "container_name": "container2", "container_blocks": 2},
    {"container_id": 3, "container_name": "container3", "container_blocks": 1},
]

# get containers info
@app.get("/containers")
async def get_containers():
    return DUMMY_CONTAINERS

# implemnet robot move orders
@app.get("/move/{move_id}")
async def get_move(move_id: int = Path(..., gt=-1, le=4)):
    # implement robot move orders
    return {"message":"endpoint to implement"}

@app.get("/stop")
async def get_stop():
    # implement robot stop
    return {"message":"endpoint to implement"}

@app.get("/start")
async def get_start():
    # implement robot start
    return {"message":"endpoint to implement"}