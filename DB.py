# DB
# This file contains some helper functions

from sqlalchemy import create_engine

DB_STRING_FORMAT = "dbengine://user/password@connection:port/database_name"
# TODO this URI will be changed when project is deployed
DB_STRING = "postgresql://jamesacer:jamesacer@localhost:5432/test"

# TODO the idea behind these classes is encapsulation and a certain leve of abstraction
# I will not be making objects perse, but I will be using this to intereact with the data base.
class DB:
    installExtensionCMD = 'CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'
    rowNOtFound = "-1"

    def __init__(self):
        """This function creates the connection to the database and installs the necessary extension to it."""
        # Create connection
        self.db = create_engine(DB_STRING)
        # Install extension
        self.db.execute(self.installExtensionCMD)
        # TODO Create the users table
        self.db.execute()
        # TODO Create the posts table
        self.db.execute()

    # Functions with commun table interactions
    def createRow(self,*, table, columns, values):
        """This function will add a row to a table."""
        return self.db.execute(f"INSERT INTO {table}({columns}) VALUES ({values})")
    
    def getRow(self,*,table, columns, conditions):
        """This function returns rows that meet a condition"""
        return self.db.execute(f"SELECT {columns} FROM {table} WHERE {conditions}")
    
    def updateRow(self,*,table, columnsWithNewValues, conditions):
        """THis function updates rows that meet a condition"""
        return self.db.execute(f"UPDATE {table} SET {columnsWithNewValues} WHERE {conditions}")
    
    def deleteRow(self,*, table, conditions):
        """This function deletes rows that meet a conditrion""" 
        return self.db.execute(f"DELETE FROM {table} WHERE {conditions}")