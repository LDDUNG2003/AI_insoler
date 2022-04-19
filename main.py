file = open("Book1.csv", mode="r", encoding="utf-8-sig")
save = open("num.csv", mode="w", encoding="utf-8-sig")

header = file.readline()
save.write(header.strip() + ",diem trung binh,học lực \n")

row = file.readline()
while row != "":
    row_list = row.split(",")

    math = float(row_list[2])
    lit = float(row_list[3])
    eng = float(row_list[4])

    ave = (math + lit + eng)/3
    ave = round(ave,1)
    rank = ""
    if ave >= 8.0:
        rank = "gioi"
    elif ave >= 6.5:
        rank = "kha"
    elif ave < 6.5 :
        rank = "trung binh"
    row_new = row.strip() + "," + str(ave) + "," + rank + "\n"
    print(row_new)
    save.write(row_new)
    row = file.readline()
