from abi import *
from web3 import HTTPProvider, Web3
class farm():
    def __init__(self):
        self.web3 = Web3(HTTPProvider('http://140.112.230.86:30400'))
        self.abi= abi
        self.sc_addr = self.web3.toChecksumAddress("0xebfb59b2e1de60807411fb6a02538e1a20a394ac")
        self.sd_addr = self.web3.toChecksumAddress("0x132f98e1aa89ff2557f117906997d993fa33338f")
        self.contract = self.web3.eth.contract(abi = self.abi, address = self.sc_addr)
    def send(self):
        photoHash = "0x1500000000000000000000000000000000000000000000000000000000000000"
        photoInfo = 0x1100000000000000000000000000000000000000000000000000000000000000
        rpt=self.contract.functions.addPhoto(photoHash,photoInfo).transact({'from':self.sd_addr})
        print(rpt.hex())
    def call(self):
        rpt = self.contract.functions.getPhoto(0).call()
        rpt[1] = rpt[1].hex()
        print(rpt)
