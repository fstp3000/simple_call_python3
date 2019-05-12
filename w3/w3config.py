from w3.abi import *
from web3 import HTTPProvider, Web3
class farm():
    def __init__(self):
        self.web3 = Web3(HTTPProvider('http://140.112.230.86:30400'))
        self.abi= abi
        self.sc_addr = self.web3.toChecksumAddress("0x2c60332b32d4820a88a40fa11a26f120f2ff4192")
        self.sd_addr = self.web3.toChecksumAddress("0x132f98e1aa89ff2557f117906997d993fa33338f")
        self.contract = self.web3.eth.contract(abi = self.abi, address = self.sc_addr)
        self.photos = []
    def send(self):
        photoHash = "0x1500000000000000000000000000000000000000000000000000000000000000"
        catogory = "0x1100000000000000000000000000000000000000000000000000000000000000"
        numbers = 5
        machineID = 10
        localtime = 60000
        gps = 100000
        rpt=self.contract.functions.addPhoto(photoHash,
                                             catogory,
                                             numbers,
                                             machineID,
                                             localtime,
                                             gps
                                            ).transact({'from':self.sd_addr})
        print(rpt.hex())
        print("complete")
    def scan(self):
        step = 0
        photos = []
        while True:
            rpt = self.contract.functions.getPhoto(step).call()
            rpt[1] = "0x" + rpt[1].hex()
            rpt[2] = "0x" + rpt[2].hex()
            if rpt[1] == '0x0000000000000000000000000000000000000000000000000000000000000000':
                #print('Total', step, 'photos on the blockchain')
                self.photos = photos
                break
            #print(rpt)
            photos.append(rpt)
            step += 1
    def call(self):
        if self.photos is not []:
            print("scaning...")
            self.scan()
            print("scan done")
        for photo in self.photos:
            print(photo)
    def call3(self):
        rpt = self.contract.functions.getPhoto(0).call()
