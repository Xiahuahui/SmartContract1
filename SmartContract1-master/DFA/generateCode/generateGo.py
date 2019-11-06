import json
def resolveJson(path):
    file = open(path,'r')
    fileJson = json.load(file)
    InitStatus = fileJson['InitStatus']
    FsmArray=fileJson['FsmArray']
    #print(FsmArray)
    CurrentStatus=[]
    Action=[]
    NewStatus=[]
    for array in FsmArray:
        strCurrentStatus = ''.join(map(str,array['CurrentStatus']))
        CurrentStatus.append(strCurrentStatus)
        Action.append(array['Action'])
        strNewStatus = ''.join(map(str,array['NewStatus']))
        NewStatus.append(strNewStatus)
    return (InitStatus,CurrentStatus,Action,NewStatus)
def transferGo(path, fileName):
    file = open(fileName + ".go", 'w')
    result = resolveJson(path)
    initStatus = result[0]
    currentStatus = result[1]
    currentStatus_str = '","'.join(currentStatus)
    action = result[2]
    for i in range(len(action)):
        if "Sat" in action[i]:
            action[i]="Sat"
        elif "Vio" in action[i]:
            action[i]="Vio"
        else: action[i] ="Term"
    action_str = '","'.join(action)
    newStatus = result[3]
    newStatus_str='","'.join(newStatus)
    str1 = '//status.go\n\n\n'
    strPackage = 'package main\n\n'
    strImport = 'import (\n  "fmt"\n  "reflect"\n ' \
               + '  "github.com/hyperledger/fabric/core/chaincode/shim"\n  pb "github.com/hyperledger/fabric/protos/peer"\n)\n\n\n'
    strInitFSM = 'func InitFSM(initStatus string) *FSM {\n   var action  = [...]string{"'+action_str+'"}\n   var currentStatus  = [...]string{"'+currentStatus_str\
               +'"}\n   var newStatus  = [...]string{"'+newStatus_str+'"}\n   var events []EventDesc = make([]EventDesc, 0)\n   var termNum=len(action)\n   for i := 0; i < termNum; i ++ {'\
               + '\n    events = append(events, EventDesc{Name: action[i], Src: []string{currentStatus[i]}, Dst: newStatus[i]})\n   '\
               + '}\n   f := NewFSM(\n   initStatus,\n   events,\n   Callbacks{},\n   )\n   return f;\n}\n\n\n'
    strInit = '// =========================================\n//       Init - initializes chaincode\n// =========================================\n'\
               + 'func (t *SimpleChaincode) Init(stub shim.ChaincodeStubInterface) pb.Response {\n  formNumber := "EXP1"\n  status :="'+result[0]+'"\n  stub.PutState(formNumber, []byte(status))\n return shim.Success([]byte(status))\n}\n\n\n'
    strMain = '// ============\n//     Main\n// ============\nfunc main() {\n  err := shim.Start(new(SimpleChaincode))\n  if err != nil {\n'\
               + '    fmt.Printf("Error starting Contract chaincode: %s", err)\n  }\n}\n\n\n'
    strSimpleChaincode='type SimpleChaincode struct {\n}\n\n'
    # invokeArray = []
    # invokeStr = ''
    strCurrent='func (t *SimpleChaincode)Current_State(stub shim.ChaincodeStubInterface, args []string) pb.Response {\n   formNumber := args[0]\n   bstatus, err := stub.GetState(formNumber)\n   if err != nil {\n      return shim.Error("Query form status fail, form number:" + formNumber)\n   }\n   status := string(bstatus)\n   '\
               +'fmt.Println("Form[" + formNumber + "] status:" + status)\n   return shim.Success(nil)\n}\n\n'


    invokeTitle = '// ======================================================\n//       Invoke - Our entry point for Invocations\n'\
               + '// ======================================================\nfunc (t *SimpleChaincode) Invoke(stub shim.ChaincodeStubInterface) pb.Response {\n  '\
               + ' function, args := stub.GetFunctionAndParameters()\n   fmt.Println("invoke is running " + function)\n   if function == "Current_State" {\n      return t.Current_State(stub, args)\n   } else {\n      return Call_FsmEvent(stub,function,args)\n   }\n}\n\n'
    # for k in range(len(action)):
    #     invokeArray.append('if function == "' + action[k] + '" {\n    return FsmEvent(stub, args, "' + action[k] + \
    #            '")\n  } else ')
    #     invokeStr = invokeStr + invokeArray[k]
    # strError = '{\n    return shim.Error("Function doesn\'t exits, make sure function is right!")\n  }\n\n  return shim.Success(nil)\n}\n\n\n'
    strInvoke = invokeTitle

    strFsmEvent = 'func Call_FsmEvent(stub shim.ChaincodeStubInterface, event string,params []string) pb.Response{\n   name:=event\n'\
               + '   formNumber := params[0]\n   bstatus, err := stub.GetState(formNumber)\n   if err != nil {\n      return shim.Error("Query form status fail, form number:" + formNumber)\n   }\n\n   status := string(bstatus)\n'\
               + '   fmt.Println("Form[" + formNumber + "] status:" + status)\n   f := InitFSM(status)\n   err = f.Event(event)\n   if err != nil {\n      return shim.Error("Current status is " + status + " does not support event:" + event)\n  }\n'\
               + '   f_name:= reflect.ValueOf(command[name])\n   if len(params) != f_name.Type().NumIn()+1 {\n      return shim.Error("Params Error!")\n   }\n\n   //然后将传入参数转为反射类型切片\n   in := make([]reflect.Value, len(params)-1)\n   for k, param := range params[1:] {\n'\
               + '      in[k] = reflect.ValueOf(param)\n    }\n   //利用函数反射对象的call方法调用函数\n   f_name.Call(in)\n   status = f.Current()\n   fmt.Println("New status:" + status)\n   stub.PutState(formNumber, []byte(status))\n'\
               + '   return shim.Success([]byte(status))\n}\n\n'

    funcArray = []
    funcStr = ''
    action_set=set(action)
    action_set=list(action_set)
    for i in range(len(action_set)):
        funcArray.append('func ' + action_set[i] + '(name string ,term string) {\n'\
                       + '   fmt.Println(name+" : "+term)\n}\n\n\n')
        funcStr = funcStr + funcArray[i]

    strCommand='var command= map[string]interface{} {\n   '
    for i in range(len(action_set)):
        strCommand =strCommand+'"'+action_set[i]+'":'+action_set[i]+', '

    strCommand=strCommand+'}'
    strSol = strPackage + strImport + strSimpleChaincode + strInitFSM +strInit + strInvoke  + strCurrent + strFsmEvent + funcStr + strCommand + strMain
    file.write(strSol)
    file.close()


if __name__ == '__main__':
    transferGo('./cce.json','status323')
    # result=resolveJson('./term2.json')
    # print(result[1])
