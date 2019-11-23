
print("""
========================================================================
| No |     Nama         |    NIM    |  Tugas  |  UTS  |  UAS  |  Akhir |
========================================================================""")

for i in range(len(nama)):
    print("|",i+1,end="")
    if i < 9 :
        print("  |", end="")
    else:
        print(" |", end="")
    print(" "+nama[i],end="")
    for j in range(17-len(nama[i])):
        print(" ",end="")
    print("|  "+nim[i],end="")
    for k in range(9-len(nim[i])):
        print(" ",end="")
    print("|  "+str(tugas[i]),end="")
    for l in range(7-len(str(tugas[i]))):
        print(" ",end="")
    print("|  "+str(uts[i]),end="")
    for m in range(5-len(str(uts[i]))):
        print(" ",end="")
    print("|  "+str(uas[i]),end="")
    for n in range(5-len(str(uas[i]))):
        print(" ",end="")
    akhir = round((tugas[i]+uts[i]+uas[i])/3, 1)
    print("|  "+str(akhir),end="")
    for o in range(6-len(str(akhir))):
        print(" ",end="")
    print("|")
print("========================================================================")
