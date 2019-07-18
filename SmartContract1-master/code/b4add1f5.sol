//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1, 1, 1, 1]";
    }

    function (Term1Adeposit)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1Atimeoutdeposit)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term2B )(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term2B )(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2Bdeliver)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2Btimeoutdeliver)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term3A )(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term3A )(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term3A , Term5C )(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term4C , Term5C )(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term3Aconfirm)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term3Atimeoutconfirm)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5Crefund)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term4C , Term5C )(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term4Cjudge(term2.Vio), Term5Cjudge(term2.Vio))(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term4Cjudge(term2.Vio), Term5C!judge(term2.Vio))(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term4C!judge(term2.Vio), Term5Cjudge(term2.Vio))(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term4C!judge(term2.Vio), Term5C!judge(term2.Vio))(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (  Term4C )(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term4Ctransfer)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term4Ctransfer, Term5Crefund)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term4Ctransfer)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5Crefund)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1]" && action=="(Term1Adeposit)"){
            currentStatus="[3, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

}