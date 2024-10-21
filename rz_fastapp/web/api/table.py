from typing import Any

from aiosqlite import Connection
from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/tables")
async def tables(request: Request) -> dict[str, list[Any]]:
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
    table_names = [row[0] for row in result]
    return {"tables": table_names}
