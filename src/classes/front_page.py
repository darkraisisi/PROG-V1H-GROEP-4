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
        frontPage.root.configure(background='#FCC63F')

        'Filter button A - C'
        button1 = Button(master=frontPage.root, text='A - C', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['A', 'B', 'C']))
        button1.grid(row=0, column=0, pady=4)

        'Filter button D - F'
        button1 = Button(master=frontPage.root, text='D - F', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['D', 'E', 'F']))
        button1.grid(row=0, column=1, pady=4)

        'Filter button G - I'
        button1 = Button(master=frontPage.root, text='G - I', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['G', 'H', 'I']))
        button1.grid(row=0, column=2, pady=4)

        'Filter button J - L'
        button1 = Button(master=frontPage.root, text='J - L', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['J', 'K', 'L']))
        button1.grid(row=1, column=0, pady=4)

        'Filter button M - O'
        button1 = Button(master=frontPage.root, text='M - O', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['M', 'N', 'O']))
        button1.grid(row=1, column=1, pady=4)

        'Filter button P - R'
        button1 = Button(master=frontPage.root, text='P - R', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['P', 'Q', 'R']))
        button1.grid(row=1, column=2, pady=4)

        'Filter button S - U'
        button1 = Button(master=frontPage.root, text='S - U', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['S', 'T', 'U']))
        button1.grid(row=2, column=0, pady=4)

        'Filter button V - X'
        button1 = Button(master=frontPage.root, text='V - X', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['V', 'W', 'X']))
        button1.grid(row=2, column=1, pady=4)

        'Filter button Y - Z'
        button1 = Button(master=frontPage.root, text='Y - Z', bg='#212B5C', font=('Helvetica', 23, 'bold'),
                         command=lambda: frontPage.stationFilter(['Y', 'Z']))
        button1.grid(row=2, column=2, pady=4)

        frontPage.root.mainloop()
