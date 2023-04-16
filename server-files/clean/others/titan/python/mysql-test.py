from _globals import *
import os
import sys
sys.path.append(os.path.abspath("/home/rojeta/server/python-core"))
from lib import *

my = EasyMysql()

print(my.fetch('SELECT * FROM servers'));
