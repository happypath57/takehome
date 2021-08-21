# encoding: utf-8
import asyncio

from asyncpgsa import PG

from simple_ocr.config import POSTGRES_SERVER


class PostgreSQLClient:

    def __init__(self):
        self._client = None

    async def initialize(self):
        self._client = PG()
        await self._client.init(
            **POSTGRES_SERVER,
        )

    @property
    def client(self):
        if not self._client:
            asyncio.run(self.initialize())
        return self._client


class Dao:
    _instance = None
    _pg_client = None

    @property
    def pg_client(self):
        if not self._pg_client:
            self._pg_client = PostgreSQLClient()
        return self._pg_client.client
