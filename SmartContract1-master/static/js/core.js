var canvas = document.getElementById('canvas');
//set canvas pos
if(canvas.currentStyle){
    canvas.setAttribute('width',canvas.parentElement.clientWidth-canvas.parentElement.currentStyle.paddingRight);
}else{
    canvas.setAttribute('width',canvas.parentElement.clientWidth-parseInt(getComputedStyle(canvas.parentElement).paddingRight));
}
getStandTr = function () {
    var tr = document.createElement('tr');
    var td = document.createElement('td');
    var select = document.createElement('select');
    var option = document.createElement('option');
    option.value="||";
    option.innerText='||';
    select.appendChild(option);
    option = document.createElement('option');
    option.value="&&";
    option.innerText='&&';
    select.appendChild(option);
    td.appendChild(select);
    tr.appendChild(td);
    td = document.createElement('td');
    select = document.createElement('select');
    option = document.createElement('option');
    option.value='action';
    option.innerText='action';
    select.appendChild(option);
    option = document.createElement('option');
    option.value='Term';
    option.innerText='Term';
    select.appendChild(option);
    select.addEventListener('change',function (ev) {
        var selectTerm=this.parentElement.parentElement.childNodes[2];
        var state=this.parentElement.parentElement.childNodes[3];
        if(this.value=='Term'){
            selectTerm.childNodes[0].remove();
            var select = document.createElement('select');
            for(var key in shapeList){
                var option = document.createElement('option');
                option.value='Term'+shapeList[key].termID;
                option.innerText='Term'+shapeList[key].termID+' '+shapeList[key].getPre();
                select.appendChild(option);
            }
            select.style.width="300px";
            selectTerm.appendChild(select)
            var select = document.createElement('select');
            var stateList=['.Sat','.Vio','.Exp'];
            for(var key in stateList){
                var option = document.createElement('option');
                option.value=stateList[key];
                option.innerText=stateList[key];
                select.appendChild(option);
            }
            state.appendChild(select);
        }else{
            selectTerm.childNodes[0].remove();
            var input = document.createElement('input');
            input.style.width='300px';
            selectTerm.appendChild(input);
            state.childNodes[0].remove();
        }
    });
    td.appendChild(select);
    tr.appendChild(td);
    td = document.createElement('td');
    var input = document.createElement('input');
    input.style.width='100%';
    td.appendChild(input);
    tr.appendChild(td);
    td = document.createElement('td');
    tr.appendChild(td);
    td = document.createElement('td');
    var a = document.createElement('a');
    a.setAttribute('href','#');
    a.setAttribute('class','easyui-linkbutton');
    a.setAttribute('icon','icon-cancel');
    a.setAttribute('size','small');
    a.addEventListener('click',function (ev) {
        this.parentElement.parentElement.remove();
    });
    td.appendChild(a);
    tr.appendChild(td);
    return tr;
};
var ctx=null;
ctx=canvas.getContext('2d');
var shapeList=[];
var createPosX=null;
var createPosY=null;
var selectShape=null;
var ismove=false;
init = function(){
    var editPre = document.getElementById('premise');
    while(editPre.lastChild!=null){
        editPre.lastChild.remove();
    }
    var table = document.createElement('table');
    var tr = document.createElement('tr');
    var td = document.createElement('td');
    tr.appendChild(td);
    td = document.createElement('td');
    var select = document.createElement('select');
    option = document.createElement('option');
    option.value='action';
    option.innerText='action';
    select.appendChild(option);
    var option = document.createElement('option');
    option.value='Term';
    option.innerText='Term';
    select.addEventListener('change',function (ev) {
        var selectTerm=this.parentElement.parentElement.childNodes[2];
        var state=this.parentElement.parentElement.childNodes[3];
        if(this.value=='Term'){
            selectTerm.childNodes[0].remove();
            var select = document.createElement('select');
            for(var key in shapeList){
                var option = document.createElement('option');
                option.value='Term'+shapeList[key].termID;
                option.innerText='Term'+shapeList[key].termID+' '+shapeList[key].getPre();
                select.appendChild(option);
            }
            select.style.width="300px";
            selectTerm.appendChild(select)
            var select = document.createElement('select');
            var stateList=['.Sat','.Vio','.Exp'];
            for(var key in stateList){
                var option = document.createElement('option');
                option.value=stateList[key];
                option.innerText=stateList[key];
                select.appendChild(option);
            }
            state.appendChild(select);
        }else{
            selectTerm.childNodes[0].remove();
            var input = document.createElement('input');
            input.style.width='100%';
            selectTerm.appendChild(input);
            state.childNodes[0].remove();
        }
    });
    select.appendChild(option);
    td.appendChild(select);
    tr.appendChild(td);
    td = document.createElement('td');
    var input = document.createElement('input');
    input.style.width='300px';
    td.appendChild(input);
    tr.appendChild(td);
    td = document.createElement('td');
    tr.appendChild(td);
    td = document.createElement('td');
    tr.appendChild(td);
    table.appendChild(tr);
    editPre.appendChild(table);
    var p = document.createElement('p');
    a = document.createElement('a');
    a.setAttribute('href','#');
    a.setAttribute('class','easyui-linkbutton');
    a.setAttribute('icon','icon-add');
    a.setAttribute('size','small');
    a.addEventListener('click',addCondition);
    p.appendChild(a);
    editPre.appendChild(p);
    table.appendChild(tr);
    $.parser.parse(p);
};
addCondition = function(ev){
    var editPre = document.getElementById('premise');
    var table = this.parentElement.parentElement.childNodes[0];
    table.appendChild(getStandTr());
    $.parser.parse(table);
};
//set termList
$('#termList').datagrid({
    fitColumns:true,
    scrollbarSize:0,
    nowrap:false,
    columns:[[
        {field:'TermID',title:'Term ID',width:'70px',align:'center',halign:'center'},
        {field:'actor',title:'actor',width:'60px',align:'center',halign:'center'},
        {field:'premise',title:'premise',width:'30%',align:'center',halign:'center'},
        {field:'result',title:'result',width:'30%',align:'center',halign:'center'},
        {field:'beginTime',title:'begin time',width:'100px',align:'center',halign:'center'},
        {field:'endTime',title:'end time',width:'100px',align:'center',halign:'center'}
    ]],
    onClickRow:function (index,row) {
        if(shapeList[index].isClicked()) {
            shapeList[index].color='green';
        }else{
            shapeList[index].color='red';
        }
        redraw(ctx);
    }
});
//右击面板
canvas.oncontextmenu=function (ev) {
    ev.preventDefault();//取消默认的浏览器自带右键

    selectShape=checkSelectShape(ev);
    createPosX=ev.offsetX;
    createPosY=ev.offsetY;
    if(selectShape==null){
        $('#createTermMenu').menu('show',{
            left:ev.pageX,
            top:ev.pageY
        });
    }else{
        $('#setTermMenu').menu('show',{
            left:ev.pageX,
            top:ev.pageY
        });
    }

};
//面板消失
window.onclick = function (ev) {
    $('#createTermMenu').menu('hide');
    $('#setTermMenu').menu('hide');
};
//canvas上的监听事件
canvas.onclick = function (ev) {
    selectShape=checkSelectShape(ev);
};
canvas.addEventListener('mousedown',function (ev) {
    console.log(ev);
    selectShape=checkSelectShape(ev);
    console.log(selectShape);
    if(selectShape!=null&&ev.button==0){
        ismove=true;
    }
});
canvas.addEventListener('mouseup',function (ev) {
    ismove=false;
    if(selectShape!=null&&ev.button==0){
        if(selectShape.isClicked()){
            selectShape.color='green';
            $('#termList').datagrid('unselectRow',selectShape.termID-1);
        }else{
            selectShape.color='red';
            $('#termList').datagrid('selectRow',selectShape.termID-1);
        }
        redraw(ctx);
    }
});
canvas.addEventListener('mousemove',function (ev) {
    if(ismove==true){
        console.log('move');
        selectShape.changePos(ev.offsetX,ev.offsetY);
        selectShape.color='green';
        $('#termList').datagrid('unselectRow',selectShape.termID-1);
        redraw(ctx);
    }
});
//创建新的term(包含图形和将term加入termlist)
var createTerm = document.getElementById('createTerm');
createTerm.addEventListener('click',function (ev) {
    if(ctx!=null){
        shapeList.push(new Circle(createPosX,createPosY,shapeList.length+1,ctx));
        addToTermList(shapeList[shapeList.length-1]);
        redraw(ctx);
    }
});
//检查是否点击到了图形，如果是，将图形返回
checkSelectShape = function(ev){
    for(var i = 0;i < shapeList.length;i++){
        var shape=shapeList[i.toString()];
        if(ev.offsetX<=shape.node.x+shape.radius&&ev.offsetX>=shape.node.x-shape.radius&&ev.offsetY<=shape.node.y+shape.radius&&ev.offsetY>=shape.node.y-shape.radius){
            return shape;
        }
    }
    return null;
};

