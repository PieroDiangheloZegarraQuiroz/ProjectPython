from urllib import request

remote_url = 'https://www.muycomputerpro.com/zona-impresion-profesional/wp-content/uploads/2016/02/color.jpeg'
local_file = '/Users/sebas/Documents/pythonProject/proyecto/Models/llk'

request.urlretrieve(remote_url, local_file)

