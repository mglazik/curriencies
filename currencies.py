#!/bin/python
# -*- coding: utf-8 -*-

import argparse
import wget
import json
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument('kasa')
parser.add_argument('waluta1')
parser.add_argument('waluta2')
args = parser.parse_args()

api_link = 'http://api.nbp.pl/api/exchangerates/tables/c/?format=json'
api_cur = 'tabela.txt'

if not os.path.isfile(api_cur): 
    wget.download(api_link, out=api_cur, bar=0)
    print('\n POBIERAM PIERWSZĄ TABELĘ')

old_file = float(os.path.getctime(api_cur))
new_file = float(time.time())

if new_file>old_file+43200: #12 godzin
    print ('POBIERAM NOWĄ TABELĘ')
    os.remove(api_cur)
    wget.download(api_link, out=api_cur, bar=0)

t = open(api_cur, "r")
nbp = json.load(t)

ilosc_walut = len(nbp[0]['rates'])

def pobierz_waluta(va):
       return nbp[0]['rates'][va]['code']

def pobierz_buy(va):
        return nbp[0]['rates'][va]['bid']

def pobierz_sell(va):
        return nbp[0]['rates'][va]['ask']

#BID
buytest = {'PLN':1,}

for va in range(ilosc_walut):
    buytest[pobierz_waluta(va)]= pobierz_buy(va)

#ASK
selltest = {'PLN':1,}

for va in range(ilosc_walut):
    selltest[pobierz_waluta(va)]= pobierz_sell(va)

try:
    a = float(args.kasa)
    b = buytest[args.waluta1]
    c = selltest[args.waluta2]
except:
    print('WPROWADŹ POPRAWNE DANE: \n Kwotę, oraz dwa oznaczenia waluty z listy dostępnych (case sensitive): ',*buytest, sep = ' ')
    exit()

kurs = round(c/b, 5)
wynik = round(a*b/c, 2)

print('\nKurs wymiany: ~', kurs)
print("\033[1m---------------------------------------\n   {} {} to {} {}   \n---------------------------------------\033[0;0m".format(args.kasa, args.waluta1, wynik, args. waluta2))
print('\nObsługiwane waluty:',*buytest, sep = ' ')