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
        button3 = Button(master=frontPage.root, text='Toon reisinformatie', bg='#212B5C',
                         font=('Helvetica', 23, 'bold'), command=lambda: frontPage.showInfoPage('UT'))
        button3.grid(row=2, column=0, pady=32)

        '''Station wijzigen button'''
        button4 = Button(master=frontPage.root, text='Station wijzigen', bg='#212B5C', activebackground='#212B5C',
                         font=('Helvetica', 23, 'bold'), command=frontPage.filterPage)
        button4.grid(row=3, column=0)

        frontPage.root.mainloop()

    def showInfoPage(stationCode):
        succes, res = ApiManager.getDeparturesForStation(stationCode)
        print(res)
        print(succes)
        print('BeepBoop')

    def stationFilter(letters: list):
        """Function for filtering station results"""
        returnDict = {}
        succes, res = ApiManager.getAllStations()  # Get all the stations
        if succes:
            for station in res:
                if station['land'] == 'NL':
                    for letter in letters:  # Check letters in station[0]
                        # print(station)
                        if station['namen']['lang'][0] == letter:
                            returnDict.update({station['namen']['lang']: station['code']})
                            break
            return returnDict
        else:
            return returnDict

    def filterPage():
        """Page with all the filterbuttons"""

        frontPage.root.columnconfigure(0, weight=0)

        'Filter button A - C'
        filterButton1 = Button(master=frontPage.root, text='A - C', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['A', 'B', 'C']))
        filterButton1.place(x=10, y=20)

        'Filter button D - F'
        filterButton2 = Button(master=frontPage.root, text='D - F', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['D', 'E', 'F']))
        filterButton2.place(x=10, y=90)

        'Filter button G - I'
        filterButton3 = Button(master=frontPage.root, text='G - I ', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['G', 'H', 'I']))
        filterButton3.place(x=10, y=160)

        'Filter button J - L'
        filterButton4 = Button(master=frontPage.root, text='J - L ', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['J', 'K', 'L']))
        filterButton4.place(x=10, y=240)

        'Filter button M - O'
        filterButton5 = Button(master=frontPage.root, text='M - O', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['M', 'N', 'O']))
        filterButton5.place(x=10, y=310)

        'Filter button P - R'
        filterButton6 = Button(master=frontPage.root, text='P - R ', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['P', 'Q', 'R']))
        filterButton6.place(x=10, y=380)

        'Filter button S - U'
        filterButton7 = Button(master=frontPage.root, text='S - U', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['S', 'T', 'U']))
        filterButton7.place(x=10, y=450)

        'Filter button V - X'
        filterButton8 = Button(master=frontPage.root, text='V - X', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['V', 'W', 'X']))
        filterButton8.place(x=10, y=520)

        'Filter button Y - Z'
        filterButton9 = Button(master=frontPage.root, text='Y - Z', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['Y', 'Z']))
        filterButton9.place(x=10, y=590)

        frontPage.root.mainloop()
