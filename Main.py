from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "JAHTECH IS LIVE 🔥"}

@app.get("/health")
def health():
    return {"status": "ok"}
