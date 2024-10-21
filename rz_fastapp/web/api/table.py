from typing import Iterable

from aiosqlite import Connection, Row
from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/tables")
async def tables(request: Request) -> dict[str, Iterable[Row]]:
    """Retrieve the list of table names from the SQLite database.

    Args:
        request (Request): The request object containing the database connection.

    Returns:
        dict[str, str]: A dictionary with the list of table names.

    """
    db: Connection = request.app.state.db
    statement: str = "SELECT name FROM sqlite_master WHERE type='table';"
    async with db.execute(statement) as cursor:
        result = await cursor.fetchall()
    return {"tables": result}
