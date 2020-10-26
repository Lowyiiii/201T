import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,uic
import sqlite3

class Person(QMainWindow):
    def __init__(self):
        super(Person, self).__init__()
        uic.loadUi('personel.ui', self)
        self.personel = sqlite3.connect("201.db")
        self.c = self.personel.cursor()
        self.pushButton_3.clicked.connect(self.enter_data)
        # self.pushButton_5.clicked.connect(self.yegan_window)
        self.pushButton.clicked.connect(self.pezeshki_window)
        self.radioButton_3.toggled.connect(self.farzand_clicked)
        self.radioButton.toggled.connect(self.vaziyat_clicked)
        self.radioButton_9.toggled.connect(self.bimari)
        self.radioButton_5.toggled.connect(self.sazmani_clicked)
        self.radioButton_6.toggled.connect(self.shakhsi_clicked)
        self.radioButton_7.toggled.connect(self.mostajer_clicked)
        self.data = ""
        self.tahol = ""
        # self.


    def enter_data(self):
        daraje = self.lineEdit.text()
        fname =  self.lineEdit_2.text()
        lname =  self.lineEdit_3.text()
        personel_code = self.lineEdit_4.text()
        shenasname_number = self.lineEdit_5.text()
        code_meli = self.lineEdit_6.text()
        father = self.lineEdit_7.text()
        yegan = self.lineEdit_8.text()
        shoghle_amali = self.lineEdit_9.text()
        shoghle_sazmani = self.lineEdit_10.text()
        madrak = self.lineEdit_11.text()
        goroohe_khoon = self.lineEdit_12.text()
        ayele = self.lineEdit_18.text()
        address_qaz = self.lineEdit_22.text()
        address_other = self.lineEdit_23.text()
        mobile = self.lineEdit_24.text()
        home = self.lineEdit_25.text()
        own_hekmat_num = self.lineEdit_26.text()
        own_hekmat_card = self.lineEdit_27.text()
        own_sepah_num = self.lineEdit_28.text()
        own_sepah_card = self.lineEdit_29.text()
        wife_hekmat_num = self.lineEdit_30.text()
        wife_hekmat_card = self.lineEdit_31.text()
        fname_hamsar = self.lineEdit_13.text()
        lname_hamsar = self.lineEdit_14.text()
        shenasname_hamsar = self.lineEdit_15.text()
        code_meli_hamsar = self.lineEdit_16.text()
        birthday_hamsar =  self.lineEdit_17.text()
        daraje = self.lineEdit.text()
        fname =  self.lineEdit_2.text()
        lname =  self.lineEdit_3.text()
        personel_code = self.lineEdit_4.text()
        shenasname_number = self.lineEdit_5.text()
        code_meli = self.lineEdit_6.text()
        father = self.lineEdit_7.text()
        yegan = self.lineEdit_8.text()
        shoghle_amali = self.lineEdit_9.text()
        shoghle_sazmani = self.lineEdit_10.text()
        madrak = self.lineEdit_11.text()
        goroohe_khoon = self.lineEdit_12.text()
        ayele = self.lineEdit_18.text()
        address_qaz = self.lineEdit_22.text()
        address_other = self.lineEdit_23.text()
        mobile = self.lineEdit_24.text()
        home = self.lineEdit_25.text()
        own_hekmat_num = self.lineEdit_26.text()
        own_hekmat_card = self.lineEdit_27.text()
        own_sepah_num = self.lineEdit_28.text()
        own_sepah_card = self.lineEdit_29.text()
        wife_hekmat_num = self.lineEdit_30.text()
        wife_hekmat_card = self.lineEdit_31.text()
        fname_hamsar = self.lineEdit_13.text()
        lname_hamsar = self.lineEdit_14.text()
        shenasname_hamsar = self.lineEdit_15.text()
        code_meli_hamsar = self.lineEdit_16.text()
        birthday_hamsar =  self.lineEdit_17.text()


        query_personel='''INSERT into personel(daraje,fname,lname,personel_code,shenasname_number,code_meli,
        father,yegan,shoghle_amali,shoghle_sazmani,madrak,gorohe_khoon,ayele,arzyabi96,arzyabi97,arzyabi98,
        address_qaz,address_other,mobile,home,own_hekmat_num,own_hekmat_card,own_sepah_num,own_sepah_card,wife_hekmat_num,wife_hekmat_card,manzel) 
        values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'''\
            .format(daraje,fname,lname,personel_code,shenasname_number,code_meli,father,yegan,shoghle_amali,shoghle_sazmani,madrak,goroohe_khoon,
                    ayele,address_qaz,address_other,mobile,home,own_hekmat_num,own_hekmat_card,
                    own_sepah_num,own_sepah_card,wife_hekmat_num,wife_hekmat_card,self.data)
        self.c.execute(query_personel)
        self.personel.commit()
        query_hamsar = '''INSERT into hamsar(personel_code,fname,lname,shenasname_number,code_meli,birthday) 
        values("{}","{}","{}","{}","{}","{}")'''.format(personel_code,fname_hamsar,lname_hamsar,shenasname_hamsar,code_meli_hamsar,birthday_hamsar)
        self.c.execute(query_hamsar)
        self.personel.commit()
        # self.c.close()
        # self.personel.close()


        query_personel='''INSERT into personel(daraje,fname,lname,personel_code,shenasname_number,code_meli,
        father,yegan,shoghle_amali,shoghle_sazmani,madrak,gorohe_khoon,ayele,arzyabi96,arzyabi97,arzyabi98,
        address_qaz,address_other,mobile,home,own_hekmat_num,own_hekmat_card,own_sepah_num,own_sepah_card,wife_hekmat_num,wife_hekmat_card,manzel) 
        values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'''\
            .format(daraje,fname,lname,personel_code,shenasname_number,code_meli,father,yegan,shoghle_amali,shoghle_sazmani,madrak,goroohe_khoon,
                    ayele,address_qaz,address_other,mobile,home,own_hekmat_num,own_hekmat_card,
                    own_sepah_num,own_sepah_card,wife_hekmat_num,wife_hekmat_card,self.data)
        self.c.execute(query_personel)
        self.personel.commit()
        query_hamsar = '''INSERT into hamsar(personel_code,fname,lname,shenasname_number,code_meli,birthday) 
        values("{}","{}","{}","{}","{}","{}")'''.format(personel_code,fname_hamsar,lname_hamsar,shenasname_hamsar,code_meli_hamsar,birthday_hamsar)
        self.c.execute(query_hamsar)
        self.personel.commit()
        # self.c.close()
        # self.personel.close()



    def changed_window(self):
        self.farzand = Farzand()
        self.farzand.show()

    def yegan_window(self):
        self.yegan = Yegan()
        self.yegan.show()

    def pezeshki_window(self):
        self.pezeshki = Pezeshki()
        self.pezeshki.show()

    def farzand_clicked(self,enabled):
        if enabled:
            self.changed_window()

    def vaziyat_clicked(self,enabled):
        if enabled:
            self.radioButton.setChecked(True)
            self.lineEdit_13.setDisabled(True)
            self.lineEdit_14.setDisabled(True)
            self.lineEdit_15.setDisabled(True)
            self.lineEdit_16.setDisabled(True)
            self.lineEdit_17.setDisabled(True)
        if not enabled:
            self.lineEdit_13.setDisabled(False)
            self.lineEdit_14.setDisabled(False)
            self.lineEdit_15.setDisabled(False)
            self.lineEdit_16.setDisabled(False)
            self.lineEdit_17.setDisabled(False)

    def bimari(self,enabled):
        if enabled:
            self.radioButton_10.setDisabled(True)
            self.radioButton_11.setDisabled(True)
            self.pushButton.setDisabled(True)
        if not enabled:

            self.radioButton_10.setDisabled(False)
            self.radioButton_11.setDisabled(False)
            self.pushButton.setDisabled(False)
    def sazmani_clicked(self,enabled):
        if enabled:
            self.data = self.radioButton_5.text()
            print(self.data)
            return self.data

    def shakhsi_clicked(self,enabled):
        if enabled:
            self.data = self.radioButton_6.text()
            print(self.data)
            return self.data
    def mostajer_clicked(self,enabled):
        if enabled:
            self.data = self.radioButton_7.text()
            print(self.data)
            return self.data

    def mojarad_clicked(self,enabled):
        if enabled:
            self.data = self.radioButton.text()
            print(self.data)
            return self.data

    def moteahel_clicked(self,enabled):
        if enabled:
            self.data = self.radioButton_5.text()
            print(self.data)
            return self.data
