#任意の文字列や文書を連続したn個の文字で分割するテキスト分割方法.
#特に,nが1の場合をuni-gram,2の場合をbi-gram,3の場合をtri-gramと呼ぶ.

def ngram(text,n):
    #n字数ごとずらす
    x=[]
    z=list(text)
    for y in range(len(z)):
        
        if y==len(z)-n+1:
           break;
        x.append(z[y:y+n])
    return x




a="I am an NLPer"

print("uni-gram",ngram(a,1))
print("bi-gram",ngram(a,2))
print("tri-gram",ngram(a,3))