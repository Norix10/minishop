from asyncio import current_task

from sqlalchemy.ext.asyncio import (
    create_async_engine, 
    async_sessionmaker, 
    async_scoped_session,
    AsyncSession
)

from core.config import settings

class DataBaseHealper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
        )
    def get_scoped_session(self):
        session = async_scoped_session(
            self.session_factory,
            scopefunc=current_task
        )
        return session
    
    async def session_dependency(self) -> AsyncSession:  # type: ignore
        async with self.session_factory() as session:
            yield session
            await session.close()
    async def scoped_session_dependency(self) -> AsyncSession: # type: ignore
        session = self.get_scoped_session()
        yield session
        await session.close()

db_healper = DataBaseHealper(
    url=settings.db_url,
    echo=settings.db_echo
)