OLD={3:239.80,8:59.99,9:69.99,10:69.99,12:49.99,13:69.99,14:39.99,15:59.99,17:69.99,18:69.99,19:54.99,20:99.00,22:59.99,24:59.99,25:79.99,26:49.99,28:73.80,30:34.99,33:60.00,34:84.99,35:119.00,36:159.80,37:199.99,38:79.99,41:59.99,44:89.99,49:69.99,50:69.99,53:89.99,54:179.99,56:69.99,59:149.99,61:119.99,62:59.99,65:99.99,67:191.80,68:179.80,78:67.80,80:89.99,81:34.99,83:129.99,85:69.99,88:89.99,90:49.99,92:149.99,96:39.99,97:119.99,99:54.99,100:79.99,102:130.00,103:79.99,106:58.99,108:25.99,112:59.99,114:79.99,116:99.00,117:99.99,119:49.99,120:119.00,125:59.00}
def cat(n,nome):
    l=nome.lower()
    if n in (56,120,62,37,61,125,109,54,3,92,36): return 'praia'
    if 'calcinha' not in l and any(k in l for k in ['biquíni','saída','pareô','maiô']): return 'praia'
    if any(k in l for k in ['fitness','macaquinho','cintura alta','t-shirt','zara']): return 'fitness'
    if any(k in l for k in ['cinta','bermuda','shorts','short skin','anágua']): return 'modeladores'
    if any(k in l for k in ['pijama','peluciado','camisola','baby-doll','robe','shortdoll']): return 'noite'
    return 'lingerie'
