import tkinter as tk
from nl2sql import nl2sql
from db import db
import tkinter.messagebox

# GUI界面
window = tk.Tk()
window.title('自然语言查询接口')
window.geometry('1750x1250')
welcome = tk.Label(window, text='你好！欢迎使用自然语言查询接口', bg='white', font=('Arial', 18), width=30, height=2)
welcome.pack()
entry = tk.Entry(window, show=None, font=('Arial', 18))
entry.pack()
show_segments = tk.Text(window, height=2, width=50, font=('Arial', 15))
show_segments.place(x=470, y=100, anchor='nw')
show_sql = tk.Text(window, height=2, width=50, font=('Arial', 15))
show_sql.place(x=470, y=160)
show_result = tk.Text(window, height=3, width=50, font=('Arial', 15))
show_result.place(x=470, y=220)

def to_sql():
    raw = entry.get()
    seg = nl2sql.cut_words(raw)
    show_segments.insert('insert', '/'.join(seg))
    a = db.info()
    sql = nl2sql.nl2sql(seg, a)
    show_sql.insert('insert', sql)
    result = db.query(sql)
    show_result.insert('insert', result)
    if result:
        tkinter.messagebox.showinfo(title='成功', message='查询成功！')
    else:
        tkinter.messagebox.showerror(title='失败', message='查询失败！')


def clear():
    show_sql.delete('1.0', 'end')
    show_result.delete('1.0', 'end')
    show_segments.delete('1.0', 'end')


button1 = tk.Button(window, text='查询', font=('Arial', 15), width=8, height=1, command=to_sql)
button1.place(x=930, y=60)
button2 = tk.Button(window, text='清除', font=('Arial', 15), width=8, height=1, command=clear)
button2.place(x=1050, y=60)
l1 = tk.Label(window, text='请输入查询的对象:', bg='white', font=('Arial', 13), width=15, height=1)
l1.place(x=460, y=64)
l2 = tk.Label(window, text='分词结果:', bg='white', font=('Arial', 15), width=8, height=1)
l2.place(x=370, y=110)
l3 = tk.Label(window, text='SQL:', bg='white', font=('Arial', 15), width=8, height=1)
l3.place(x=370, y=172)
l4 = tk.Label(window, text='查询结果:', bg='white', font=('Arial', 15), width=8, height=1)
l4.place(x=370, y=230)
table1 = tk.PhotoImage(file="pic/交大社团.png")  # file：t图片路径
imgLabel = tk.Label(window, image=table1)  # 把图片整合到标签类中
imgLabel.place(x=420, y=300)
table2 = tk.PhotoImage(file="pic/选课.png")
imgLabel = tk.Label(window, image=table2)  # 把图片整合到标签类中
imgLabel.place(x=420, y=565)

window.mainloop()
