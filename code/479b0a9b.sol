//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1]";
    }

    function Ture-rew(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-rew"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Timeout-rew(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-rew"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Ture-玩儿(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-rew"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function Timeout-玩儿(String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="Ture-rew"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

}