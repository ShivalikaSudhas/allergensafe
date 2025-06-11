from pydantic import BaseModel

class TextInput(BaseModel):
    text: str
# pyright: ignore[reportMissingImports]