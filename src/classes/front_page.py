from managers.api_manager import ApiManager
from tkinter import *
from PIL import ImageTk, Image
import os
import datetime


def showStationButtons(returnDict):
    # frameFilter = Frame
    if frontPage.filterScreen.winfo_children()[-1].winfo_children():
        lst = frontPage.filterScreen.winfo_children()[-1].grid_slaves()
        for item in lst:
            item.destroy()
    i = 1
    c = 0

    for station in returnDict:
        button = Button(master=frontPage.filterScreen.winfo_children()[-1], text=station, bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.showInfoPage(returnDict[station])).grid(row=i,column=c,padx=5,pady=5)
        i += 1
        if i == 10 or i == 20 or i == 30 or i == 40:
            c += 1
            i = 1

        # print(button)



class frontPage(object):
    dirPath = os.path.dirname(__file__)
    filePath = os.path.join(dirPath, '../images/ns-logo.jpg')

    def raiseFrame(_frame:Frame):
        _frame.tkraise()

    w = '1280'
    h = '720'

    root = Tk()
    root.state('zoomed')
    mainScreen = Frame(root, width=w, height=h)
    filterScreen = Frame(root, width=w, height=h)
    travelInfoScreen = Frame(root, width=w, height=h)

    '''Default grootte van het scherm'''

    root.geometry('{}x{}'.format(w, h))
    for frame in (mainScreen, filterScreen, travelInfoScreen):
        frame.grid(row=0, column=0, sticky='news')
        
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

        filterBackButton = Button(master=frontPage.filterScreen, text='Terug', bg='#212B5C',fg='#ffffff', font=('Helvetica', 10),command=lambda:frontPage.raiseFrame(frontPage.mainScreen))
        filterBackButton.grid(row=0,column=0)

        'Filter button A - C'
        filterButton1 = Button(master=frontPage.filterScreen, text='A - C', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['A', 'B', 'C'])).grid(row=1,column=1,padx=5,pady=5,sticky=W+E)

        'Filter button D - F'
        filterButton2 = Button(master=frontPage.filterScreen, text='D - F', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['D', 'E', 'F'])).grid(row=2,column=1,padx=5,pady=5,sticky=W+E)

        'Filter button G - I'
        filterButton3 = Button(master=frontPage.filterScreen, text='G - I ', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['G', 'H', 'I'])).grid(row=3,column=1,padx=5,pady=5,sticky=W+E)

        'Filter button J - L'
        filterButton4 = Button(master=frontPage.filterScreen, text='J - L ', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['J', 'K', 'L'])).grid(row=4,column=1,padx=5,pady=5,sticky=W+E)

        'Filter button M - O'
        filterButton5 = Button(master=frontPage.filterScreen, text='M - O', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['M', 'N', 'O'])).grid(row=5,column=1,padx=5,pady=5,sticky=W+E)

        'Filter button P - R'
        filterButton6 = Button(master=frontPage.filterScreen, text='P - R ', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['P', 'Q', 'R'])).grid(row=6,column=1,padx=5,pady=5,sticky=W+E)

        'Filter button S - U'
        filterButton7 = Button(master=frontPage.filterScreen, text='S - U', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['S', 'T', 'U'])).grid(row=7,column=1,padx=5,pady=5,sticky=W+E)

        'Filter button V - X'
        filterButton8 = Button(master=frontPage.filterScreen, text='V - X', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['V', 'W', 'X'])).grid(row=8,column=1,padx=5,pady=5,sticky=W+E)

        'Filter button Y - Z'
        filterButton9 = Button(master=frontPage.filterScreen, text='Y - Z', bg='#212B5C', font=('Helvetica', 23, 'bold'),command=lambda: frontPage.stationFilter(['Y', 'Z'])).grid(row=9,column=1,padx=5,pady=5,sticky=W+E)

        filterScreen2 = Frame(master=frontPage.filterScreen).grid(row=1,column=2,padx=5,pady=5,rowspan=10)


        print(filterScreen2)

# START TRAVEL INFO SCREEN
        frontPage.travelInfoScreen.configure(background='#FCC63F')
        frontPage.travelInfoScreen.columnconfigure(0, weight=1)
        # label3_1 = Label(frontPage.travelInfoScreen, text="Ik ben roemer en ik hou van memes", background='#FCC63F',foreground='#212B5C',height=3,font=('', 16, 'bold')).pack()
        button3_1 = Button(master=frontPage.travelInfoScreen, text='Terug',fg='#ffffff', bg='#212B5C', font=('Helvetica', 10),command=lambda:frontPage.raiseFrame(frontPage.mainScreen))
        # button3_1.grid(row=0,column=0,pady=1)
        button3_1.pack(side=TOP)
        
        logo = Label(master=frontPage.travelInfoScreen, text='vertrektijden', background='#FCC63F', foreground='dark blue',font=('Ariel', 30, 'bold'))
        logo.pack(side=TOP)
# Raise main screen and initiate main gui loop
        frontPage.mainScreen.tkraise()
        frontPage.root.mainloop()


    def showInfoPage(stationCode):
        frontPage.raiseFrame(frontPage.travelInfoScreen)
        succes, res = ApiManager.getDeparturesForStation(stationCode)
        print(res[0])
        print(succes)
        for train in res:
            group = Label(frontPage.travelInfoScreen, width=frontPage.w, height=1, bg='white')
            group.lower()

            tijden = Label(master=group, text=train["plannedDateTime"], background='white', foreground='dark blue', font=('Ariel', 24),
                        height=1)
            tijden.pack(side=LEFT)

            bestemming = Label(master=group, text=f'Bestemming: {train["direction"]}', background='white', foreground='dark blue',
                            font=('Ariel', 24, 'bold'), height=1)
            bestemming.pack(side=LEFT)

            spoor = Label(master=group, text=f'Spoor {train["plannedTrack"]}', background='white', foreground='red', font=('Ariel', 24), height=1)
            spoor.pack(side=RIGHT)

            soort = Label(master=group, text=train["trainCategory"], background='white', foreground='dark blue', font=('Ariel', 20),
                        height=1)
            soort.pack(side=LEFT)

            group.pack(side=TOP, fill=X)
        print('BeepBoop')

    def stationFilter(letters: list):
        """Function for filtering station results"""
        returnDict = {}
        succes, res = ApiManager.getAllStations()  # Get all the stations
        if succes:
            for station in res:
                if station['land'] == 'NL':
                    for letter in letters:  # Check letters in station[0]
                        if station['namen']['lang'][0] == letter:
                            returnDict.update({station['namen']['lang']: station['code']})
                            break
            showStationButtons(returnDict)
        else:
            frontPage.raiseFrame(frontPage.mainScreen)