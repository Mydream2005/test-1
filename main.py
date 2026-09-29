import fastapi

print("Hello, World!")

app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

