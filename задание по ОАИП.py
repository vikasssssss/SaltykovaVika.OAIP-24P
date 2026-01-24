
dan=[]
for i in range (5):
    a=input(f'напишите что-нибудь(макс {5-i} строк) ')
    dan.append(a)

with open("file.txt", "w", encoding="utf-8") as file:
    for line in dan:
        file.write(line + "\n")
with open("file.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())



