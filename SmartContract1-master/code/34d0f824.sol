//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1]";
    }

    function [["[['B', 'judge(B,4)', 'Term1Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="[["[['B', 'judge(B,4)', 'Term1Term1']]"]]"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '!judge(B,4)', 'Term1Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="[["[['B', 'judge(B,4)', 'Term1Term1']]"]]"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satpay', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="[["[['B', 'judge(B,4)', 'Term1Term1']]"]]"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viopay', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="[["[['B', 'judge(B,4)', 'Term1Term1']]"]]"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

}