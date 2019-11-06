package main

import (
  "fmt"
  "reflect"
   "github.com/hyperledger/fabric/core/chaincode/shim"
  pb "github.com/hyperledger/fabric/protos/peer"
)


type SimpleChaincode struct {
}

func InitFSM(initStatus string) *FSM {
   var action  = [...]string{"Term","Term","Term","Term","Term","Term","Term","Term","Term"}
   var currentStatus  = [...]string{"[1, 1]","[1, 1]","[2, 1]","[2, 1]","[4, 1]","[3, 1]","[5, 1]","[3, 2]","[3, 2]"}
   var newStatus  = [...]string{"[2, 1]","[4, 1]","[3, 1]","[5, 1]","[4, 4]","[3, 2]","[5, 4]","[3, 3]","[3, 5]"}
   var events []EventDesc = make([]EventDesc, 0)
   var termNum=len(action)
   for i := 0; i < termNum; i ++ {
    events = append(events, EventDesc{Name: action[i], Src: []string{currentStatus[i]}, Dst: newStatus[i]})
   }
   f := NewFSM(
   initStatus,
   events,
   Callbacks{},
   )
   return f;
}


// =========================================
//       Init - initializes chaincode
// =========================================
func (t *SimpleChaincode) Init(stub shim.ChaincodeStubInterface) pb.Response {
  formNumber := "EXP1"
  status :="[1, 1]"
  stub.PutState(formNumber, []byte(status))
 return shim.Success([]byte(status))
}


// ======================================================
//       Invoke - Our entry point for Invocations
// ======================================================
func (t *SimpleChaincode) Invoke(stub shim.ChaincodeStubInterface) pb.Response {
   function, args := stub.GetFunctionAndParameters()
   fmt.Println("invoke is running " + function)
   if function == "Current_State" {
      return t.Current_State(stub, args)
   } else {
      return Call_FsmEvent(stub,function,args)
   }
}

func (t *SimpleChaincode)Current_State(stub shim.ChaincodeStubInterface, args []string) pb.Response {
   formNumber := args[0]
   bstatus, err := stub.GetState(formNumber)
   if err != nil {
      return shim.Error("Query form status fail, form number:" + formNumber)
   }
   status := string(bstatus)
   fmt.Println("Form[" + formNumber + "] status:" + status)
   return shim.Success(nil)
}

func Call_FsmEvent(stub shim.ChaincodeStubInterface, event string,params []string) pb.Response{
   name:=event
   formNumber := params[0]
   bstatus, err := stub.GetState(formNumber)
   if err != nil {
      return shim.Error("Query form status fail, form number:" + formNumber)
   }

   status := string(bstatus)
   fmt.Println("Form[" + formNumber + "] status:" + status)
   f := InitFSM(status)
   err = f.Event(event)
   if err != nil {
      return shim.Error("Current status is " + status + " does not support event:" + event)
  }
   f_name:= reflect.ValueOf(command[name])
   if len(params) != f_name.Type().NumIn()+1 {
      return shim.Error("Params Error!")
   }

   //然后将传入参数转为反射类型切片
   in := make([]reflect.Value, len(params)-1)
   for k, param := range params[1:] {
      in[k] = reflect.ValueOf(param)
    }
   //利用函数反射对象的call方法调用函数
   f_name.Call(in)
   status = f.Current()
   fmt.Println("New status:" + status)
   stub.PutState(formNumber, []byte(status))
   return shim.Success([]byte(status))
}

func Term(name string ,term string) {
   fmt.Println(name+" : "+term)
}


var command= map[string]interface{} {
   "Term":Term, }// ============
//     Main
// ============
func main() {
  err := shim.Start(new(SimpleChaincode))
  if err != nil {
    fmt.Printf("Error starting Contract chaincode: %s", err)
  }
}


