function Circle(x,y,termID,ctx){
    this.radius=8;
    this.termID=termID;
    this.preTerm=[];
    this.result="";
    this.beginTime="";
    this.endTime="";
    this.actor="";
    this.color="green";
    this.node={
        'index':termID-1,
        'x':x,
        'y':y,
        'vx':500,
        'vy':300
    };
}

Circle.prototype.drawCircle = function (ctx) {
    ctx.beginPath();
    ctx.fillStyle=this.color;
    ctx.arc(this.node.x,this.node.y,this.radius,0,2*Math.PI);
    ctx.stroke();
    ctx.fill();
    ctx.font="italic 15px Arial";
    ctx.fillStyle="black";
    ctx.fillText("Term"+this.termID, this.node.x+10, this.node.y+4);
};

Circle.prototype.drawLine = function (shapeList,ctx) {
    var delid=null;
    for(var key=0;key<this.preTerm.length;key++){
        if(typeof this.preTerm[key].term == 'object'){
            var id=this.preTerm[key].term.termID-1;
            if(id<0){
                delid=key;
                continue;
            }
            if(delid==0&&key==1)
                this.preTerm[key].logic="";
            var startX=shapeList[id].node.x;
            var startY=shapeList[id].node.y;
            var ang=(this.node.x-startX)/(this.node.y-startY);
            ang=Math.atan(ang);
            if((this.node.x-startX<0&&this.node.y-startY>0)||(this.node.x-startX>0&&this.node.y-startY>0)){
                startX=startX+Math.sin(ang)*this.radius;
                startY=startY+Math.cos(ang)*this.radius;
                var endX=this.node.x-Math.sin(ang)*(this.radius+2);
                var endY=this.node.y-Math.cos(ang)*(this.radius+2);
            }else if((this.node.x-startX>0&&this.node.y-startY<0)||(this.node.x-startX<0&&this.node.y-startY<0)){
                startX=startX-Math.sin(ang)*this.radius;
                startY=startY-Math.cos(ang)*this.radius;
                var endX=this.node.x+Math.sin(ang)*(this.radius+2);
                var endY=this.node.y+Math.cos(ang)*(this.radius+2);
            }
            ctx.beginPath();
            //ctx.translate(startX,startY,0);
            ctx.moveTo(startX,startY);
            ctx.lineTo(endX,endY);
            ctx.fill();
            ctx.stroke();
            ctx.save();

            ctx.translate(endX,endY);

            if(endY-startY >= 0){
                ctx.rotate(-ang);
            }else{
                ctx.rotate(Math.PI-ang);//加个180度，反过来
            }
            ctx.lineTo(-5,-10);
            ctx.lineTo(0,-5);
            ctx.lineTo(5,-10);
            ctx.lineTo(0,0);
            ctx.fillStyle='red';
            ctx.fill(); //箭头是个封闭图形
            ctx.restore();   //恢复到堆的上一个状态，其实这里没什么用。
            ctx.closePath();
        }
    }
    if(delid!=null){
        this.preTerm.splice(delid,1);
    }
};

Circle.prototype.getPre = function(){
    var pre="";
    var delid=null;
    for(var key=0;key<this.preTerm.length;key++){
        if(this.preTerm[key].term.termID==0){
            delid=key;
            continue;
        }
        if(delid==0&&key==1)
            this.preTerm[key].logic="";
        pre+=this.preTerm[key].logic;
        if(typeof this.preTerm[key].term == 'string') {
            pre+=this.preTerm[key].term;
        }else{
            pre+=('Term'+this.preTerm[key].term.termID);
        }
        pre+=this.preTerm[key].state;
    }
    if(delid!=null){
        this.preTerm.splice(delid,1);
    }
    return pre;
};

Circle.prototype.isClicked = function(){
    if(this.color=='green')
        return false;
    return true;
};

Circle.prototype.setPreTerm = function (preTerm) {
    this.preTerm=preTerm;
};

Circle.prototype.setResult = function (result) {
    this.result=result;
};

Circle.prototype.setTime = function (beginTime,endTime) {
    this.beginTime=beginTime;
    this.endTime=endTime;
};

Circle.prototype.setActor = function (actor) {
    this.actor=actor;
};

Circle.prototype.changeTermID = function (termID) {
    this.termID=termID;
    this.node.index=termID-1;
};

Circle.prototype.changePos = function(x,y){
    this.node.x=x;
    this.node.y=y;
};