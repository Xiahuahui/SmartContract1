//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1]";
    }

    function Ture-das(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-das"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Timeout-das(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-das"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Ture-撒大声地(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-das"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Timeout-撒大声地(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-das"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

}