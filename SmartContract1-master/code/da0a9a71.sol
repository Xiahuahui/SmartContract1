//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1, 1]";
    }

    function [["[['A', 'Satdeposit(A,Contract,100)', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satdeposit(A,Contract,100)', 'Term1']]"]]"){
            currentStatus="[3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viodeposit(A,Contract,100)', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satdeposit(A,Contract,100)', 'Term1']]"]]"){
            currentStatus="[3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satdeposit(A,Contract,100)', 'Term1']]"]]"){
            currentStatus="[3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satdeposit(A,Contract,100)', 'Term1']]"]]"){
            currentStatus="[3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satdeliver(B,A,book)', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satdeposit(A,Contract,100)', 'Term1']]"]]"){
            currentStatus="[3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viodeliver(B,A,book)', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satdeposit(A,Contract,100)', 'Term1']]"]]"){
            currentStatus="[3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satdeposit(A,Contract,100)', 'Term1']]"]]"){
            currentStatus="[3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satdeposit(A,Contract,100)', 'Term1']]"]]"){
            currentStatus="[3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satdeposit(A,Contract,100)', 'Term1']]"]]"){
            currentStatus="[3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satconfirm(A,book)', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satdeposit(A,Contract,100)', 'Term1']]"]]"){
            currentStatus="[3, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vioconfirm(A,book)', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satdeposit(A,Contract,100)', 'Term1']]"]]"){
            currentStatus="[3, 1, 1]";
            return true;
        }
        else
            return false;
    }

}