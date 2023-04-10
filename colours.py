from tkinter import *

class Colors(Tk):
    def __init__(self):
        super().__init__()
        self.title('Цвета')
        self.geometry("250x325")

        self.lbl = Label(text="", width=230)
        self.e1 = Entry(width=150, justify=CENTER)

        color_dic = {'#ff0000': 'Красный', '#ff7d00': 'Оранжевый', '#ffff00': 'Жёлтый', '#00ff00': 'Зелёный', '#007dff': 'Голубой', '#0000ff': 'Синий', '#7d00ff': 'Фиолетовый'}

        for colour in color_dic.keys():
            sa=lambda c=colour, ruc=color_dic[colour]: self.onclick(c, ruc)
            b = Button(text='', command=sa, bg=colour, width=50, height=2)
            self.lbl.pack()
            self.e1.pack()
            b.pack()
    
    def onclick(self, colour, ru_colour):
        self.e1.delete(0, END)
        self.e1.insert(0, colour)
        self.lbl['text'] = ru_colour

if __name__=='__main__':
    root = Colors()
    root.mainloop()