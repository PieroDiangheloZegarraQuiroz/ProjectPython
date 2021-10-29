import uuid
u = uuid.uuid1()
rs = str(u)
rs2 = rs.replace('-', '')
print(rs2[:12])
