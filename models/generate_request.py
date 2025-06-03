from pydantic import BaseModel


class GenerateRequest(BaseModel):
    prompt: str
    think: bool = False
