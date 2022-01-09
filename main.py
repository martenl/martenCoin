from Transaction import Transaction
from Wallet import Wallet


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    sender = 'sender'
    receiver = 'receiver'
    amount = 1
    type = 'TRANSFER'

    wallet = Wallet()
    transaction = wallet.create_transaction(receiver, amount, type)
    signature = transaction.signature

    signatureValid = Wallet.signature_valid(transaction.payload(), signature, wallet.public_key_string())
    my_scammy_transaction = transaction.toJson()
    my_scammy_transaction['amount'] = 100
    print(signatureValid)
