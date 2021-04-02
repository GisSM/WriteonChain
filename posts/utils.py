from web3 import Web3

def send_transaction(message):

    w3 = Web3(Web3.HTTPProvider('https://ropsten.infura.io/v3/759e569e7aa946afaba848dac94fe25d'))
    address = '0x3a32D02cD13eA415Bc22D8E7656fCE90ABC5A382'
    privateKey = '0x40c9d93c931913e7e6d6876a009eab43b05df64b1aa83009861ee43870b11e75'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gas_price
    value = w3.toWei(0,'ether')
    signedTx=w3.eth.account.sign_transaction({
        'nonce':nonce,
        'gasPrice':gasPrice,
        'gas':100000,
        'to':'0x0000000000000000000000000000000000000000',
        'value':value,
        'data':message.encode('utf-8')
    },privateKey)
    tx=w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId=w3.toHex(tx)
    return txId
