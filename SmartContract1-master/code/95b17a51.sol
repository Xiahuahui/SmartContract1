//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1, 1, 2, 1, 1]";
    }

    function (Sat0, Sat3)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Sat0, Vio3)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Vio0, Sat3)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Vio0, Vio3)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Sat1)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Vio1)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Sat1)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Vio1)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp1)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp1)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Sat2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Vio2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp2, Sat5)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp2, Vio5)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Sat2, Exp5)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Vio2, Exp5)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp2, Sat5)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp2, Vio5)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp2)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp2, Exp5)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Sat4, Exp5)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Vio4, Exp5)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp4, Sat5)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp4, Vio5)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp4)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp4)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Sat4)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Vio4)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Sat4)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Vio4)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp4)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp4)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp4, Exp5)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Exp4)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 2, 1, 1]" && action=="(Sat0, Sat3)"){
            currentStatus="[3, 2, 1, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

}