class Search(QMainWindow):
    def __init__(self):
        super(Search, self).__init__()
        uic.loadUi('search.ui',self)
        self.pushButton.clicked.connect(self.Personel_search)
        self.show()

    def Personel_search(self):
        self.personel_search = Personel_search()
        self.personel_search.show()


class Nahast(QMainWindow):
    def __init__(self):
        super(Nahast, self).__init__()
        self.nahast = sqlite3.connect("201.db")
        self.c = self.nahast.cursor()
        uic.loadUi('nahast.ui',self)
        self.pushButton.clicked.connect(self.enter_data)
        self.show()

    def enter_data(self):

        personel_code = self.lineEdit.text()
        start_date = self.lineEdit_2.text()
        end_date = self.lineEdit_3.text()
        marhale = self.lineEdit_4.text()
        letter_no = self.lineEdit_5.text()

        query_nahast = '''INSERT into nahast(personel_code,start_date,end_date,marhale,letter_no) 
        values("{}","{}","{}","{}","{}")''' \
            .format(personel_code, start_date, end_date, marhale, letter_no)
        self.c.execute(query_nahast)
        self.nahast.commit()

class Tashvigh(QMainWindow):
    def __init__(self):
        super(Tashvigh, self).__init__()
        self.tashvigh = sqlite3.connect("201.db")
        self.c = self.tashvigh.cursor()
        uic.loadUi('tashvigh.ui',self)
        self.pushButton.clicked.connect(self.enter_data)
        self.show()
    def enter_data(self):

        personel_code = self.lineEdit.text()
        date = self.lineEdit_2.text()
        elat = self.lineEdit_3.text()
        type = self.lineEdit_4.text()
        letter_no = self.lineEdit_5.text()

        query_tashvigh = '''INSERT into tashvigh(personel_code,date,elat,type,letter_no) 
        values("{}","{}","{}","{}","{}")''' \
            .format(personel_code, date, elat, type, letter_no)
        self.c.execute(query_tashvigh)
        self.tashvigh.commit()

