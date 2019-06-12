//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1]";
    }

    function (Term0: execute 2323)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="(Term0: execute 2323)"){
            currentStatus="[3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term0: Violate 2323)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="(Term0: execute 2323)"){
            currentStatus="[3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term1: execute 3434)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="(Term0: execute 2323)"){
            currentStatus="[3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term1: Violate 3434)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="(Term0: execute 2323)"){
            currentStatus="[3, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term1: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="(Term0: execute 2323)"){
            currentStatus="[3, 2]";
            return true;
        }
        else
            return false;
    }

}