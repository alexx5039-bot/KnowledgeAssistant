from fastapi import HTTPException, status

from app.db import repositories
from app.db.models.document import Document
from app.db.repositories.document import DocumentRepository

class DocumentService:
    def __init__(self, repository: DocumentRepository):
        self.repository = repository

    async def create_document_service(
            self,
            filename: str,
            file_path: str
    ) -> Document:

        existing_document = await self.repository.get_document_by_filename(
            filename=filename
        )
        if existing_document:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="File already exists"
            )
        document = await self.repository.create_document(
            filename=filename,
            file_path=file_path
        )
        return document

    async def get_document_by_id_service(self, document_id: int) -> Document:
        document = await self.repository.get_document_by_id(document_id)
        if document is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="File not found"
            )
        return document

    async def get_document_by_filename_service(self, filename: str) -> Document:
        document = await self.repository.get_document_by_filename(filename)
        if document is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="File not found"
            )
        return document

    async def get_documents_service(self) -> list[Document]:
        documents = await self.repository.get_documents()
        if not documents:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Files not found"
            )
        return documents

    async def delete_document_service(
            self,
            document_id: int
    ) -> None:

        document = await self.get_document_by_id_service(document_id)

        await self.repository.delete_document(document.id)