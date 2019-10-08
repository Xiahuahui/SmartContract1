//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 2, 1, 1]";
    }

    function [["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satpay', 'Term1'], ['B', 'Viodeliver', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viopay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viopay', 'Term1'], ['B', 'Viodeliver', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term4'], ['B', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term4'], ['B', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term4'], ['B', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term4'], ['B', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satconfirm', 'Term4'], ['B', 'Sattransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vioconfirm', 'Term4'], ['B', 'Sattransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satconfirm', 'Term4'], ['B', 'Viotransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vioconfirm', 'Term4'], ['B', 'Viotransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Sattransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viotransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satconfirm', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vioconfirm', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['B', 'Satdeliver', 'Term2']]"]]"){
            currentStatus="[3, 3, 1, 1]";
            return true;
        }
        else
            return false;
    }

}