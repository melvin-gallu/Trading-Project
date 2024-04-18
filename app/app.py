from fastapi import FastAPI, Query, Path, Body, Cookie, Header, status, Form, File, UploadFile
from pydantic import BaseModel, Field, EmailStr
from typing import Annotated, Any, Union

app = FastAPI()

@app.post("/file/")
async def create_file(file: Annotated[bytes|None, File()] = None):
    """
    Store the whole content of the file in memory.
    Works well only for small size files
    """
    return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile|None = None):
    """
    Store in memory up to max size limit, then store in disk.
    Works well for large files without consuming all the memory.
    """
    if not file:
        return {"message": "No upload file sent"}
    
    actual_file = file.file
    contents = file.file.read()
    contents = await actual_file.read() #same as line just above
    return {"filename": file.filename}

@app.post("/uploadfiles/")
async def create_upload_files(files: list[UploadFile|None]|None = None):
    if not files:
        return {"message": "No upload file sent"}
    return {"filenames": [file.filename for file in files]}


@app.post("/form-files")
async def create_form_file(file: Annotated[UploadFile, File()], token: Annotated[str, Form()]):
    """
    Path for a form with file
    """
    return {
        "file content type": file.content_type,
        "token": token
    }