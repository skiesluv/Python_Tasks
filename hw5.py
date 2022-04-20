import os,sys
import sqlite3

path = sys.argv[1]

db = os.path.join(os.path.dirname(__file__), path)
sql = '''UPDATE ServerPorts
         SET port_number = 443
         WHERE servers_id = 1 OR servers_id = 6;
         SELECT servers_id, port_number FROM ServerPorts;'''
conn = sqlite3.connect(db)
result = conn.execute(sql).fetchall()

conn.close()