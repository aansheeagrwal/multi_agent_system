# api/endpoints.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from agents.classifier_agent import classify_and_process_file
import shutil
import os

router = APIRouter()

@router.post("/process-file/")
async def process_file(file: UploadFile = File(...)):
    # Check file extension for safety
    allowed_extensions = {".pdf", ".txt", ".json"}
    _, ext = os.path.splitext(file.filename)
    ext = ext.lower()

    if ext not in allowed_extensions:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    # Save the uploaded file temporarily
    temp_file_path = f"/tmp/{file.filename}"
    try:
        with open(temp_file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Process file with classifier_agent
        result = classify_and_process_file(temp_file_path)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing error: {e}")

    finally:
        # Clean up temp file
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)

    return JSONResponse(content={"result": result})
