//BCMETH means Blockchain Match Ethereum 
pragma solidity ^0.4.24;

contract BCMETH {
    String currentStatus;
    constructor () public {
        currentStatus="[2, 1, 1, 1, 1, 1, 1, 1]";
    }

    function [["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', '!judge(B,4)', 'Term5Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Sat2323', 'Term1'], ['A', '!judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Sat2323', 'Term1'], ['A', '!judge(A,7)', 'Term3Term3'], ['B', '!judge(B,4)', 'Term5Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vio2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vio2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', '!judge(B,4)', 'Term5Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vio2323', 'Term1'], ['A', '!judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Vio2323', 'Term1'], ['A', '!judge(A,7)', 'Term3Term3'], ['B', '!judge(B,4)', 'Term5Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satdfdf', 'Term3'], ['B', '', 'Term2'], ['B', 'Satertert', 'Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satdfdf', 'Term3'], ['B', '', 'Term2'], ['B', 'Vioertert', 'Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viodfdf', 'Term3'], ['B', '', 'Term2'], ['B', 'Satertert', 'Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viodfdf', 'Term3'], ['B', '', 'Term2'], ['B', 'Vioertert', 'Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satdfdf', 'Term3'], ['A', '', 'Term6'], ['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viodfdf', 'Term3'], ['A', '', 'Term6'], ['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term2'], ['B', 'Satertert', 'Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term2'], ['B', 'Vioertert', 'Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satdfdf', 'Term3'], ['B', '', 'Term2'], ['B', 'Satertert', 'Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satdfdf', 'Term3'], ['B', '', 'Term2'], ['B', 'Vioertert', 'Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viodfdf', 'Term3'], ['B', '', 'Term2'], ['B', 'Satertert', 'Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viodfdf', 'Term3'], ['B', '', 'Term2'], ['B', 'Vioertert', 'Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satdfdf', 'Term3'], ['A', '', 'Term6'], ['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viodfdf', 'Term3'], ['A', '', 'Term6'], ['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term2'], ['B', 'Satertert', 'Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term2'], ['B', 'Vioertert', 'Term5']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', '', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', 'Satdfdf', 'Term2'], ['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', 'Viodfdf', 'Term2'], ['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', 'Satdfdf', 'Term2'], ['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', 'Viodfdf', 'Term2'], ['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', 'Satdfdf', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', 'Viodfdf', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', 'Satdfdf', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', 'Viodfdf', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satdfdf', 'Term2'], ['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viodfdf', 'Term2'], ['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satdfdf', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viodfdf', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', 'Satdfdf', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', 'Viodfdf', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', 'Satdfdf', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['B', 'Viodfdf', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satdfdf', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viodfdf', 'Term2']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6'], ['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4'], ['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', '', 'Term6']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satjuiiu', 'Term6'], ['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viojuiiu', 'Term6'], ['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satjuiiu', 'Term6'], ['B', '', 'Term4'], ['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viojuiiu', 'Term6'], ['B', '', 'Term4'], ['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4'], ['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4'], ['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satjuiiu', 'Term6']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viojuiiu', 'Term6']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satjuiiu', 'Term6'], ['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viojuiiu', 'Term6'], ['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4'], ['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4'], ['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satjuiiu', 'Term6']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viojuiiu', 'Term6']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satjuiiu', 'Term6'], ['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viojuiiu', 'Term6'], ['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satjuiiu', 'Term6'], ['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viojuiiu', 'Term6'], ['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4'], ['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satjuiiu', 'Term6']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viojuiiu', 'Term6']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7'], ['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Satjuiiu', 'Term6']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['A', 'Viojuiiu', 'Term6']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satfddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Viofddsf', 'Term4']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', '', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Satere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['B', 'Vioere', 'Term7']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', '', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

    function [["[['C', 'Sat', 'Term8']]"]](String actionStr) public returns(bool){
        if(currentStatus=="[2, 1, 1, 1, 1, 1, 1, 1]" && action=="[["[['A', 'Sat2323', 'Term1'], ['A', 'judge(A,7)', 'Term3Term3'], ['B', 'judge(B,4)', 'Term5Term5']]"]]"){
            currentStatus="[3, 1, 2, 1, 2, 1, 1, 1]";
            return true;
        }
        else
            return false;
    }

}