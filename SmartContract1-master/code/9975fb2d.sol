//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1, 1]";
    }

    function [["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satpay', 'Term1'], ['A', '!judge(A,4)', 'Term2Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viopay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viopay', 'Term1'], ['A', '!judge(A,4)', 'Term2Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satdeliver', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viodeliver', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satdeliver', 'Term2'], ['B', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viodeliver', 'Term2'], ['B', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Sattransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viotransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Sattransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viotransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Sattransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viotransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Sattransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viotransfer', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

}