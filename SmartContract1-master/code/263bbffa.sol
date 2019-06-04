//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1, 1, 1, 1]";
    }

    function (Term0: execute 预付款)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term0: Violate预付款)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1: execute 发货)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1: Violate发货)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: execute 确认, Term4: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: Violate确认, Term4: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: timeout, Term4: execute 回退)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: timeout, Term4: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term3: execute 转账)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term3: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term3: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term3: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term0: execute 预付款)"){
            currentStatus="[3, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

}