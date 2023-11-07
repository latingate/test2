# main.py

import uvicorn

#Alternatively your can run from the terminal:
# uvicorn main:app in the current path

async def app(scope, receive, send):
    ...

if __name__ == "__main__":
    config = uvicorn.Config("main:app", port=5000, log_level="info")
    server = uvicorn.Server(config)
    server.run()


# # Example #1
# #
# async def app(scope, receive, send):
#     assert scope['type'] == 'http'
#
#     await send({
#         'type': 'http.response.start',
#         'status': 200,
#         'headers': [
#             [b'content-type', b'text/plain'],
#         ],
#     })
#     await send({
#         'type': 'http.response.body',
#         'body': b'Hello, world!',
#     })



# Example #2
# https://fastapi.tiangolo.com/
#
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {"Hello": "World"}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = None):
    if item_id == 1:
        q = 'item #1'
    return {"item_id": item_id, "q": q}

@app.get('/gal')
def read_root():
    return ('hello gal')

