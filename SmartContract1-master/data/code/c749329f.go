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

  if function == "[A]deposit([A],Contract,10)" {
    return FsmEvent(stub, args, "[A]deposit([A],Contract,10)")
  } else if function == "[A]deposit([A],Contract,10)超时" {
    return FsmEvent(stub, args, "[A]deposit([A],Contract,10)超时")
  } else if function == "[B]" {
    return FsmEvent(stub, args, "[B]")
  } else if function == "[B]" {
    return FsmEvent(stub, args, "[B]")
  } else if function == "[B]deliver([B],[A],book)" {
    return FsmEvent(stub, args, "[B]deliver([B],[A],book)")
  } else if function == "[B]deliver([B],[A],book)超时" {
    return FsmEvent(stub, args, "[B]deliver([B],[A],book)超时")
  } else if function == "[A]" {
    return FsmEvent(stub, args, "[A]")
  } else if function == "[A]" {
    return FsmEvent(stub, args, "[A]")
  } else if function == "[A]===>[C]" {
    return FsmEvent(stub, args, "[A]===>[C]")
  } else if function == "[C]===>[C]" {
    return FsmEvent(stub, args, "[C]===>[C]")
  } else if function == "[A]confirm([A],book)" {
    return FsmEvent(stub, args, "[A]confirm([A],book)")
  } else if function == "[A]confirm([A],book)超时" {
    return FsmEvent(stub, args, "[A]confirm([A],book)超时")
  } else if function == "[C]===>[C]refund([A],100)" {
    return FsmEvent(stub, args, "[C]===>[C]refund([A],100)")
  } else if function == "[C]===>[C]" {
    return FsmEvent(stub, args, "[C]===>[C]")
  } else if function == "[B]!judge([B],C2.vio)" {
    return FsmEvent(stub, args, "[B]!judge([B],C2.vio)")
  } else if function == "[B]judge([B],C2.vio)" {
    return FsmEvent(stub, args, "[B]judge([B],C2.vio)")
  } else if function == "[C]transfer([B],100)" {
    return FsmEvent(stub, args, "[C]transfer([B],100)")
  } else if function == "[C]transfer([B],100)===>[C]" {
    return FsmEvent(stub, args, "[C]transfer([B],100)===>[C]")
  } else if function == "[C]" {
    return FsmEvent(stub, args, "[C]")
  } else if function == "[C]refund([A],100)" {
    return FsmEvent(stub, args, "[C]refund([A],100)")
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


func (this *Routers) [A]deposit([A],Contract,10)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [A]deposit([A],Contract,10)超时((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [B]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [B]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [B]deliver([B],[A],book)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [B]deliver([B],[A],book)超时((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [A]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [A]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [A]===>[C]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [C]===>[C]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [A]confirm([A],book)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [A]confirm([A],book)超时((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [C]===>[C]refund([A],100)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [C]===>[C]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [B]!judge([B],C2.vio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [B]judge([B],C2.vio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [C]transfer([B],100)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [C]transfer([B],100)===>[C]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [C]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [C]refund([A],100)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