fireSelect = function(ele,value){
    ele.value=value;
    if("createEvent" in document){
        var evt=document.createEvent("HTMLEvents");
        evt.initEvent("change",false,true);
        ele.dispatchEvent(evt);
    }
    else{
        ele.fireEvent('onchange');
    }
};

setTermPre = function (shape) {
    var editPre = document.getElementById('premise');
    var table = editPre.firstChild;
    var tr = null;
    for(var key=0;key<shape.preTerm.length;key++){
        if(typeof table.childNodes[key] == 'undefined'){
            tr = getStandTr();
            table.appendChild(tr);
            $.parser.parse(table);
        }else{
            tr = table.childNodes[key];
        }
        if(shape.preTerm[key].logic!=''){
            fireSelect(tr.childNodes[0].firstChild,shape.preTerm[key].logic);
        }
        if(typeof shape.preTerm[key].term == 'object') {
            fireSelect(tr.childNodes[1].firstChild,'Term');
            fireSelect(tr.childNodes[2].firstChild,'Term'+shape.preTerm[key].term.termID);
            fireSelect(tr.childNodes[3].firstChild,shape.preTerm[key].state);
        }else{
            tr.childNodes[2].firstChild.value=shape.preTerm[key].term;
        }
    }
};

var setTerm = document.getElementById('setTerm');
setTerm.addEventListener('click',function (ev) {
    init();
    $("#editTermWin").window('open');
    var actorSelector = document.getElementById('actor');
    fireSelect(actorSelector,selectShape.actor);
    document.getElementById('termID').innerText=selectShape.termID;
    document.getElementById('result').value=selectShape.result;
    $('#beginTime').datetimebox('setValue',selectShape.beginTime);
    $('#endTime').datetimebox('setValue',selectShape.endTime);
    setTermPre(selectShape)
});

