from pydantic import BaseModel

class RequestTree(BaseModel):
    temperature: float
    humidity: int
    is_raining: bool

class ResponseTree(BaseModel):
    can_play: bool
