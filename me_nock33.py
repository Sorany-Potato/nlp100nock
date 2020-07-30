'''
33. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
'''
#mecab -d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd
mecab_list = []
hit=''
hit2=''
with open('nekobrain.txt.mecab','r')as f:
    for line in f:
        if not line =='EOS\n':
            based=line.split('\t')
            other=based[1].split(',')
            Base=other[6]
            Pos=other[0]
            if Pos=='名詞' and hit2=='':
                hit=based[0]
            if Pos=='名詞' and hit2:
                mecab_list.append(hit+hit2+based[0])
                hit2=''
            else:
                hit2=''
            if Pos=='助詞' and Base=='の':
                hit2=based[0]
                
            



for result in mecab_list:
    print(result)



#'-d /usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd'