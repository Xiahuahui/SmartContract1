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

  if function == "(Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3), Term2Ajudge(A,2), Term3Ajudge(A,2))" {
    return FsmEvent(stub, args, "(Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3), Term2Ajudge(A,2), Term3Ajudge(A,2))")
  } else if function == "(Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3), Term2Ajudge(A,2), Term3A!judge(A,2))" {
    return FsmEvent(stub, args, "(Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3), Term2Ajudge(A,2), Term3A!judge(A,2))")
  } else if function == "(Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3), Term2A!judge(A,2), Term3Ajudge(A,2))" {
    return FsmEvent(stub, args, "(Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3), Term2A!judge(A,2), Term3Ajudge(A,2))")
  } else if function == "(Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3), Term2A!judge(A,2), Term3A!judge(A,2))" {
    return FsmEvent(stub, args, "(Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3), Term2A!judge(A,2), Term3A!judge(A,2))")
  } else if function == "(Term1A!judge(A,2)|A!judge(B,3), Term2Ajudge(A,2), Term3Ajudge(A,2))" {
    return FsmEvent(stub, args, "(Term1A!judge(A,2)|A!judge(B,3), Term2Ajudge(A,2), Term3Ajudge(A,2))")
  } else if function == "(Term1A!judge(A,2)|A!judge(B,3), Term2Ajudge(A,2), Term3A!judge(A,2))" {
    return FsmEvent(stub, args, "(Term1A!judge(A,2)|A!judge(B,3), Term2Ajudge(A,2), Term3A!judge(A,2))")
  } else if function == "(Term1A!judge(A,2)|A!judge(B,3), Term2A!judge(A,2), Term3Ajudge(A,2))" {
    return FsmEvent(stub, args, "(Term1A!judge(A,2)|A!judge(B,3), Term2A!judge(A,2), Term3Ajudge(A,2))")
  } else if function == "(Term1A!judge(A,2)|A!judge(B,3), Term2A!judge(A,2), Term3A!judge(A,2))" {
    return FsmEvent(stub, args, "(Term1A!judge(A,2)|A!judge(B,3), Term2A!judge(A,2), Term3A!judge(A,2))")
  } else if function == "(Term1Asaterer, Term2Asat, Term3Asat)" {
    return FsmEvent(stub, args, "(Term1Asaterer, Term2Asat, Term3Asat)")
  } else if function == "(Term1Asaterer, Term2Asat, Term3Avio)" {
    return FsmEvent(stub, args, "(Term1Asaterer, Term2Asat, Term3Avio)")
  } else if function == "(Term1Asaterer, Term2Avio, Term3Asat)" {
    return FsmEvent(stub, args, "(Term1Asaterer, Term2Avio, Term3Asat)")
  } else if function == "(Term1Asaterer, Term2Avio, Term3Avio)" {
    return FsmEvent(stub, args, "(Term1Asaterer, Term2Avio, Term3Avio)")
  } else if function == "(Term1Avioerer, Term2Asat, Term3Asat)" {
    return FsmEvent(stub, args, "(Term1Avioerer, Term2Asat, Term3Asat)")
  } else if function == "(Term1Avioerer, Term2Asat, Term3Avio)" {
    return FsmEvent(stub, args, "(Term1Avioerer, Term2Asat, Term3Avio)")
  } else if function == "(Term1Avioerer, Term2Avio, Term3Asat)" {
    return FsmEvent(stub, args, "(Term1Avioerer, Term2Avio, Term3Asat)")
  } else if function == "(Term1Avioerer, Term2Avio, Term3Avio)" {
    return FsmEvent(stub, args, "(Term1Avioerer, Term2Avio, Term3Avio)")
  } else if function == "(Term1Asaterer, Term2Asat)" {
    return FsmEvent(stub, args, "(Term1Asaterer, Term2Asat)")
  } else if function == "(Term1Asaterer, Term2Avio)" {
    return FsmEvent(stub, args, "(Term1Asaterer, Term2Avio)")
  } else if function == "(Term1Avioerer, Term2Asat)" {
    return FsmEvent(stub, args, "(Term1Avioerer, Term2Asat)")
  } else if function == "(Term1Avioerer, Term2Avio)" {
    return FsmEvent(stub, args, "(Term1Avioerer, Term2Avio)")
  } else if function == "(Term1Asaterer, Term3Asat)" {
    return FsmEvent(stub, args, "(Term1Asaterer, Term3Asat)")
  } else if function == "(Term1Asaterer, Term3Avio)" {
    return FsmEvent(stub, args, "(Term1Asaterer, Term3Avio)")
  } else if function == "(Term1Avioerer, Term3Asat)" {
    return FsmEvent(stub, args, "(Term1Avioerer, Term3Asat)")
  } else if function == "(Term1Avioerer, Term3Avio)" {
    return FsmEvent(stub, args, "(Term1Avioerer, Term3Avio)")
  } else if function == "(Term1Asaterer)" {
    return FsmEvent(stub, args, "(Term1Asaterer)")
  } else if function == "(Term1Avioerer)" {
    return FsmEvent(stub, args, "(Term1Avioerer)")
  } else if function == "(Term2Asat, Term3Asat)" {
    return FsmEvent(stub, args, "(Term2Asat, Term3Asat)")
  } else if function == "(Term2Asat, Term3Avio)" {
    return FsmEvent(stub, args, "(Term2Asat, Term3Avio)")
  } else if function == "(Term2Avio, Term3Asat)" {
    return FsmEvent(stub, args, "(Term2Avio, Term3Asat)")
  } else if function == "(Term2Avio, Term3Avio)" {
    return FsmEvent(stub, args, "(Term2Avio, Term3Avio)")
  } else if function == "(Term2Asat)" {
    return FsmEvent(stub, args, "(Term2Asat)")
  } else if function == "(Term2Avio)" {
    return FsmEvent(stub, args, "(Term2Avio)")
  } else if function == "(Term3Asat)" {
    return FsmEvent(stub, args, "(Term3Asat)")
  } else if function == "(Term3Avio)" {
    return FsmEvent(stub, args, "(Term3Avio)")
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


func (this *Routers) (Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3), Term2Ajudge(A,2), Term3Ajudge(A,2))((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3), Term2Ajudge(A,2), Term3A!judge(A,2))((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3), Term2A!judge(A,2), Term3Ajudge(A,2))((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3), Term2A!judge(A,2), Term3A!judge(A,2))((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1A!judge(A,2)|A!judge(B,3), Term2Ajudge(A,2), Term3Ajudge(A,2))((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1A!judge(A,2)|A!judge(B,3), Term2Ajudge(A,2), Term3A!judge(A,2))((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1A!judge(A,2)|A!judge(B,3), Term2A!judge(A,2), Term3Ajudge(A,2))((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1A!judge(A,2)|A!judge(B,3), Term2A!judge(A,2), Term3A!judge(A,2))((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Asaterer, Term2Asat, Term3Asat)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Asaterer, Term2Asat, Term3Avio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Asaterer, Term2Avio, Term3Asat)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Asaterer, Term2Avio, Term3Avio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Avioerer, Term2Asat, Term3Asat)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Avioerer, Term2Asat, Term3Avio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Avioerer, Term2Avio, Term3Asat)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Avioerer, Term2Avio, Term3Avio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Asaterer, Term2Asat)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Asaterer, Term2Avio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Avioerer, Term2Asat)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Avioerer, Term2Avio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Asaterer, Term3Asat)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Asaterer, Term3Avio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Avioerer, Term3Asat)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Avioerer, Term3Avio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Asaterer)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term1Avioerer)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term2Asat, Term3Asat)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term2Asat, Term3Avio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term2Avio, Term3Asat)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term2Avio, Term3Avio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term2Asat)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term2Avio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term3Asat)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) (Term3Avio)((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


