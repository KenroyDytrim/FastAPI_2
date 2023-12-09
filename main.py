import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from public.users import U_R

app = FastAPI()

app.include_router(U_R)

@app.get('/', response_class = HTMLResponse)
def index():
    return "<b> Привет, пользователь! </b>"

if __name__ == '__main__':
    uvicorn.run(app, host = "127.0.0.1", port = 8000)