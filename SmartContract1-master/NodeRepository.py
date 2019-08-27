from  GNode import GNode
from ReduceGNode import ReducedGnode
from Settings import settings
import mysql.connector
import mysql.connector.pooling
import pickle
import json
import time
#存储节点的仓库类    单例
class NodeRepository:
    beforecount=0
    searchCount=0
    def __init__(self):
        pass
    def getnode(self,id):
        pass
    def remove(self,id):
        pass
    def addnode(self,node):
        pass
    def printl(self):
        pass
    def getnum(self):
        pass
    def loadNodes(self,idList):
        pass
    def cleanTable(self):
        pass
    def saveLeafIdList(self,idList):
        pass
class MemoryNodeRepository(NodeRepository):
    """docstring for MemoryNodeRepository"""
    def __init__(self):
        self._repository = []     #存储过程中需要的所有节点
        self._nodeId = []         #存储节点的id 便于存取
    def getnode(self,id):
        if id in self._nodeId:
            index = self._nodeId.index(id)
            return self._repository[index]
        else:
            return -1
    def remove(self,id):
        if id in self._nodeId:
            index = self._nodeId.index(id)
            del self._repository[index]
            del self._nodeId[index]
        else:
            print("没有该节点")
    def addnode(self,node):
        if node.getId() not in self._nodeId:
            self._repository.append(node)
            self._nodeId.append(node.getId())
    def printl(self):
        return self._nodeId
        
    def getnum(self):
        return len(self._repository)
    def loadNodes(self,idList):
        nodes = []
        List = []          #避免重复取到相同的节点
        for id in idList:
            if id not in List:
                List.append(id)
                n = self.getnode(id)
                nodes.append(n)
        return nodes
    def cleanTable(self):
        pass

    def updateNode(self,node):
        pass

    def saveLeafIdList(self,iii,idList):
        pass

