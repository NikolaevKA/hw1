time=int(input('Введите промежуток времени в секундах: '))
#time=50
hrs=time//3600
min=time//60-hrs*60
sec=time-hrs*3600-min*60
if hrs<10:
    _hrs=0
else: _hrs=""
if min<10:
    _min=0
else: _min=""
if sec<10:
    _sec=0
else: _sec=""
print (f" {_hrs}{hrs} : {_min}{min} : {_sec}{sec}")



