
from flask import Flask
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

app = Flask(__name__)
 
@app.route("/")
def elements():
    rpc_port = 18885
    rpc_user = 'user2'
    rpc_password = 'password2'

    try:
        rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:%s"%(rpc_user, rpc_password, rpc_port))
    
        result = rpc_connection.getwalletinfo("bitcoin")
    
    except JSONRPCException as json_exception:
        return "A JSON RPC Exception occured: " + str(json_exception)
    except Exception as general_exception:
        return "An Exception occured: " + str(general_exception)

    return str(result['balance'])

if __name__ == "__main__":
    app.run(host='0.0.0.0')