var delTerm = document.getElementById('delTerm');
delTerm.addEventListener('click',function (ev) {
    shapeList[selectShape.termID-1]=null;
    shapeList.splice(selectShape.termID-1,1);
    $('#termList').datagrid('deleteRow',selectShape.termID-1);
    selectShape.termID=0;
    for(var key in shapeList){
        shapeList[key].changeTermID(parseInt(key)+1);
        $('#termList').datagrid('updateRow',{
            index:key,
            row:{
                TermID:'Term'+shapeList[key].termID,
                premise:shapeList[key].getPre()
            }
        });
    }
    redraw(ctx);
});

preToString = function () {
    var editPre = document.getElementById('premise');
    var table = editPre.firstChild;
    var preStr="";
    for(var i =0; i< table.childNodes.length; i++){
        for(var j=0;j<4;j++) {
            if(table.childNodes[i].childNodes[j].firstChild!=null&&j!=1){
                preStr+=table.childNodes[i].childNodes[j].firstChild.value;
            }
        }
    }
    return preStr;
};

termSetPre = function () {
    var editPre = document.getElementById('premise');
    var table = editPre.firstChild;
    var preStr="";
    var tmpTerm={};
    selectShape.preTerm=[];
    for(var i =0; i< table.childNodes.length; i++){
        tmpTerm={
            'logic':'',
            'term':'',
            'state':''
        };
        if(table.childNodes[i].childNodes[0].firstChild!=null){
            tmpTerm.logic=table.childNodes[i].childNodes[0].firstChild.value;
        }
        if(table.childNodes[i].childNodes[1].firstChild.value=='action'){
            tmpTerm.term=table.childNodes[i].childNodes[2].firstChild.value;
        }else{
            var index = parseInt(table.childNodes[i].childNodes[2].firstChild.value.slice(4));
            tmpTerm.term=shapeList[index-1];
            tmpTerm.state=table.childNodes[i].childNodes[3].firstChild.value;
        }
        selectShape.preTerm.push(tmpTerm);
    }
};

var termset = document.getElementById('termSet');
termset.onclick = function (ev) {
    selectShape.actor=document.getElementById('actor').value;
    termSetPre();
    selectShape.result=document.getElementById('result').value;
    selectShape.beginTime=$('#beginTime').datetimebox('getValue');
    selectShape.endTime=$('#endTime').datetimebox('getValue');;
    setTermList(selectShape);
    $('#editTermWin').window('close');
    redraw(ctx);
};

var cancel = document.getElementById('cancel');
cancel.onclick = function (ev) {
    $('#editTermWin').window('close');
};

addToTermList = function(shape){
    $("#termList").datagrid('insertRow',{
        index:shape.termID-1,
        row:{
            TermID:'Term'+shape.termID,
            actor:shape.actor,
            premise:shape.getPre(),
            result:shape.result,
            beginTime:shape.beginTime,
            endTime:shape.endTime
        }
    });
};
setTermList = function(shape){
    $("#termList").datagrid('updateRow',{
        index:shape.termID-1,
        row:{
            TermID:'Term'+shape.termID,
            actor:shape.actor,
            premise:shape.getPre(),
            result:shape.result,
            beginTime:shape.beginTime,
            endTime:shape.endTime
        }
    });
};

redraw = function (ctx) {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    for(var key in shapeList){
        shapeList[key].drawCircle(ctx);
        shapeList[key].drawLine(shapeList,ctx);
    }
};

$('#beginTime').datetimebox({
});
$('#endTime').datetimebox({
});

getContent = function () {
    var content = [];
    var rows = $("#termList").datagrid('getRows');
    for(var key=0;key<rows.length;key++){
        var res={};
        res['person'] = rows[key].actor;
        res['premise'] = rows[key].premise;
        res['res'] = rows[key].result;
        res['time'] = rows[key].beginTime+','+rows[key].endTime;
        content.push(res);
    }
    return content;
};
