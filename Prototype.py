import json
import hashlib
import json
import datetime
from flask import Flask, jsonify

class BLOCKCHAIN:
    def __init__(self):
        self.chain = []
        #creates genesis block
        self.new_block(proof=1, previous_hash='0')
    
    def new_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
 
    def print_previous_block(self):
        return self.chain[-1]
 
 
 #Proof of work protocol I will be chainging this to find faster methods also will be testing privacy mechanisms 
    def PoW(self, last_proof):
        #parameters are created here to create a new block
        proof = 1
        valid = 0
        
        while valid is 0:
            hash_guessed = hashlib.sha256(str(proof**2-last_proof**2).encode()).hexdigest()
            if hash_guessed[:5] == "00000":
                valid = 1
            else:
                proof += 1
        
        return proof    
    
    def hash(self, block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

#creates app and the object of the class BLOCKCHAIN
app = Flask(__name__)
blockchain = BLOCKCHAIN()

#/mine is the command to mine blocks 
@app.route('/mine', methods=['GET'])
def mine():
    #loops to mine a certain number of blocks 
    for _ in range(600):
        previous_block = blockchain.print_previous_block()
        previous_proof = previous_block['proof']
        proof = blockchain.PoW(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.new_block(proof, previous_hash)
     
        block = {'message': 'A block is MINED',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'proof': block['proof'],
                    'previous_hash': block['previous_hash']}
     
    return jsonify(block), 200

#working on displaying and checking if valid here




# Run the flask server locally
if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='0.0.0.0', port=port)