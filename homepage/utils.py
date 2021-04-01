from web3 import Web3

def balance_eth():
    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/759e569e7aa946afaba848dac94fe25d'))
    address = '0x3a32D02cD13eA415Bc22D8E7656fCE90ABC5A382'
    return w3.eth.get_balance(address)