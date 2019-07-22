//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1, 1]";
    }

    function (Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))"){
            currentStatus="[2, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|A!judge(B))(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))"){
            currentStatus="[2, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term1A!judge(B,2)|A!judge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))"){
            currentStatus="[2, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term1A!judge(B,2)|A!judge(A,3), Term2A!judge(A)|A!judge(B))(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))"){
            currentStatus="[2, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term1Asat1212, Term2Asat333)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))"){
            currentStatus="[2, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term1Asat1212, Term2Avio333)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))"){
            currentStatus="[2, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term1Avio1212, Term2Asat333)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))"){
            currentStatus="[2, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term1Avio1212, Term2Avio333)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))"){
            currentStatus="[2, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term1Asat1212)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))"){
            currentStatus="[2, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term1Avio1212)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))"){
            currentStatus="[2, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term2Asat333)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))"){
            currentStatus="[2, 2]";
            return true;
        }
        else
            return false;
    }

    function (Term2Avio333)(String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="(Term1A!judge(B,2)|Ajudge(A,3), Term1Ajudge(B,2)|A!judge(A,3), Term1Ajudge(B,2)|Ajudge(A,3), Term2A!judge(A)|Ajudge(B), Term2Ajudge(A)|A!judge(B), Term2Ajudge(A)|Ajudge(B))"){
            currentStatus="[2, 2]";
            return true;
        }
        else
            return false;
    }

}