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

    function [["[['B', 'Satdeliver', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viodeliver', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satdeliver', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viodeliver', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Sattransfer\\n', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viotransfer\\n', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Sattransfer\\n', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viotransfer\\n', 'Term3']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1]" && action=="[["[['A', 'Satpay', 'Term1'], ['A', 'judge(A,4)', 'Term2Term2']]"]]"){
            currentStatus="[3, 2, 1]";
            return true;
        }
        else
            return false;
    }

}