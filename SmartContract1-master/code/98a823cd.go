package main

import (
  "fmt"
  "reflect"
  "io/ioutil"
  "encoding/json"
  "github.com/looplab/fsm"

  "github.com/hyperledger/fabric/core/chaincode/shim"
  pb "github.com/hyperledger/fabric/protos/peer"
)


// =========================================
//       Init - initializes chaincode
// =========================================
func (c *ContractChaincode) Init(stub shim.ChaincodeStubInterface) pb.Response {
  return shim.Success(nil)
}


// ============
//     Main
// ============
func main() {
  err := shim.Start(new(ContractChaincode))
  if err != nil {
    fmt.Printf("Error starting Contract chaincode: %s", err)
  }
}


// ======================================================
//       Invoke - Our entry point for Invocations
// ======================================================
func (c *ContractChaincode) Invoke(stub shim.ChaincodeStubInterface) pb.Response {
  function, args := stub.GetFunctionAndParameters()

  if function == "(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))" {
    return FsmEvent(stub, args, "(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))")
  } else if function == "(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|A!judge(B))" {
    return FsmEvent(stub, args, "(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|A!judge(B))")
  } else if function == "(Term1A!judge(B,2)|A!judge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))" {
    return FsmEvent(stub, args, "(Term1A!judge(B,2)|A!judge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))")
  } else if function == "(Term1A!judge(B,2)|A!judge(A,3), Term2A!judge(A)|A!judge(B))" {
    return FsmEvent(stub, args, "(Term1A!judge(B,2)|A!judge(A,3), Term2A!judge(A)|A!judge(B))")
  } else if function == "(Term1Asat1212, Term2Asat333)" {
    return FsmEvent(stub, args, "(Term1Asat1212, Term2Asat333)")
  } else if function == "(Term1Asat1212, Term2Avio333)" {
    return FsmEvent(stub, args, "(Term1Asat1212, Term2Avio333)")
  } else if function == "(Term1Avio1212, Term2Asat333)" {
    return FsmEvent(stub, args, "(Term1Avio1212, Term2Asat333)")
  } else if function == "(Term1Avio1212, Term2Avio333)" {
    return FsmEvent(stub, args, "(Term1Avio1212, Term2Avio333)")
  } else if function == "(Term1Asat1212)" {
    return FsmEvent(stub, args, "(Term1Asat1212)")
  } else if function == "(Term1Avio1212)" {
    return FsmEvent(stub, args, "(Term1Avio1212)")
  } else if function == "(Term2Asat333)" {
    return FsmEvent(stub, args, "(Term2Asat333)")
  } else if function == "(Term2Avio333)" {
    return FsmEvent(stub, args, "(Term2Avio333)")
  } else {
    return shim.Error("Function doesn't exits, make sure function is right!")
  }

  return shim.Success(nil)
}


func InitFSM() *fsm.FSM {
  var events []fsm.EventDesc = make([]fsm.EventDesc, 0)
  for i := 0; i < termNum; i ++ {
    events = append(events, fsm.EventDesc{Name: action[i], Src: []string{currentStatus[i]}, Dst: newStatus[i]})
  }
  f := fsm.NewFSM(
    initStatus,
    events,
    fsm.Callbacks{},
  )
  return f;
}


func FsmEvent(stub shim.ChaincodeStubInterface, args []string, event string) pb.Response{
  var ruTest Routers
  var str string
  var resError string

  crMap := make(ControllerMapsType, 0)
  vf := reflect.ValueOf(&ruTest)
  vft := vf.Type()
  //读取方法数量
  mNum := vf.NumMethod()

  //遍历路由器的方法，并将其存入控制器映射变量中
  for i := 0; i < mNum; i++ {
    mName := vft.Method(i).Name
    crMap[mName] = vf.Method(i)
  }

  policyID := args[0]
  bstatus, err := stub.GetState(policyID)
  if err != nil{
    return shim.Error("Query policy status fail, policy ID: " + policyID)
  }

  status := string(bstatus)
  fmt.Println("Policy[" + policyID + "] status:" + status)
  f := fMap[policyID]
  err = f.Event(event)
  if err != nil {
    return shim.Error("Current status is " + status + " not support envent:" + event)
  } else if event == "TimeOut" {
    str = "Done"
  } else {
    parms := []reflect.Value{reflect.ValueOf(stub), reflect.ValueOf(args)}
    result := crMap[event].Call(parms)
    resError = reflect.Value.String(result[0])
    str = reflect.Value.String(result[1])
  }

  if str != "Done" {
    return shim.Error(resError)
  }

  stub.PutState(policyID, []byte(status))
  status = f.Current()
  fmt.Println("New status:" + status)
  return shim.Success([]byte(status))
}


func (this *Routers) (Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|A!judge(B))((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1A!judge(B,2)|A!judge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1A!judge(B,2)|A!judge(A,3), Term2A!judge(A)|A!judge(B))((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Asat1212, Term2Asat333)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Asat1212, Term2Avio333)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Avio1212, Term2Asat333)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Avio1212, Term2Avio333)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Asat1212)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Avio1212)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term2Asat333)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term2Avio333)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}

