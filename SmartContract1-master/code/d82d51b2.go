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

  if function == "(Term0: execute 343 )" {
    return FsmEvent(stub, args, "(Term0: execute 343 )")
  } else if function == "(Term0: Violate 343 )" {
    return FsmEvent(stub, args, "(Term0: Violate 343 )")
  } else if function == "(Term1: execute  )" {
    return FsmEvent(stub, args, "(Term1: execute  )")
  } else if function == "(Term1: Violate  )" {
    return FsmEvent(stub, args, "(Term1: Violate  )")
  } else if function == "(Term1: timeout )" {
    return FsmEvent(stub, args, "(Term1: timeout )")
  } else if function == "(Term2: execute  )" {
    return FsmEvent(stub, args, "(Term2: execute  )")
  } else if function == "(Term2: Violate  )" {
    return FsmEvent(stub, args, "(Term2: Violate  )")
  } else if function == "(Term2: timeout )" {
    return FsmEvent(stub, args, "(Term2: timeout )")
  } else if function == "(Term2: timeout )" {
    return FsmEvent(stub, args, "(Term2: timeout )")
  } else if function == "(Term3: execute  )" {
    return FsmEvent(stub, args, "(Term3: execute  )")
  } else if function == "(Term3: Violate  )" {
    return FsmEvent(stub, args, "(Term3: Violate  )")
  } else if function == "(Term3: timeout )" {
    return FsmEvent(stub, args, "(Term3: timeout )")
  } else if function == "(Term3: timeout )" {
    return FsmEvent(stub, args, "(Term3: timeout )")
  } else if function == "(Term3: timeout )" {
    return FsmEvent(stub, args, "(Term3: timeout )")
  } else if function == "(Term4: execute  )" {
    return FsmEvent(stub, args, "(Term4: execute  )")
  } else if function == "(Term4: Violate  )" {
    return FsmEvent(stub, args, "(Term4: Violate  )")
  } else if function == "(Term4: timeout )" {
    return FsmEvent(stub, args, "(Term4: timeout )")
  } else if function == "(Term4: timeout )" {
    return FsmEvent(stub, args, "(Term4: timeout )")
  } else if function == "(Term4: timeout )" {
    return FsmEvent(stub, args, "(Term4: timeout )")
  } else if function == "(Term4: timeout )" {
    return FsmEvent(stub, args, "(Term4: timeout )")
  } else if function == "(Term5: execute  )" {
    return FsmEvent(stub, args, "(Term5: execute  )")
  } else if function == "(Term5: Violate  )" {
    return FsmEvent(stub, args, "(Term5: Violate  )")
  } else if function == "(Term5: timeout )" {
    return FsmEvent(stub, args, "(Term5: timeout )")
  } else if function == "(Term5: timeout )" {
    return FsmEvent(stub, args, "(Term5: timeout )")
  } else if function == "(Term5: timeout )" {
    return FsmEvent(stub, args, "(Term5: timeout )")
  } else if function == "(Term5: timeout )" {
    return FsmEvent(stub, args, "(Term5: timeout )")
  } else if function == "(Term5: timeout )" {
    return FsmEvent(stub, args, "(Term5: timeout )")
  } else if function == "(Term6: execute  )" {
    return FsmEvent(stub, args, "(Term6: execute  )")
  } else if function == "(Term6: Violate  )" {
    return FsmEvent(stub, args, "(Term6: Violate  )")
  } else if function == "(Term6: timeout )" {
    return FsmEvent(stub, args, "(Term6: timeout )")
  } else if function == "(Term6: timeout )" {
    return FsmEvent(stub, args, "(Term6: timeout )")
  } else if function == "(Term6: timeout )" {
    return FsmEvent(stub, args, "(Term6: timeout )")
  } else if function == "(Term6: timeout )" {
    return FsmEvent(stub, args, "(Term6: timeout )")
  } else if function == "(Term6: timeout )" {
    return FsmEvent(stub, args, "(Term6: timeout )")
  } else if function == "(Term6: timeout )" {
    return FsmEvent(stub, args, "(Term6: timeout )")
  } else if function == "(Term7: execute  )" {
    return FsmEvent(stub, args, "(Term7: execute  )")
  } else if function == "(Term7: Violate  )" {
    return FsmEvent(stub, args, "(Term7: Violate  )")
  } else if function == "(Term7: timeout )" {
    return FsmEvent(stub, args, "(Term7: timeout )")
  } else if function == "(Term7: timeout )" {
    return FsmEvent(stub, args, "(Term7: timeout )")
  } else if function == "(Term7: timeout )" {
    return FsmEvent(stub, args, "(Term7: timeout )")
  } else if function == "(Term7: timeout )" {
    return FsmEvent(stub, args, "(Term7: timeout )")
  } else if function == "(Term7: timeout )" {
    return FsmEvent(stub, args, "(Term7: timeout )")
  } else if function == "(Term7: timeout )" {
    return FsmEvent(stub, args, "(Term7: timeout )")
  } else if function == "(Term7: timeout )" {
    return FsmEvent(stub, args, "(Term7: timeout )")
  } else if function == "(Term8: execute  )" {
    return FsmEvent(stub, args, "(Term8: execute  )")
  } else if function == "(Term8: Violate  )" {
    return FsmEvent(stub, args, "(Term8: Violate  )")
  } else if function == "(Term8: timeout )" {
    return FsmEvent(stub, args, "(Term8: timeout )")
  } else if function == "(Term8: timeout )" {
    return FsmEvent(stub, args, "(Term8: timeout )")
  } else if function == "(Term8: timeout )" {
    return FsmEvent(stub, args, "(Term8: timeout )")
  } else if function == "(Term8: timeout )" {
    return FsmEvent(stub, args, "(Term8: timeout )")
  } else if function == "(Term8: timeout )" {
    return FsmEvent(stub, args, "(Term8: timeout )")
  } else if function == "(Term8: timeout )" {
    return FsmEvent(stub, args, "(Term8: timeout )")
  } else if function == "(Term8: timeout )" {
    return FsmEvent(stub, args, "(Term8: timeout )")
  } else if function == "(Term8: timeout )" {
    return FsmEvent(stub, args, "(Term8: timeout )")
  } else if function == "(Term9: execute  )" {
    return FsmEvent(stub, args, "(Term9: execute  )")
  } else if function == "(Term9: Violate  )" {
    return FsmEvent(stub, args, "(Term9: Violate  )")
  } else if function == "(Term9: timeout )" {
    return FsmEvent(stub, args, "(Term9: timeout )")
  } else if function == "(Term9: timeout )" {
    return FsmEvent(stub, args, "(Term9: timeout )")
  } else if function == "(Term9: timeout )" {
    return FsmEvent(stub, args, "(Term9: timeout )")
  } else if function == "(Term9: timeout )" {
    return FsmEvent(stub, args, "(Term9: timeout )")
  } else if function == "(Term9: timeout )" {
    return FsmEvent(stub, args, "(Term9: timeout )")
  } else if function == "(Term9: timeout )" {
    return FsmEvent(stub, args, "(Term9: timeout )")
  } else if function == "(Term9: timeout )" {
    return FsmEvent(stub, args, "(Term9: timeout )")
  } else if function == "(Term9: timeout )" {
    return FsmEvent(stub, args, "(Term9: timeout )")
  } else if function == "(Term9: timeout )" {
    return FsmEvent(stub, args, "(Term9: timeout )")
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


func (this *Routers) (Term0: execute 343 )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term0: Violate 343 )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1: execute  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1: Violate  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term2: execute  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term2: Violate  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term2: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term2: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term3: execute  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term3: Violate  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term3: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term3: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term3: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term4: execute  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term4: Violate  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term4: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term4: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term4: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term4: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term5: execute  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term5: Violate  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term5: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term5: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term5: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term5: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term5: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term6: execute  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term6: Violate  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term6: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term6: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term6: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term6: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term6: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term6: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term7: execute  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term7: Violate  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term7: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term7: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term7: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term7: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term7: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term7: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term7: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term8: execute  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term8: Violate  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term8: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term8: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term8: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term8: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term8: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term8: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term8: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term8: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term9: execute  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term9: Violate  )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term9: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term9: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term9: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term9: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term9: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term9: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term9: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term9: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term9: timeout )((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


