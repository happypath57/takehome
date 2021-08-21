# encoding: utf-8

import uvicorn
from fastapi import FastAPI
import nest_asyncio

from simple_ocr.ocr.view import ocr_router

nest_asyncio.apply()

app = FastAPI()

app.include_router(ocr_router)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5000)