class DataBaseNodeRepository(NodeRepository):
    startTime = time.time()
    endTime = time.time()
    #创建连接池
    def __init__(self):
        self.cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "nodepool",
                                                              pool_size = 30,
                                                              **settings.dbConfig['local'])
    #根据节点的id取到相应node
    def getnode(self,id):
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:    
            selectSql = "select * from `GNode` where `id` = '"+str(id)+"'"
            cursor.execute(selectSql)
            result = cursor.fetchall()
            if(len(result)==0):
                print("getnode")
                print(id)
                return -1
            if(result[0][6]=="GNode"):
                node = GNode()
                GNode.Id = GNode.Id - 1
            else:
                node = ReducedGnode()
                GNode.Id = GNode.Id - 1
                node.setStateSet(json.loads(result[0][5]))
            node.setId(result[0][0])
            node.setOutEdges(pickle.loads(result[0][1]))
            node.setChildrenId(json.loads(result[0][2]))
            node.setParentsId(json.loads(result[0][3]))
            node.setCmtsFromDB(pickle.loads(result[0][4]))
            node.setType(result[0][6])
            NodeRepository.searchCount=NodeRepository.searchCount+1
            if NodeRepository.searchCount%1000==0:
                DataBaseNodeRepository.endTime = time.time()
                print("已查询节点数：",NodeRepository.searchCount)
                print("花费时间：",DataBaseNodeRepository.endTime-DataBaseNodeRepository.startTime)
                DataBaseNodeRepository.startTime=DataBaseNodeRepository.endTime
            return node
        except Exception:
            print("发生异常")
            print(id)
            raise
            return -1
        finally:
            cnx.close()
    def remove(self,id):
        #print("remove",id)
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:            
            delSql = "delete from `GNode` where `id` = '"+str(id)+"'"
            cursor.execute(delSql)
            cnx.commit()
        except Exception:
            print("没有此节点")
            cnx.rollback()
        finally:
            cnx.close()
    def addnode(self,node):
        #print("addnode",node.getId())
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:            
            insertSql = "insert into `GNode`(`id`,`outEdges`,`childrenId`,`parentsId`,`CMTs`,`stateSet`,`type`) values (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(insertSql,( node.getId(),pickle.dumps(node.getOutEdges()),json.dumps( node.getChildrenId() ),json.dumps( node.getParentsId() ),pickle.dumps(node.getCmts()),json.dumps( node.getStateSet() ),node.getType() ))
            cnx.commit()
        except Exception:
            print("发生异常")
            raise
            cnx.rollback()
        finally:
            cnx.close()
    def printl(self):
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:    
            selectSql = "select id from `GNode`"
            cursor.execute(selectSql)
            result = cursor.fetchall()
            idList = []
            for id in result:
                idList.append(id[0])
            return idList
        except Exception:
            print("发生异常")
            raise
            return -1
        finally:
            cnx.close()
    def getnum(self):
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:    
            selectSql = "select count(*) from `GNode`"
            cursor.execute(selectSql)
            result = cursor.fetchall()
            return result[0][0]
        except Exception:
            print("发生异常num")
            raise
            return -1
        finally:
            cnx.close()

    def loadNodes(self,idList):
        if(len(idList)==0):
            return []
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        nodeList=[]
        try:  
            idListTmp = [str(id) for id in idList]  
            idListstr = "("+",".join( idListTmp )+")"
            selectSql = "select * from `GNode` where `id` in "+idListstr+""
            cursor.execute(selectSql)
            resultSet = cursor.fetchall()
            for result in resultSet:
                if(result[6]=="GNode"):
                    node = GNode()
                    GNode.Id = GNode.Id - 1
                else:
                    node = ReducedGnode()
                    GNode.Id = GNode.Id - 1
                    node.setStateSet(json.loads(result[5]))
                node.setId(result[0])
                node.setOutEdges(pickle.loads(result[1]))
                node.setChildrenId(json.loads(result[2]))
                node.setParentsId(json.loads(result[3]))
                node.setCmtsFromDB(pickle.loads(result[4]))
                node.setType(result[6])
                nodeList.append(node)
            NodeRepository.searchCount=NodeRepository.searchCount+len(idList)
            if NodeRepository.searchCount - NodeRepository.beforecount >1000:
                NodeRepository.beforecount=NodeRepository.searchCount
                DataBaseNodeRepository.endTime = time.time()
                print("已查询节点数：",NodeRepository.searchCount)
                print("花费时间：",DataBaseNodeRepository.endTime-DataBaseNodeRepository.startTime)
                DataBaseNodeRepository.startTime=DataBaseNodeRepository.endTime
            return nodeList
        except Exception:
            print("发生异常")
            raise
            return nodeList
        finally:
            cnx.close()

    def cleanTable(self):
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:
            dropSql = "drop table `GNode`"
            cursor.execute(dropSql)
            dropSql = "drop table `leafidlist`"
            cursor.execute(dropSql)
            createSql = ("CREATE TABLE IF NOT EXISTS `GNode`("+
                            "`id` INT UNSIGNED,"+
                            "`outEdges` LONGBLOB,"+
                            "`childrenId` LONGText,"+
                            "`parentsId` LONGText,"+
                            "`CMTs` LONGBlob,"+
                            "`stateSet` LONGText,"+
                            "`type` VARCHAR(20),"+
                            "PRIMARY KEY (`id`),"+
                            "INDEX GnodeID (`id`)"+
                        ")ENGINE=InnoDB DEFAULT CHARSET=utf8")
            cursor.execute(createSql)
            createSql = ("CREATE TABLE IF NOT EXISTS `leafidlist`("+
                            "`id` INT UNSIGNED AUTO_INCREMENT,"+
                            "`leaflist` MediumText,"+
                            "`GnodeId` INT,"+
                            "PRIMARY KEY (`id`)"+
                        ")ENGINE=InnoDB DEFAULT CHARSET=utf8")
            cursor.execute(createSql)
            cnx.commit()
        except Exception as e:
            raise
            cnx.rollback()
        finally:
            cnx.close()
    
    def updateNode(self,node):
        #print("updateNode",node.getId(),node.getOutEdges())
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:            
            updateSql = "update `GNode` set `outEdges` = %s,`childrenId` = %s,`parentsId` = %s,`CMTs` = %s,`stateSet` = %s,`type` = %s where `id` = %s"
            cursor.execute(updateSql,( pickle.dumps(node.getOutEdges()),json.dumps( node.getChildrenId() ),json.dumps( node.getParentsId() ),pickle.dumps(node.getCmts()),json.dumps(node.getStateSet()),node.getType(),node.getId()))
            cnx.commit()
        except Exception:
            print("发生异常")
            raise
            cnx.rollback()
        finally:
            cnx.close()

    def saveLeafIdList(self,idList,id):
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:            
            insertSql = "insert into `leafidlist`(`leaflist`,`GnodeId`) values('"+json.dumps(idList)+"','"+str(id)+"')"
            cursor.execute(insertSql)
            cnx.commit()
        except Exception:
            print("发生异常")
            raise
            cnx.rollback()
        finally:
            cnx.close()
    def getLeafIdList(self):
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:            
            searchSql = "select * from `leafidlist`"
            cursor.execute(searchSql)
            result = cursor.fetchall()
            idList = json.loads(result[0][1])
            print(idList)
            return idList,result[0][2]
        except Exception:
            print("发生异常")
            raise
            cnx.rollback()
        finally:
            cnx.close()

if(settings.mode=="database" or settings.mode=='db'):
    nodeRepository = DataBaseNodeRepository()
else:
    nodeRepository = MemoryNodeRepository()
#nodeRepository.cleanTable()
if __name__ == '__main__':
    if(settings.mode=="database" or settings.mode=='db'):
        GnodeList = DataBaseNodeRepository()
    else:
        GnodeList = MemoryNodeRepository()
    GnodeList.cleanTable()