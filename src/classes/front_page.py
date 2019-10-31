from managers.api_manager import ApiManager
from tkinter import *
from PIL import ImageTk, Image
import os

class frontPage(object):
    dirPath = os.path.dirname(__file__)
    filePath = os.path.join(dirPath, '../images/ns-logo.jpg')
    root = Tk()

    '''Default grootte van het scherm'''

    w = '1280'
    h = '720'
    root.geometry('{}x{}'.format(w, h))

    '''Achtergrond kleur'''
    def mainPage():
        print('lmao')
        frontPage.root.configure(background='#FCC63F')

        '''Bovenste label 'welkom bij NS' '''
        label = Label(frontPage.root, text="Welkom bij NS", background='#FCC63F',
                    foreground='#212B5C',
                    font=('Helvetica', 16, 'bold italic'),
                    width=14,
                    height=3)

        label.grid(column=0, row=0)
        frontPage.root.columnconfigure(0, weight=1)

        '''Logo van NS'''
        img = ImageTk.PhotoImage(Image.open(frontPage.filePath))
        label2 = Label(frontPage.root, image=img)
        label2.grid(column=0, row=1)

        '''Reisinformatie button'''
        button3 = Button(master=frontPage.root, text='Toon reisinformatie', bg='#212B5C',font=('Helvetica', 23, 'bold'), command = lambda : frontPage.showInfoPage('UT'))
        button3.grid(row=2, column=0, pady=32)

        frontPage.root.mainloop()

    def showInfoPage(stationCode):
        succes, res = ApiManager.getDeparturesForStation(stationCode)
        print(res)
        print(succes)
        print('BeepBoop')
        label2 = Label(frontPage.root, text='TESTING')