class Tanbih(QMainWindow):
    def __init__(self):
        super(Tanbih, self).__init__()
        self.tanbih = sqlite3.connect("201.db")
        self.c = self.tanbih.cursor()
        uic.loadUi('tanbih.ui',self)
        self.pushButton.clicked.connect(self.enter_data)
        self.show()


    def enter_data(self):

        personel_code = self.lineEdit.text()
        date = self.lineEdit_2.text()
        elat = self.lineEdit_3.text()
        type = self.lineEdit_4.text()
        letter_no = self.lineEdit_5.text()

        query_tanbih = '''INSERT into tanbih(personel_code,date,elat,type,letter_no) 
        values("{}","{}","{}","{}","{}")''' \
            .format(personel_code, date, elat, type, letter_no)
        self.c.execute(query_tanbih)
        self.tanbih.commit()

class Tashilat(QMainWindow):
    def __init__(self):
        super(Tashilat, self).__init__()
        self.tashilat = sqlite3.connect("201.db")
        self.c = self.tashilat.cursor()
        uic.loadUi('tashilat.ui', self)
        self.pushButton.clicked.connect(self.enter_data)
        self.show()

    def enter_data(self):

        personel_code = self.lineEdit.text()
        date = self.lineEdit_2.text()
        mablagh = self.lineEdit_3.text()

        query_tashilat = '''INSERT into tashilat(personel_code,date,mablagh) 
        values("{}","{}","{}")''' \
            .format(personel_code, date, mablagh)
        self.c.execute(query_tashilat)
        self.tashilat.commit()


