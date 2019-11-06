#!/bin/bash

#SFTP配置信息
#用户名
echo $1
name=$1

USER=root
#密码
PASSWORD=Bjszgc59@RUC.xxl
#待上传文件根目录
SRCDIR=/home/xiahuahui/打印机/SmartContract/data/SmartContract1-master/data/code/${name}
#FTP目录
DESDIR=/home/puweiwang/SCASverify/artifacts/src/github.com/business
#IP
IP=202.112.114.22
#端口
PORT=22
#目录下的所有文件
FILE=${name}
#发送文件 (关键部分）
sshpass -p ${PASSWORD} scp -r ${SRCDIR} ${USER}@${IP}:${DESDIR}
echo -e "完成"



