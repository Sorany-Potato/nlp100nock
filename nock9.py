import random
#random関数を使用するためimport
text="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

a=text.split( )
#aにtextを空白で分けたものをいれる
x=[]
#受け入れ先
for c in a:
    #aの中の単語の数だけ繰り返し
    if len(c) >= 5:
        #cに取り出した単語が5文字以上の場合
        z=c[1:-1]
        #zに初めと最後の単語を除いたものをいれる
        y=[]
        #random.shuffleを使うに文字列ではできないのでリストにいれる
        #for内で宣言しないと次の動作でyの中身が増えすぎて余計なものが混じるので繰り返し宣言しなおす
        for kl in range(len(z)):
            #リストyに一文字づついれる
            y.append(z[kl])
        random.shuffle(y)
        #初めと最後を除いたyがランダムに並べ替えられる
        w=c[0]+''.join(y)+c[-1]
        #yを文字列にして最初と最後の文字を追加したものをwにいれる
        x.append(w)
        #リストxに追加
    else:
        x.append(c)
        #4文字以下ならそのままxに追加

print(' '.join(x))
#文字列で表示

        
