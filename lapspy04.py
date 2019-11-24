nama = []
nim = []
tugas = []
uts = []
uas = []
tanya = []

while True:
    in_nama = input("Nama : ")
    in_nim = input("Nim : ")
    in_tugas = int(input("Nilai Tugas : "))
    in_uts = int(input("Nilai UTS : "))
    in_uas = int(input("Nilai UAS : "))
    in_tanya = input("Tambah data(y/t)? ")
    nama.append(in_nama)
    nim.append(in_nim)
    tugas.append(in_tugas)
    uts.append(in_uts)
    uas.append(in_uas)
    tanya.append(in_tanya)
    if in_tanya == 't':
        break
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
    akhir = round(float(tugas[i]*0.3+uts[i]*0.35+uas[i]*0.35), 1)
    print("|  "+str(akhir),end="")
    for o in range(6-len(str(akhir))):
        print(" ",end="")
    print("|")
print("========================================================================")
