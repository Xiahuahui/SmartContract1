from GNode import GNode
from ReduceGNode import ReducedGnode
from Settings import settings
import mysql.connector
import mysql.connector.pooling
import pickle
import json
import time


# 存储节点的仓库类    单例
class NodeRepository:

    def __init__(self):
        pass

    def getnode(self, id):
        pass

    def remove(self, id):
        pass

    def addnode(self, node):
        pass

    def printl(self):
        pass

    def getnum(self):
        pass

    def loadNodes(self, idList):
        pass

    def cleanTable(self):
        pass

    def saveLeafIdList(self, idList):
        pass


class MemoryNodeRepository(NodeRepository):
    """docstring for MemoryNodeRepository"""

    def __init__(self):
        self._repository = []  # 存储过程中需要的所有节点
        self._nodeId = []  # 存储节点的id 便于存取

    def getnode(self, id):
        if id in self._nodeId:
            index = self._nodeId.index(id)
            return self._repository[index]
        else:
            return -1

    def remove(self, id):
        if id in self._nodeId:
            index = self._nodeId.index(id)
            del self._repository[index]
            del self._nodeId[index]
        else:
            print("没有该节点")

    def addnode(self, node):
        if node.getId() not in self._nodeId:
            self._repository.append(node)
            self._nodeId.append(node.getId())

    def printl(self):
        return self._nodeId

    def getnum(self):
        return len(self._repository)

    def loadNodes(self, idList):
        nodes = []
        List = []  # 避免重复取到相同的节点
        for id in idList:
            if id not in List:
                List.append(id)
                n = self.getnode(id)
                nodes.append(n)
        return nodes

    def cleanTable(self):
        pass

    def updateNode(self, node):
        pass

    def saveLeafIdList(self, idList, id):
        pass

    def getLeafIdList(self):
        pass

    def saveUpperNodeIds(self, upperIdList, newIdList):
        pass

    def getUpperNodeIds(self):
        pass

    def updateNode(self, node, paramsList):
        pass


