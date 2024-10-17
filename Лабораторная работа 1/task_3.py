# TODO Найдите количество книг, которое можно разместить на дискете

spacedisketa = 1.44 #mb
pages = 100
lines = 50
symbols = 25
symbolspace = 4 #byte

onebookspace = symbols*symbolspace*lines*pages
spacedisketa *=(2**20)
ammountbooks = spacedisketa//onebookspace

print("Количество книг, помещающихся на дискету:", int(ammountbooks))
