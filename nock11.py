'''
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，
trコマンド，もしくはexpandコマンドを用いよ．
'''
#python3 nock11.py popular-names.txt
#コマンド：expand -t 1 popular-names.txt
#diff nock11w <(expand -t 1 popular-names.txt)
import sys
filename=sys.argv
with open(filename[1]) as f:
    ctxt=f.read()
    #ctxtに読みとったものをいれる
    ctxt=ctxt.replace("\t"," ")
    #replaceでctxtのtabをspaceに変換
with open('nock11w.txt', mode="w") as f1:
    f1.write(ctxt)
    #違うファイル名で保存。既存のファイル名ではない場合新規で作られる

