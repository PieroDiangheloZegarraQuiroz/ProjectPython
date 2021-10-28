from Connection import ConnectionDB

data, quantity = ConnectionDB.Connection().listFile22()

for x in data:
    rec_data = x[2]

with open(f'{x[1]}.pdf', 'wb') as f:
    f.write(rec_data)
