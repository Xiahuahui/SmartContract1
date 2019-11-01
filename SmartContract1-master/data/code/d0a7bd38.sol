//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1]";
    }

    function [["[['B', 'Sat二二', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['B', 'Sat二二', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vio二二', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['B', 'Sat二二', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['B', 'Sat二二', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['B', 'Sat二二', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Sat', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['B', 'Sat二二', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vio', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['B', 'Sat二二', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

}