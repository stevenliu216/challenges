# Challenge 35 Part 1
A blockchain is simply a database where new data is stored in a container and then chained together with past data. The integrity of the data is ensured by hashing the block's contents. For this challenge, we are going to build our own blockchain technology. 

## Requirements
The first step is to represent a Block in python. Complete this challenge by populating the provided Block class's members and generating its hash. A Block is made up of:
- An index number
- The current time
- The data (A string in our implementation)
- Previous block's hash. If the Block is the very first one, let the previous hash be 0.
- Current block's hash

## Hints
Python has the `hashlib` module. Use its sha256 hashing algorithm to generate the current Block's hash based on the Block's index, timestamp, data, and previous block's hash.

### Function prototype:
```python
import hashlib as hasher
import datetime as date

class Block:
  def __init__(self, index, timestamp, data, previous_hash):
    self.index = 
    self.timestamp = 
    self.data = 
    self.previous_hash = 0
    self.hash = self.hash_block()
  
  def hash_block(self):
    '''
        1. Calculate a SHA256 hash based on:
            - self.index
            - self.timestamp
            - self.data
            - self.previous_hash
        2. Return the computed hash as a hexadecimal string 
    '''
    pass

if __name__=='__main__':
    block = Block(0, date.datetime.now(), "Example data", "0"))
    print("Index: {}\nTimestamp: {}\nData: {}\nPrevious Hash: {}\nHash: {}".format(block.index, block.timestamp, block.data, block.previous_hash, block.hash))
 ```


### Example Output
```
Index: 0
Timestamp: 2019-07-15 12:46:26.857417
Data: Example data
Previous Hash: 0
Hash: ee295c1b3dd06272fd921c6d4c2642af39a3a5bb828881ba32d1334eab42e714
```
 
### Explanation
* The `block` is a `Block` object with properties as we defined. 
* The Hash was calculated and displayed as a hex string
