# encoding: utf-8

from fastapi import UploadFile, File, APIRouter

from simple_ocr.dao.ocr import OCRDao
from simple_ocr.ocr.helpers import validate_extension, add_filename_suffix, OCRRecognition, common_response

ocr_router = APIRouter()


@ocr_router.post("/ocr/", summary="上传图片")
async def upload_image(
        file: UploadFile = File(...)
    ):
    """

    :param file:
    :return:
    """
    filename = file.filename
    filename_split = filename.rsplit(".", 1)
    is_ok = validate_extension(filename_split[-1])
    if not is_ok:
        return common_response(code=400, message="File Extension Error!, Only png/jpg allowed!")
    new_filename = add_filename_suffix(filename_split)
    ocr_recognition = OCRRecognition()
    try:
        result = await ocr_recognition.do_ocr(file)
    except Exception as e:
        result = str(e)
        return common_response(code=500, message=result)

    dao = OCRDao()

    picture_id = await dao.insert_picture(filename=new_filename)

    await dao.insert_letters(picture_id, letters=result)

    return common_response(data=result)





