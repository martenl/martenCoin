from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from BlockChainUtils import BlockChainUtils
from Transaction import Transaction


class Wallet:

    def __init__(self, ):
        self.keyPair = RSA.generate(2048)

    def sign(self, data):
        hashed_data = BlockChainUtils.hash(data)
        signature_scheme_object = PKCS1_v1_5.new(self.keyPair)
        return signature_scheme_object.sign(hashed_data).hex()

    @staticmethod
    def signature_valid(data, signature, public_key):
        signature = bytes.fromhex(signature)
        data_hash = BlockChainUtils.hash(data)
        public_key = RSA.importKey(public_key)
        signature_scheme_object = PKCS1_v1_5.new(public_key)
        return signature_scheme_object.verify(data_hash, signature)

    def public_key_string(self):
        return self.keyPair.public_key().exportKey('PEM').decode('utf-8')

    def create_transaction(self, receiver, amount, type):
        transaction = Transaction(self.public_key_string(), receiver, amount, type)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction
