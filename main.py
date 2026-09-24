import fastapi

print("Hello, World!")

app = fastapi.FastAPI()

@app.get("/")