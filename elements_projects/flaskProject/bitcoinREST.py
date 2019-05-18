from flask import Flask
from decimal import *
from flask import json, jsonify
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from flask_cors import CORS

rpc_port = 18443
rpc_user = 'admin1'
rpc_password = '1234'


app = Flask(__name__)
CORS(app)

def CallRPC( commands ):
    global rpc_port
    global rrpc_user
    global rpc_password

    try:
        rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%(rpc_user, rpc_password, rpc_port))
        print (f"connection: {rpc_connection}")
        result = rpc_connection.batch_(commands)
        print(f"Result type: {type(result)}")
    except JSONRPCException as json_exception:
        return "A JSON RPC Exception occured: " + str(json_exception)
    except Exception as general_exception:
        return "An Exception occured: " + str(general_exception)
    return result


@app.route("/")
def home():
    return jsonify(CallRPC([["getblockchaininfo", '["chain":"regtest"]']]))

@app.route("/getwalletinfo")
def getwalletinfo():
    # it doesn't work with params '[]', '[""]', None, '["walletname": None]' so I used CallRPC([["getwalletinfo" ]])
    return jsonify(CallRPC([["getwalletinfo" ]]))

@app.route("/listunspent")
def listunspent():
    return jsonify(CallRPC([["listunspent", None]]))

@app.route("/listtransactions")
def llisttransactions():
    return jsonify(CallRPC([["listtransactions", None]]))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6002)
