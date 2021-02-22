import os
from flask import Flask, request
from dotenv import load_dotenv
from flask_pymongo import PyMongo
import time
import math

app = Flask(__name__)
app.config['MONGO_URI'] = os.getenv('MY_URL")
mongo = PyMongo(app)
myCollection = mongo.db.g16
i = 0
cost_t = [0]
times = [0]

@app.route('/status', methods=['GET']) #158.108.182.18:3000/status?slot={NumOfSlot} -> เชคstatusของช่องslot
def find():
    slot = request.args.get("slot")
    flit = {"slot_number": slot ,"time_out": None}
    query = myCollection.find(flit)
    output = [{"status": 0}]
    for ele in query:
        output[ele["status"]] = 1
    return { "result": output }

@app.route('/cost', methods=['GET']) #158.108.182.18:3000/cost?ID={IdOfCar} -> เชคราคาของรถIDนั้น
def cost():
    flit = request.args
    query = myCollection.find(flit)
    money = int(math.ceil((query["time_out"] - query["time_in"])/60)*20)
    output = [{cost: money}]
    return { "result": output}

@app.route('/time_cost', methods=['GET']) #158.108.182.18:3000/time_cost -> คืนค่าอาเรเป็น time interval แกนx,แกนy
def array_cost():
    flit = {"time_out": None}
    query = myCollection.find(flit)
    global cost_t
    summ = cost_t[-1]
    global times
    t = int(math.ceil(time.time()))
    for ele in query:
        if (t-ele["time_in"])%60 == 0:
            summ += 20
    cost_t.append(summ)
    times.append(time.time())
    return { "result": [times,cost_t]}

@app.route('/updatecar', methods=['POST']) #158.108.182.18:3000/updatecar -> hardware ส่งสถานะ
def insert_one():
    data = request.json
    if data["Status"] == 1:
        global i
        i +=1 
        flit = {"slot_number": data["No"] ,"time_out": None}
        query = myCollection.find(flit)
        for ele in query:
            return {'result': 'slot full'}
        myInsert = {
                "type": "car",
                "ID" : i,
                "slot_number" : data["No"],
                "time_in": int(math.ceil(time.time())),
                "time_out": None
                }
        myCollection.insert_one(myInsert)
        return {'result': 'add car in'}
    else :
        filt = {"slot_number" : data["No"],
                "time_out": None
                }
        updated_content = {"$set": {'time_out' : int(math.ceil(time.time()))}}
        myCollection.update_one(filt, updated_content)
        return {'result': 'add car out'}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='3000', debug=True)
    
