a="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
a = a.replace(";","")
a = a.replace(",","")
a = a.replace(".","")
#a内の;,.を除く（置き換え）
b = a.split( )
#空白で分割したものをbに収納
x=[]
#入れるためのリストの作成
for c in b:
    x.append(len(c))
#forでxのリストにlenで数えたものを1つづつ追加
#lenは要素数を表示する

print(x)