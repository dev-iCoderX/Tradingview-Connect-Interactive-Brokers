from fastapi import FastAPI
from src.req import OrderDetail
from src.order import Order
import sys, os
import logging


logging.basicConfig(filename='log.log', format='[%(asctime)s] %(levelname)-8s :%(message)s')
logging.info(f"Start")
def GetError():
    excType, excObj, excTb = sys.exc_info()
    fname = os.path.split(excTb.tb_frame.f_code.co_filename)[1]
    err = str(excType) + "-" + str(fname) + "-" +str(excTb.tb_lineno)
    logging.warning(f"Get all open orders: {err} => Failed!")
    return {
        "status":False,
        "message":err
        }
success = {
    "status":True,
    "message":"Success!"
    }
app = FastAPI()
@app.get("/")
def Home():
    return {
        "message": "Hello"
    }

@app.post("/alert")
async def Alert(item: OrderDetail):
    try:
        Order(item)
        return success
    except:
        return GetError()
