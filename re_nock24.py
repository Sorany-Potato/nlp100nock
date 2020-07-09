'''
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
'''
# coding: utf-8
#python3 nock24.py
import re
file_pattern=r'.*?\[\[ファイル\:(.*?\..{3,4}?)(?:\|+?.*?\|?.*?\]\]|\]\])'
gallery_pattern='(.*?\..{3,}?)\|.*'
is_=''
with open('nock20w.txt') as f:
    for line in f:
        if '<gallery>' in line:
            is_ =True
        if '</gallery>' in line:
            is_ =False
            #-1をかけると+と-で判定できるという考え
        if  is_:
            result = re.findall(gallery_pattern, line)
            #judgeがあるときはgallery_pattern
        else:
            result = re.findall(file_pattern, line)
            #judgeがないときはfile_pattern
            #これでgalleryも抽出
        for x in result:
            print(x)

#|国章画像 = [[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]
#{{center|[[ファイル:United States Navy Band - God Save the Queen.ogg]]}}
"""
<gallery>
PalaceOfWestminsterAtNight.jpg|ウェストミンスター宮殿
Westminster Abbey - West Door.jpg|[[ウェストミンスター寺院]]
Edinburgh Cockburn St dsc06789.jpg|[[エディンバラ旧市街|エディンバラの旧市街]]・[[エディンバラ新市街|新市街]]
Canterbury Cathedral - Portal Nave Cross-spire.jpeg|[[カンタベリー大聖堂]]
Kew Gardens Palm House, London - July 2009.jpg|[[キューガーデン|キュー王立植物園]]
2005-06-27 - United Kingdom - England - London - Greenwich.jpg|[[グリニッジ|マリタイム・グリニッジ]]
Stonehenge2007 07 30.jpg|[[ストーンヘンジ]]
Yard2.jpg|[[ダラム城]]
Durham Kathedrale Nahaufnahme.jpg|[[ダラム大聖堂]]
Roman Baths in Bath Spa, England - July 2006.jpg|[[バース市街]]
Fountains Abbey view02 2005-08-27.jpg|[[ファウンテンズ修道院]]跡を含む[[スタッドリー王立公園]]
Blenheim Palace IMG 3673.JPG|[[ブレナム宮殿]]
Liverpool Pier Head by night.jpg|[[海商都市リヴァプール]]
Hadrian's Wall view near Greenhead.jpg|[[ローマ帝国の国境線]] ([[ハドリアヌスの長城]])
London Tower (1).JPG|[[ロンドン塔]]
</gallery>
"""