class DataBaseNodeRepository(NodeRepository):
    
    # 创建连接池
    def __init__(self):
        self.cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name="nodepool",
                                                                       pool_size=30,
                                                                   **settings.dbConfig['local'])
        self.buffer = {}

    # 根据节点的id取到相应node
    def getnode(self, id):
        if str(id) in self.buffer:
            return self.buffer[str(id)]
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:
            selectSql = "select * from `GNode` where `id` = '" + str(id) + "'"
            cursor.execute(selectSql)
            result = cursor.fetchall()
            if (len(result) == 0):
                print("getnode")
                print(id)
                return -1
            if (result[0][6] == "GNode"):
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
            return node
        except Exception:
            print("发生异常")
            print(id)
            raise
            return -1
        finally:
            cnx.close()

    def remove(self, id):
        if str(id) in self.buffer:
            del self.buffer[str(id)]
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:
            delSql = "delete from `GNode` where `id` = '" + str(id) + "'"
            cursor.execute(delSql)
            cnx.commit()
        except Exception:
            print("没有此节点")
            cnx.rollback()
        finally:
            cnx.close()

    def addnode(self, node):
        # print("addnode",node.getId())
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:
            insertSql = "insert into `GNode`(`id`,`outEdges`,`childrenId`,`parentsId`,`CMTs`,`stateSet`,`type`) values (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(insertSql, (node.getId(), pickle.dumps(node.getOutEdges()), json.dumps(node.getChildrenId()),
                                       json.dumps(node.getParentsId()), pickle.dumps(node.getCmts()),
                                       json.dumps(node.getStateSet()), node.getType()))
            cnx.commit()
        except Exception:
            print("发生异常")
            raise
            cnx.rollback()
        finally:
            cnx.close()

    def addNodeToBuffer(self,node):
        self.buffer[str(node.getId())] = node

    def delNodeFromBuffer(self,node):
        if str(node.getId()) in self.buffer:
            del self.buffer[str(node.getId())]

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

    def loadNodes(self, idList):
        if (len(idList) == 0):
            return []
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        nodeList = []
        try:
            idListTmp = [str(id) for id in idList]
            idListstr = "(" + ",".join(idListTmp) + ")"
            selectSql = "select * from `GNode` where `id` in " + idListstr + ""
            cursor.execute(selectSql)
            resultSet = cursor.fetchall()
            for result in resultSet:
                if (result[6] == "GNode"):
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
            dropSql = "drop table `mergeLeafOver`"
            cursor.execute(dropSql)
            createSql = ("CREATE TABLE IF NOT EXISTS `GNode`(" +
                         "`id` INT UNSIGNED," +
                         "`outEdges` LONGBLOB," +
                         "`childrenId` LONGText," +
                         "`parentsId` LONGText," +
                         "`CMTs` LONGBlob," +
                         "`stateSet` LONGText," +
                         "`type` VARCHAR(20)," +
                         "PRIMARY KEY (`id`)," +
                         "INDEX GnodeID (`id`)" +
                         ")ENGINE=InnoDB DEFAULT CHARSET=utf8")
            cursor.execute(createSql)
            createSql = ("CREATE TABLE IF NOT EXISTS `leafidlist`(" +
                         "`id` INT UNSIGNED AUTO_INCREMENT," +
                         "`leaflist` MediumText," +
                         "`GnodeId` INT," +
                         "PRIMARY KEY (`id`)" +
                         ")ENGINE=InnoDB DEFAULT CHARSET=utf8")
            cursor.execute(createSql)
            createSql = ("CREATE TABLE IF NOT EXISTS `mergeLeafOver`(" +
                         "`id` INT UNSIGNED AUTO_INCREMENT," +
                         "`upperNodeIds` MediumText," +
                         "`newIdList` MediumText," +
                         "PRIMARY KEY (`id`)" +
                         ")ENGINE=InnoDB DEFAULT CHARSET=utf8")
            cursor.execute(createSql)
            cnx.commit()
        except Exception as e:
            raise
            cnx.rollback()
        finally:
            cnx.close()

    def updateNode(self, node):
        # print("updateNode",node.getId(),node.getOutEdges())
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:
            updateSql = "update `GNode` set `outEdges` = %s,`childrenId` = %s,`parentsId` = %s,`CMTs` = %s,`stateSet` = %s,`type` = %s where `id` = %s"
            cursor.execute(updateSql, (
            pickle.dumps(node.getOutEdges()), json.dumps(node.getChildrenId()), json.dumps(node.getParentsId()),
            pickle.dumps(node.getCmts()), json.dumps(node.getStateSet()), node.getType(), node.getId()))
            cnx.commit()
        except Exception:
            print("发生异常")
            raise
            cnx.rollback()
        finally:
            cnx.close()


    def getParams(self,node,paramsList):
        allParams=['outEdges','childrenId','parentsId','CMTs','stateSet','type','id']
        params = []
        for param in paramsList:
            if(param == allParams[0]):
                params.append(pickle.dumps(node.getOutEdges()))
            elif(param == allParams[1]):
                params.append(json.dumps(node.getChildrenId()))
            elif(param == allParams[2]):
                params.append(json.dumps(node.getParentsId()))
            elif(param == allParams[3]):
                params.append(pickle.dumps(node.getCmts()))
            elif(param == allParams[4]):
                params.append(json.dumps(node.getStateSet()))
            elif(param == allParams[5]):
                params.append(node.getType())
            elif(param == allParams[6]):
                params.append(node.getId())
        params.append(node.getId())
        params = tuple(params)
        return params
    #paramsList:
    #   ['outEdges','childrenId','parentsId','CMTs','stateSet','type','id']
    def updateNode(self,node,paramsList):
        if str(node.getId()) in self.buffer:
            return
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:
            updateSql = "update `GNode` set"
            #`outEdges` = %s,`childrenId` = %s,`parentsId` = %s,`CMTs` = %s,`stateSet` = %s,`type` = %s where `id` = %s"
            for param in paramsList:
                updateSql = updateSql + " `" + param + '` = %s,'
            updateSql = updateSql[:-1]
            updateSql = updateSql+' where `id` = %s'
            params = self.getParams(node,paramsList)
            cursor.execute(updateSql, params)
            cnx.commit()
        except Exception:
            print("发生异常")
            raise
            cnx.rollback()
        finally:
            cnx.close()

    def batchUpdate(self,cursor,params):
        paramData=[]
        updateSql = "UPDATE `GNode` SET"
        dataList=[]
        for id in self.buffer:
            dataList.append(self.getParams(self.buffer[id],params))
        #['outEdges','childrenId','parentsId','CMTs','stateSet','type','id']
        for i in range(0,len(params)):
            updateSql = updateSql+"`"+params[i]+"` = CASE `id` "
            for data in dataList:
                updateSql = updateSql+"WHEN %s THEN %s "
                paramData.append(data[-1])
                paramData.append(data[i])
            updateSql=updateSql+"END,"
        updateSql = updateSql[:-1]
        updateSql = updateSql+" WHERE `id` IN ("
        for data in dataList:
            updateSql = updateSql+"%s,"
            paramData.append(data[-1])
        updateSql = updateSql[:-1]
        updateSql = updateSql+")"
        return updateSql,paramData

    def bufferUpdateToDB(self):
        if len(self.buffer)==0:
            return
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:
            updateSql,data = self.batchUpdate(cursor,["outEdges","childrenId","parentsId"])
            cursor.execute(updateSql,data)
            cnx.commit()
        except Exception:
            print("发生异常")
            raise
            cnx.rollback()
        finally:
            cnx.close()

    def saveLeafIdList(self, idList, id):
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:
            insertSql = "insert into `leafidlist`(`leaflist`,`GnodeId`) values('" + json.dumps(idList) + "','" + str(
                id) + "')"
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
            #print(idList)
            return idList, result[0][2]
        except Exception:
            print("发生异常")
            raise
            cnx.rollback()
        finally:
            cnx.close()

    def saveUpperNodeIds(self, upperIdList, newIdList):
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:
            insertSql = "insert into `mergeLeafOver`(`upperNodeIds`,`newIdList`) values('" + json.dumps(
                upperIdList) + "','" + json.dumps(newIdList) + "')"
            cursor.execute(insertSql)
            cnx.commit()
        except Exception:
            print("发生异常")
            raise
            cnx.rollback()
        finally:
            cnx.close()

    def getUpperNodeIds(self):
        cnx = self.cnxpool.get_connection()
        cursor = cnx.cursor()
        try:
            searchSql = "select * from `mergeLeafOver`"
            cursor.execute(searchSql)
            result = cursor.fetchall()
            return json.loads(result[0][1]), json.loads(result[0][2])
        except Exception:
            print("发生异常")
            raise
            cnx.rollback()
        finally:
            cnx.close()


if (settings.mode == "database" or settings.mode == 'db'):
    nodeRepository = DataBaseNodeRepository()
else:
    nodeRepository = MemoryNodeRepository()
#nodeRepository.cleanTable()
if __name__ == '__main__':
    if (settings.mode == "database" or settings.mode == 'db'):
        GnodeList = DataBaseNodeRepository()
    else:
        GnodeList = MemoryNodeRepository()
    GnodeList.cleanTable()