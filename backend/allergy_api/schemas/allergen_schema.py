from pydantic import BaseModel # pyright: ignore[reportMissingImports] 

class TextInput(BaseModel):
    text: str