class Farzand(QMainWindow):
    def __init__(self):
        super(Farzand, self).__init__()
        self.farzandan = sqlite3.connect("201.db")
        self.c = self.farzandan.cursor()
        uic.loadUi('farzandan.ui',self)
        self.pushButton.clicked.connect(self.enter_data)
        self.show()

    def enter_data(self):

        personel_code = self.lineEdit.text()
        fname = self.lineEdit_2.text()
        lname = self.lineEdit_3.text()
        shenasname_number = self.lineEdit_4.text()
        code_meli = self.lineEdit_5.text()
        birthday = self.lineEdit_6.text()

        query_farzandan = '''INSERT into farzandan(personel_code,fname,lname,shenasname_number,code_meli,birthday) 
        values("{}","{}","{}","{}","{}","{}")''' \
            .format(personel_code, fname, lname, shenasname_number, code_meli,birthday)
        self.c.execute(query_farzandan)
        self.farzandan.commit()



class Pezeshki(QMainWindow):
    def __init__(self):
        super(Pezeshki, self).__init__()
        self.pezeshki = sqlite3.connect("201.db")
        self.c = self.pezeshki.cursor()
        uic.loadUi('pezeshki.ui',self)
        self.pushButton.clicked.connect(self.enter_data)
        self.show()


    def enter_data(self):

        personel_code = self.lineEdit.text()
        tabaghe = self.lineEdit_2.text()
        date = self.lineEdit_3.text()


        query_pezeshki = '''INSERT into pezeshki(personel_code,tabaghe,date) 
        values("{}","{}","{}")''' \
            .format(personel_code, tabaghe, date)
        self.c.execute(query_pezeshki)
        self.pezeshki.commit()

