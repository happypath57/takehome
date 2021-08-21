# encoding: utf-8
import base64
import random
import time
import uuid
from typing import List
import hashlib
import hmac

import aiohttp
from aiohttp import FormData
from fastapi import UploadFile

from simple_ocr.config import BAIDU_GET_TOKEN_URL, BAIDU_APP_KEY, BAIDU_APP_SECRET, BAIDU_OCR_URL
from simple_ocr.constants import ALLOW_PICTURE_EXTENSIONS


def validate_extension(extension: str) -> bool:
    """

    :param extension:
    :return:
    """
    return extension in ALLOW_PICTURE_EXTENSIONS


def add_filename_suffix(filename_split: List[str]) -> str:
    """

    :param filename_split:
    :return:
    """
    return f"{filename_split[0]}-{uuid.uuid4().hex}{filename_split[1]}"


class OCRRecognition:
    _token = {}

    async def get_token(self) -> str:
        """

        :return:
        """
        if not self._token or self._token["expires_in"] < int(time.time()):
            async with aiohttp.ClientSession() as sess:
                async with sess.get(
                    url=BAIDU_GET_TOKEN_URL.format(
                        client_id=BAIDU_APP_KEY,
                        client_secret=BAIDU_APP_SECRET,
                    ), verify_ssl=False,) as resp:
                    state = resp.status
                    if state != 200:
                        raise Exception("Get Token Error!")
                    resp = await resp.json()
                    print(resp)
                    self._token = {
                        "token": resp["access_token"],
                        "expires_in": resp["expires_in"] + int(time.time())
                    }
        return self._token["token"]

    async def do_ocr(self, file: UploadFile) -> List[str]:
        """

        :param file:
        :return:
        """
        token = await self.get_token()
        base64_str = base64.b64encode(await file.read(),).decode("utf-8")
        return await self._do_ocr(base64_str, token)

    async def _do_ocr(self, base64_str: str, token: str) -> List[str]:
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        form_data = FormData()
        form_data.add_field("image", base64_str)
        async with aiohttp.ClientSession() as sess:
            async with sess.post(
                    url=f"{BAIDU_OCR_URL}?access_token={token}",
                    headers=headers,
                    data=form_data,
                    verify_ssl=False
            ) as resp:
                if resp.status != 200:
                    raise Exception("OCR Parse Error!")
                resp = await resp.json()
                return [r["words"] for r in resp["words_result"]]


