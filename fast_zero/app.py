from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_class=HTMLResponse)
def read_root():
    return """
    <html>
      <head>
        <title> Nosso olá mundo! </title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>
    """
