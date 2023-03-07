from fastapi import FastAPI
import threading
import uvicorn
import time
import asyncio


app = FastAPI()


@app.get("/")
async def read_root():
    current_thread = threading.current_thread().ident
    print('Current thread: ', current_thread)
    await asyncio.sleep(2)
    return str(current_thread)


@app.get("/sync")
def read_root():
    # cpu bound
    current_thread = threading.current_thread().ident
    print('Current thread: ', current_thread)
    time.sleep(2)
    return str(current_thread)


uvicorn.run(app, port=5001)
