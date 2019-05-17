abi = [
	{
		"constant": False,
		"inputs": [
			{
				"name": "photohash",
				"type": "bytes32"
			},
			{
				"name": "category",
				"type": "bytes32"
			},
			{
				"name": "numbers",
				"type": "int32"
			},
			{
				"name": "machineID",
				"type": "int32"
			},
			{
				"name": "localtime",
				"type": "int32"
			},
			{
				"name": "gps",
				"type": "int32"
			}
		],
		"name": "addPhoto",
		"outputs": [],
		"payable": False,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [],
		"name": "getnumPhotos",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": True,
		"inputs": [
			{
				"name": "photoID",
				"type": "uint256"
			}
		],
		"name": "getPhoto",
		"outputs": [
			{
				"name": "",
				"type": "uint256"
			},
			{
				"name": "",
				"type": "bytes32"
			},
			{
				"name": "",
				"type": "bytes32"
			},
			{
				"name": "",
				"type": "int32"
			},
			{
				"name": "",
				"type": "int32"
			},
			{
				"name": "",
				"type": "int32"
			},
			{
				"name": "",
				"type": "int32"
			}
		],
		"payable": False,
		"stateMutability": "view",
		"type": "function"
	}
]


