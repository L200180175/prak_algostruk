def binary (kumpulan,target):
    low = 0
    high = len(kumpulan) -1
    listku = []

    while low <= high:
        if kumpulan [low] == target:
            listku.append(low)
            low += 1
        else:
            low += 1
    return listku


s = [2,3,5,6,6,6,8,9,9,10,11,12,13,14]
dicari = 6
print("Posisi data ", dicari, " pada list ", s, "adalah ",binary(s, dicari))
