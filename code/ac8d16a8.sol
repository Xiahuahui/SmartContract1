//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1]";
    }

    function B0(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="B0"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function S0(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="B0"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function V0(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="B0"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

}