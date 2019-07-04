//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1, 2]";
    }

    function (Term1: execute 2323)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 2]" && action=="(Term1: execute 2323)"){
            currentStatus="[2, 3]";
            return true;
        }
        else
            return false;
    }

    function (Term1: Violate 2323)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 2]" && action=="(Term1: execute 2323)"){
            currentStatus="[2, 3]";
            return true;
        }
        else
            return false;
    }

    function (Term0: execute 4)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 2]" && action=="(Term1: execute 2323)"){
            currentStatus="[2, 3]";
            return true;
        }
        else
            return false;
    }

    function (Term0: Violate 4)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 2]" && action=="(Term1: execute 2323)"){
            currentStatus="[2, 3]";
            return true;
        }
        else
            return false;
    }

    function (Term0: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 2]" && action=="(Term1: execute 2323)"){
            currentStatus="[2, 3]";
            return true;
        }
        else
            return false;
    }

}