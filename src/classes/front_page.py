from managers.api_manager import ApiManager
from tkinter import *
from PIL import ImageTk, Image
import os
import datetime

class frontPage(object):
    dirPath = os.path.dirname(__file__)
    filePath = os.path.join(dirPath, '../images/ns-logo.jpg')

    def raiseFrame(_frame:Frame):
        _frame.tkraise()

    w = '1280'
    h = '720'

    root = Tk()
    mainScreen = Frame(root, width=w, height=h)
    filterScreen = Frame(root, width=w, height=h)
    travelInfoScreen = Frame(root, width=w, height=h)

    '''Default grootte van het scherm'''


    root.geometry('{}x{}'.format(w, h))
    for frame in (mainScreen, filterScreen, travelInfoScreen):
        frame.grid(row=0, column=0, sticky='news',)
        
    def __init__():
        '''Achtergrond kleur'''
# START MAIN SCREEN
        frontPage.mainScreen.configure(background='#FCC63F')

        '''Bovenste label 'welkom bij NS' '''
        label = Label(frontPage.mainScreen, text="Welkom bij NS", background='#FCC63F',
                        foreground='#212B5C',
                        font=('Helvetica', 16, 'bold italic'),
                        width=14,
                        height=3)

        label.grid(column=0, row=0)
        frontPage.mainScreen.columnconfigure(0, weight=1)

        '''Logo van NS'''
        img = ImageTk.PhotoImage(Image.open(frontPage.filePath))
        label2 = Label(frontPage.mainScreen, image=img)
        label2.grid(column=0, row=1)

        '''Reisinformatie button'''
        button3 = Button(frontPage.mainScreen, text='Toon reisinformatie', bg='#212B5C',
                            font=('Helvetica', 23, 'bold'), command=lambda:frontPage.showInfoPage('UT'))
        button3.grid(row=2, column=0, pady=32)

        '''Station wijzigen button'''
        button4 = Button(frontPage.mainScreen, text='Station wijzigen', bg='#212B5C', activebackground='#212B5C',
                            font=('Helvetica', 23, 'bold'), command=lambda: frontPage.raiseFrame(frontPage.filterScreen))
        button4.grid(row=3, column=0)

# START FILTER SCREEN
        """Page with all the filterbuttons"""
        frontPage.filterScreen.configure(background='#FCC63F')
        frontPage.filterScreen.columnconfigure(0, weight=0)

        filterBackButton = Button(master=frontPage.filterScreen, text='Terug', bg='#212B5C', font=('Helvetica', 10),command=lambda:frontPage.raiseFrame(frontPage.mainScreen))
        filterBackButton.grid(row=0,column=0)

        'Filter button A - C'
        filterButton1 = Button(master=frontPage.filterScreen, text='A - C', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['A', 'B', 'C'])).grid(row=1,column=1,padx=5,pady=5)

        'Filter button D - F'
        filterButton2 = Button(master=frontPage.filterScreen, text='D - F', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['D', 'E', 'F'])).grid(row=2,column=1,padx=5,pady=5)

        'Filter button G - I'
        filterButton3 = Button(master=frontPage.filterScreen, text='G - I ', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['G', 'H', 'I'])).grid(row=3,column=1,padx=5,pady=5)

        'Filter button J - L'
        filterButton4 = Button(master=frontPage.filterScreen, text='J - L ', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['J', 'K', 'L'])).grid(row=4,column=1,padx=5,pady=5)

        'Filter button M - O'
        filterButton5 = Button(master=frontPage.filterScreen, text='M - O', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['M', 'N', 'O'])).grid(row=5,column=1,padx=5,pady=5)

        'Filter button P - R'
        filterButton6 = Button(master=frontPage.filterScreen, text='P - R ', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['P', 'Q', 'R'])).grid(row=6,column=1,padx=5,pady=5)

        'Filter button S - U'
        filterButton7 = Button(master=frontPage.filterScreen, text='S - U', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['S', 'T', 'U'])).grid(row=7,column=1,padx=5,pady=5)

        'Filter button V - X'
        filterButton8 = Button(master=frontPage.filterScreen, text='V - X', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['V', 'W', 'X'])).grid(row=8,column=1,padx=5,pady=5)

        'Filter button Y - Z'
        filterButton9 = Button(master=frontPage.filterScreen, text='Y - Z', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['Y', 'Z'])).grid(row=9,column=1,padx=5,pady=5)

# START TRAVEL INFO SCREEN
        frontPage.travelInfoScreen.configure(background='#FCC63F')
        frontPage.travelInfoScreen.columnconfigure(0, weight=1)
        # label3_1 = Label(frontPage.travelInfoScreen, text="Ik ben roemer en ik hou van memes", background='#FCC63F',foreground='#212B5C',height=3,font=('', 16, 'bold')).pack()
        button3_1 = Button(master=frontPage.travelInfoScreen, text='Terug', bg='#212B5C', font=('Helvetica', 10),command=lambda:frontPage.raiseFrame(frontPage.mainScreen))
        button3_1.grid(row=0,column=0,pady=1)
        
# Raise main screen and initiate main gui loop
        frontPage.mainScreen.tkraise()
        frontPage.root.mainloop()


    def showInfoPage(stationCode):
        frontPage.raiseFrame(frontPage.travelInfoScreen)
        # succes, res = ApiManager.getDeparturesForStation(stationCode)
        # print(res)
        # print(succes)
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
            print(returnDict)
            # print(datetime.datetime.now())
            return returnDict
        else:
            # print(returnDict)
            # print(datetime.datetime.now())
            return returnDict