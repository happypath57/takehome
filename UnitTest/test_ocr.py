# encoding: utf-8
import asyncio
import base64
import warnings
from unittest import TestCase

from aiohttp.test_utils import unittest_run_loop

from simple_ocr.ocr.helpers import OCRRecognition


class TestOCR(TestCase):
    def setUp(self) -> None:
        self.loop = asyncio.get_event_loop()
        self.ocr = OCRRecognition()

    @classmethod
    def setUpClass(cls) -> None:
        warnings.simplefilter('ignore', ResourceWarning)
        warnings.simplefilter('ignore', DeprecationWarning)

    @unittest_run_loop
    async def test_01_get_token(self):
        result = await self.ocr.get_token()
        self.assertTrue(bool(result))

    @unittest_run_loop
    async def test_02_do_ocr(self):
        with open(f"./resources/test_image.png", "rb") as image:
            token = await self.ocr.get_token()
            file = image.read()
            base64_str = base64.b64encode(file).decode("utf-8")

            result = await self.ocr._do_ocr(base64_str, token)
            self.assertEqual(result[-1], "这是一个测试")
