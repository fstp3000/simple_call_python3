from w3.abi import *
from web3 import HTTPProvider, Web3
from time import sleep
import sys
class farm():
    def __init__(self):
        self.web3 = Web3(HTTPProvider('http://140.112.230.86:30400'))
        self.abi= abi
        self.sc_addr = self.web3.toChecksumAddress("0x7646cc5c03f1d4ac9f5aec134bd5838612facf31")
        self.sd_addr = self.web3.toChecksumAddress("0x132f98e1aa89ff2557f117906997d993fa33338f")
        self.contract = self.web3.eth.contract(abi = self.abi, address = self.sc_addr)
        self.photos = []
    def send(self, photoHash, catogory, numbers, machineID, localtime, gps):
        #photoHash = "0x1500000000000000000000000000000000000000000000000000000000000000"
        #catogory = "0x1100000000000000000000000000000000000000000000000000000000000000"
        #numbers = 5
        #machineID = 10
        #localtime = 60000
        #gps = 100000
        rpt=self.contract.functions.addPhoto(photoHash,
                                             catogory,
                                             numbers,
                                             machineID,
                                             localtime,
                                             gps
                                            ).transact({'from':self.sd_addr})
        print(rpt.hex())
        print("The photo has been uploaded to the blockchain")
    def scan(self):
        print("scaning...")
        num = self.contract.functions.getnumPhotos().call()
        photos = []
        for step in range(num):
            rpt = self.contract.functions.getPhoto(step).call()
            rpt[1] = "0x" + rpt[1].hex()
            rpt[2] = "0x" + rpt[2].hex()
            photos.append(rpt)
            sys.stdout.write('\r')
            sys.stdout.write("[%-20s] %d%%" % ('=' * int(20 * (step+1) / num),
                                               (step+1) * int(100/num)))
            sys.stdout.flush()
        print('\nTotal', num, 'photos on the blockchain')
        self.photos = photos
        print("scan done")
        print("=" * 78)

    def call_by_machineID(self, machineID = None):
        if self.photos is not []:
            self.scan()
        if machineID == None:
            for photo in self.photos:
                self.show(photo)
            print('Total', len(self.photos), 'photos')
        else:
            index = 0
            for photo in self.photos:
                if photo[4] == machineID:
                    index += 1
                    self.show(photo)
            print('Total', index, 'photos match machineID: ', machineID)
    def hash_is_exist(self, photoHash):
        if self.photos is not []:
            self.scan()
        flag = False
        for photo in self.photos:
            if photo[1] == photoHash:
                flag = True
                print("Exist")
                self.show(photo)
                break
        if flag==False:
            print("Not exist")
    def show(self, photo):
        print('photoID:   ', photo[0])
        print('photohash: ', photo[1])
        print('catogory:  ', photo[2])
        print('numbers:   ', photo[3])
        print('machineID: ', photo[4])
        print('localtime: ', photo[5])
        print('gps:       ', photo[6] )
        print('-' * 78)
