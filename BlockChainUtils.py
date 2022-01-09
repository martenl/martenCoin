from Crypto.Hash import SHA256
import json


class BlockChainUtils:

    @staticmethod
    def hash(data):
        bytes = json.dumps(data).encode('utf-8')
        return SHA256.new(bytes)
