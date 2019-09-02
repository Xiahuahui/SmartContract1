#! /usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Flask, request, render_template, redirect
import threading
import json
import util
import db
import DFA
import payoff1
import LCA
import time
import os
import pathlib
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
        if db.get_pass(username):
            return 'existed'
        else:
            db.save_user(username, password)
            return 'ok'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html'), 200
    else:
        username = request.form.get('form-username', default='user')
        password = request.form.get('form-password', default='pass')
        db_pass = db.get_pass(username)
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
    contracts = db.get_user_contracts(username)

    return render_template('file.html', username=username, contracts=contracts), 200

@app.route('/contract', methods=['POST'])
def contract_form():
    username = request.form.get('username', default='user')
    return render_template('contract.html', username=username), 200

@app.route('/save', methods=['POST'])
def save():
    args = request.get_json()
    contract_id = util.get_id(args['username'], args['contract_name'])
    db.save_contract(args['username'], args['contract_name'], contract_id, args['party_a'], args['sig_a'],
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
    contract = db.get_contract(username, contract_id)
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
    contract = db.get_contract(username, contract_id)
    print(contract)
    l = json.loads(contract[10])
    length = len(l)
    return render_template('contract-update.html', username=username,contract=contract, list=l,length=length), 200
@app.route('/edit', methods=['POST'])
def edit():
    args = request.get_json()
    contract_id = args['contract_id']
    db.edit_contract(args['username'], args['contract_name'], contract_id, args['party_a'], args['sig_a'],
        args['party_b'], args['sig_b'], args['valid_time'], args['object_desc'], json.dumps(args['content']))
    return 'success'
@app.route('/check', methods=['POST'])
def show_check():
    contract_id = request.form.get('contract_id', default='id')
    username = request.form.get('username', default='user')
    bestPos= request.form.get('bestPos', default='user')
    bestPos = list(bestPos)
    bestPos1 = []
    bestPos1.append(int(bestPos[1]))
    bestPos1.append(int(bestPos[3]))
    contract = db.get_contract(username, contract_id)
    a = check(contract[10],contract_id,bestPos1)
    a = a[0]
    gt = util.read_gt(contract_id)
    res = {'a': a , "gt":gt}
    return json.dumps(res), 200
@app.route('/DFA', methods=['POST'])
def show_DFA():
    contract_id = request.form.get('contract_id', default='id')
    username = request.form.get('username', default='user')
    contract = db.get_contract(username, contract_id)

    create_DFA(contract[10],contract_id)
    fsm_struct = util.read_fsm(contract_id)
    res = {'fsm': fsm_struct }
    print(fsm_struct)
    return json.dumps(res), 200
@app.route('/Reduce', methods=['POST'])
def show_Reduce():
    contract_id = request.form.get('contract_id', default='id')
    fsm_struct = util.read_fsm1(contract_id)
    res = {'fsm': fsm_struct }
    return json.dumps(res), 200

@app.route('/payoff', methods=['POST'])
def show_payoff():
    contract_id = request.form.get('contract_id', default='id')
    username = request.form.get('username', default='user')
    contract = db.get_contract(username, contract_id)
    path = pathlib.Path("./payoff/" + contract_id)
    A = path.is_file()
    if A == False:
        create_payoff(contract[10],contract_id)
    NASH = util.read_NASH(contract_id)
    payoff = util.read_payoff(contract_id)
    wight = util.read_wight(contract_id)
    Row = util.read_Row(contract_id)
    res = {'NASH':NASH  ,"payoff" :payoff,"wight":wight ,"Row":Row }
    return json.dumps(res), 200
def create_DFA(contract,contract_id):
    DFA.create_fsm(contract, contract_id)

def create_payoff(contract, contract_id):
    payoff1.create_payoff(contract, contract_id)
def check(contract, contract_id,bestPos):
    return LCA.check_payoff(contract, contract_id,bestPos)
if __name__ == '__main__':
    host = util.get_config()["host"]
    port = int(util.get_config()["port"])
    debug = util.get_config()["debug"]
    if debug == "True":
        debug = True
    else:
        debug = False
    print(debug)
    app.run(host=host, port=port, threaded=True, debug=debug)
