from flask import Flask, request
from flask_pymongo import PyMongo
import time
import math

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://exceed_user:1q2w3e4r@158.108.182.0:2277/exceed_backend'
mongo = PyMongo(app)
myCollection = mongo.db.g16
i = 0
cost_t = [0]

@app.route('/status', methods=['GET'])
def find():
    slot = request.args.get("slot")
    flit = {"slot_number": slot ,"time_out": None}
    query = myCollection.find(flit)
    output = [{"status": 0}]
    for ele in query:
        output[ele["status"]] = 1
    return { "result": output }

@app.route('/cost', methods=['GET'])
def cost():
    flit = request.args
    query = myCollection.find(flit)
    money = int(math.ceil((query["time_out"] - query["time_in"])/60)*20)
    output = [{cost: money}]
    return { "result": output}

@app.route('/time_cost', methods=['GET'])
def array_cost():
    flit = {"time_out": None}
    query = myCollection.find(flit)
    global cost_t
    summ = cost_t[-1]
    t = int(math.ceil(time.time()))
    for ele in query:
        sum += int(math.ceil((t - ele["time_in"])/60)*20)
    cost_t.append(sum)
    return { "result": cost_t}

@app.route('/updatecar', methods=['POST'])
def insert_one():
    data = request.json
    if data["Status"] == 1:
        global i
        i +=1 
        flit = {"slot_number": data["No"] ,"time_out": None}
        query = myCollection.find(flit)
        if(len(query)!=0):
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
    app.run(host='0.0.0.0', port='50005', debug=True)
    
