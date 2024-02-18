import random

def encrypt_func(text):
    ############ データを格納するための空配列を生成 ############
    afterBin = []
    cryptList = []
    cryptSentence = []
    toSentence = []
    toKeySentence = []

    ############ 関数定義 ############
    def listXOR(argA, argB):
        for a,b in zip(argA, argB):
            A = int(a,2)
            B = int(b,2)
            cryptSentence.append(bin(int(A) ^ int(B)))

    def numXOR(argC, argD):
        C = int(argC,2)
        D = int(argD,2)
        return bin(int(C) ^ int(D))

    def checkNum(checkNumber,listNum):
        randomNumber = bin(random.randint(33,126))
        retake = bin(int(checkNumber,2) ^ int(int(randomNumber,2)))
        if int(retake,2) > 32 and int(retake,2) < 127:
            cryptSentence[listNum] = retake
            cryptList[listNum] = randomNumber
        else:
            checkNum(afterBin[k], listNum)

    def checkTail(checkTailNumber,listNum):
        randomNumber = bin(random.randint(33,126))
        retake = bin(int(checkTailNumber,2) ^ int(int(randomNumber,2)))
        if int(retake,2) == 32:
            checkTail(cryptSentence[listNum-1], listNum-1)
        else:
            cryptSentence[listNum] = retake
            cryptList[listNum] = randomNumber
    
    ############ 暗号化対象文章の取得 ############
    beforeBin = list(text)

    ############ 暗号化対象文章を10進数→2進数に変換する ############
    for i in beforeBin:
        afterBin.append((f'{ord(i):b}'.zfill(8)))

    ############ 暗号鍵を2進数で作成する ############
    listNum = len(afterBin)
    for j in range(listNum):
        cryptList.append(bin(random.randint(33,126)))

    ############ 暗号化対象文章と暗号鍵を使い排他的論理和を取得する ###########
    listXOR(afterBin, cryptList)

    ############ 排他的論理和がASCIIの範囲内(有効桁33-126)であることを確認する ###########
    ############ ASCIIの範囲外(有効桁33-126)である場合暗号鍵を修正する ###########
    k = 0
    for c in cryptSentence:
        if int(c,2) > 32 and int(c,2) < 127:
            k += 1
        else:
            checkNum(afterBin[k], k)
            k += 1

    ############ 排他的論理和の末尾がASCIIの半スペース（10進数：32及び2進数：00100000） ###########
    ############ 末尾がASCIIの半スペース(10進数：32及び2進数：00100000)である場合暗号鍵を修正する ###########
    if int(cryptSentence[listNum-1],2) == 32:
        checktail(cryptSentence[listNum-1], listNum-1)

    ############ 排他的論理和で計算した2進数を10進数に直し、ASCIIに変換し文字列を生成。変数に格納する ###########
    for e in cryptSentence:
        e = int(e,2)
        toSentence.append(chr(e))
    toSentence = "".join(toSentence)

    ############ 排他的論理和で計算した2進数を10進数に直し、ASCIIに変換し暗号鍵を生成。変数に格納する ###########
    for f in cryptList:
        f = int(f,2)
        toKeySentence.append(chr(f))
    toKeySentence = "".join(toKeySentence)

    return toSentence, toKeySentence