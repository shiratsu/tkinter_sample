import sys
import tkinter
import tkinter.messagebox


root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

#
# ボタンが押されるとここが呼び出される
#
def DeleteEntryValue(event):
  #エントリーの中身を削除
  # EditBox.delete(0, tkinter.END)

  value = EditBox.get()
  tkinter.messagebox.showinfo(title="テキストボックスの中身", message=value)



#エントリー
EditBox = tkinter.Entry(width=50)
EditBox.insert(tkinter.END,"挿入する文字列")
EditBox.pack()

#ボタン
Button = tkinter.Button(text=u'ボタンです', width=50)
Button.bind("<Button-1>",DeleteEntryValue) 
#左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
Button.pack()

root.mainloop()