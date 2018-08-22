from threading import Lock, Thread

from indexserver.DBUtility.dbutils import DBUtils

class IndexServerHelper:


    def __init__(self):
        print ("Index Server Constructer")


    @staticmethod
    def initalize_index_table(context,start,end,gap):
        print ("Initialize Index Table")
        query="INSERT INTO `index_table` (`start`, `current`, `gap`, `end`, `context`) VALUES ("+str(start)+", "+str(start)+", "+str(gap)+", "+str(end)+", '"+str(context)+"')"
        print (query)
        DBUtils.execute_except_select_query("index_server",query)
        print ("Initialization Completed")

    @staticmethod
    def getNextIndex(context):
        query="select start,end,gap,current from index_table where context='"+str(context)+"'"
        print (query)
        resultSet=DBUtils.execute_select_query("index_server",query)
        start=int(resultSet[0][0])
        end=int(resultSet[0][1])
        gap=int(resultSet[0][2])
        current=int(resultSet[0][3])
        old_current=current
        next_expected=current+gap-1
        next_expected=min(next_expected,end)
        if next_expected>=end:
            current=start
        else:
            current=next_expected+1

        updated_query="update index_table set current='"+str(current)+"' where context='"+str(context)+"'"
        DBUtils.execute_except_select_query("index_server",updated_query)
        return str(old_current)+","+str(next_expected)