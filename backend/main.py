from fastapi import FastAPI

app = FastAPI(title="Ciucci & Capricci API")

@app.get("/")
def read_root():
    return {"message": "Welcome to Ciucci & Capricci API"}
