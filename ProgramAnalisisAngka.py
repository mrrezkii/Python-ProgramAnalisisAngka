def checkOddEven(num):                                                      # method checkOddEven dengan param num sebagai array
    isEven = 0                                                              # variable untuk counting genap
    isOdd = 0                                                               # variable untuk counting ganjil

    for i in num:                                                           # looping semua data di num
        if i % 2 == 0:                                                      # jika data hasil dibagi 2, maka
            isEven += 1                                                     # var isEven + 1
        else:                                                               # jika tidak
            isOdd += 1                                                      # var isOdd + 1

    return [isOdd, isEven]                                                  # mengembalikan nilai berupa array var isOdd dan isEven

def checkPrime(num):                                                        # method checkPrime dengan param num sebagai array
    isPrime = 0                                                             # variable untuk counting prime

    for i in num:                                                           # looping semua data di num
        if i > 1:                                                           # jika data num lebih dari 1, maka
            for j in range(2, i):                                           # looping data dari range 2 sampai data tersebut
                if (i % j) == 0:                                            # jika data num habis dibagi data dari looping data adalah 0, maka
                    break                                                   # berhentikan looping
            else:                                                           # jika tidak
                isPrime += 1                                                # var isPrime + 1
        else:                                                               # jika tidak
            pass                                                            # lewati

    return isPrime                                                          # return variable isPrime

if __name__ == "__main__":                                                  # method main

    isInput = input("Angka yang diinputkan \t : ")                          # input method main
    listInput = [int(i) for i in isInput]                                   # konversi inputan menjadi split dan bertype interger

    print("Jumlah bilangan genap \t : ", checkOddEven(listInput)[1])        # cetak beserta data even
    print("Jumlah bilangan ganjil \t : ", checkOddEven(listInput)[0])       # cetak beserta data odd
    print("Jumlah bilangan prima \t : ", checkPrime(listInput))             # cetak berserta data prime