//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1]";
    }

    function [["[['A', 'judge(A,4)', 'Term1Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '!judge(A,4)', 'Term1Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satdeliver', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viodeliver', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2]";
            return true;
        }
        else
            return false;
    }

}