from fastapi import FastAPI

app = FastAPI(title="Medical AI Assistant")


@app.get("/")
def home():
    return {
        "message": "Medical AI Assistant API is running!"
    }