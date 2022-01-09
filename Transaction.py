import uuid
import time
import copy


class Transaction:

    def __init__(self, senderPublicKey, receiverPublicKey, amount, type):
        self.senderPublicKey = senderPublicKey
        self.receiverPublicKey = receiverPublicKey
        self.amount = amount
        self.type = type
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        return self.__dict__

    def sign(self, signature):
        self.signature = signature

    def payload(self):
        json_representation = copy.deepcopy(self.toJson())
        json_representation['signature'] = ''
        return json_representation

    def __str__(self):
        return str(self.toJson())
