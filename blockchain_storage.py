from web3 import Web3
import json

# Blockchain Configuration
with open('config/blockchain_config.json', 'r') as config_file:
    config = json.load(config_file)

web3 = Web3(Web3.HTTPProvider(config["blockchain_url"]))

# Connect to Blockchain
if web3.isConnected():
    print("Connected to Ethereum Blockchain!")
else:
    raise ConnectionError("Failed to connect to Ethereum Blockchain.")

# Smart Contract Interaction
contract_address = config["contract_address"]
with open('config/contract_abi.json', 'r') as abi_file:
    contract_abi = json.load(abi_file)

contract = web3.eth.contract(address=contract_address, abi=contract_abi)

def store_transaction_data(transaction_id, metadata_hash):
    tx = contract.functions.storeData(transaction_id, metadata_hash).transact({'from': web3.eth.accounts[0]})
    web3.eth.waitForTransactionReceipt(tx)
    print(f"Data stored on blockchain with transaction ID: {transaction_id}")
