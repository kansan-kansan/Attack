from cProfile import label
from tkinter import messagebox
import tkinter as tk
import sys
import time
import threading


def main():
    def click_btn():
        try:
            pas = entry.get()#パスを取得
            textbox.delete("1.0","end")#textbox内をクリア
            #print(type(pas))
            pas_int = int(pas)#int型に変換

            t1 = time.time()#探索「開始」の時間
            now_num = 0
            for i in range(1,sys.maxsize):#無限ループ
                amari_100000000 = i % 100000000 #1億ごと
                if amari_100000000 == 0:
                    now_num += 1
                    t2 = time.time()        #探索「終了」の時間
                    elapsed_time = t2 - t1      #実行時間の計測
                    elapsed_time_ = int(elapsed_time)       #実行時間を整数型に
                    hour = elapsed_time_ // 3600            #単位を時間に
                    min = elapsed_time_ // 60               #単位を分に
                    sec = elapsed_time % 60                 #単位を秒に
                    sec = round(sec, 2)                     #秒を小数第一位に
                    #表示するものをすべてstr型に
                    now_num_to_str = str(now_num)
                    hour_str = str(hour)
                    min_str = str(min)
                    sec_str = str(sec)
                    text = "現在{0}億突破しました。かかった時間は{1}時間{2}分{3}秒です。もう少しおまちください。".format(now_num_to_str,hour_str,min_str,sec_str)
                    textbox.insert("1.0",text)


                if i == pas_int:
                    #print(f"\nThis time the password is {pas_int}.(今回のパスワードは{pas}です。)")
                    #print('\npassword unlock.(パスワードを解除いたしました。)')
                    break
            t2 = time.time()        #探索「終了」の時間
            elapsed_time = t2 - t1      #実行時間の計測
            elapsed_time_ = int(elapsed_time)       #実行時間を整数型に
            hour = elapsed_time_ // 3600            #単位を時間に
            min = elapsed_time_ // 60               #単位を分に
            sec = elapsed_time % 60                 #単位を秒に
            sec = round(sec, 2)                     #秒を小数第一位に
            #表示するものをすべてstr型に
            hour_str = str(hour)
            min_str = str(min)
            sec_str = str(sec)
            """    print(type(pas))
            print(type(hour_str))
            print(type(min_str))
            print(type(sec_str))
            """
            text = "あなたのpasは{0}です。かかった時間は{1}時間{2}分{3}秒です。".format(pas,hour_str,min_str,sec_str)
            textbox.insert("2.0",text)#テキストボックスに出力   insertの引数がわからない
            entry.delete(0,tk.END)

        except ValueError:            
            messagebox.showinfo("Error","エラー正しい数字が入力されていません。もう一度やり直してください。")#テキストボックスに出力
    """
    def stop():
        global flg
        flg = False

    def start():
        thread = threading.Thread(target=count)
        thread.start()

    def count():
        global flg
        i = 0
        while 1:
            if flg == False:
                print("動作を途中停止します。")
                flg = True
                break
            else:
                print("カウント",i)
                time.sleep(2)
                i += 1
    """
    root = tk.Tk()#window作成
    root.title("Password list attack")#タイトル
    root.geometry("600x450")#winのサイズ
    root.configure(bg='#ffffa5')

    #ラベルの背景色文字色・・・foreground、fg
    la_1 = tk.Label(text='桁数が長いと実行時間がかかることがあります',foreground='#faf0e6',background='#778899')
    la_1.place(x=30, y=30)
    #約8桁で14秒
    #もしもの配置するとき用

    #la_4 = tk.Label(text='',foreground='#faf0e6',background='#778899')
    #la_4.place(x=30, y=130)        

    #la_5 = tk.Label(text='',foreground='#faf0e6',background='#778899')
    #la_5.place(x=30, y=130)        

    #la_6 = tk.Label(text='',foreground='#faf0e6',background='#778899')
    #la_6.place(x=30, y=130)        

    entry = tk.Entry(width=30,show="*")#パス入力欄作成
    entry.place(x=80,y=80)#設置

    button = tk.Button(text="実行",command=click_btn,foreground='#faf0e6',background='#778899')#ボタン作成
    button.place(x=40,y=80)#設置

    """
    btn2_stop = tk.Button(text="停止",command=stop)
    btn2_stop.grid(row=1,column=0)
    """
    textbox = tk.Text(root,width=30,height=15,font=("",12))#テキストボックス作成
    textbox.place(x=40,y=160)#設置

    la_2 = tk.Label(text='8桁(1億)で約15秒です。',foreground='#faf0e6',background='#778899')
    la_2.place(x=30, y=110)   

    a = tk.Label(text='1億(約15秒間隔)ごとにメッセージが出力されます。',foreground='#1b44c5',background='#bfda1e')
    a.place(x=30, y=130 )
    #txt_a = tk.Entry(width=20)
    #txt_a.place(x=90 ,y=140)

    root.mainloop()#ループ


if __name__ == "__main__":
    main()