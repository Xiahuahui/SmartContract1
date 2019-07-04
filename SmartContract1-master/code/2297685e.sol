//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1, 2]";
    }

    function (Term1: execute  )(String actionStr) public returns(bool){
        if(currentStatus=="[1, 2]" && action=="(Term1: execute  )"){
            currentStatus="[2, 3]";
            return true;
        }
        else
            return false;
    }

    function (Term1: Violate  )(String actionStr) public returns(bool){
        if(currentStatus=="[1, 2]" && action=="(Term1: execute  )"){
            currentStatus="[2, 3]";
            return true;
        }
        else
            return false;
    }

    function (Term0: execute  )(String actionStr) public returns(bool){
        if(currentStatus=="[1, 2]" && action=="(Term1: execute  )"){
            currentStatus="[2, 3]";
            return true;
        }
        else
            return false;
    }

    function (Term0: Violate  )(String actionStr) public returns(bool){
        if(currentStatus=="[1, 2]" && action=="(Term1: execute  )"){
            currentStatus="[2, 3]";
            return true;
        }
        else
            return false;
    }

    function (Term0: timeout )(String actionStr) public returns(bool){
        if(currentStatus=="[1, 2]" && action=="(Term1: execute  )"){
            currentStatus="[2, 3]";
            return true;
        }
        else
            return false;
    }

}