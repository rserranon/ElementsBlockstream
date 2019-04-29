
from flask import Flask
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

rpc_port = 18888
rpc_user = 'user3'
rpc_password = 'password3'


app = Flask(__name__)

def getWalletInfo():
    global rpc_port
    global rrpc_user
    global rpc_password

    try:
        rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%(rpc_user, rpc_password, rpc_port))
        jsonResult = rpc_connection.getwalletinfo()
    except JSONRPCException as json_exception:
        return "A JSON RPC Exception occured: " + str(json_exception)
    except Exception as general_exception:
        return "An Exception occured: " + str(general_exception)
    print(jsonResult)
    return jsonResult

@app.route("/")
def home():
    result = getWalletInfo()
    return str(result['balance'])

@app.route("/txcount")
def txcount():
    result = getWalletInfo()
    return str(result['txcount'])

@app.route("/hdmasterkeyid")
def masterkeyid():
    result = getWalletInfo()
    return str(result['hdmasterkeyid'])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
