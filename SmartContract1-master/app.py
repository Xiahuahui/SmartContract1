#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect
import threading
import json
from DFA import contractdb,create_Reducedfsm,create_fsm,generateCode,createStrategies,reduceStrategies,DGA,Nash,createPayoffMatrix,createReducedPayoffMatrix
import os
from Settings import settings,saveChainCodeDictToFile as scd,readChainCodeDictFromFile as rcd
import pickle as pickle
app = Flask(__name__)
@app.route('/', methods=['GET'])
def form():
    return render_template('index.html'), 200
@app.route('/signup', methods=['GET', 'POST'])
def enroll():
    if request.method == 'GET':
        return render_template('enroll.html'), 200
    else:
        username = request.form.get('form-username', default='user')
        password = request.form.get('form-password', default='pass')
        if contractdb.get_pass(username):
            return 'existed'
        else:
            contractdb.save_user(username, password)
            return 'ok'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html'), 200
    else:
        username = request.form.get('form-username', default='user')
        password = request.form.get('form-password', default='pass')
        db_pass = contractdb.get_pass(username)
        if not db_pass:
            return 'none'
        elif db_pass != password:
            return 'wrong'
        else:
            return 'right'

@app.route('/user', methods=['POST'])
def login_success():
    username = request.form.get('username', default='user')
    return render_template('user.html', username=username), 200

@app.route('/file', methods=['POST'])
def show_file():
    username = request.form.get('username', default='user')
    contracts = contractdb.get_user_contracts(username)

    return render_template('file.html', username=username, contracts=contracts), 200

@app.route('/contract', methods=['POST'])
def contract_form():
    username = request.form.get('username', default='user')
    return render_template('contract.html', username=username), 200

@app.route('/save', methods=['POST'])
def save():
    args = request.get_json()
    contract_id = settings.get_id(args['username'], args['contract_name'])
    contractdb.save_contract(args['username'], args['contract_name'], contract_id, args['party_a'], args['sig_a'],
        args['party_b'], args['sig_b'], args['valid_time'], args['object_desc'], json.dumps(args['content']))
    print(args['content'])
    #t = threading.Thread(target=create_task, args=(args['content'],contract_id))
    #t.start()
    #t.join()
    #create_task(json.dumps(args['content']),contract_id)
    return 'success'

@app.route('/query', methods=['POST'])
def query():
    username = request.form.get('username', default='user')
    contract_id = request.form.get('contract_id', default='id')
    #print(contract_id)
    contract = contractdb.get_contract(username, contract_id)
    #print(contract)
    l = json.loads(contract[10])
    print(l)
    return render_template('contract-content.html', contract=contract, list=l), 200


@app.route('/update', methods=['POST'])
def update():
    username = request.form.get('username', default='user')
    print(username)
    contract_id = request.form.get('contract_id', default='id')
    print(contract_id)
    contract = contractdb.get_contract(username, contract_id)
    print(contract)
    l = json.loads(contract[10])
    length = len(l)
    return render_template('contract-update.html', username=username,contract=contract, list=l,length=length), 200
@app.route('/edit', methods=['POST'])
def edit():
    args = request.get_json()
    contract_id = args['contract_id']
    if os.path.isfile('./data/fsm/'+ contract_id):
        os.remove('./data/fsm/'+ contract_id)
    if os.path.isfile('./data/reducedFsm/'+ contract_id):
        os.remove('./data/reducedFsm/'+ contract_id)
    if os.path.isfile('./data/MyWorkPlace/fsm/' + contract_id + '.pkl'):
        os.remove('./data/MyWorkPlace/fsm/' + contract_id + '.pkl')
    if os.path.isfile('./data/MyWorkPlace/reducedFsm/' + contract_id + '.pkl'):
        os.remove('./data/MyWorkPlace/reducedFsm/' + contract_id + '.pkl')
    if os.path.isfile('./data/code/'+ contract_id + '.go'):
        os.remove('./data/code/'+ contract_id + '.go')
    if os.path.isfile('./data/code/'+ contract_id + 'sol'):
        os.remove('./data/code/'+ contract_id + 'sol')
    if os.path.isfile('./data/MyWorkPlace/choices/' + contract_id + '.pkl'):
        os.remove('./data/MyWorkPlace/choices/' + contract_id + '.pkl')
    if os.path.isfile('./data/MyWorkPlace/reducedChoices/' + contract_id + '.pkl'):
        os.remove('./data/MyWorkPlace/reducedChoices/' + contract_id + '.pkl')
    contractdb.edit_contract(args['username'], args['contract_name'], contract_id, args['party_a'], args['sig_a'],
        args['party_b'], args['sig_b'], args['valid_time'], args['object_desc'], json.dumps(args['content']))
    return 'success'
@app.route('/check', methods=['POST'])
def show_check():
    return '', 200
@app.route('/DFA', methods=['POST'])
def show_DFA():
    contract_id = request.form.get('contract_id', default='id')
    username = request.form.get('username', default='user')
    contract = contractdb.get_contract(username, contract_id)
    path = "./data/fsm/"+contract_id
    if not os.path.isfile(path):
        print(contract[10])
        create_fsm(contract[10],contract_id)
    else:
        print("该状态机已经存在,可以直接返回")
    fsm_struct = settings.read_file(path)
    res = {'fsm': fsm_struct }
    return json.dumps(res), 200
