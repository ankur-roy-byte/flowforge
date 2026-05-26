from sqlalchemy.ext.asyncio import AsyncSession


class DagRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

