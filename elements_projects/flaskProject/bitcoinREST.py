
from flask import Flask
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

rpc_port = 19001
rpc_user = 'admin1'
rpc_password = '123'


app = Flask(__name__)


def CallRPC( commands ):
    global rpc_port
    global rrpc_user
    global rpc_password

    try:
        rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%(rpc_user, rpc_password, rpc_port))
        print (f"connection: {rpc_connection}")

        jsonResult = rpc_connection.batch_(commands)
    except JSONRPCException as json_exception:
        return "A JSON RPC Exception occured: " + str(json_exception)
    except Exception as general_exception:
        return "An Exception occured: " + str(general_exception)
    return jsonResult


@app.route("/")
def home():
    result = CallRPC([["getwalletinfo", ""]])
    return str(result['balance'])

@app.route("/getwalletinfo")
def getwalletinfo():
    result = CallRPC([["getwalletinfo", None]])
    return str(result)

@app.route("/listunspent")
def listunspent():
    result = CallRPC([["listunspent", None]])
    return str(result)

@app.route("/listtransactions")
def llisttransactions():
    result = CallRPC([["listtransactions", None]])
    return str(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6002)
