import os
import asyncio
from dotenv import load_dotenv
from turso_python import AsyncTursoConnection

load_dotenv()

async def getDataFromRepositories(conn):
    result = await conn.execute_query("SELECT * FROM repositories")
    rows = result['results'][0]['response']['result']['rows']
    for record in rows:
        for colValue in record:
            if colValue['type'] != 'null':
                print (colValue['value'])
            else:
                print(colValue['type'])


async def main():
    databaseUrl = os.getenv("TOKEN_URL")
    databaseToken = os.getenv("TOKEN_DB")

    async with AsyncTursoConnection(databaseUrl, databaseToken) as conn:
        await getDataFromRepositories(conn)

asyncio.run(main())
