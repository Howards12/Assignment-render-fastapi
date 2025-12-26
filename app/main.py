from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from my Render FastAPI app"}

@app.get("/square")
def square(n: int = Query(..., ge=0, le=100000)):
    return {"n": n, "square": n * n}
