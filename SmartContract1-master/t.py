args = request.get_json()
print(args)
editusername = args['username']
editcontract_id = args['contract_id']
# print(contract_id)
contract = db.get_contract(editusername, editcontract_id)
l = json.loads(contract[10])