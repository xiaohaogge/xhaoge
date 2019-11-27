# 此模块用于读取order.xml文件中的信息；

import os
import xml.etree.ElementTree as ET


def startReadOrder():
    basedir = os.path.dirname(__file__)
    Dom = ET.parse(basedir+'\Order.xml')
    adlut = []
    child = []
    infant = []
    orderDict = {"0":adlut,"1":child,"2":infant}
    Dom.getroot()
    try:
        for i in range(10000):
            passenger = {}
            name = Dom.findall('./Order/People/human/name')[i]
            ageType = Dom.findall('./Order/People/human/ageType')[i]
            gender = Dom.findall('./Order/People/human/gender')[i]
            nationality = Dom.findall('./Order/People/human/nationality')[i]
            cardType = Dom.findall('./Order/People/human/cardType')[i]
            cardNum = Dom.findall('./Order/People/human/cardNum')[i]
            birthday = Dom.findall('./Order/People/human/birthday')[i]
            cardExpired = Dom.findall('./Order/People/human/cardExpired')[i]
            cardIssuePlace = Dom.findall('./Order/People/human/cardIssuePlace')[i]
            ticketNumbers = Dom.findall('./Order/People/human/ticketNumbers')[i]
            ticketNumbersAsText = Dom.findall('./Order/People/human/ticketNumbersAsText')[i]
            
            passenger['name'] = name.text
            passenger['ageType'] = ageType.text
            passenger['gender'] = gender.text
            passenger['nationality'] = nationality.text
            passenger['cardType'] = cardType.text
            passenger['cardNum'] = cardNum.text
            passenger['birthday'] = birthday.text
            passenger['cardExpired'] = cardExpired.text
            passenger['cardIssuePlace'] = cardIssuePlace.text
            passenger['ticketNumbers'] = ticketNumbers.text
            passenger['ticketNumbersAsText'] = ticketNumbersAsText.text
            if int(ageType.text) == 0:
                adlut.append(passenger)
            elif int(ageType.text) == 1:
                child.append(passenger)
            else:
                infant.append(passenger)

    except Exception:
        print("orderDict:",orderDict)
        return orderDict