@app.route('/Reduce', methods=['POST'])
def show_Reduce():
    contract_id = request.form.get('contract_id', default='id')
    username = request.form.get('username', default='user')
    path = "./data/fsm/" + contract_id
    print("测试")
    if not os.path.isfile("./data/reducedFsm/" + contract_id):
        if not os.path.isfile(path):
            print("重新生成")
            contract = contractdb.get_contract(username, contract_id)
            create_fsm(contract[10], contract_id)
        print("化简")
        create_Reducedfsm(contract_id)
    else:
        print("化简的状态机已经存在")
    fsm_struct = settings.read_file('./data/reducedFsm/'+contract_id)
    res = {'fsm': fsm_struct }
    return json.dumps(res), 200
@app.route('/test', methods=['POST'])
def test():
    contract_id = request.form.get('contract_id', default='id')
    username = request.form.get('username', default='user')
    payoff_dict = request.form.get('payInput',default = 'payInput')
    payoff_dict = json.loads(payoff_dict)
    if not os.path.isfile("./data/fsm/" + contract_id):
        print("重新生成")
        contract = contractdb.get_contract(username, contract_id)
        create_fsm(contract[10], contract_id)
    print("生成策略")
    print("接收到的数据: ",payoff_dict)
    Payoff = {}
    for state, payoff in payoff_dict.items():
        item = []
        payoffList = payoff.split(',')
        print(state + " " + payoffList[0] + " " + payoffList[1]);
        item.append(int(payoffList[0]))
        item.append(int(payoffList[1]))
        print(state,type(state))
        if state not in payoff:
            print(type(Payoff))
            Payoff[state]= item
        print("当前的payoff:   ",Payoff)
    straSetA,straSetB,ChoicesA,ChoicesB= reduceStrategies(contract_id)
    matrixc,matrixd = createReducedPayoffMatrix(ChoicesA,ChoicesB,Payoff,contract_id)
    nashStates = Nash(ChoicesA,ChoicesB,matrixc,matrixd,contract_id)
    print("纳什均衡叶节点的状态:  ",nashStates)
    res = {'nashStates':nashStates}
    return json.dumps(res), 200
@app.route('/code', methods=['POST'])
def show_code():
    contract_id = request.form.get('contract_id', default='id')
    print("contract_id: ",contract_id)
    print("调用成功")
    username = request.form.get('username', default='user')
    print(username)
    if not os.path.isfile("./data/code/" + contract_id + 'go'):
        if not os.path.isfile("./data/fsm/" + contract_id):
            print("重新生成")
            contract = contractdb.get_contract(username, contract_id)
            create_fsm(contract[10], contract_id)
        generateCode('./data/fsm/' + contract_id,'./data/code/' + contract_id)
    go_code = settings.process_code('./data/code/'+ contract_id + '.go')
    print(go_code)
    res = {'go': go_code}
    return json.dumps(res), 200
@app.route('/deploy', methods=['POST'])
def deployCode():
    print("端口调用成功")
    contract_id = request.form.get('contract_id', default='id')
    chainCodeDict = rcd("chainCodeDict.text")
    contract_codeId = None
    if contract_id not in chainCodeDict:
        contract_codeId = contract_id + '1'
        chainCodeDict[contract_id] = [contract_codeId]
        scd(chainCodeDict,'chainCodeDict.text')
    else:
        contract_codeIds = chainCodeDict[contract_id]
        contract_codeId = int(contract_codeIds[-1][len(contract_id):]) + 1
        contract_codeId = contract_id + str(contract_codeId)
        chainCodeDict[contract_id].append(contract_codeId)
        scd(chainCodeDict, 'chainCodeDict.text')
    os.system('mkdir ./data/code/' + contract_codeId)
    os.system('cp ./data/code/cc/* ./data/code/' + contract_codeId)
    os.system('cp ./data/code/'+contract_id+'.go'+' ./data/code/' + contract_codeId)
    os.system('mv ./data/code/'+contract_codeId + '/' + contract_id +'.go' + " " +'./data/code/'+contract_codeId + '/' + contract_codeId +'.go')
    contract_codeId = chainCodeDict[contract_id][-1]
    os.system("./scripts/putChaincode.sh"+ " " +contract_codeId)
    print("上传成功")
    os.system('gnome-terminal -x bash -c "sh ./scripts/install.sh'+" "+contract_codeId +';exec bash;"')
    print("链码成功部署")
    os.system('rm -rf ./data/code/' + contract_codeId)
    print("本地链码部署包成功删除")
    return "" , 200
if __name__ == '__main__':
    host = settings.dbConfig['local']["host"]
    port = int(settings.dbConfig['local']["port"])
    debug = settings.dbConfig['local']["debug"]
    if debug == "True":
        debug = True
    else:
        debug = False
    print(debug)
    app.run(host=host, port=port, threaded=True, debug=debug)
