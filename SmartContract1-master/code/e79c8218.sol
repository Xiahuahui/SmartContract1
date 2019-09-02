//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1]";
    }

    function (String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action==""){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function (String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action==""){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function (String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action==""){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function (String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action==""){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

}