//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 2, 2]";
    }

    function (Sat0, Sat1, Sat2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 2]" && action=="(Sat0, Sat1, Sat2)"){
            currentStatus="[3, 3, 3]";
            return true;
        }
        else
            return false;
    }

    function (Sat0, Sat1, Vio2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 2]" && action=="(Sat0, Sat1, Sat2)"){
            currentStatus="[3, 3, 3]";
            return true;
        }
        else
            return false;
    }

    function (Sat0, Vio1, Sat2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 2]" && action=="(Sat0, Sat1, Sat2)"){
            currentStatus="[3, 3, 3]";
            return true;
        }
        else
            return false;
    }

    function (Sat0, Vio1, Vio2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 2]" && action=="(Sat0, Sat1, Sat2)"){
            currentStatus="[3, 3, 3]";
            return true;
        }
        else
            return false;
    }

    function (Vio0, Sat1, Sat2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 2]" && action=="(Sat0, Sat1, Sat2)"){
            currentStatus="[3, 3, 3]";
            return true;
        }
        else
            return false;
    }

    function (Vio0, Sat1, Vio2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 2]" && action=="(Sat0, Sat1, Sat2)"){
            currentStatus="[3, 3, 3]";
            return true;
        }
        else
            return false;
    }

    function (Vio0, Vio1, Sat2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 2]" && action=="(Sat0, Sat1, Sat2)"){
            currentStatus="[3, 3, 3]";
            return true;
        }
        else
            return false;
    }

    function (Vio0, Vio1, Vio2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 2]" && action=="(Sat0, Sat1, Sat2)"){
            currentStatus="[3, 3, 3]";
            return true;
        }
        else
            return false;
    }

}