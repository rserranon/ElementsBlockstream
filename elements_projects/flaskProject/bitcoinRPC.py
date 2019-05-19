# Adapted from @Gavin Andresen and Taylor Gering spendfrom

from decimal import *
import time
import logging
import json
from flask import json, jsonify
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

logging.basicConfig(level=logging.DEBUG)

def check_json_precision():
    """Make sure json library being used does not lose precision converting BTC values"""
    n = Decimal("20000000.00000003")
    satoshis = int(json.loads(json.dumps(float(n)))*1.0e8)
    if satoshis != 2000000000000003:
        raise RuntimeError("JSON encode/decode loses precision")

class RPCbitcoin:
    def __init__(self, connectURI, passphrase = "", fee = Decimal("0.0001"), unlockseconds =5, minconfs = 1):

        #call to verify JSON precision
        check_json_precision()

        # global settings for RPCbitcoin conections
        self.logger = logging.getLogger(__name__)
        self.BASE_FEE = fee
        self.MINCONFS = minconfs
        self.UNLOCKSECONDS = unlockseconds

        # get RPC connection to bitcoind daemon
        self.bitcoindConnection = self.connectRPC(connectURI, passphrase)

    def connectRPC(self, uri, passphrase):
        """Connect to a bitcoin JSON-RPC server"""
        try:
            result = AuthServiceProxy(uri)
            # ServiceProxy is lazy-connect, so send an RPC command mostly to catch connection errors,
            # but also make sure the bitcoind we're talking to is/isn't testnet:
            self.logger.info(f"Connected to {result.getmininginfo()['chain']}")
            print ("result")
            print (result)
            result.passphrase = passphrase

            return result
        except:
            raise

    def getnewaddress(self, label = "", addressType = "legacy" ):
        self.logger.debug(f"Generate new address {label} of type {addressType} ")
        return self.bitcoindConnection.getnewaddress(label, addressType)

    def listrecievedbyaddress(self, searchAddress=None):
        self.logger.debug(f"list addresses called with search account = {searchAddress}")
        address_to_account = dict()
        # TODO verify that searchAddress can be passed as None
        for info in self.bitcoindConnection.listreceivedbyaddress(self.MINCONFS, searchAddress):
            self.logger.debug(f"info {info}")
            # TODO, verify if account is a valid key and the logic of this if
            if not searchAddress or searchAdress == info["account"]:
                address_to_account[info["address"]] = info["account"]

        self.logger.debug("list_addresses returns object of length {len(address_to_account)}")
        return address_to_account

    def getwalletinfo(self, targetwallet=""):
        self.logger.debug(f"get wallet {targetwallet} information")
        # it doesn't work using the parameter targetwallet self.bitcoindConnection.getwalletinfo(targetwallet)
        # so I used self.bitcoindConnection.getwalletinfo(), TODO find a fix for thix to use several wallets
        return self.bitcoindConnection.getwalletinfo()

    # Createwallet it does work but we need to understand better how to switch walltets
    # and make getwalletinfo work with the parameter targetwallet
    def createwallet(self, walletname):
        self.logger.debug(f"create wallet with name: {walletname}")
        return self.bitcoindConnection.createwallet(walletname)

    def listtransactions(self):
        transactions = self.bitcoindConnection.listtransactions()
        self.logger.debug(f"Number of transactions = {len(transactions)}")
        return transactions

RPCUSER = "admin1"
RPCPASS = "1234"
RPCPORT = 18443
myWalletConnection = RPCbitcoin("http://%s:%s@127.0.0.1:%s"%(RPCUSER, RPCPASS, RPCPORT))

#myWalletConnection.createwallet("testwallet")
myWalletConnection.getwalletinfo()
myWalletConnection.getnewaddress(label = "My New Address")
myWalletConnection.listtransactions()
myWalletConnection.listrecievedbyaddress()
