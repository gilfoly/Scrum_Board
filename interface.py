from web3 import Web3
import json
url = 'http://127.0.0.1:8545'


web3 = Web3(Web3.HTTPProvider(url))
print(web3.isConnected())

abi = json.loads('[{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"stories","outputs":[{"name":"id","type":"uint256"},{"name":"name","type":"string"},{"name":"writer","type":"address"},{"name":"status","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_name","type":"string"}],"name":"createStory","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_id","type":"uint256"}],"name":"updateStatus","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_id","type":"uint256"}],"name":"emergency","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"StoryCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"anonymous":false,"inputs":[{"indexed":false,"name":"id","type":"uint256"},{"indexed":false,"name":"name","type":"string"},{"indexed":false,"name":"writer","type":"address"},{"indexed":false,"name":"status","type":"uint256"}],"name":"StoryCreated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"id","type":"uint256"},{"indexed":false,"name":"name","type":"string"},{"indexed":false,"name":"writer","type":"address"},{"indexed":false,"name":"status","type":"uint256"}],"name":"InEmergency","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"id","type":"uint256"},{"indexed":false,"name":"name","type":"string"},{"indexed":false,"name":"writer","type":"address"},{"indexed":false,"name":"status","type":"uint256"}],"name":"StatusUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"id","type":"uint256"},{"indexed":false,"name":"name","type":"string"},{"indexed":false,"name":"writer","type":"address"},{"indexed":false,"name":"status","type":"uint256"}],"name":"InTesting","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"id","type":"uint256"},{"indexed":false,"name":"name","type":"string"},{"indexed":false,"name":"writer","type":"address"},{"indexed":false,"name":"status","type":"uint256"}],"name":"Completed","type":"event"}]')
address = web3.toChecksumAddress('0x4fe4035fa76788dcd3f3b855f703d86ff2cdc4be')
ScrumModel = web3.eth.contract(abi = abi, address = address)

account = web3.eth.accounts
user = account[0]



def createStory(name):
	tx_hash = ScrumModel.functions.createStory(name).transact({
		'from': user
		})
	tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
def emergency(id):
	tx_hash = ScrumModel.functions.emergency(id).transact({
		'from':user
		})
	tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

def updateStatus(id):
	tx_hash = ScrumModel.functions.updateStatus(id).transact({
		'from':user
		})
	tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

def Data():
	StoryCount = ScrumModel.functions.StoryCount().call()

	iceboxList = []
	emergencyList =[]
	inprogressList = []
	testingList = []
	completeList = []

	for i in range(1,StoryCount+1):
		story = ScrumModel.functions.stories(i).call()
		if story[3] == 1:
			iceboxList.append(story)
		elif story[3] == 2:
			emergencyList.append(story)
		elif story[3] == 3:
			inprogressList.append(story)
		elif story[3] == 4:
			testingList.append(story)
		else:
			completeList.append(story)
	return iceboxList,emergencyList,inprogressList,testingList,completeList,user

