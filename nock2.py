a="パトカー"
b="タクシー"
y=[]
x=0
while True:
#常に繰り返す
    y.append(a[x])
    #aのx値目をyに追加
    y.append(b[x])
    #bのx値目をyに追加
    if a[x]==a[-1]:
        break;
    #aのx番目の値がaの最後の値と同じなら繰り返しを終了する
    x+=1
    #上の繰り返しの終了判定をしてからxを増やす

print(''.join(y))
#(''.join(y))でリストを文字列で表示
#joinは空白や記号を任意の文字に指定できる