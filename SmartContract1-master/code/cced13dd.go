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

  if function == "[["[['', 'Sat', 'Term6'], ['A', 'Sat2323', 'Term1'], ['A', 'judge(A,4)', 'Term5Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['', 'Sat', 'Term6'], ['A', 'Sat2323', 'Term1'], ['A', 'judge(A,4)', 'Term5Term5']]"]]")
  } else if function == "[["[['', 'Vio', 'Term6'], ['A', 'Sat2323', 'Term1'], ['A', 'judge(A,4)', 'Term5Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['', 'Vio', 'Term6'], ['A', 'Sat2323', 'Term1'], ['A', 'judge(A,4)', 'Term5Term5']]"]]")
  } else if function == "[["[['', 'Sat', 'Term6'], ['A', 'Sat2323', 'Term1'], ['A', '!judge(A,4)', 'Term5Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['', 'Sat', 'Term6'], ['A', 'Sat2323', 'Term1'], ['A', '!judge(A,4)', 'Term5Term5']]"]]")
  } else if function == "[["[['', 'Vio', 'Term6'], ['A', 'Sat2323', 'Term1'], ['A', '!judge(A,4)', 'Term5Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['', 'Vio', 'Term6'], ['A', 'Sat2323', 'Term1'], ['A', '!judge(A,4)', 'Term5Term5']]"]]")
  } else if function == "[["[['', 'Sat', 'Term6'], ['A', 'Vio2323', 'Term1'], ['A', 'judge(A,4)', 'Term5Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['', 'Sat', 'Term6'], ['A', 'Vio2323', 'Term1'], ['A', 'judge(A,4)', 'Term5Term5']]"]]")
  } else if function == "[["[['', 'Vio', 'Term6'], ['A', 'Vio2323', 'Term1'], ['A', 'judge(A,4)', 'Term5Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['', 'Vio', 'Term6'], ['A', 'Vio2323', 'Term1'], ['A', 'judge(A,4)', 'Term5Term5']]"]]")
  } else if function == "[["[['', 'Sat', 'Term6'], ['A', 'Vio2323', 'Term1'], ['A', '!judge(A,4)', 'Term5Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['', 'Sat', 'Term6'], ['A', 'Vio2323', 'Term1'], ['A', '!judge(A,4)', 'Term5Term5']]"]]")
  } else if function == "[["[['', 'Vio', 'Term6'], ['A', 'Vio2323', 'Term1'], ['A', '!judge(A,4)', 'Term5Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['', 'Vio', 'Term6'], ['A', 'Vio2323', 'Term1'], ['A', '!judge(A,4)', 'Term5Term5']]"]]")
  } else if function == "[["[['B', '', 'Term2'], ['B', 'Satdwwewe', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term2'], ['B', 'Satdwwewe', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term2'], ['B', 'Viodwwewe', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term2'], ['B', 'Viodwwewe', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term2'], ['B', 'Satdwwewe', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term2'], ['B', 'Satdwwewe', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term2'], ['B', 'Viodwwewe', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term2'], ['B', 'Viodwwewe', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term2']]"]]")
  } else if function == "[["[['B', '', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term2']]"]]")
  } else if function == "[["[['B', '', 'Term2'], ['B', '', 'Term3'], ['B', 'Satdwwewe', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term2'], ['B', '', 'Term3'], ['B', 'Satdwwewe', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term2'], ['B', '', 'Term3'], ['B', 'Viodwwewe', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term2'], ['B', '', 'Term3'], ['B', 'Viodwwewe', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term2'], ['B', '', 'Term3'], ['B', 'Satdwwewe', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term2'], ['B', '', 'Term3'], ['B', 'Satdwwewe', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term2'], ['B', '', 'Term3'], ['B', 'Viodwwewe', 'Term5']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term2'], ['B', '', 'Term3'], ['B', 'Viodwwewe', 'Term5']]"]]")
  } else if function == "[["[['B', '', 'Term2'], ['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term2'], ['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term2'], ['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term2'], ['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term2'], ['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term2'], ['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term2'], ['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term2'], ['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term2']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term2']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term2'], ['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term2'], ['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term2'], ['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term2'], ['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term2']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term2']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term2']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term2']]"]]")
  } else if function == "[["[['B', 'Satdfdf', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satdfdf', 'Term2']]"]]")
  } else if function == "[["[['B', 'Viodfdf', 'Term2']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Viodfdf', 'Term2']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3']]"]]")
  } else if function == "[["[['B', '', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', '', 'Term3']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['B', 'Satyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Satyty', 'Term3']]"]]")
  } else if function == "[["[['B', 'Vioyty', 'Term3']]"]]" {
    return FsmEvent(stub, args, "[["[['B', 'Vioyty', 'Term3']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', '', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', '', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Saterer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Saterer', 'Term4']]"]]")
  } else if function == "[["[['A', 'Vioerer', 'Term4']]"]]" {
    return FsmEvent(stub, args, "[["[['A', 'Vioerer', 'Term4']]"]]")
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


func (this *Routers) [["[['', 'Sat', 'Term6'], ['A', 'Sat2323', 'Term1'], ['A', 'judge(A,4)', 'Term5Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['', 'Vio', 'Term6'], ['A', 'Sat2323', 'Term1'], ['A', 'judge(A,4)', 'Term5Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['', 'Sat', 'Term6'], ['A', 'Sat2323', 'Term1'], ['A', '!judge(A,4)', 'Term5Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['', 'Vio', 'Term6'], ['A', 'Sat2323', 'Term1'], ['A', '!judge(A,4)', 'Term5Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['', 'Sat', 'Term6'], ['A', 'Vio2323', 'Term1'], ['A', 'judge(A,4)', 'Term5Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['', 'Vio', 'Term6'], ['A', 'Vio2323', 'Term1'], ['A', 'judge(A,4)', 'Term5Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['', 'Sat', 'Term6'], ['A', 'Vio2323', 'Term1'], ['A', '!judge(A,4)', 'Term5Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['', 'Vio', 'Term6'], ['A', 'Vio2323', 'Term1'], ['A', '!judge(A,4)', 'Term5Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term2'], ['B', 'Satdwwewe', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term2'], ['B', 'Viodwwewe', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term2'], ['B', 'Satdwwewe', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term2'], ['B', 'Viodwwewe', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term2'], ['B', '', 'Term3'], ['B', 'Satdwwewe', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term2'], ['B', '', 'Term3'], ['B', 'Viodwwewe', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term2'], ['B', '', 'Term3'], ['B', 'Satdwwewe', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term2'], ['B', '', 'Term3'], ['B', 'Viodwwewe', 'Term5']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term2'], ['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term2'], ['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term2'], ['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term2'], ['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term2'], ['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term2'], ['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satdfdf', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Viodfdf', 'Term2']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', '', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Satyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['B', 'Vioyty', 'Term3']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', '', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Saterer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


func (this *Routers) [["[['A', 'Vioerer', 'Term4']]"]]((stub shim.ChaincodeStubInterface,
args []string) (pb.Response, string) {
  return shim.Success(nil), "Done"
}


