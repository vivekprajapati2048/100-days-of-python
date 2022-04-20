import tkinter

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I'm a label", font=("Arial", 24))
my_label.pack()



window.mainloop()


'''
References:
https://docs.python.org/3/library/tkinter.html#the-packer
https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
'''