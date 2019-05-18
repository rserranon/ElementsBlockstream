# Adapted from @Gavin Andresen and Taylor Gering spendfrom

from decimal import *
import time
import logging
import json
from flask import json, jsonify
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

logging.basicConfig(level=logging.DEBUG)

def check_json_precision():
    pass
   #"""Make sure json library being used does not lose precision converting BTC values"""

class BitcoinWalletRPC:
    def __init__(self, connectURI, passphrase = "", fee = Decimal("0.0001"), unlockseconds =5, minconfs = 1):
    #call to verify JSON precision, TODO implement
    #check_json_precision()
        self.logger = logging.getLogger(__name__)
        self.BASE_FEE = fee
        self.MINCONFS = minconfs
        self.UNLOCKSECONDS = unlockseconds

        # get connection to bitcoind daemon
        self.bitcoindConnection = self.connect_JSON(connectURI, passphrase)

    def connect_JSON(self, uri, passphrase):
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

    def list_addresses(self, searchaccount=None):
        self.logger.debug(f"list addresses called with search account = {searchaccount}")
        address_to_account = dict()
        for info in self.bitcoindConnection.listreceivedbyaddress(self.MINCONFS):
            self.logger.debug(f"info {info}")
            if not searchaccount or searchaccount == info["account"]:
                address_to_account[info["address"]] = info["account"]

        self.logger.debug("list_addresses returns object of length %d", len(address_to_account))
        self.logger.debug("list_addresses returns object of length %s", address_to_account)
        return address_to_account

    def walletInfo(self, targetwallet=""):
        self.logger.debug(f"get wallet {targetwallet} information")
        return self.bitcoindConnection.getwalletinfo(targetwallet)

    def createwallet(self, walletname):
        self.logger.debug(f"create wallet with name: {walletname}")
        return self.bitcoindConnection.createwallet(walletname)

    def listtransactions(self):
        transactions = self.bitcoindConnection.listtransactions()
        self.logger.debug(transactions)
        return transactions

RPCUSER = "admin1"
RPCPASS = "123"
RPCPORT = 18443
myWalletConnection = BitcoinWalletRPC("http://%s:%s@127.0.0.1:%s"%(RPCUSER, RPCPASS, RPCPORT))

myWalletConnection.list_addresses()
#myWalletConnection.createwallet("testwallet")
# TODO RPC method getwalletinfo is not working
#myWalletConnection.walletInfo("")
myWalletConnection.listtransactions()

