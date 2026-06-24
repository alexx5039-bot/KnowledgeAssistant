from pydantic import BaseModel, ConfigDict

class DocumentResponse(BaseModel):
    id: int
    filename: str
    file_path: str

    model_config = ConfigDict(
        from_attributes=True
    )
