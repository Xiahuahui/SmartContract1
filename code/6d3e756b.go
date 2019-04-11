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

  if function == "Ture-`1321`" {
    return FsmEvent(stub, args, "Ture-`1321`")
  } else if function == "Timeout-`1321`" {
    return FsmEvent(stub, args, "Timeout-`1321`")
  } else if function == "Timeout-04" {
    return FsmEvent(stub, args, "Timeout-04")
  } else if function == "Timeout-03" {
    return FsmEvent(stub, args, "Timeout-03")
  } else if function == "Ture-`12" {
    return FsmEvent(stub, args, "Ture-`12")
  } else if function == "Timeout-`12" {
    return FsmEvent(stub, args, "Timeout-`12")
  } else if function == "Timeout-04" {
    return FsmEvent(stub, args, "Timeout-04")
  } else if function == "Timeout-03" {
    return FsmEvent(stub, args, "Timeout-03")
  } else if function == "Ture-04" {
    return FsmEvent(stub, args, "Ture-04")
  } else if function == "Timeout-03" {
    return FsmEvent(stub, args, "Timeout-03")
  } else if function == "Ture-`1321`" {
    return FsmEvent(stub, args, "Ture-`1321`")
  } else if function == "Timeout-`1321`" {
    return FsmEvent(stub, args, "Timeout-`1321`")
  } else if function == "Timeout-03" {
    return FsmEvent(stub, args, "Timeout-03")
  } else if function == "Ture-`1321`" {
    return FsmEvent(stub, args, "Ture-`1321`")
  } else if function == "Timeout-`1321`" {
    return FsmEvent(stub, args, "Timeout-`1321`")
  } else if function == "Timeout-04" {
    return FsmEvent(stub, args, "Timeout-04")
  } else if function == "Timeout-04" {
    return FsmEvent(stub, args, "Timeout-04")
  } else if function == "Ture-03" {
    return FsmEvent(stub, args, "Ture-03")
  } else if function == "Timeout-04" {
    return FsmEvent(stub, args, "Timeout-04")
  } else if function == "Timeout-03" {
    return FsmEvent(stub, args, "Timeout-03")
  } else if function == "Ture-`12" {
    return FsmEvent(stub, args, "Ture-`12")
  } else if function == "Timeout-`12" {
    return FsmEvent(stub, args, "Timeout-`12")
  } else if function == "Timeout-03" {
    return FsmEvent(stub, args, "Timeout-03")
  } else if function == "Ture-`12" {
    return FsmEvent(stub, args, "Ture-`12")
  } else if function == "Timeout-`12" {
    return FsmEvent(stub, args, "Timeout-`12")
  } else if function == "Timeout-04" {
    return FsmEvent(stub, args, "Timeout-04")
  } else if function == "Ture-123`13" {
    return FsmEvent(stub, args, "Ture-123`13")
  } else if function == "Timeout-123`13" {
    return FsmEvent(stub, args, "Timeout-123`13")
  } else if function == "Timeout-03" {
    return FsmEvent(stub, args, "Timeout-03")
  } else if function == "Ture-04" {
    return FsmEvent(stub, args, "Ture-04")
  } else if function == "Timeout-03" {
    return FsmEvent(stub, args, "Timeout-03")
  } else if function == "Ture-`1321`" {
    return FsmEvent(stub, args, "Ture-`1321`")
  } else if function == "Timeout-`1321`" {
    return FsmEvent(stub, args, "Timeout-`1321`")
  } else if function == "Ture-03" {
    return FsmEvent(stub, args, "Ture-03")
  } else if function == "Timeout-04" {
    return FsmEvent(stub, args, "Timeout-04")
  } else if function == "Ture-`131" {
    return FsmEvent(stub, args, "Ture-`131")
  } else if function == "Timeout-`131" {
    return FsmEvent(stub, args, "Timeout-`131")
  } else if function == "Timeout-03" {
    return FsmEvent(stub, args, "Timeout-03")
  } else if function == "Timeout-04" {
    return FsmEvent(stub, args, "Timeout-04")
  } else if function == "Ture-`12" {
    return FsmEvent(stub, args, "Ture-`12")
  } else if function == "Timeout-`12" {
    return FsmEvent(stub, args, "Timeout-`12")
  } else if function == "Timeout-04" {
    return FsmEvent(stub, args, "Timeout-04")
  } else if function == "Timeout-03" {
    return FsmEvent(stub, args, "Timeout-03")
  } else if function == "Timeout-03" {
    return FsmEvent(stub, args, "Timeout-03")
  } else if function == "Ture-123`13" {
    return FsmEvent(stub, args, "Ture-123`13")
  } else if function == "Timeout-123`13" {
    return FsmEvent(stub, args, "Timeout-123`13")
  } else if function == "Ture-`131" {
    return FsmEvent(stub, args, "Ture-`131")
  } else if function == "Timeout-`131" {
    return FsmEvent(stub, args, "Timeout-`131")
  } else if function == "Timeout-04" {
    return FsmEvent(stub, args, "Timeout-04")
  } else if function == "Timeout-04" {
    return FsmEvent(stub, args, "Timeout-04")
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


func (this *Routers) Ture-`1321`((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-`1321`((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-`12((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-`12((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-`1321`((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-`1321`((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-`1321`((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-`1321`((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-`12((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-`12((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-`12((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-`12((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-123`13((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-123`13((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-`1321`((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-`1321`((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-`131((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-`131((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-`12((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-`12((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-03((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-123`13((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-123`13((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Ture-`131((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-`131((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) Timeout-04((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


