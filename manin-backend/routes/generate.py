from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.llm import generate_manim_code
from services.cleaner import strip_markdown
from services.manim import render_code_to_video
import uuid
import os

router = APIRouter()  # FastAPI's version of Blueprint

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate")
async def generate(request: PromptRequest):
    prompt = request.prompt
    if not prompt.strip():
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    max_retries = 1
    attempt = 0
    errors = None
    cleaned_code = ""
    video_id = str(uuid.uuid4())

    while attempt <= max_retries:
        if attempt == 0:
            llm_code = generate_manim_code(prompt)
        else:
            repair_prompt = (
                "The following Manim code failed to render with this error:\n"
                f"{errors}\n"
                "Here is the code:\n"
                f"{cleaned_code}\n"
                "Please return a corrected version, OUTPUT ONLY the valid Python code for a Manim Scene class named PromptScene."
            )
            llm_code = generate_manim_code(repair_prompt)

        cleaned_code = strip_markdown(llm_code)
        final_path, errors = render_code_to_video(cleaned_code, video_id)

        if not errors:
            return {"video_id": video_id}

        attempt += 1

    # After retries, still not fixed
    raise HTTPException(
        status_code=500,
        detail={
            "error": errors,
            "code_attempted": cleaned_code,
            "message": "Failed to generate working Manim code, even after auto-correction. You may retry or edit the code."
        }
    )


@router.get("/video/{video_id}")
async def get_video(video_id: str):
    from fastapi.responses import FileResponse
    videos_path = os.path.abspath("videos")
    file_path = os.path.join(videos_path, f"{video_id}.mp4")
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Video not found")
    return FileResponse(file_path, media_type='video/mp4')
