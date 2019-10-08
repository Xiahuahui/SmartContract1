//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[1, 1, 1, 1]";
    }

    function [["[['A', 'deposit(A,100)', 'Term1Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '!deposit(A,100)', 'Term1Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satdeliver', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viodeliver', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term2'], ['C', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term2'], ['C', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term2'], ['C', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satconfirm', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vioconfirm', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term3'], ['C', 'Satrefund', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sattransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[1, 1, 1, 1]" && action=="[["[['A', 'deposit(A,100)', 'Term1Term1']]"]]"){
            currentStatus="[2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

}