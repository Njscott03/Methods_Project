from user import *
import sqlite3
import sys

class Inventory:

    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName

    