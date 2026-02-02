def max_suma(arr):
    maks = akt = arr[0]
    for x in arr[1:]:
        akt = max(x, akt + x)
        maks = max(maks, akt)
    return maks

arr = [int(x) for x in input("podaj ciag: ").split()]
print(max_suma(arr))