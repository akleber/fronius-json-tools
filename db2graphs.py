import matplotlib.pyplot as plt
import sqlite3 as lite


con = lite.connect('examples/fronius.db')

with con:
    cur = con.cursor()    
    
    cur.execute("SELECT timestamp, powerflow_P_PV from fronius")
    rows = cur.fetchall() 

x = [ row[0] for row in rows ]
y = [ row[1] for row in rows ]

#print(data)
#print(x)

plt.plot(x, y)
#plt.show()
plt.savefig('examples/plot.png', bbox_inches='tight')