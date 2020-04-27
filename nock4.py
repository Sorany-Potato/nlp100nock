a="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
a=a.replace(",","")
a=a.replace(".","")
b=a.split()
#,.を抜いて文字列を単語に分ける
r=[1,5,6,7,8,9,15,16,19]
x={}
y=1

for c in b:
    for s in r:
        if y==s:
            w=c[0]
            
            x[w]=y
            break;
        
        elif s==r[-1]:
            w=c[:2]
            x[w]=y
    y+=1

print(x)
    