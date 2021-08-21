# encoding: utf-8
from typing import List

from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as psql_insert

from simple_ocr.dao import Dao


# state
from simple_ocr.models import t_picture, t_letter

ENABLE = 1
DISABLE = 0


class OCRDao(Dao):

    async def insert_picture(self, filename: str,
                             state: int = ENABLE,
                             url: str = None) -> int:
        """

        :param state:
        :param filename:
        :return:
        """
        value = dict(filename=filename,
                     state=state,
                     url=url)
        sql = t_picture.insert().values(**value).returning(t_picture.c.id)
        sql.parameters = None
        res = await self.pg_client.fetchrow(sql)
        return res["id"]

    async def insert_letters(self, picture_id: str,
                             letters: List[str]) -> None:
        """

        :param picture_id:
        :param letters:
        :return:
        """
        to_insert = []
        for letter in letters:
            to_insert.append({
                "main_id": picture_id,
                "letter": letter,
                "state": ENABLE
            })
        sql = psql_insert(t_letter).values(to_insert)
        sql.parameters = None
        res = await self.pg_client.fetch(sql)
        return res
