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

  if function == "[["[['ghjfdk', 'ghjfdks', 'Term2Term2'], ['付', '付款', 'Term1Term1']]"]]" {
    return FsmEvent(stub, args, "[["[['ghjfdk', 'ghjfdks', 'Term2Term2'], ['付', '付款', 'Term1Term1']]"]]")
  } else if function == "[["[['!ghjfdk', '!ghjfdks', 'Term2Term2'], ['付', '付款', 'Term1Term1']]"]]" {
    return FsmEvent(stub, args, "[["[['!ghjfdk', '!ghjfdks', 'Term2Term2'], ['付', '付款', 'Term1Term1']]"]]")
  } else if function == "[["[['!付', '!付款', 'Term1Term1'], ['ghjfdk', 'ghjfdks', 'Term2Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['!付', '!付款', 'Term1Term1'], ['ghjfdk', 'ghjfdks', 'Term2Term2']]"]]")
  } else if function == "[["[['!ghjfdk', '!ghjfdks', 'Term2Term2'], ['!付', '!付款', 'Term1Term1']]"]]" {
    return FsmEvent(stub, args, "[["[['!ghjfdk', '!ghjfdks', 'Term2Term2'], ['!付', '!付款', 'Term1Term1']]"]]")
  } else if function == "[["[['A', 'Satasdfa', 'Term1'], ['B', 'Sat', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satasdfa', 'Term1'], ['B', 'Sat', 'Term2']]"]]")
  } else if function == "[["[['A', 'Satasdfa', 'Term1'], ['B', 'Vio', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satasdfa', 'Term1'], ['B', 'Vio', 'Term2']]"]]")
  } else if function == "[["[['A', 'Vioasdfa', 'Term1'], ['B', 'Sat', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioasdfa', 'Term1'], ['B', 'Sat', 'Term2']]"]]")
  } else if function == "[["[['A', 'Vioasdfa', 'Term1'], ['B', 'Vio', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioasdfa', 'Term1'], ['B', 'Vio', 'Term2']]"]]")
  } else if function == "[["[['A', 'Satasdfa', 'Term1']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satasdfa', 'Term1']]"]]")
  } else if function == "[["[['A', 'Vioasdfa', 'Term1']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioasdfa', 'Term1']]"]]")
  } else if function == "[["[['A', '', 'Term5'], ['B', 'Sat', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term5'], ['B', 'Sat', 'Term2']]"]]")
  } else if function == "[["[['A', '', 'Term5'], ['B', 'Vio', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term5'], ['B', 'Vio', 'Term2']]"]]")
  } else if function == "[["[['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]")
  } else if function == "[["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"], ["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"], ["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"], ["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"], ["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]")
  } else if function == "[["[['A', '', 'Term3'], ['A', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term3'], ['A', '', 'Term5']]"]]")
  } else if function == "[["[['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]")
  } else if function == "[["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"]]")
  } else if function == "[["[['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]")
  } else if function == "[["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['A', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['A', '', 'Term5']]"]]")
  } else if function == "[["[['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]")
  } else if function == "[["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"], ["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"], ["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"], ["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"], ["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]")
  } else if function == "[["[['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]")
  } else if function == "[["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"]]")
  } else if function == "[["[['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]")
  } else if function == "[["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"], ["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"], ["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"], ["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"], ["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]")
  } else if function == "[["[['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]")
  } else if function == "[["[['!aaaaaa', '!aaaaaaa', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['!aaaaaa', '!aaaaaaa', 'Term3Term3']]"]]")
  } else if function == "[["[['aaaaaa', 'aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['aaaaaa', 'aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]")
  } else if function == "[["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['!bbbbbbb', '!bbbbbbbb', 'Term3Term3']]"], ["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"], ["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['!bbbbbbb', '!bbbbbbbb', 'Term3Term3']]"], ["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"], ["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]")
  } else if function == "[["[['A', 'Satargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satargaf', 'Term3']]"]]")
  } else if function == "[["[['A', 'Vioargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioargaf', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['A', 'Satargaf', 'Term3'], ['A', 'Sat', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satargaf', 'Term3'], ['A', 'Sat', 'Term5']]"]]")
  } else if function == "[["[['A', 'Satargaf', 'Term3'], ['A', 'Vio', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satargaf', 'Term3'], ['A', 'Vio', 'Term5']]"]]")
  } else if function == "[["[['A', 'Vioargaf', 'Term3'], ['A', 'Sat', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioargaf', 'Term3'], ['A', 'Sat', 'Term5']]"]]")
  } else if function == "[["[['A', 'Vioargaf', 'Term3'], ['A', 'Vio', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioargaf', 'Term3'], ['A', 'Vio', 'Term5']]"]]")
  } else if function == "[["[['A', 'Satargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satargaf', 'Term3']]"]]")
  } else if function == "[["[['A', 'Vioargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioargaf', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['A', 'Satargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satargaf', 'Term3']]"]]")
  } else if function == "[["[['A', 'Vioargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioargaf', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['A', 'Satargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satargaf', 'Term3']]"]]")
  } else if function == "[["[['A', 'Vioargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioargaf', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['A', 'Satargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satargaf', 'Term3']]"]]")
  } else if function == "[["[['A', 'Vioargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioargaf', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['A', 'Satargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satargaf', 'Term3']]"]]")
  } else if function == "[["[['A', 'Vioargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioargaf', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['A', 'Satargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satargaf', 'Term3']]"]]")
  } else if function == "[["[['A', 'Vioargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioargaf', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['A', 'Satargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satargaf', 'Term3']]"]]")
  } else if function == "[["[['A', 'Vioargaf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioargaf', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satfsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satfsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Viofsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viofsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satfsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satfsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Viofsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viofsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satfsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satfsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Viofsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viofsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satfsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satfsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Viofsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viofsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satfsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satfsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Viofsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viofsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satfsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satfsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Viofsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viofsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satfsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satfsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Viofsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viofsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satfsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satfsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Viofsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viofsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satfsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satfsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Viofsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viofsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satfsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satfsd', 'Term4']]"]]")
  } else if function == "[["[['B', 'Viofsd', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viofsd', 'Term4']]"]]")
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


func (this *Routers) [["[['ghjfdk', 'ghjfdks', 'Term2Term2'], ['付', '付款', 'Term1Term1']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['!ghjfdk', '!ghjfdks', 'Term2Term2'], ['付', '付款', 'Term1Term1']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['!付', '!付款', 'Term1Term1'], ['ghjfdk', 'ghjfdks', 'Term2Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['!ghjfdk', '!ghjfdks', 'Term2Term2'], ['!付', '!付款', 'Term1Term1']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satasdfa', 'Term1'], ['B', 'Sat', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satasdfa', 'Term1'], ['B', 'Vio', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioasdfa', 'Term1'], ['B', 'Sat', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioasdfa', 'Term1'], ['B', 'Vio', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satasdfa', 'Term1']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioasdfa', 'Term1']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term5'], ['B', 'Sat', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term5'], ['B', 'Vio', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"], ["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"], ["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term3'], ['A', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['A', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"], ["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"], ["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5']]"], ["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['A', '', 'Term5'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"], ["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['A', '', 'Term5'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['!aaaaaa', '!aaaaaaa', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['aaaaaa', 'aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['!bbbbbbb', '!bbbbbbbb', 'Term3Term3']]"], ["[['!aaaaaa', '!aaaaaaa', 'Term3Term3'], ['bbbbbbb', 'bbbbbbbb', 'Term3Term3']]"], ["[['!bbbbbbb', '!bbbbbbbb', 'Term3Term3'], ['aaaaaa', 'aaaaaaa', 'Term3Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satargaf', 'Term3'], ['A', 'Sat', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satargaf', 'Term3'], ['A', 'Vio', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioargaf', 'Term3'], ['A', 'Sat', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioargaf', 'Term3'], ['A', 'Vio', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioargaf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satfsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viofsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satfsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viofsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satfsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viofsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satfsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viofsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satfsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viofsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satfsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viofsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satfsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viofsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satfsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viofsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satfsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viofsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satfsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viofsd', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


