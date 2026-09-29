import fastapi

print("Hello, World!")

app = fastapi.FastAPI()

@app.get("/")
def read_root(age: int):
    return {"Hello": "World", "My-Age": age}

