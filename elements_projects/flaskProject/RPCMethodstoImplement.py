# RPC methods to implement
# Original list obtained from MetacoSA/NBitcoin licensed under the MIT License
# acording to: bitcoincore v0.18.0
# Link: https://bitcoincore.org/en/doc/0.18.0/rpc/network/getnetworkinfo/i
#
# TODO final reorder according to bitcoincore.org documentation and link, to be done while implementing each method
#
# Category		    	Name			            Implemented
#------------------     ---------------------------         -----------------------
# ------------------ BLOCKCHAIN and UTXO
# blockchain		        getblockchaininfo                       Yes
# blockchain		        getblockcount
# blockchain		        getblock
# blockchain		        getblockhash
# blockchain		        getchaintips
# blockchain		        getdifficulty
# blockchain		        getmempoolinfo
# blockchain		        getrawmempool
# blockchain		        gettxout
# blockchain		        gettxoutproof
# blockchain		        verifytxoutproof
# blockchain		        gettxoutsetinfo
# blockchain		        verifychain
#------------------- CONTROL
# callscontrol			getinfo
# callscontrol			help
# callscontrol			stop
# ------------------ GENERATING
# generating		        generate
# generating		        generatetoaddess
# ------------------ MINING
# mining			 getblocktemplate
# mining			 getmininginfo
# mining			 getnetworkhashps
# mining			 prioritisetransaction
# mining			 submitblock
# ------------------ NETWORK
# network			getnetworkinfo
# network			addnode
# network			disconnectnode
# network			getaddednodeinfo
# network			getconnectioncount
# network			getnettotals
# network			getpeerinfo
# network			ping
# network			setban
# network			listbanned
# network			clearbanned
# ------------------ RAW TRANSACTIONS
# rawtransactions	        createrawtransaction
# rawtransactions	        decoderawtransaction
# rawtransactions	        decodescript
# rawtransactions	        getrawtransaction
# rawtransactions	        sendrawtransaction
# rawtransactions	        signrawtransaction
# rawtransactions	        fundrawtransaction
# ------------------ UTIL
# util			        createmultisig
# util			        validateaddress
# util			        verifymessage
# util			        estimatefee
# util			        estimatesmartfee
# ------------------ WALLET
# wallet			 addmultisigaddress
# wallet			 backupwallet
# wallet                         createwallet                           Yes
# wallet			 dumpprivkey
# wallet			 dumpwallet
# wallet			 encryptwallet
# wallet			 getaccountaddress
# wallet			 getaccount
# wallet			 getaddressesbyaccount
# wallet			 getbalance
# wallet			 getnewaddress                          Yes
# wallet			 getrawchangeaddress
# wallet			 getreceivedbyaccount
# wallet			 getreceivedbyaddress
# wallet			 gettransaction
# wallet			 getunconfirmedbalance
# wallet			 getwalletinfo                          Yes
# wallet			 importprivkey
# wallet			 importwallet
# wallet			 importaddress
# wallet			 keypoolrefill
# wallet			 listaccounts
# wallet			 listaddressgroupings
# wallet			 listlockunspent
# wallet			 listreceivedbyaccount
# wallet			 listreceivedbyaddress                  Yes
# wallet			 listsinceblock
# wallet			 listtransactions                       Yes
# wallet			 listunspent
# wallet			 lockunspent
# wallet			 move
# wallet			 sendfrom
# wallet			 sendmany
# wallet			 sendtoaddress
# wallet			 setaccount
# wallet			 settxfee
# wallet			 signmessage
# wallet			 walletlock
# wallet			 walletpassphrasechange
# wallet			 walletpassphrase
# wallet			 walletprocesspsbt
# ------------------ PSBT
# psbt - decodepsbt
# psbt - combinepsbt
# psbt - finalizepsbt
# psbt - createpsbt
# psbt - convertopsbt
# wallet			 walletcreatefundedpsbt
# ------------------ t shown in help
# hidden			invalidateblock
# hidden			reconsiderblock
# hidden			setmocktime
# hidden			resendwallettransactions
