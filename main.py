from TransactionPool import TransactionPool
from Wallet import Wallet
from Block import Block
import pprint


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

    wallet = Wallet()
    transaction = wallet.create_transaction(receiver, amount, type)
    transaction2 = wallet.create_transaction(receiver, amount * 100, type)
    # txPool = TransactionPool()
    # print(txPool.transactionExists(transaction))
    # txPool.addTransaction(transaction)
    # print(txPool.transactionExists(transaction))
    # signature = transaction.signature


    myBlock = wallet.create_block([transaction, transaction2], 'last hash', 1)

    pprint.pprint(myBlock.toJson())
    valid = Wallet.signature_valid(myBlock.payload(), myBlock.signature, wallet.public_key_string())
    print(valid)
    # signatureValid = Wallet.signature_valid(transaction.payload(), signature, wallet.public_key_string())
    # my_scammy_transaction = transaction.toJson()
    # my_scammy_transaction['amount'] = 100
    # print(signatureValid)
