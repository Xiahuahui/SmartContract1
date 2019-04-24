//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1]";
    }

    function Ture-fsd(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-fsd"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Timeout-fsd(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-fsd"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Ture-发顺丰(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-fsd"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Timeout-发顺丰(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-fsd"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

}