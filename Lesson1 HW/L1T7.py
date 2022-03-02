startrun=int(input('Ведите стартовую производительность бегуна в день в километрах: '))
targetrun=int(input('Ведите целевую производительность бегуна в день в километрах: '))
i=0
realrun=startrun
while i<1000:
    i=i+1
    realrun=realrun*1.1
    if realrun>=targetrun:
        break
print(f"Необходимое количество тренировочных дней бегуна:",i)










