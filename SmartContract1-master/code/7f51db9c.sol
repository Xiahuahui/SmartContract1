//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 2, 1]";
    }

    function (Sat0, Sat1)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1]" && action=="(Sat0, Sat1)"){
            currentStatus="[3, 3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Sat0, Vio1)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1]" && action=="(Sat0, Sat1)"){
            currentStatus="[3, 3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Vio0, Sat1)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1]" && action=="(Sat0, Sat1)"){
            currentStatus="[3, 3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Vio0, Vio1)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1]" && action=="(Sat0, Sat1)"){
            currentStatus="[3, 3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Sat2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1]" && action=="(Sat0, Sat1)"){
            currentStatus="[3, 3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Vio2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1]" && action=="(Sat0, Sat1)"){
            currentStatus="[3, 3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Exp2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1]" && action=="(Sat0, Sat1)"){
            currentStatus="[3, 3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Sat2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1]" && action=="(Sat0, Sat1)"){
            currentStatus="[3, 3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Vio2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1]" && action=="(Sat0, Sat1)"){
            currentStatus="[3, 3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Sat2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1]" && action=="(Sat0, Sat1)"){
            currentStatus="[3, 3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Vio2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1]" && action=="(Sat0, Sat1)"){
            currentStatus="[3, 3, 2]";
            return true;
        }
        else
            return false;
    }

}