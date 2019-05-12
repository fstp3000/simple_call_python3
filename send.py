from w3.w3config import farm

if __name__=="__main__":
    #photohash type byte32
    photoHash = "0x1500000000000000000000000000000000000000000000000000000000000000"
    #catogory type byte32, ex laddy bugs
    catogory = "0x1100000000000000000000000000000000000000000000000000000000000000"
    #numbers type int32, number of laddy bugs
    numbers = 5
    #machineID type int32, to known who send the message
    machineID = 10
    #localtime type int32, the local timestamp
    localtime = 60000
    #gps type int32
    gps = 100000

    #web3 initialize
    ethereum = farm()
    #send function
    ethereum.send(photoHash, catogory, numbers, machineID, localtime, gps)
