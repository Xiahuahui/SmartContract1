//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 2]";
    }

    function (Term0: execute 232, Term1: execute 32323)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2]" && action=="(Term0: execute 232, Term1: execute 32323)"){
            currentStatus="[3, 3]";
            return true;
        }
        else
            return false;
    }

    function (Term0: execute 232, Term1: Violate32323)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2]" && action=="(Term0: execute 232, Term1: execute 32323)"){
            currentStatus="[3, 3]";
            return true;
        }
        else
            return false;
    }

    function (Term0: Violate232, Term1: execute 32323)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2]" && action=="(Term0: execute 232, Term1: execute 32323)"){
            currentStatus="[3, 3]";
            return true;
        }
        else
            return false;
    }

    function (Term0: Violate232, Term1: Violate32323)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 2]" && action=="(Term0: execute 232, Term1: execute 32323)"){
            currentStatus="[3, 3]";
            return true;
        }
        else
            return false;
    }

}