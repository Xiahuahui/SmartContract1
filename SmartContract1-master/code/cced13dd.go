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

  if function == "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]")
  } else if function == "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3']]"]]")
  } else if function == "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3']]"]]")
  } else if function == "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term5']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term5']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term5']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', '', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term6']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term6']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term6']]"]]")
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


func (this *Routers) [["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Sat2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', 'judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Sat././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioiiuwuew', 'Term1'], ['A', 'Vio2323', 'Term2'], ['B', '!judge(B,4)', 'Term4Term4'], ['B', 'Vio././', 'Term7']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Satwewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Viowewe', 'Term4'], ['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term3'], ['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term6']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


