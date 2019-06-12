//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1, 1]";
    }

    function (Term0: execute 23)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="(Term0: execute 23)"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term0: Violate 23)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="(Term0: execute 23)"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1: execute 34)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="(Term0: execute 23)"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1: Violate 34)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="(Term0: execute 23)"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="(Term0: execute 23)"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: execute 565)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="(Term0: execute 23)"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: Violate 565)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="(Term0: execute 23)"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="(Term0: execute 23)"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="(Term0: execute 23)"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

}