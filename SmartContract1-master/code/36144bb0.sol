//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1, 1]";
    }

    function [["[['A', 'judge(A,4)', 'Term1Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '!judge(A,4)', 'Term1Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satdeliver', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viodeliver', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satpay', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viopay', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1]" && action=="[["[['A', 'judge(A,4)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1]";
            return true;
        }
        else
            return false;
    }

}