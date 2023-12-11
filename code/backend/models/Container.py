from pydantic import BaseModel

class Container(BaseModel):
    container_id: int
    container_name: str
    container_blocks: int
