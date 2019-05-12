from w3.w3config import farm

if __name__=="__main__":
    #web3 initialize
    ethereum = farm()
    #find all machineID you specified
    #machineID could be None, it will show all the photos
    ethereum.call_by_machineID(machineID = 10)
