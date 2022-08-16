from tkinter import Button, Label
import random
import nustatymai
import ctypes
import sys
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('minesweeper.log')
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
file_handler.setFormatter(formatter)


class Laukelis:
    visi_mgt = []
    mgt_skaicius = nustatymai.langeliu_sk - nustatymai.minu_sk
    kiek_liko_langeliu = None
    def __init__(self, x, y, mina=False):
        self.atidaryta = False
        self.mina = mina
        self.mygtukas = None
        self.x = x
        self.y = y
        self.gal_mina = False
        Laukelis.visi_mgt.append(self)
        logger.info(f'Langeliu kurimas {self.x}, {self.y}')

    def sukurti_mygtuka(self, vieta):
        mgt = Button(vieta, width=7, height=3)
        mgt.bind('<Button-1>', self.kaire_pas)
        mgt.bind('<Button-3>', self.desne_pas)
        self.mygtukas = mgt

    @staticmethod
    def minu_sukurimas():
        minu_list = random.sample(Laukelis.visi_mgt, nustatymai.minu_sk)
        for mina in minu_list:
            mina.mina = True
        return minu_list
    @staticmethod
    def likusiu_skaicius(vieta):
        liko_langeliu = Label(vieta,
                      bg='black',
                      fg='white',
                      font=('', 30),
                      text=f'Liko langeliu:\n {Laukelis.mgt_skaicius}'
                      )
        Laukelis.kiek_liko_langeliu = liko_langeliu
    def kaire_pas(self, paspaudimas):
        if self.mina:
            self.sprogo_mina()
        else:
            if self.kiek_aplink_minu == 0:
                for mgt in self.aplink_paspausta:
                    mgt.atidaryti()
                    if mgt.atidaryti == 0:
                        mgt.atidaryti()
            self.atidaryti()
            if Laukelis.mgt_skaicius == 0:
                ctypes.windll.user32.MessageBoxW(0, 'Laimejote','Zaidimas baigtas', 0)

    def sprogo_mina(self):
        self.mygtukas.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'Pralaimejote', 'Zaidimas baigtas', 0)
        sys.exit()

    def mygtuko_paimimas(self, x, y):
        for mygtukas in Laukelis.visi_mgt:
            if mygtukas.x == x and mygtukas.y == y:
                return mygtukas

    @property
    def aplink_paspausta(self):
        mgt = [
            self.mygtuko_paimimas(self.x - 1, self.y - 1),
            self.mygtuko_paimimas(self.x - 1, self.y),
            self.mygtuko_paimimas(self.x - 1, self.y + 1),
            self.mygtuko_paimimas(self.x, self.y - 1),
            self.mygtuko_paimimas(self.x + 1, self.y - 1),
            self.mygtuko_paimimas(self.x + 1, self.y),
            self.mygtuko_paimimas(self.x + 1, self.y + 1),
            self.mygtuko_paimimas(self.x, self.y + 1)

        ]
        mgt = [x for x in mgt if x is not None]
        return mgt

    @property
    def kiek_aplink_minu(self):
        minos = 0
        for mgt in self.aplink_paspausta:
            if mgt.mina:
                minos += 1
        return minos

    def atidaryti(self):
        if not self.atidaryta:
            Laukelis.mgt_skaicius -= 1
            Laukelis.kiek_liko_langeliu.configure(text=f'Liko langeliu:\n {Laukelis.mgt_skaicius}')
            self.mygtukas.configure(text=self.kiek_aplink_minu)
        self.atidaryta = True


    def desne_pas(self, paspaudimas):
        if not self.gal_mina:
            self.mygtukas.configure(bg='green')
            self.gal_mina =True
        else:
            self.mygtukas.configure(bg='SystemButtonFace')
            self.gal_mina = False

    def __repr__(self):
        return f'({self.x}, {self.y})'
