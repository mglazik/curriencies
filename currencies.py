#!/bin/python
# -*- coding: utf-8 -*-

import argparse
import wget
import json
import os
import time
import datetime


parser = argparse.ArgumentParser()
parser.add_argument('kasa')
parser.add_argument('waluta1')
parser.add_argument('waluta2')
args = parser.parse_args()


if  os.path.isfile('tabela.txt'):
    print("")
else:
    wget.download("http://api.nbp.pl/api/exchangerates/tables/c/?format=json", out="tabela.txt", bar=0)
    print('\n POBIERAM PIERWSZĄ TABELĘ')

o = float(os.path.getctime("tabela.txt"))
n = float(time.time())


if n>o+43200: #12 godzin
    print ('POBIERAM NOWĄ TABELĘ')
    os.remove('tabela.txt')
    wget.download("http://api.nbp.pl/api/exchangerates/tables/c/?format=json", out="tabela.txt", bar=0)


t = open('tabela.txt', "r")
nbp = json.load(t)


def pobierz_waluta(v):
       return nbp[0]['rates'][v]['code']

def pobierz_buy(v1):
        return nbp[0]['rates'][v1]['bid']

def pobierz_sell(v2):
        return nbp[0]['rates'][v2]['ask']

#BID
buy = {'PLN': 1, 
        pobierz_waluta(0): pobierz_buy(0),
        pobierz_waluta(1): pobierz_buy(1),
        pobierz_waluta(2): pobierz_buy(2),
        pobierz_waluta(3): pobierz_buy(3),
        pobierz_waluta(4): pobierz_buy(4),
        pobierz_waluta(5): pobierz_buy(5),
        pobierz_waluta(6): pobierz_buy(6),
        pobierz_waluta(7): pobierz_buy(7),
        pobierz_waluta(8): pobierz_buy(8),
        pobierz_waluta(9): pobierz_buy(9),
        pobierz_waluta(10): pobierz_buy(10),
        pobierz_waluta(11): pobierz_buy(11),
        } 
#ASK
sell = {'PLN': 1,
        pobierz_waluta(0): pobierz_sell(0),
        pobierz_waluta(1): pobierz_sell(1),
        pobierz_waluta(2): pobierz_sell(2),
        pobierz_waluta(3): pobierz_sell(3),
        pobierz_waluta(4): pobierz_sell(4),
        pobierz_waluta(5): pobierz_sell(5),
        pobierz_waluta(6): pobierz_sell(6),
        pobierz_waluta(7): pobierz_sell(7),
        pobierz_waluta(8): pobierz_sell(8),
        pobierz_waluta(9): pobierz_sell(9),
        pobierz_waluta(10): pobierz_sell(10),
        pobierz_waluta(11): pobierz_sell(11),
        } 


try:
    a = float(args.kasa)
    b = buy[args.waluta1]
    c = sell[args.waluta2]
except:
    print('WPROWADŹ POPRAWNE DANE: \n Kwotę, oraz dwa oznaczenia waluty z listy dostępnych (case sensitive): \nPLN, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}. \n'.format(pobierz_waluta(0), pobierz_waluta(1), pobierz_waluta(2), pobierz_waluta(3), pobierz_waluta(4), pobierz_waluta(5), pobierz_waluta(6), pobierz_waluta(7), pobierz_waluta(8), pobierz_waluta(9), pobierz_waluta(10), pobierz_waluta(11)))
    exit()

kurs = round(c/b, 5)
wynik = round(a*b/c, 2)

print('\nKurs wymiany: ~', kurs)
print("\033[1m---------------------------------------\n   {} {} to {} {}   \n---------------------------------------\033[0;0m".format(args.kasa, args.waluta1, wynik, args. waluta2))
print('\nObsługiwane waluty: PLN, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}. \n'.format(pobierz_waluta(0), pobierz_waluta(1), pobierz_waluta(2), pobierz_waluta(3), pobierz_waluta(4), pobierz_waluta(5), pobierz_waluta(6), pobierz_waluta(7), pobierz_waluta(8), pobierz_waluta(9), pobierz_waluta(10), pobierz_waluta(11)))