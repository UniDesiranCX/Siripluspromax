from fastapi import FastAPI
from starlette.requests import Request
import requests
from starlette.responses import Response
import uvicorn

app = FastAPI()


@app.get("/hi")
def main(request: Request):
    data = request.query_params
    msg = data.get("msg")
    if not data.get("title"):
        url = f"https://siripluspromax.tech/dTxrYVsBy5CWXvF9jrsNFa/{msg}"
    else:
        title = data.get("title")
        url = f"https://siripluspromax.tech/dTxrYVsBy5CWXvF9jrsNFa/{title}/{msg}"
    response = requests.post(url)
    if response.json()["code"] == 200 or response.status_code == 200:
        return Response("ok")
    else:
        return Response("failed")

if __name__ == '__main__':
    uvicorn.run(app)
