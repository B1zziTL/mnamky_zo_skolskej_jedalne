#vlozenie modulu
import tkinter

#nastavenie platna a jeho rozmerov
canvas = tkinter.Canvas(width=500, height=250) 
canvas.pack()

#napisy
canvas.create_text(250,50,font='Arial 30',text='VÝBER JEDLA')
canvas.create_text(250,240,font='Arial 10',text='kód študenta:')

#otvorenie suboru a prepisanie akychkolvek predoslych info
subor = open('zapisnik.txt', 'w', encoding='utf-8')

def stvorceky(): #funkcia na vykreslenie stvorcov
    #nejake premenne a zoznam
    listik = ['green','red','blue','orange']
    ii = 0
    x = 40
    y = 100

    #vykreslenie stvorcov
    for i in range(4):
        canvas.create_rectangle(x,y,x+100,y+100,fill=listik[ii],outline='')
        ii += 1
        x += 110

def klik_blik(suradnice): #funkcia na zapisanie dat do suboru
    #otvorenie suboru a dopisanie info do neho
    subor = open('zapisnik.txt', 'a', encoding='utf-8')

    #zistenie suradnic kliku a zistenie vstupu
    x = suradnice.x
    y = suradnice.y
    data = entry1.get()

    #podmienky potrebne na spravne zapisanie dat
    if len(entry1.get()) != 0:
        if x >= 40 and x <= 140:
            if y >= 100 and y <= 200:
                subor.write(data + ' z' + '\n')
        elif x >= 150 and x <= 250:
            if y >= 100 and y <= 200:
                subor.write(data + ' c' + '\n')
        elif x >= 260 and x <= 360:
            if y >= 100 and y <= 200:
                subor.write(data + ' m' + '\n')
        elif x >= 370 and x <= 470:
           if y >= 100 and y <= 200:
                subor.write(data + ' o' + '\n')

    #zatvorenie suboru             
    subor.close()

#privolanie funkcie
stvorceky()

#vytvorenie vstupu
entry1 = tkinter.Entry()
entry1.pack()

#nastavenie tlacidla mysky
canvas.bind('<Button-1>',klik_blik)

#zatvorenie suboru
subor.close()
