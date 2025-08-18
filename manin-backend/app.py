from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.generate import router  # Import FastAPI router, not Flask blueprint
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# 2. Set up CORS middleware (FastAPI version)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to your frontend's origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Include your API router (was Blueprint in Flask)
app.include_router(router)

# 4. Root route, FastAPI style (returns dict, not jsonify)
@app.get("/")
async def home():
    return {"message": "Hello from FastAPI backend!"}

# 5. No need for if __name__ == "__main__": block
# Instead, run your app like:
#   uvicorn main:app --reload
