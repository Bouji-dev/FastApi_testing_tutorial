from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def read_root():
    return {'message': 'Hello World'}

@app.get('/ping')
async def get_ping():
    return {'status': 'ok'}
