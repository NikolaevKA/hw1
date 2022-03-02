

with open("L5T2.txt", "r", encoding="utf-8") as f:
 content=f.read()
 mylist=list(content)
 print("Всего слов, включая предлоги:", mylist.count(' ')+mylist.count('\n'))
 print("Всего строк: ", mylist.count('\n'))

