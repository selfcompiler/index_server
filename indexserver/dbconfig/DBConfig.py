import yaml
import os
import sys


filePath=str(os.getcwd())+"/dbconfig/dbconfig.yaml"
class DBConfig:
    """
      DB Config Class to Read *.yaml config file

      Patter of *.yaml file :

      key:
        host : 10.85.147.15
        user : common
        password : common
        database: fkmp_med_production

    """
    def __init__(self):
        print ("Initialize DBConfig")

    @staticmethod
    def getPassword(key):
        cfg=""
        with open(filePath, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        return cfg[key]['password']

    @staticmethod
    def getHost(key):
        cfg=""
        with open(filePath, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        print("Key "+key)
        print (cfg)
        return cfg[key]['host']

    @staticmethod
    def getUser(key):
        cfg = ""
        with open(filePath, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        return cfg[key]['user']

    @staticmethod
    def getDB(key):
        cfg = ""
        with open(filePath, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        return cfg[key]['database']

    @staticmethod
    def printDetails(key):
        cfg = ""
        with open(filePath, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        print("Key : " + key)
        print (self.cfg[key])


#print (os.getcwd())
#print (DBConfig.getDB("fkmp_mediator"))