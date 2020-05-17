import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def get_utc_time(self):
        return datetime.utcfromtimestamp(float(self.timestamp))

    def calc_hash(self):
        encodedData = hashlib.sha256(self.data.encode('utf-8'))
        encodedTimestamp = hashlib.sha256(self.timestamp.encode('utf-8'))
        encodedData.hexdigest()
        encodedTimestamp.update(encodedData.digest())
        if(self.previous_hash is not None):
            encodedTimestamp.update(self.previous_hash.hash.encode("utf-8"))
        return encodedTimestamp.hexdigest()


class BlockChain:

    def __init__(self):
        self.tail = None

    def add_block(self, data):
        if self.tail is None:
            self.tail = Block(str(datetime.now().timestamp()), data, None)
        else:
            tail = self.tail
            block = Block(str(datetime.now().timestamp()), data, tail)
            self.tail = block

        return self.tail

    def print_blockchain(self):
        tail = self.tail
        while tail is not None:
            print("<-", tail.data, tail.hash, tail.get_utc_time())
            tail = tail.previous_hash


def test_block_created():
    blockchain = BlockChain()
    blockchain.add_block("hey")
    blockchain.add_block("ho")
    blockchain.add_block("lets")
    blockchain.add_block("go")
    blockchain.print_blockchain()


def _check_hash(hash_previous, hash_after):
    current = hash_previous
    after = hash_after

    while current is not None:
        current_hash = current.hash
        if after.previous_hash.hash != current_hash:
            return "Not Passed"
        after = current
        current = current.previous_hash

    return "Pass"


def test_hash_matching():
    blockchain = BlockChain()
    blockchain.add_block("hey")
    blockchain.add_block("ho")
    blockchain.add_block("lets")
    blockchain.add_block("go")
    print(_check_hash(blockchain.tail.previous_hash, blockchain.tail))


def test_created_before():
    blockchain = BlockChain()
    start = blockchain.add_block("hey")
    blockchain.add_block("ho")
    blockchain.add_block("lets")
    blockchain.add_block("go")

    current = blockchain.tail
    while current.previous_hash is not None:
        current = current.previous_hash

    print("Pass" if current == start else "Not Passed")


test_block_created()
test_hash_matching()
test_created_before()