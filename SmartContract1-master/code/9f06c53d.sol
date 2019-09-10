//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 2]";
    }

    function [["[['A', 'Satconfirm', 'Term2'], ['B', 'Satpay', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2]" && action=="[["[['A', 'Satconfirm', 'Term2'], ['B', 'Satpay', 'Term1']]"]]"){
            currentStatus="[3, 3]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vioconfirm', 'Term2'], ['B', 'Satpay', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2]" && action=="[["[['A', 'Satconfirm', 'Term2'], ['B', 'Satpay', 'Term1']]"]]"){
            currentStatus="[3, 3]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satconfirm', 'Term2'], ['B', 'Viopay', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2]" && action=="[["[['A', 'Satconfirm', 'Term2'], ['B', 'Satpay', 'Term1']]"]]"){
            currentStatus="[3, 3]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vioconfirm', 'Term2'], ['B', 'Viopay', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 2]" && action=="[["[['A', 'Satconfirm', 'Term2'], ['B', 'Satpay', 'Term1']]"]]"){
            currentStatus="[3, 3]";
            return true;
        }
        else
            return false;
    }

}