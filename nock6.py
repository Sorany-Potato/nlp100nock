import ngram
import list_subtraction

a="paraparaparadise"
b="paragraph"

x=sorted(set(ngram.ngram(a,2)))
y=sorted(set(ngram.ngram(b,2)))
print("x:",x)
print("y:",y)

w=x+y

""" 関数ngramの内容

def ngram(text,n):
    #n字数ごとずらす
    x=[]
    for y in range(len(text)):
        
        if y==len(text)-n+1:
           break;
        x.append(text[y:y+n])
    return x
"""
f=sorted(set(w))

#set型は重複しない要素（同じ値ではない要素、ユニークな要素）のコレクション
#しかし元の順序とは異なる
s=sorted(set(list_subtraction.list_subtraction(w,f)))
c=sorted(set(list_subtraction.list_subtraction(x,s)))
d=sorted(set(list_subtraction.list_subtraction(y,s)))
"""list1-list2の関数

def list_subtraction(list1,list2):
#リスト同士の引き算
    r=list1
    for a in list2:
        if a in r:
            r.remove(a)
    return r
"""
print("和集合：",f)
print("積集合：",s)
print("差集合x-y：",c)
print("差集合y-x：",d)

if 'se' in x:
    print("xに含まれる")
else:
    print("xに含まれない")
        
if 'se' in y:
    print("yに含まれる")
else:
    print("yに含まれない")