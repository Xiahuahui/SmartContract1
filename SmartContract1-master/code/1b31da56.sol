//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 2]";
    }

    function (Term0: execute 1212, Term1: execute 1212)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2]" && action=="(Term0: execute 1212, Term1: execute 1212)"){
            currentStatus="[3, 3]";
            return true;
        }
        else
            return false;
    }

    function (Term0: Violate1212, Term1: execute 1212)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2]" && action=="(Term0: execute 1212, Term1: execute 1212)"){
            currentStatus="[3, 3]";
            return true;
        }
        else
            return false;
    }

}