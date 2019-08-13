addTermList = function () {
    for(var key=0;key<shapeList.length;key++) {
        addToTermList(shapeList[key]);
    }
};

parsePre = function(pre){
    var preTerm=[];
    var term=pre.split(/&&|\|\|/g);
    var logic = pre.match(/&&|\|\|/g);
    for(var key=0;key<term.length;key++){
        var tmpTerm={
            'logic':'',
            'term':'',
            'state':''
        };
        if(key!=0)
            tmpTerm.logic=logic[key-1];
        if(term[key].slice(0,4)!='Term')
            tmpTerm.term=term[key];
        else{
            var tmpTermid = term[key].split('.')[0];
            tmpTerm.term=shapeList[parseInt(tmpTermid.slice(4))-1];
            tmpTerm.state=term[key].slice(term[key].length-4);
        }
        preTerm.push(tmpTerm);
    }
    return preTerm;
};
var lay={};
var col={};
addShape = function (content) {

    var shape=null;
    for(var key=0;key<content.length;key++){
        shapeList.push(new Circle(key*10,key*100,key+1,ctx));
    }
    for(var key=0;key<content.length;key++){
        shape = shapeList[key];
        shape.setActor(content[key].person);
        shape.setPreTerm(parsePre(content[key].premise));
        shape.setResult(content[key].res);
        shape.setTime(content[key].beginTime,content[key].endTime);
        if(typeof lay[shape.termID-1]== 'undefined') {
            lay[shape.termID-1]=parseInt(1);
        }
        for(var i=0;i<shape.preTerm.length;i++){
            if(typeof shape.preTerm[i].term == "object"){
                if(typeof lay[shape.preTerm[i].term.termID-1] == "object"){
                    lay[shape.preTerm[i].term.termID-1]=parseInt(1);
                }
                lay[shape.termID-1]=Math.max(lay[shape.termID-1],lay[shape.preTerm[i].term.termID-1]+1);
            }
        }
        if(typeof col[lay[shape.termID-1]]=="undefined"){
            col[lay[shape.termID-1]]=parseInt(1);
        }
        console.log(shape);
        console.log(col[lay[shape.termID-1]]*90+lay[shape.termID-1]*10+1);
        console.log(lay[shape.termID-1]*35+key+1);
        shape.changePos(col[lay[shape.termID-1]]*90+(Math.sqrt(key*20))*10+1,lay[shape.termID-1]*35+key+1);
        col[lay[shape.termID-1]]++;
    }
};
updateInit = function(content){
    addShape(content);
    addTermList();
    redraw(ctx);
};