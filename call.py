from web3 import HTTPProvider, Web3

web3 = Web3(HTTPProvider('http://140.112.230.86:30400'))

print(web3.eth.blockNumber)


abi = [{"constant": False,"inputs":[{"name":"photohash","type":"bytes32"},{"name":"output","type":"uint256"}],"name":"addPhoto","outputs":[],"payable":False,"stateMutability":"nonpayable","type": "function"},{"constant":True,"inputs":[{"name":"photoID","type":"uint256"}],"name":"getPhoto","outputs":[{"name":"","type":"uint256"},{"name":"","type":"bytes32"},{"name":"","type":"uint256"}],"payable":False,"stateMutability": "view","type": "function"}]

sc_address = "0xebfb59b2e1de60807411fb6a02538e1a20a394ac"
sc_address = web3.toChecksumAddress(sc_address);
sender_address = "0x132f98e1aa89ff2557f117906997d993fa33338f"
sender_address = web3.toChecksumAddress(sender_address)
contract = web3.eth.contract(abi = abi, address = sc_address);


photoHash = "0x1500000000000000000000000000000000000000000000000000000000000000"
photoInfo = 0x1100000000000000000000000000000000000000000000000000000000000000

re = contract.functions.addPhoto(photoHash,photoInfo).transact({'from': sender_address})
#re = contract.functions.getPhoto(0).call({'from': sender_address})
print(re.hex())