class Personel_search(QMainWindow):
    def __init__(self):

        super(Personel_search, self).__init__()
        self.personel_search_info_sql = sqlite3.connect("201.db")
        self.c = self.personel_search_info_sql.cursor()
        uic.loadUi('personel_search.ui',self)
        # self.pushButton.clicked.connect(self.search_info_window)
        self.pushButton.clicked.connect(self.passing_information)
        # self.show()
        self.personel_search_info = Personel_search_info()
    def search_info_window(self):
        self.search_info = Personel_search_info()
        self.search_info.show()

    def passing_information(self):
        pcode = self.lineEdit.text()
        query_pcode = '''SELECT * from personel WHERE personel_code = %s'''% ''.join(str(pcode))
        query_farzandan = '''SELECT * from farzandan WHERE personel_code = %s'''% ''.join(str(pcode))
        query_hamsar =  '''SELECT * from hamsar WHERE personel_code = %s'''% ''.join(str(pcode))
        query_nahast =  '''SELECT * from nahast WHERE personel_code = %s'''% ''.join(str(pcode))
        query_pezeshki =  '''SELECT * from pezeshki WHERE personel_code = %s'''% ''.join(str(pcode))
        query_tanbih =  '''SELECT * from tanbih WHERE personel_code = %s'''% ''.join(str(pcode))
        query_tashilat =  '''SELECT * from tashilat WHERE personel_code = %s'''% ''.join(str(pcode))
        query_tashvigh =  '''SELECT * from tashvigh WHERE personel_code = %s'''% ''.join(str(pcode))

        # self.c.execute(query_pcode)
        daraje_query = '''SELECT daraje from personel WHERE personel_code = %s'''% ''.join(str(pcode))
        self.c.execute(daraje_query)
        daraje = self.c.fetchone()[0]
        print(daraje)
        self.personel_search_info_sql.commit()

        fname_query = '''SELECT fname from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(fname_query)
        fname = self.c.fetchone()[0]
        print(fname)
        self.personel_search_info_sql.commit()

        lname_query = '''SELECT lname from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(lname_query)
        lname = self.c.fetchone()[0]
        print(lname)
        self.personel_search_info_sql.commit()

        personel_code_query = '''SELECT personel_code from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(personel_code_query)
        personel_code = self.c.fetchone()[0]
        print(personel_code)
        self.personel_search_info_sql.commit()

        shenasname_number_query = '''SELECT shenasname_number from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(shenasname_number_query)
        shenasname_number = self.c.fetchone()[0]
        print(shenasname_number)
        self.personel_search_info_sql.commit()

        code_meli_query = '''SELECT code_meli from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(code_meli_query)
        code_meli = self.c.fetchone()[0]
        print(code_meli)
        self.personel_search_info_sql.commit()

        father_query = '''SELECT father from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(father_query)
        father = self.c.fetchone()[0]
        print(father)
        self.personel_search_info_sql.commit()

        yegan_query = '''SELECT daraje from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(yegan_query)
        yegan = self.c.fetchone()[0]
        print(yegan)
        self.personel_search_info_sql.commit()

        shoghle_amali_query = '''SELECT shoghle_amali from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(shoghle_amali_query)
        shoghle_amali = self.c.fetchone()[0]
        print(shoghle_amali)
        self.personel_search_info_sql.commit()

        shoghle_sazmani_query = '''SELECT shoghle_sazmani from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(shoghle_sazmani_query)
        shoghle_sazmani = self.c.fetchone()[0]
        print(shoghle_sazmani)
        self.personel_search_info_sql.commit()

        madrak_query = '''SELECT madrak from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(madrak_query)
        madrak = self.c.fetchone()[0]
        print(madrak)
        self.personel_search_info_sql.commit()

        gorohe_khoon_query = '''SELECT gorohe_khoon from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(gorohe_khoon_query)
        gorohe_khoon = self.c.fetchone()[0]
        print(gorohe_khoon)
        self.personel_search_info_sql.commit()

        ayele_query = '''SELECT ayele from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(ayele_query)
        ayele = self.c.fetchone()[0]
        print(ayele)
        self.personel_search_info_sql.commit()

        arzyabi96_query = '''SELECT arzyabi96 from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(arzyabi96_query)
        arzyabi96 = self.c.fetchone()[0]
        print(arzyabi96)
        self.personel_search_info_sql.commit()

        arzyabi97_query = '''SELECT arzyabi97 from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(arzyabi97_query)
        arzyabi97 = self.c.fetchone()[0]
        print(arzyabi97)
        self.personel_search_info_sql.commit()

        arzyabi98_query = '''SELECT daraje from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(arzyabi98_query)
        arzyabi98 = self.c.fetchone()[0]
        print(arzyabi98)
        self.personel_search_info_sql.commit()

        address_qaz_query = '''SELECT address_qaz from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(address_qaz_query)
        address_qaz = self.c.fetchone()[0]
        print(address_qaz)
        self.personel_search_info_sql.commit()

        address_other_query = '''SELECT daraje from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(address_other_query)
        address_other = self.c.fetchone()[0]
        print(address_other)
        self.personel_search_info_sql.commit()

        mobile_query = '''SELECT mobile from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(mobile_query)
        mobile = self.c.fetchone()[0]
        print(mobile)
        self.personel_search_info_sql.commit()

        home_query = '''SELECT home from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(home_query)
        home = self.c.fetchone()[0]
        print(home)
        self.personel_search_info_sql.commit()

        own_hekmat_num_query = '''SELECT own_hekmat_num from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(own_hekmat_num_query)
        own_hekmat_num = self.c.fetchone()[0]
        print(own_hekmat_num)
        self.personel_search_info_sql.commit()

        own_hekmat_card_query = '''SELECT own_hekmat_card from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(own_hekmat_card_query)
        own_hekmat_card = self.c.fetchone()[0]
        print(own_hekmat_card)
        self.personel_search_info_sql.commit()

        own_sepah_num_query = '''SELECT own_sepah_num from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(own_sepah_num_query)
        own_sepah_num = self.c.fetchone()[0]
        print(own_sepah_num)
        self.personel_search_info_sql.commit()

        own_sepah_card_query = '''SELECT own_hekmat_num from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(own_sepah_card_query)
        own_sepah_card = self.c.fetchone()[0]
        print(own_sepah_card)
        self.personel_search_info_sql.commit()

        wife_hekmat_num_query = '''SELECT wife_hekmat_num from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(wife_hekmat_num_query)
        wife_hekmat_num = self.c.fetchone()[0]
        print(wife_hekmat_num)
        self.personel_search_info_sql.commit()

        wife_hekmat_card_query = '''SELECT wife_hekmat_card from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(wife_hekmat_card_query)
        wife_hekmat_card = self.c.fetchone()[0]
        print(wife_hekmat_card)
        self.personel_search_info_sql.commit()

        manzel_query = '''SELECT manzel from personel WHERE personel_code = %s''' % ''.join(str(pcode))
        self.c.execute(manzel_query)
        manzel = self.c.fetchone()[0]
        print(manzel)
        self.personel_search_info_sql.commit()

        # self.personel_search_info_sql.commit()
        # self.c.execute(query_farzandan)
        # self.personel_search_info_sql.commit()
        # self.c.execute(query_hamsar)
        # self.personel_search_info_sql.commit()
        # self.c.execute(query_nahast)
        # self.personel_search_info_sql.commit()
        # self.c.execute(query_pezeshki)
        # self.personel_search_info_sql.commit()
        # self.c.execute(query_tanbih)
        # self.personel_search_info_sql.commit()
        # self.c.execute(query_tashilat)
        # self.personel_search_info_sql.commit()
        # self.c.execute(query_tashvigh)
        # self.personel_search_info_sql.commit()

        self.personel_search_info.label_3.setText(daraje)
        self.personel_search_info.label_5.setText(fname)
        self.personel_search_info.label_7.setText(lname)
        self.personel_search_info.label_9.setText(personel_code)
        self.personel_search_info.label_11.setText(code_meli)
        self.personel_search_info.label_27.setText(shenasname_number)
        self.personel_search_info.label_13.setText(father)
        self.personel_search_info.label_15.setText(yegan)
        self.personel_search_info.label_17.setText(shoghle_amali)
        self.personel_search_info.label_19.setText(shoghle_sazmani)
        self.personel_search_info.label_23.setText(gorohe_khoon)
        self.personel_search_info.label_21.setText(madrak)
        self.personel_search_info.label_663.setText(ayele)
        self.personel_search_info.label_664.setText(manzel)
        self.personel_search_info.label_661.setText(arzyabi96)
        self.personel_search_info.label_657.setText(arzyabi97)
        self.personel_search_info.label_660.setText(arzyabi98)
        self.personel_search_info.label_696.setText(own_hekmat_num)
        self.personel_search_info.label_705.setText(own_hekmat_card)
        self.personel_search_info.label_698.setText(own_sepah_num)
        self.personel_search_info.label_700.setText(own_sepah_card)
        self.personel_search_info.label_704.setText(wife_hekmat_num)
        self.personel_search_info.label_703.setText(wife_hekmat_card)
        self.personel_search_info.label_715.setText(mobile)
        self.personel_search_info.label_712.setText(home)
        self.personel_search_info.label_708.setText(address_qaz)
        self.personel_search_info.label_714.setText(address_other)

        self.personel_search_info.display_info()


class Personel_search_info(QMainWindow):
    def __init__(self):
        super(Personel_search_info, self).__init__()
        uic.loadUi('personel_search_info_scroll.ui',self)
        self.setFixedWidth(800)
        self.setFixedHeight(680)
        # self.show()

    def display_info(self):
        self.show()


class Yegan(QMainWindow):
    def __init__(self):
        super(Yegan, self).__init__()
        self.yegan = sqlite3.connect("201.db")
        self.c = self.yegan.cursor()
        uic.loadUi('yegan.ui',self)
        self.pushButton.clicked.connect(self.enter_data)
        self.show()

    def enter_data(self):
        personel_code = self.lineEdit_2.text()
        yegan = self.lineEdit.text()
        query_yegan = '''INSERT into yegan(personel_code,yegan) 
        values("{}","{}")''' \
            .format(personel_code, yegan)
        self.c.execute(query_yegan)
        self.yegan.commit()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('main.ui',self)
        self.pushButton.clicked.connect(self.person_window)
        self.pushButton_2.clicked.connect(self.search_window)
        self.pushButton_3.clicked.connect(self.nahast_window)
        self.pushButton_4.clicked.connect(self.tanbih_window)
        self.pushButton_5.clicked.connect(self.tashvigh_window)
        self.pushButton_6.clicked.connect(self.tashilat_window)
        self.show()
    def person_window(self):
        self.personel = Person()
        self.personel.show()

    def search_window(self):
        self.search  = Search()
        self.search.show()

    def nahast_window(self):
        self.nahast = Nahast()
        self.nahast.show()

    def tashvigh_window(self):
        self.tashvigh = Tashvigh()
        self.tashvigh.show()

    def tanbih_window(self):
        self.tanbih = Tanbih()
        self.tanbih.show()

    def tashilat_window(self):
        self.tashilat = Tashilat()
        self.tashilat.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())




