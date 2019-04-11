//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1, 1]";
    }

    function S0(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="S0"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function V0(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="S0"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function S1(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="S0"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function V1(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="S0"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function E1(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="S0"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function S2(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="S0"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function V2(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="S0"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function E2(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="S0"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function E2(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="S0"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

}