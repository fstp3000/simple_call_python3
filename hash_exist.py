from w3.w3config import farm

if __name__=="__main__":
    #web3 initialize
    ethereum = farm()
    #find all machineID you specified
    ethereum.hash_is_exist(photoHash = "0x1500000000000000000000000000000000000000000000000000000000000000")
