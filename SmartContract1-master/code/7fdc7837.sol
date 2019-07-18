//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1, 1, 1]";
    }

    function (  Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3))(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1]" && action=="(  Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3))"){
            currentStatus="[2, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term1A!judge(A,2)|A!judge(B,3))(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1]" && action=="(  Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3))"){
            currentStatus="[2, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1A)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1]" && action=="(  Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3))"){
            currentStatus="[2, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1Atimeout)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1]" && action=="(  Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3))"){
            currentStatus="[2, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term2B , Term3A )(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1]" && action=="(  Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3))"){
            currentStatus="[2, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term2B , Term3A )(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1]" && action=="(  Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3))"){
            currentStatus="[2, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term2B , Term3A )(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1]" && action=="(  Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3))"){
            currentStatus="[2, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2B, Term3A)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1]" && action=="(  Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3))"){
            currentStatus="[2, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2B, Term3Atimeout)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1]" && action=="(  Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3))"){
            currentStatus="[2, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2Btimeout, Term3A)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1]" && action=="(  Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3))"){
            currentStatus="[2, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2Btimeout, Term3Atimeout)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1]" && action=="(  Term1A!judge(A,2)|Ajudge(B,3), Term1Ajudge(A,2)|A!judge(B,3), Term1Ajudge(A,2)|Ajudge(B,3))"){
            currentStatus="[2, 1, 1]";
            return true;
        }
        else
            return false;
    }

}