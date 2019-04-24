//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1]";
    }

    function Ture-sAS(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-sAS"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Timeout-sAS(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-sAS"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Ture-ASAS(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-sAS"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Timeout-ASAS(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-sAS"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

}