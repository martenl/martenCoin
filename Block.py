import copy
import time

import Transaction


class Block:

    def __init__(self, transactions: list, last_hash: str, forger, block_count: int):
        self.transactions = transactions
        self.last_hash = last_hash
        self.forger = forger
        self.block_count = block_count
        self.time_stamp = time.time()
        self.signature = ''

    def toJson(self):
        json = self.__dict__
        #print(type(self))
        #print(self.transactions[0])
        #print(self.transactions)
        json['transactions'] = list(map(lambda tx: tx.toJson() if type(tx) == Transaction.Transaction else tx, self.transactions))
        return json

    def __str__(self):
        return str(self.toJson())

    def payload(self):
        payload = copy.deepcopy(self.toJson())
        payload['signature'] = ''
        return payload

    def sign(self, signature):
        self.signature = signature
