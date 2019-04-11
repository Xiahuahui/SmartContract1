//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1]";
    }

    function Sat0(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="Sat0"){
            currentStatus="[3, 2]";
            return true;
        }
        else
            return false;
    }

    function Vio0(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="Sat0"){
            currentStatus="[3, 2]";
            return true;
        }
        else
            return false;
    }

    function Sat1(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="Sat0"){
            currentStatus="[3, 2]";
            return true;
        }
        else
            return false;
    }

    function Vio1(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="Sat0"){
            currentStatus="[3, 2]";
            return true;
        }
        else
            return false;
    }

    function Exp1(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="Sat0"){
            currentStatus="[3, 2]";
            return true;
        }
        else
            return false;
    }

}