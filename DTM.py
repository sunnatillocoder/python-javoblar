# Mening birinchi dasturim :) # 2023 - yil.

from tkinter import *

oyna = Tk()
oyna.title('DTM CALCULYATOR 2023')
oyna.geometry('350x350')

def ball():
	natija.config(text = 3.1 * int(t_javob.get()))

def ball2():
	natija.config(text = 2.1 * int(t_javob.get()))

def ball3():
	natija.config(text = 1.1 * int(t_javob.get()))

def umumiy():
	natija.config(text = ball.get() + ball2.get() + ball3.get())
	return natija2

t_javob = Entry()
t_javob.place(x = 40, y= 40, width = 280, height = 40)

tugma = Button(text = 'Matematika', fg = 'black', bg = 'green', command = ball)
tugma.place(x= 0, y = 310, width = 350, height =40)

tugma2 = Button(text = 'Fizika', fg = 'black', bg = 'green', command = ball2)
tugma2.place(x= 0, y = 250, width = 350, height =40)

tugma3 = Button(text = 'Majburiy', fg = 'black', bg = 'green', command = ball3)
tugma3.place(x= 0, y = 190, width = 350, height =40)


natija = Label(text = 'Natija', bg = 'green', fg = 'black')
natija.place(x = 220, y = 100, width=110, height = 40)


oyna.mainloop()