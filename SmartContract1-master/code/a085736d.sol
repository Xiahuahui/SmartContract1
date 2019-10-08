//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1]";
    }

    function [["[['A', 'Sat二二', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat二二', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vio二二', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat二二', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat二二', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat二二', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Sathhh', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat二二', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viohhh', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat二二', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

}