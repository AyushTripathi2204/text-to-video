import os
import uuid
import shutil
import glob
import subprocess

def render_code_to_video(code, video_id):
    tmp_scripts_path = os.path.abspath("tmp_scripts")
    os.makedirs(tmp_scripts_path, exist_ok=True)
    script_path = os.path.join(tmp_scripts_path, f"tmp_{video_id}.py")
    with open(script_path, "w", encoding="utf-8") as f:
        f.write(code)

    try:
        result = subprocess.run(
            ["manim", script_path, "PromptScene", "-qm"],
            capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        return None, {"stderr": e.stderr, "stdout": e.stdout}

    mp4_candidates = glob.glob(
        os.path.abspath(os.path.join("media", "videos", f"tmp_{video_id}", "**", "PromptScene.mp4")),
        recursive=True
    )
    if not mp4_candidates:
        return None, {"error": "No MP4 found"}
    final_path = os.path.abspath(os.path.join("videos", f"{video_id}.mp4"))
    shutil.move(mp4_candidates[0], final_path)
    os.remove(script_path)
    return final_path, None
