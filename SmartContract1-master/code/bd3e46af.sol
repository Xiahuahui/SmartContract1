//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1]";
    }

    function [["[['A', 'Sat阿萨所]', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat阿萨所]', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vio阿萨所]', 'Term1']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat阿萨所]', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat阿萨所]', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'judge(C,A)', 'Term2Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat阿萨所]', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '!judge(C,A)', 'Term2Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat阿萨所]', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Sat', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat阿萨所]', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vio', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1]" && action=="[["[['A', 'Sat阿萨所]', 'Term1']]"]]"){
            currentStatus="[3, 1]";
            return true;
        }
        else
            return false;
    }

}