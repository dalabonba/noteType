# from tkinter import *
import tkinter as tk   #兩種載入方式，如果用第2行這種的話，在使用tkinter套件的 函數/方法 時，前面就要加「tk.」。
                       # as tk 的tk也可以改成其他你想取的名字，也可以直接import tkinter就好，
                       #這樣的話在使用tkinter套件的 函數/方法 時，前面就要加「tkinter.」。

import sqlite3

# 新增資料庫
conn = sqlite3.connect('test.db') #連結現有資料庫。而如果程式放的資料夾沒有test.db這個檔案，這行程式就會就新增一個test.db檔案。

# 建立 cursor 物件
db = conn.cursor()




def select(): #select功能:將table1的資料放進變數data
    global data #將data設為全域變數
    data =[]
    for row in db.execute('SELECT * FROM table1'): #從table1資料表取得所有資料
        data.append(list(row))
    
    print('data=\n',data)
    
    

def delete(): #delete功能:刪除最後一筆資料
    s = len(data) #計算data有幾筆資料，將結果放進s
    db.execute(f'DELETE FROM table1 WHERE id={s};') #刪除資料庫的table1資料表的id=s的資料，也就是最後一筆資料。會刪除一整列的資料
    conn.commit() #進行資料庫檔案更新
    update() #執行update副程式:更新畫面



def update(): #update功能:更新畫面
    listbox1.delete(0,tk.END) #刪除listbox1從頭到尾顯示的資料!!!!!!!!!!!!!!!!!!!!!!!!!36~38行是我從delete裡面移過來的，這樣比較合理
    listbox2.delete(0,tk.END) #刪除listbox2從頭到尾顯示的資料
    listbox3.delete(0,tk.END) #刪除listbox3從頭到尾顯示的資料
    select() #執行select副程式:將table1的資料放進變數data
    for i in data: #將data的值一個一個取出來放進i
        print('i=',i)
        listbox1.insert(tk.END,i[1])#在listbox1最下面插入i[1]  (i裡面索引值為1的值)
        listbox2.insert(tk.END,i[2])
        listbox3.insert(tk.END,i[3])


def modify(): #modify功能:修改資料表的資料
    try: # try-except說明 https://pydoing.blogspot.com/2011/01/python-try.html  如果使用者沒有先點選listbox就按修改按鈕會在第51行發生例外情況:tuple index out of range，意思是我所指定的數組(tuple)的索引值(index)超過這個數組(tuple)的最大索引值
        selectIndex=listbox1.curselection() #listbox1.curselection()會以數組型態回傳listbox1被選中的單一資料或複數資料的索引值
        print(f'selectIndex原本是{type(selectIndex)}資料型別，{selectIndex}')
        selectIndex=selectIndex[0] #在後面加[0]可以取出其中的第一個值
        print(f'selectIndex[0]會變成是{type(selectIndex)}資料型別，{selectIndex}')
        selectIndex=selectIndex+1 #因為我的table1資料表裡的id是從1開始算，而這個取得的listbox最上面的第一個值的索引值是從0開始算，所以我要+1來讓他跟我table1資料表裡的id變一樣
        
        if entry1GetText.get()=="" or entry2GetText.get()=="" or entry3GetText.get()=="":
            tk.messagebox.showerror('警告', '所有輸入框都要填資料')
        else:
            print(f"第1個輸入框取得:{entry1GetText.get()}\n第2個輸入框取得:{entry2GetText.get()}\n第3個輸入框取得:{entry3GetText.get()}")
            
            db.execute(f'UPDATE table1 SET title = "{entry1GetText.get()}" WHERE id = {selectIndex}') # 重點!去看sqlite.py範例檔的PART5:修改資料表資料的部分。這幾行看不懂的來問我
            db.execute(f'UPDATE table1 SET content = "{entry2GetText.get()}" WHERE id = {selectIndex}')
            db.execute(f'UPDATE table1 SET remark = "{entry3GetText.get()}" WHERE id = {selectIndex}')
            conn.commit()
            update()
            
    except: #發生例外情況執行except裡的程式
        tk.messagebox.showerror('警告', '請在最左邊的listbox選擇要修改的資料列')
    


window = tk.Tk()
window.title("資料")

listbox1 = tk.Listbox(window)
listbox1.grid(row=0, column=0)#佈局方式我改用grid了，https://www.delftstack.com/zh-tw/tutorial/tkinter-tutorial/tkinter-geometry-managers/

listbox2 = tk.Listbox(window)
listbox2.grid(row=0, column=1)

listbox3 = tk.Listbox(window)
listbox3.grid(row=0, column=2)



# tkinter中的文本輸入框說明 https://shengyu7697.github.io/python-tkinter-entry/
entry1GetText = tk.StringVar()
entry1 = tk.Entry(window, textvariable=entry1GetText)
entry1.grid(row=1, column=0)

entry2GetText = tk.StringVar()
entry2 = tk.Entry(window, textvariable=entry2GetText)
entry2.grid(row=1, column=1)

entry3GetText = tk.StringVar()
entry3 = tk.Entry(window, textvariable=entry3GetText)
entry3.grid(row=1, column=2)



update()#執行update副程式:更新畫面
btn1 = tk.Button(window,text = '新增')
btn1.grid(row=2, column=3)

btn2 = tk.Button(window,text = '修改',command = modify)#按下按鈕執行modify副程式:修改資料表的資料
btn2.grid(row=3, column=3)

btn3 = tk.Button(window,text = '刪除',command = delete)#按下按鈕執行delete副程式:刪除最後一筆資料
btn3.grid(row=4, column=3)



window.mainloop()  #循環刷新視窗畫面

# 關閉資料庫
conn.close()