from pydantic import BaseModel

class Todo(BaseModel):
    name: str
    description: str
    complete: bool
    
class UpdateTodo(BaseModel):
    name: str | None = None
    description: str | None = None
    complete: bool | None = None