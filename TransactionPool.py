
class TransactionPool:

    def __init__(self):
        self.transactions = []

    def addTransaction(self, tx):
        if not self.transactionExists(tx):
            self.transactions.append(tx)

    def transactionExists(self, tx):
        return any(map(lambda x: x == tx, self.transactions))
