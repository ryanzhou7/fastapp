from contextlib import asynccontextmanager
from typing import AsyncGenerator

import aiosqlite
from fastapi import FastAPI
from fastapi.logger import logger


@asynccontextmanager
async def lifespan_setup(
    app: FastAPI,
) -> AsyncGenerator[None, None]:
    """Actions to run on application startup.

    This function uses fastAPI app to store data
    in the state, such as db_engine.

    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """
    app.state.db = await aiosqlite.connect("sqlite.db")
    logger.error("This and code above runs prior to app start")
    yield
     # Close the database connection
    await app.state.db.close()
    logger.error("This and code below runs after app finished execution")
