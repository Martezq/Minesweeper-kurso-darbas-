from tkinter import *
from mygtukas import Laukelis
import nustatymai
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('minesweeper.log')
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)


langas = Tk(className='Minesweeper')
langas.configure(bg='black')
langas.geometry(f'{nustatymai.plotis}x{nustatymai.aukstis}')
langas.resizable(False, False)
icona = PhotoImage(file='mumu.png')
langas.iconphoto(False, icona)

virs_frame = Frame(langas, bg='black', width=nustatymai.plotis, height=nustatymai.aukscio_dalis(25))
soninis_frame = Frame(langas, bg='black', width=nustatymai.plocio_dalis(30), height=nustatymai.aukscio_dalis(75))
minu_frame = Frame(langas, bg='black', width=nustatymai.plocio_dalis(75), height=nustatymai.aukscio_dalis(75))
pavadinimas = Label(virs_frame, bg='black', fg='white', text='Minesweeper', font=('', 48))

pavadinimas.place(x=nustatymai.plocio_dalis(25), y=0)
virs_frame.place(x=0, y=0)
soninis_frame.place(x=0, y=nustatymai.aukscio_dalis(30))
minu_frame.place(x=nustatymai.plocio_dalis(30), y=nustatymai.aukscio_dalis(25))


for x in range(nustatymai.lauko_dydis):
    for y in range(nustatymai.lauko_dydis):
        myg = Laukelis(x, y)
        myg.sukurti_mygtuka(minu_frame)
        myg.mygtukas.grid(column=x, row=y)

Laukelis.likusiu_skaicius(soninis_frame)
Laukelis.kiek_liko_langeliu.place(x=0, y=0)
Laukelis.minu_sukurimas()
logger.info(f'minos {Laukelis.minu_sukurimas()}')
langas.mainloop()
