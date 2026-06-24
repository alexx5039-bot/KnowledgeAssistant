from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


from app.db.models.document import Document


class DocumentRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_document(self, filename: str, file_path: str) -> Document:
        document = Document(filename=filename, file_path=file_path)
        self.db.add(document)
        await self.db.commit()
        await self.db.refresh(document)
        return document


    async def get_document_by_id(self, document_id: int) -> Document | None:
        document = await self.db.get(Document, document_id)
        return document


    async def get_document_by_filename(
            self,
            filename: str
    ) -> Document | None:
        stmt = select(Document).where(Document.filename == filename)
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()


    async def get_documents(self) -> list[Document]:
        result = await self.db.execute(select(Document))
        return list(result.scalars().all())


    async def delete_document(self, document_id: int):
        document = await self.get_document_by_id(document_id)
        if document is None:
            return None

        await self.db.delete(document)
        await self.db.commit()

        return document
