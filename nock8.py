def cipher(text):#文字列の英語小文字のみ暗号・複合化
    x=[]
    for a in range(0,len(text)):
        #1文字づつ繰り返し
        if text[a].islower():
            #islower()で文字列が小文字か判定
            x.append(chr(219-ord(text[a])))
            #TRUEなら暗号化
        else:
            x.append(text[a])
            #そうでない場合そのまま追加
    x="".join(x)
    #listを文字列に変換
    return x


s="私はsleepy"
x=cipher(s)
print(x)
y=cipher(x)
print(y)
