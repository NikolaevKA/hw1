

content=input("Введите данные строки для сохранения в файл: ")
content=content+"\n"
f=open("L5T1.txt", "w", encoding="utf-8")
f.write(content)
f.close

while content != "\n":
    content = input("Введите данные строки для сохранения в файл или оставьте строку пустой для завершения ввода: ")
    content = content + "\n"
    f = open("L5T1.txt", "a", encoding="utf-8")
    f.write(content)
    f.close