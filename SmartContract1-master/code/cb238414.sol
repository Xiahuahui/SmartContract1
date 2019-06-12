//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1, 1, 1, 1, 1, 1, 1]";
    }

    function (Term0: execute 预付金)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term0: Violate 预付金)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1: execute 生产货物)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1: Violate 生产货物)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1: execute 生产货物 ,Term2: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term1: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: execute 惩罚操作 ,Term3: execute 运送货物)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: execute 惩罚操作 ,Term3: Violate 运送货物)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: execute 惩罚操作 ,Term3: execute 运送货物 ,Term4: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: timeout ,Term3: timeout ,Term7: execute intel退还押金并惩罚)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term3: execute 运送货物)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term3: Violate 运送货物)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term3: execute 运送货物 ,Term4: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term2: timeout ,Term3: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term4: execute 换货 ,Term7: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term4: Violate 换货 ,Term7: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term4: timeout ,Term7: execute intel退还押金并惩罚)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: timeout ,Term6: execute Lenovo付款 ,Term7: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: timeout ,Term6: Violate Lenovo付款 ,Term7: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term4: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term4: execute 换货 ,Term7: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term4: Violate 换货 ,Term7: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term4: timeout ,Term7: execute intel退还押金并惩罚)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: timeout ,Term6: execute Lenovo付款 ,Term7: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: timeout ,Term6: Violate Lenovo付款 ,Term7: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term4: timeout ,Term7: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: timeout ,Term6: execute Lenovo付款)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: timeout ,Term6: Violate Lenovo付款)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: execute 违约操作 ,Term6: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: timeout ,Term6: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: timeout ,Term6: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: timeout ,Term6: execute Lenovo付款)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: timeout ,Term6: Violate Lenovo付款)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: execute 违约操作 ,Term6: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: timeout ,Term6: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function (Term5: timeout ,Term6: timeout)(String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="(Term0: execute 预付金)"){
            currentStatus="[3, 2, 1, 1, 1, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

}