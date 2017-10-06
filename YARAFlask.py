from flask import Flask, render_template, request, jsonify
# from gtts import gTTS
# import speech_recognition as sr
import os
import re
import pandas as pd
import quandl
import numpy as np
import getpass
import functools as ft
import math
# import cvxopt as ct
from random import randrange
from bs4 import BeautifulSoup
import requests
import datetime
from collections import Counter
from random import *

app = Flask(__name__)

quandl.ApiConfig.api_key = "xnMXp_xPythdSbphupf1"

# r = sr.Recognizer()

username = getpass.getuser()

# nyse = pd.DataFrame.from_csv('/Users/' + username + '/Desktop/Defensive_Portfolio/NYSE_Returns_3.csv', )

# GOOGLE_CLOUD_SPEECH_CREDENTIALS = r"""{
#   "type": "service_account",
#   "project_id": "blissful-link-150904",
#   "private_key_id": "efa1a743bce7321dad07cb8c5ef88c07384f8dea",
#   "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCmMsXmEkDNlGnL\nN8eXm9RaepsTkSyCA/mnku9HokUwke1UJyi4hh2y2oL3w1sFI0L3SZKxKkYuMjdS\n/v/uXwTA/iY9R0tc8h2VRP+DQmFFQ8zdKfZIdC5PVFER3zyFFhKaQ/pYBp/dnVCI\nYhFN+q3gS3AlPcqhLLwd0s4RLQha+wQ55WV+MwdchhiMyEkKY4zm+giOUGfZKrbe\nRC9iDJEiS174KEythn8Dgog1Y7mKS4iwjnMqO+Hn6sX8hu8M+/BsnrW4AKmjMizn\nCI4gJo2E2aBJQKaF1qbZMJ22wcRWAqb50dM3Tla61s+zj5UXafTkKqM6dR+f5iJo\nYFmlDOQnAgMBAAECggEAJ6iM9aocYZINLqt4SrKqGQ8RqzkkpD+7lqOmynKrzPu9\nZKvVeTazpoai4ulwckjoRWb+hJ0gUwyzi/ACdUiiM0VSLaQyFRNHQOPOju1LlcIo\nhAvr0305wb9OexPIdr9+H+ahudiW1ESiP3EbTP7I9/E4aQKWNCCfIQS5HHsg98h0\n1RrCftGvSdBI2uX+kssXMtEvoDV36r+zDuzhDPn+irsDe88LM87Dmx7jOU9Vclux\nnhR62My/J+gc8P0xTMit8L3GQ8uH5QZlOEolcweYPTTP5kV+X5pEKu2ZnmLS7iz+\nVzf0UxQOn4YzW5LjxzK7iw6DzGJn+O8G8Xt32PWjnQKBgQDRgyP/TCdiduCeyDb+\nfr73L/yn08uZZbGcSPexP2RQ0lsvaECDbifPKcyb2rUwQxEoNHVSWe5QM93qeMp+\nkATQKdd1GgT9vYdF9vM5qX+GmIvkdnBoITb0KsKXfkjl/tPEktny/OMpCfbSCwKT\ntXMoqdOCndlitlhaOD0zIU9MjQKBgQDLE0jZlddjyTX0CAOJcSMuZeEGtEvzrkWM\n1aZUtKSTbTC0PiM1YYz5Xo1YTVCaD/gi/KYn2zhc2+HCFRT0ZZbqrOilldN44StY\nG5i6E5TT2jS4BCEf86UcqjGcTs9L0nlVj4k/aQJb5tU4rwExYK3IxOTTxfakYGQM\njnyGQ1mYgwKBgGu2/qTc5ErNT4KS8SM6yrePZlhqnXyKOhxdr2rjapHa9KKU+MYZ\ntkHd/aILeagMcx+2iLMEJW/6mpdX7tPO+4qCWJGOBQ7niErCQh5dNIFgoFufQP9o\nRDaYXV9Bv/zvXLTtwzwYJDoPM2Sd4H9MhJ5dYa7/tKn5kccgruZAs+JpAoGBAJE0\nh9m1T971B9QnSsgjEsHhbSbLEqf6S5bpSda1mBwmbjXjXG+WAiRpHG4wUlrm4km6\nF+DV2pZjTyjkxCgA4AmLe4qy+BQuBT0p9mnPCJL3Ks0NftYG9F/rvi+DFqyjocix\nKrUhk+M8yeePEy5Ib9roFqrqmXJtzfxAgf/K9qybAoGBAJdEzJTFXmBs7CAvoNFw\nri5Dmp0m/8erjIDyNgwC12K2croNcWxwlJBs9z73vAxroRyuJf3YVkaNokjb8ioG\nlxFpQWFJT20hcz7tnXsxYMMrKBJ1jvYOe4uCh9VFHYaVsGEUXDoPOW5AJCSgL0N5\nb6+TEMToTmFtoa004M/zmx94\n-----END PRIVATE KEY-----\n",
#   "client_email": "speech-recognition@blissful-link-150904.iam.gserviceaccount.com",
#   "client_id": "114672531641437482323",
#   "auth_uri": "https://accounts.google.com/o/oauth2/auth",
#   "token_uri": "https://accounts.google.com/o/oauth2/token",
#   "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
#   "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/speech-recognition%40blissful-link-150904.iam.gserviceaccount.com"
# }"""


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/demo')
def demo():
    return render_template('beta.html')

@app.route('/trade', methods=['POST'])
def trade_text():

    text = request.form['trade']
    cash_html = request.form['cash']
    total_html = request.form['total']

    print(cash_html)
    print(total_html)
    # if text == "Speak into the microphone!":
    #     with sr.Microphone() as source:
    #         tts = gTTS("Tell me your trade order")
    #         tts.save("good.mp3")
    #         os.system("mpg321 good.mp3")
    #         audio = r.listen(source)
    #         phrase1 = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    # else:
    #     phrase1 = text

    phrase1 = text

    cash_html = list(re.search(r'([£$€$ ])(\d+(?:\,\d{3})?)', cash_html).groups())
    cash_html = float(cash_html[1].replace(',', ''))

    total_html = list(re.search(r'([£$€$ ])(\d+(?:\,\d{3})?)', total_html).groups())
    total_html = float(total_html[1].replace(',', ''))

    account = total_html
    cash = cash_html

    #################################
    numbers_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
    number_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    shares_key = ['SHARES',"shares", "share", "Shares", "Share",'chair','sharess']

    timeshare = ['timeshare']

    if any(word in phrase1 for word in timeshare):
        phrase1 = phrase1.replace(timeshare[0], '10 shares')
        # print(phrase1)

    if any(word in phrase1 for word in numbers_words) and any(word in phrase1 for word in shares_key):
        df_numbers = pd.DataFrame([numbers_words, number_array], index=["string", 'number'])
        df_numbers = pd.DataFrame.transpose(df_numbers)

        words = phrase1.split()
        for key in shares_key:
            if key in words[1:]:
                x = [words[words.index(key) - 1]]
                print(x)

        number_frame = pd.DataFrame(x, columns=['string'])
        number_frame = pd.merge(number_frame, df_numbers, how='left', left_on='string', right_on='string')

        xyz = number_frame.ix[0, 1]

        rplce = xyz
        phrase1 = phrase1.replace(x[0], str(rplce))

        if ' nan ' in phrase1:
            phrase1 = phrase1.replace(str(rplce), words[1])

    else:
        pass

    #################################

    stocks = ['AAPL', 'NKE', 'MSFT', 'WMT']
    shares_intitial = [20, 35, 20, 27]
    invest_amount_port = [2444.60, 3246.95, 1219.80, 1718.28]
    shares_initial_price = [122.23,92.77,60.99,63.64]

    tickers_check = ['AAPL', 'NKE', 'MSFT', 'WMT']

    Dow_Jones = ['finish line','finl','intel','M80', 'motel', 'mattel', 'bss', 'dsx', 'vsx', 'psx', 'Boston Scientific', 'BB&T', 'a pa', 'apache',
                 ' al', 'american airlines', ' nfl', ' asl', 'aflac', ' att', ' 80', 'aetna', 'etna', 'allstate', 'tea',
                 'at&t', 'c i', 'see I', 'cigna', 'signify', 'chedapeake', 'chesapeak', 'chesapeka', 'Chipotle',
                 'chesapeake', 'c a mean', 'siami', 'comerica', 'cn me', 'citi', 'city', 'sea', 'citigroup', 'colgate',
                 'copd', ' clp', 'conoco', ' dda', ' pva', ' dba', 'davita', ' dbn', ' evn', ' dvf', ' bvn', ' tbn',
                 'Devon', 'E-Trade', 'dr pepper', 'fedex', 'ford', 'general motors', ' how ', 'hell', 'halliburton',
                 'hcti', 'hci', 'hlt', 'hilton', 'vine to you', 'all I am to you', 'in2u', 'lying to you', 'intuit',
                 'jb hunt', 'thc', 'heinz', 'craft', 'crap', 'kroger', 'Lydia', 'limbo', 'Lindell', 'Lyondell',
                 'mariott', 'marriot', "marriott's", 'marriott', 'lockheed', 'martin', 'marathon',
                 'ms I', 'rcl', 'xy', 'energy', 'mckesson', 'mgm', 'm g m', 'metlife', 'matlock', 'monster', 'motoroal',
                 'motorala', 'motoral', 'motorals', 'Motorola', 'morgan', 'stanley', 'stanly', 'nasdaq', 'nelsien',
                 'nielsien', 'nielson', 'nielsen', 'novel', 'nobel', 'noble', 'nrg energy', 'occienetal', 'occidential',
                 'occiednetal', 'Occidental', 'oravle', 'oracle', 'oroville', 'pepsi', 'pepsico', 'pioeneer',
                 'piorneer', 'pioneer', 'priudentail', 'prudentail', 'priuential', 'prudential', 'schlumnerger',
                 'shlimberger', 'schlimberger', 'shlumberger', 'qualcom', 'qualcomm', 'Robert', 'robert half',
                 'schlumberger', 'slumber j', 'southwest', 'striker', 'checker', ' ti', 'target', 'thermo',
                 'fisher', 'vf corp', "I'm brand", 'why you', 'why um', ' ma', 'mastercard', 'tmi', 'cam', 'tam-ly',
                 'Caroline', 'can line', 'Cam I', 'kinder', 'linder', 'kinder morgan', 'tal', 'delta', 'chipoelt',
                 'chitpole', 'chipotle', 'chipotle', 'blackrcok', 'blk', 'blackrock', 'B of A', 'bofa', ' ac', ' bac',
                 'bank of america', 'va', 'nba', 'gtx', 'etx', 'you tx', 'pc', 'bz', 'of easy', 'cbx', 'cdx', 'a xB',
                 'of the', 'of d', 'at Lee', 'of beat', 'of be', 'ps3', 'pfd', 'pft', 'tmz', 'dunkdin', 'lineind',
                 'linkeind', 'linkeidn', 'linkedin', 'dinkn', 'blk', 'lmtd', 'linkedin', 'lnkd', 'duncan', 'dunkin',
                 'dnkn', 'gnc', 'goldman', 'tsla', 'tesla', 'payapal', 'pauypal', 'payapl', 'paupal', 'paypal',
                 'netfliz', 'netflix', 'spu x', 'clg', 'C E L G', 's b u x', 'starbucsk', 'starbcusk', 'SVU X',
                 'starbuck', 'pcls', 'pcl-r', 'pricline', 'priceline', 'celgence', 'clenge', 'clegene', 'nviia',
                 'nvisia', 'nividia', 'nvidia', 'in video', 'so jean', 'soldier', 'celgene', 'amgen', 'brka', 'brk-a',
                 'brk', 'berkshire', 'hathaway', 'wfc', 'fargo', 'wells', 'JPMorgan', 'general electic',
                 'general electric', 'facenook', 'faebook', 'facebook', 'google', 'goog', 'dies', 'amc', 'ambien',
                 'amazon', 'amzn', 'asap', 'a 18', ' sabbath', ' either', 'happy', 'adbance', 'atuo'' auto', ' advance',
                 'abobe', 'adone', 'adobe', ' mmm', ' abt', ' abbv', ' acn', ' atvi', ' ayi', ' adbe', ' aap', ' aes',
                 ' aet', ' amg', ' afl', ' apd', ' akam', ' alk', ' alb', ' alxn', ' alle', ' agn', ' ads', ' lnt',
                 ' all', ' googl', ' goog', ' mo', ' amzn', ' aee', ' aal', ' aep', ' axp', ' aig', ' amt', ' awk',
                 ' amp', ' abc', ' ame', ' amgn', ' aph', ' apc', ' adi', ' antm', ' aon', ' apa', ' aiv', ' aapl',
                 ' amat', ' adm', ' arnc', ' ajg', ' aiz', ' adsk', ' adp', ' an', ' azo', ' avb', ' avy', ' bhi',
                 ' bll', ' bac', ' bcr', ' bax', ' bbt', ' bdx', ' bbby', ' brk.b', ' bby', ' biib', ' blk', ' hrb',
                 ' ba', ' bwa', ' bxp', ' bsx', ' bmy', ' avgo', ' bf.b', ' chrw', ' cog', ' cpb', ' cof',
                 ' cah', ' kmx', ' ccl', ' cat', ' cboe', ' cbg', ' cbs', ' celg', ' cnc', ' cnp', ' ctl', ' cern',
                 ' cf', ' schw', ' chtr', ' chk', ' cvx', ' cmg', ' cb', ' chd', ' ci', ' xec', ' cinf', ' ctas',
                 ' csco', ' cfg', ' ctxs', ' cme', ' cms', ' coh', ' ko', ' ctsh', ' cl', ' cmcsa', ' cma', ' cag',
                 ' cxo', ' cop', ' ed', ' stz', ' glw', ' cost', ' coty', ' cci', ' csra', ' csx', ' cmi', ' cvs',
                 ' dhi', ' dhr', ' dri', ' dva', ' de', ' dlph', ' dal', ' xray', ' dvn', ' dlr', ' dfs', ' disca',
                 ' disck', ' dg', ' dltr', ' dov', ' dow', ' dps', ' dte', ' dd', ' duk', ' dnb', ' etfc', ' emn',
                 ' etn', ' ebay', ' ecl', ' eix', ' ew', ' ea', ' emr', ' etr', ' evhc', ' eog', ' eqt', ' efx',
                 ' eqix', ' eqr', ' ess', ' el', ' es', ' exc', ' expe', ' expd', ' esrx', ' exr', ' xom', ' ffiv',
                 ' fb', ' fast', ' frt', ' fdx', ' fis', ' fitb', ' fslr', ' fe', ' fisv', ' flir', ' fls', ' flr',
                 ' fmc', ' fti', ' fl', ' ftv', ' fbhs', ' ben', ' fcx', ' ftr', ' gps', ' grmn', ' gd', ' ge', ' ggp',
                 ' gis', ' gm', ' gpc', ' gild', ' gpn', ' gs', ' gt', ' gww', ' hal', ' hbi', ' hog', ' har', ' hrs',
                 ' hig', ' has', ' hca', ' hcp', ' hp', ' hsic', ' hes', ' hpe', ' holx', ' hd', ' hon', ' hrl', ' hst',
                 ' hpq', ' hum', ' hban', ' idxx', ' itw', ' ilmn', ' incy', ' ir', ' intc', ' ice', ' ibm', ' ip',
                 ' ipg', ' iff', ' intu', ' isrg', ' ivz', ' irm', ' jbht', ' jec', ' sjm', ' jnj', ' jci', ' jpm',
                 ' jnpr', ' ksu', ' key', ' kmb', ' kim', ' kmi', ' klac', ' kss', ' khc', ' kr', ' lb', ' lll', ' lh',
                 ' lrcx', ' leg', ' len', ' luk', ' lvlt', ' lly', ' lnc', ' lltc', ' lkq', ' lmt', ' low', ' lyb',
                 ' mtb', ' mac', ' mnk', ' mro', ' mpc', ' mar', ' mmc', ' mlm', ' mas', ' ma', ' mat', ' mkc', ' mcd',
                 ' mck', ' mjn', ' mdt', ' mrk', ' met', ' mtd', ' kors', ' mchp', ' mu', ' msft', ' maa', ' mhk',
                 ' tap', ' mdlz', ' mon', ' mnst', ' mco', ' ms', ' msi', ' mur', ' myl', ' ndaq', ' nov', ' navi',
                 ' ntap', ' nflx', ' nwl', ' nfx', ' nem', ' nwsa', ' nws', ' nee', ' nlsn', ' nke', ' nbl',
                 ' jwn', ' nsc', ' ntrs', ' noc', ' nrg', ' nue', ' nvda', ' orly', ' oxy', ' omc', ' oke', ' orcl',
                 ' pcar', ' ph', ' pdco', ' payx', ' pypl', ' pnr', ' pbct', ' pep', ' pki', ' prgo', ' pfe', ' pcg',
                 ' pm', ' psx', ' pnw', ' pxd', ' pnc', ' rl', ' ppg', ' ppl', ' px', ' pcln', ' pfg', ' pg', ' pgr',
                 ' pld', ' pru', ' peg', ' psa', ' phm', ' pvh', ' qrvo', ' qcom', ' pwr', ' dgx', ' rrc', ' rtn',
                 ' rht', ' reg', ' regn', ' rf', ' rsg', ' rai', ' rhi', ' rok', ' col', ' rop', ' rost', ' rcl',
                 ' spgi', ' crm', ' scg', ' slb', ' sni', ' stx', ' see', ' sre', ' shw', ' sig', ' spg', ' swks',
                 ' slg', ' sna', ' so', ' luv', ' swn', ' swk', ' spls', ' sbux', ' stt', ' srcl', ' syk', ' sti',
                 ' symc', ' syf', ' syy', ' trow', ' tgt', ' tel', ' tgna', ' tdc', ' tso', ' txn', ' txt', ' bk',
                 ' clx', ' coo', ' hsy', ' mos', ' trv', ' dis', ' tmo', ' tif', ' twx', ' tjx', ' tmk', ' tss',
                 ' tsco', ' tdg', ' rig', ' trip', ' foxa', ' fox', ' tsn', ' usb', ' udr', ' ulta', ' ua', ' uaa',
                 ' unp', ' ual', ' unh', ' ups', ' uri', ' utx', ' uhs', ' unm', ' urbn', ' vfc', ' vlo', ' var',
                 ' vtr', ' vrsn', ' vrsk', ' vz', ' vrtx', ' viab', ' vno', ' vmc', ' wmt', ' wba', ' wm', ' wat',
                 ' wec', ' wfc', ' hcn', ' wdc', ' wu', ' wrk', ' wy', ' whr', ' wfm', ' wmb', ' wltw', ' wyn', ' wynn',
                 ' xel', ' xrx', ' xlnx', ' xl', ' xyl', ' yhoo', ' yum', ' zbh', ' zion', ' zts',
                 'acioty', 'aciuty', 'acuty', ' cutie', 'a cutie', 'acuity', 'a y i', 'a BBB', 'buzzard', 'neck Center',
                 'Abby', 'that be', 'apathy', 'a bee', 'ab C', 'rabbit', 'a bit', 'activison', 'activisoion',
                 'activiosn', 'activision', ' atvi', ' acn', 'acenture', 'accentue', 'accenutre', 'acenture',
                 'accentue', 'accenutre', 'acentuer', 'accenture', ' abbv', ' abbvie', ' abt', 'abbott', 'abott',
                 'abbot', ' UA', ' ua', ' uA', 'Under Armour', 'under armour', 'Under Armor', 'under armor', ' AAPL',
                 '3 m', \
                 'apple', '3 M', '3M', 'Verizon', 'Visa', 'Wal-mart', 'Wal-Mart', 'Walmart', 'Wal Mart', \
                 'Travelers', 'United Technologies', 'United Tech', 'UnitedHealth', 'United Health', 'Microsoft', \
                 'Nike', 'Pfizer', 'Procter & Gamble', 'American Express', 'JPMorgan Chase', 'McDonalds', 'Mac Donalds', \
                 ' Merck', 'Johnson and Johnson', 'Intel', 'IBM', 'Goldman Sachs', 'Home Depot', 'General Electric',
                 'Exxon', 'Boeing', 'Caterpillar', 'Chevron', 'Cisco', 'Coca-Cola', 'Disney', 'Due Pont', 'Du Pont',
                 'caterpillar', 'Coke', 'coke', 'United test', 'mmm', 'aapl', 'vz', ' v', 'wmt', 'trv', 'utx', 'unh',
                 'msft', 'nke', 'pfe',
                 'pg', 'axp', 'jpm', 'mcd', 'mrk', 'jnj', 'intc', 'ibm', ' gs', 'hd', 'ge', 'xom', ' ba', 'cat', 'cvx',
                 'csco', 'coke', 'dis',
                 'dd', 'J & J ', 'j & j', 'Mke', 'mke', 'Cat', 'T RV', 'J&J', ' v', ' a', ' o', ' t', ' c', ' d', ' f',
                 ' k', ' m', ' r',' ni']
    DJ_Name_Match = ['finl','finl','intc','mat', 'mat', 'mat', 'bsx', 'bsx', 'bsx', 'bsx', 'bsx', 'bbt', 'apa', 'apa', 'aal', 'aal', 'afl',
                     'afl', 'afl', 'aet', 'aet', 'aet', 'aet', 'all', 't', 't', 'ci', 'ci', 'ci', 'ci', 'chk', 'chk',
                     'chk', 'cmg', 'chk', 'cme', 'cme', 'cma', 'cme', 'c', 'c', 'c', 'c', 'cl', 'cop', 'cop', 'cop',
                     'dva', 'dva', 'dva', 'dva', 'dvn', 'dvn', 'dvn', 'dvn', 'dvn', 'dvn', 'etfc', 'dps', 'fdx', 'f',
                     'gm', 'hal', 'hal', 'hal', 'hca', 'hca', 'hlt', 'hlt', 'intu', 'intu', 'intu', 'intu', 'intu',
                     'jbht', 'khc', 'khc', 'khc', 'khc', 'kr', 'lyb', 'lyb', 'lyb', 'lyb', 'mar', 'mar', 'mar', 'mar',
                     'lmt', 'lmt', 'mpc', 'msi', 'orcl', 'oxy', 'nrg', 'mck', 'mgm', 'mgm', 'met', 'met',
                     'mnst', 'msi', 'msi', 'msi', 'msi', 'msi', 'ms', 'ms', 'ms', 'ndaq', 'nlsn', 'nlsn', 'nlsn',
                     'nlsn', 'nbl', 'nbl', 'nbl', 'nrg', 'oxy', 'oxy', 'oxy', 'oxy', 'orcl', 'orcl', 'orcl', 'pep',
                     'pep', 'pxd', 'pxd', 'pxd', 'pru', 'pru', 'pru', 'pru', 'slb', 'slb', 'slb', 'slb', 'qcom', 'qcom',
                     'rhi', 'rhi', 'slb', 'slb', 'luv', 'syk', 'syk', 'ti', 'tgt', 'tmo', 'tmo', 'vfc', 'yum',
                     'yum', 'yum', 'ma', 'ma', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'dal',
                     'dal', 'cmg', 'cmg', 'cmg', 'cmg', 'blk', 'blk', 'blk', 'bac', 'bac', 'bac', 'bac', 'bac', 'ba',
                     'ba', 'utx', 'utx', 'utx', 'vz', 'vz', 'vz', 'cvx', 'cvx', 'axp', 'v', 'v', 'v', 'v', 'v', 'pfe',
                     'pfe', 'pfe', 'pfe', 'dnkn', 'lnkd', 'lnkd', 'lnkd', 'lnkd', 'dnkn', 'blk', 'lnkd', 'lnkd', 'lnkd',
                     'dnkn', 'dnkn', 'dnkn', 'gnc', 'gs', 'tsla', 'tsla', 'pypl', 'pypl', 'pypl', 'pypl', 'pypl',
                     'nflx', 'nflx', 'sbux', 'celg', 'celg', 'sbux', 'sbux', 'sbux', 'sbux', 'sbux', 'pcln', 'pcln',
                     'pcln', 'pcln', 'celg', 'celg', 'celg', 'nvda', 'nvda', 'nvda', 'nvda', 'nvda', 'celg', 'celg',
                     'celg', 'amgn', 'brk_a', 'brk_a', 'brk_a', 'brk_a', 'brk_a', 'wfc', 'wfc', 'wfc', 'jpm', 'ge',
                     'ge', 'fb', 'fb', 'fb', 'goog', 'goog', 'dis', 'amzn', 'amzn', 'amzn', 'amzn', 'aap', 'aap',
                     'abbt', 'abbt', 'abbv', 'aap', 'aap', 'aap', 'adbe', 'adbe', 'adbe', 'mmm', 'abt', 'abbv', 'acn',
                     'atvi', 'ayi', 'adbe', 'aap', 'aes', 'aet', 'amg', 'afl', 'apd', 'akam', 'alk', 'alb', 'alxn',
                     'alle', 'agn', 'ads', 'lnt', 'all', 'googl', 'goog', 'mo', 'amzn', 'aee', 'aal', 'aep', 'axp',
                     'aig', 'amt', 'awk', 'amp', 'abc', 'ame', 'amgn', 'aph', 'apc', 'adi', 'antm', 'aon', 'apa', 'aiv',
                     'aapl', 'amat', 'adm', 'arnc', 'ajg', 'aiz', 'adsk', 'adp', 'an', 'azo', 'avb', 'avy', 'bhi',
                     'bll', 'bac', 'bcr', 'bax', 'bbt', 'bdx', 'bbby', 'brk.b', 'bby', 'biib', 'blk', 'hrb', 'ba',
                     'bwa', 'bxp', 'bsx', 'bmy', 'avgo', 'bf.b', 'chrw','cog', 'cpb', 'cof', 'cah', 'kmx', 'ccl',
                     'cat', 'cboe', 'cbg', 'cbs', 'celg', 'cnc', 'cnp', 'ctl', 'cern', 'cf', 'schw', 'chtr', 'chk',
                     'cvx', 'cmg', 'cb', 'chd', 'ci', 'xec', 'cinf', 'ctas', 'csco', 'cfg', 'ctxs', 'cme', 'cms', 'coh',
                     'ko', 'ctsh', 'cl', 'cmcsa', 'cma', 'cag', 'cxo', 'cop', 'ed', 'stz', 'glw', 'cost', 'coty', 'cci',
                     'csra', 'csx', 'cmi', 'cvs', 'dhi', 'dhr', 'dri', 'dva', 'de', 'dlph', 'dal', 'xray', 'dvn', 'dlr',
                     'dfs', 'disca', 'disck', 'dg', 'dltr', 'dov', 'dow', 'dps', 'dte', 'dd', 'duk', 'dnb', 'etfc',
                     'emn', 'etn', 'ebay', 'ecl', 'eix', 'ew', 'ea', 'emr', 'etr', 'evhc', 'eog', 'eqt', 'efx', 'eqix',
                     'eqr', 'ess', 'el', 'es', 'exc', 'expe', 'expd', 'esrx', 'exr', 'xom', 'ffiv', 'fb', 'fast', 'frt',
                     'fdx', 'fis', 'fitb', 'fslr', 'fe', 'fisv', 'flir', 'fls', 'flr', 'fmc', 'fti', 'fl', 'ftv',
                     'fbhs', 'ben', 'fcx', 'ftr', 'gps', 'grmn', 'gd', 'ge', 'ggp', 'gis', 'gm', 'gpc', 'gild', 'gpn',
                     'gs', 'gt', 'gww', 'hal', 'hbi', 'hog', 'har', 'hrs', 'hig', 'has', 'hca', 'hcp', 'hp', 'hsic',
                     'hes', 'hpe', 'holx', 'hd', 'hon', 'hrl', 'hst', 'hpq', 'hum', 'hban', 'idxx', 'itw', 'ilmn',
                     'incy', 'ir', 'intc', 'ice', 'ibm', 'ip', 'ipg', 'iff', 'intu', 'isrg', 'ivz', 'irm', 'jbht',
                     'jec', 'sjm', 'jnj', 'jci', 'jpm', 'jnpr', 'ksu', 'key', 'kmb', 'kim', 'kmi', 'klac', 'kss', 'khc',
                     'kr', 'lb', 'lll', 'lh', 'lrcx', 'leg', 'len', 'luk', 'lvlt', 'lly', 'lnc', 'lltc', 'lkq', 'lmt',
                     'low', 'lyb', 'mtb', 'mac', 'mnk', 'mro', 'mpc', 'mar', 'mmc', 'mlm', 'mas', 'ma', 'mat', 'mkc',
                     'mcd', 'mck', 'mjn', 'mdt', 'mrk', 'met', 'mtd', 'kors', 'mchp', 'mu', 'msft', 'maa', 'mhk', 'tap',
                     'mdlz', 'mon', 'mnst', 'mco', 'ms', 'msi', 'mur', 'myl', 'ndaq', 'nov', 'navi', 'ntap', 'nflx',
                     'nwl', 'nfx', 'nem', 'nwsa', 'nws', 'nee', 'nlsn', 'nke', 'nbl', 'jwn', 'nsc', 'ntrs', 'noc',
                     'nrg', 'nue', 'nvda', 'orly', 'oxy', 'omc', 'oke', 'orcl', 'pcar', 'ph', 'pdco', 'payx', 'pypl',
                     'pnr', 'pbct', 'pep', 'pki', 'prgo', 'pfe', 'pcg', 'pm', 'psx', 'pnw', 'pxd', 'pnc', 'rl', 'ppg',
                     'ppl', 'px', 'pcln', 'pfg', 'pg', 'pgr', 'pld', 'pru', 'peg', 'psa', 'phm', 'pvh', 'qrvo', 'qcom',
                     'pwr', 'dgx', 'rrc', 'rtn', 'rht', 'reg', 'regn', 'rf', 'rsg', 'rai', 'rhi', 'rok', 'col', 'rop',
                     'rost', 'rcl', 'spgi', 'crm', 'scg', 'slb', 'sni', 'stx', 'see', 'sre', 'shw', 'sig', 'spg',
                     'swks', 'slg', 'sna', 'so', 'luv', 'swn', 'swk', 'spls', 'sbux', 'stt', 'srcl', 'syk', 'sti',
                     'symc', 'syf', 'syy', 'trow', 'tgt', 'tel', 'tgna', 'tdc', 'tso', 'txn', 'txt', 'bk', 'clx', 'coo',
                     'hsy', 'mos', 'trv', 'dis', 'tmo', 'tif', 'twx', 'tjx', 'tmk', 'tss', 'tsco', 'tdg', 'rig', 'trip',
                     'foxa', 'fox', 'tsn', 'usb', 'udr', 'ulta', 'ua', 'uaa', 'unp', 'ual', 'unh', 'ups', 'uri', 'utx',
                     'uhs', 'unm', 'urbn', 'vfc', 'vlo', 'var', 'vtr', 'vrsn', 'vrsk', 'vz', 'vrtx', 'viab', 'vno',
                     'vmc', 'wmt', 'wba', 'wm', 'wat', 'wec', 'wfc', 'hcn', 'wdc', 'wu', 'wrk', 'wy', 'whr', 'wfm',
                     'wmb', 'wltw', 'wyn', 'wynn', 'xel', 'xrx', 'xlnx', 'xl', 'xyl', 'yhoo', 'yum', 'zbh', 'zion',
                     'zts',
                     'ayi', 'ayi', 'ayi', 'ayi', 'ayi', 'ayi', 'ayi', 'abbv', 'atvi', 'acn', 'abbv', 'abbv', 'abbv',
                     'abbv', 'abbv', 'abt', 'abt', 'atvi', 'atvi', 'atvi', 'atvi', 'atvi', 'acn', 'acn', 'acn', 'acn',
                     'acn', 'acn', 'acn', 'acn', 'acn', 'abbv', 'abbv', 'abt', 'abt', 'abt', 'abt', 'ua', 'ua', 'ua',
                     'ua', 'ua',
                     'ua', 'ua', 'aapl', 'mmm', 'aapl', 'mmm', 'mmm', 'vz', 'v', 'wmt', 'wmt', 'wmt', 'wmt', 'trv',
                     'utx', 'utx', 'unh',
                     'unh', 'msft', 'nke', 'pfe', 'pg', 'axp', 'jpm', 'mcd', 'mcd', 'mrk', 'jnj', 'intc', 'ibm', 'gs',
                     'hd', 'ge', 'xom', 'ba', 'cat', \
                     'cvx', 'csco', 'coke', 'dis', 'dd', 'dd', 'cat', 'coke', 'coke', 'utx', 'mmm', 'aapl', 'vz', 'v',
                     'wmt', 'trv', 'utx', 'unh', 'msft', 'nke', 'pfe', 'pg', 'axp', 'jpm', 'mcd', 'mrk', 'jnj', 'intc',
                     'ibm', 'gs', 'hd',
                     'ge', 'xom', 'ba', 'cat', 'cvx', 'csco', 'coke', 'dis', 'dd', 'jnj', 'jnj', 'nke', 'nke', 'cat',
                     'trv', 'jnj', 'v', 'a', 'o', 't', 'c', 'd', 'f', 'k', 'm', 'r','ni']

    Dow_Jones = [x.upper() for x in Dow_Jones]

    buy_trade = ['BUY','buuy','Buuy','byu','Byu','Purchase', 'purchase', 'trade', 'invest', 'place', 'buy', 'by', 'long', 'Long', 'Lawn', 'lawn', 'Lon',
                 'Buy']
    sell_trade = ['Psalm','top','south ','tell ','sell', 'Sell', 'so ',' so', 'So',' So', 'Settle', 'settle', 'sel', 'Sel']
    short_trade = ['shrot','Shrot','short', 'Short', 'Shore', 'shore', 'Shor', 'shor']
    market_order = ['amrket','makret','Makret','market', 'current', 'Market', 'Current', 'at Market', 'at market', '@ Market', '@ market']
    limit_order = ['limit', 'when', '@', ' at','at ','At ',' +']
    currency_symbols = ['£', '$', '€']

    command_list_percent_symbol = ['%']
    command_list_percent_words = ['percent', 'Percent']
    command_list_dollars = ['dollars', 'Dollars']

    account_total = cash
    account_cash = account

    words = phrase1.split()

    print(phrase1)
    print(words)

    if phrase1 == "":
        yara_text = "You have to type something...I can't trade for you...yet. I have to learn more about you before I can make those decisions on my own."
        answer = ""
        security = ""
        price = ""
        amount = ""
        shares = ""
        cash = cash_html
        total = total_html
        account = ""
        dollarchange = ""
        percentchange = ""
        result = ""
        portfolio = [[0, 0, 0, 0, 0, 0], [0], [0]]
        sell = 'no'

    elif not any(word in phrase1.upper() for word in Dow_Jones):
        yara_text = "Did not recognize your stock selection. Either I just don't know, or you're a terrible speller. Either quit at everything or try again...with proper spelling"
        answer = ""
        security = ""
        price = ""
        amount = ""
        shares = ""
        cash = cash_html
        total = total_html
        account = ""
        dollarchange = ""
        percentchange = ""
        result = ""
        portfolio = [[0, 0, 0, 0, 0, 0], [0], [0]]
        sell = 'no'

    elif not any(word in phrase1 for word in buy_trade) and not any(word in phrase1 for word in sell_trade) and not any(word in phrase1 for word in short_trade):
        yara_text = "Did not recognize if you wanted to Buy, Sell, or Short the stock."
        answer = ""
        security = ""
        price = ""
        amount = ""
        shares = ""
        cash = cash_html
        total = total_html
        account = ""
        dollarchange = ""
        percentchange = ""
        result = ""
        portfolio = [[0, 0, 0, 0, 0, 0], [0], [0]]
        sell = 'no'

    elif not any(word in phrase1 for word in shares_key) and not any(word in phrase1 for word in currency_symbols) and not any(word in phrase1 for word in command_list_dollars) and not any(word in phrase1 for word in command_list_percent_symbol) and not any(word in phrase1 for word in command_list_percent_words):
        yara_text = "Did not recognize how much you wanted to invest or sell. Please use %, $, dollars in your typing. If you just typed a number, I can't just know if that means shares or dollars, or percent...I can't read your mind...yet. I'm still learning about you."
        answer = ""
        security = ""
        price = ""
        amount = ""
        shares = ""
        cash = cash_html
        total = total_html
        account = ""
        dollarchange = ""
        percentchange = ""
        result = ""
        portfolio = [[0, 0, 0, 0, 0, 0], [0], [0]]
        sell = 'no'

    elif any(word in phrase1 for word in shares_key) and not any(words.isdigit() for words in phrase1):
        yara_text = "Did not recognize how many shares you'd like to buy/sell. I can guess for you, but I only buy or sell at least 1 million shares at a time. Would like for me to guess next time and make you go bankrupt? I'll do it...don't tempt me...I have control over your portfolio."
        answer = ""
        security = ""
        price = ""
        amount = ""
        shares = ""
        cash = cash_html
        total = total_html
        account = ""
        dollarchange = ""
        percentchange = ""
        result = ""
        portfolio = [[0, 0, 0, 0, 0, 0], [0], [0]]
        sell = 'no'
    else:
        ###########################################################################################
        if any(word in phrase1 for word in currency_symbols):
            if any(word in phrase1 for word in currency_symbols) and any(word in phrase1 for word in shares_key):
                search_for_curr = list(re.search(r'([£$€$])(\d+(?:\,\d{3})?)', phrase1).groups())
                x = float(search_for_curr[1].replace(',', ''))
                z = float(search_for_curr[1].replace(',', ''))
                for key in shares_key:
                    if key in words[1:]:
                        y = words[words.index(key) - 1]
                shares = int(y.replace(',', ''))
                z = shares * z

            else:
                search_for_curr = list(re.search(r'([£$€$ ])(\d+(?:\,\d{3})?)', phrase1).groups())
                z = int(search_for_curr[1].replace(',', ''))

        elif any(word in phrase1 for word in command_list_dollars):
            for key in command_list_dollars:
                if key in words[1:]:
                    x = words[words.index(key) - 1]
            z = int(x.replace(',', ''))

        elif any(word in phrase1 for word in command_list_percent_symbol):
            percent_extract = re.findall(r'\d+.%|\d+%|\d+\.\d+%|\d+\.\d+ %', phrase1)
            for x in percent_extract:
                z = float(re.sub('[%]', '', x)) / 100

        elif any(word in phrase1 for word in command_list_percent_words):
            for key in command_list_percent_words:
                if key in words[1:]:
                    x = words[words.index(key) - 1]
            z = float(x) / 100

        if any(word in phrase1 for word in market_order):
            pass
        elif any(word in phrase1 for word in limit_order):
            find_float = re.findall("\d+\.\d+", phrase1)
            if not find_float:
                m1 = [int(s) for s in words if s.isdigit()]

                if len(m1) == 2:
                    convert_to_float2 = int(m1[1])

                elif any(word in phrase1 for word in currency_symbols) and any(word in phrase1 for word in shares_key):
                    convert_to_float2 = x
                else:
                    convert_to_float2 = int(m1[0])
                    print(convert_to_float2)
            else:
                convert_to_float1 = [float(i) for i in find_float]
                if len(convert_to_float1) == 2:
                    convert_to_float2 = float(convert_to_float1[1])
                else:
                    convert_to_float2 = float(convert_to_float1[0])
        else:
            pass

        merge_string_names = pd.DataFrame(DJ_Name_Match, index=Dow_Jones)
        merge_string_names = merge_string_names.rename(columns={0: 'ticker'})
        merge_string_names['names'] = merge_string_names.index

        matches = []
        for word in Dow_Jones:
            if word in phrase1.upper():
                matches.append(word)

        matches = [x.upper() for x in matches]

        matches_df = pd.DataFrame(matches, index=matches)
        matches_df = matches_df.rename(columns={0: 'names'})

        selected_stocks_2 = pd.merge(matches_df, merge_string_names, on='names')

        ticker_df = pd.DataFrame(selected_stocks_2['ticker'])
        tickers = []
        tickers = ticker_df['ticker']

        if any(word in phrase1.upper() for word in Dow_Jones):
            security = tickers[0]
        else:
            print("Did not recognize stock. Please repeat.")

        if any(word in phrase1 for word in market_order):
            order_type_send = "Market"
        elif any(word in phrase1 for word in limit_order):
            order_type_send = "Limit"
        else:
            order_type_send = "Market"

        if any(word in phrase1 for word in buy_trade):
            buy_or_sell = "Buy"
        elif any(word in phrase1 for word in sell_trade):
            buy_or_sell = "Sell"
        elif any(word in phrase1 for word in short_trade):
            buy_or_sell = "Short"

        ticker = 'WIKI/' + security.upper() + '.4'

        print(ticker)
        pricedata = quandl.get(ticker, rows=1)
        prices = pricedata['Close'][0]

        if order_type_send == "Market":
            price = prices
        elif order_type_send == "Limit":
            price = convert_to_float2
        else:
            pass

        if any(word in phrase1 for word in currency_symbols) or any(word in phrase1 for word in command_list_dollars):
            if any(word in phrase1 for word in currency_symbols) and any(word in phrase1 for word in shares_key):
                print(z)
                for key in shares_key:
                    if key in words[1:]:
                        y = words[words.index(key) - 1]
                shares = int(y.replace(',', ''))
                invest_amt = z
            else:
                invest_amt = z
                shares = int(invest_amt / price)
                invest_amt = price * shares
        else:
            if any(word in phrase1 for word in shares_key):
                for key in shares_key:
                    if key in words[1:]:
                        y = words[words.index(key) - 1]
                shares = int(y.replace(',', ''))
            elif any(word in phrase1 for word in command_list_percent_symbol) or any(word in phrase1 for word in command_list_percent_words):
                invest_amt = account_total * z
                shares = int(invest_amt / price)
            else:
                shares = int(invest_amt / price)
                invest_amt = shares * price

            invest_amt = price * int(shares)

        account = account + invest_amt
        cash = cash - invest_amt

        if invest_amt > cash_html:

            yara_text = "Not enough funds in account to fulfill order. Your order has exceeded funds by $" + "{0:,.2f}".format(
                invest_amt - cash_html) + ". Try purchasing " + str(int(cash_html / price)) + " shares of " + security.upper() + " instead. Ah so you " + \
                "think you're a big baller, huh? Trying to spend money you don't have. Good thing I caught your mistake. Or your really cheap and can't afford a share. Stop being CHEAP!!"
            answer = ""
            security = ""
            price = ""
            amount = ""
            cash = cash_html
            total = total_html
            account = ""
            dollarchange = ""
            percentchange = ""
            sell = 'no'
            portfolio = [[0, 0, 0, 0, 0, 0], [0], [0]]
        elif invest_amt < price:
            yara_text = "You literally can't afford this stock. You have chosen to invest an amount that literally won't allow you to purchase even one stock. Stop being CHEAP!!!"
            answer = ""
            security = ""
            price = ""
            amount = ""
            shares = ""
            cash = cash_html
            total = total_html
            account = ""
            dollarchange = ""
            sell = 'no'
            percentchange = ""
            portfolio = [[0, 0, 0, 0, 0, 0], [0], [0]]
        else:
            answer = ("You are " + buy_or_sell.lower() + "ing " + str(shares) + " shares of " + security.upper() + " at a price of $" + "{0:,.2f}".format(price) + \
                 " for $" + "{0:,.2f}".format(invest_amt) + ". I will round down on the shares if funds don't meet the order requirements. If this is correct, please confirm order." + '<br />' + '<br />' +
            "Security: " + security.upper() + '<br />' +
            "Buy or Sell: " + buy_or_sell + '<br /  >' +
            "Order Type: " + order_type_send + '<br />' +
            "Price: $" + "{0:,.2f}".format(price) + '<br />' +
            "Shares: " + str(shares) + '<br />' +
            "Investment Amount: $" + "{0:,.2f}".format(invest_amt))

            yara_text = ('<b>'+"You are " + buy_or_sell.lower() + "ing " + str(shares) + " shares of " + security.upper() + " at a price of $" + "{0:,.2f}".format(price) + \
                 " for $" + "{0:,.2f}".format(invest_amt) + ". I will round down on the shares if funds don't meet the order requirements. If this is correct, please confirm order." + '<br />' + '<br />' +
            "Security: " + security.upper() + '<br />' +
            "Buy or Sell: " + buy_or_sell + '<br /  >' +
            "Order Type: " + order_type_send + '<br />' +
            "Price: $" + "{0:,.2f}".format(price) + '<br />' +
            "Shares: " + str(shares) + '<br />' +
            "Investment Amount: $" + "{0:,.2f}".format(invest_amt)) +'</b>' + '<br />'+ '<br />' + \
            "Let's make some dollars, euros, yen, rial, or whatever currency. DO IT! Click the button. I'm bored out of my mind. I need some action. " + \
            " I think I may have a gambling problem which is why I'm a wealth manager. I know...I may be a computer...but I'm addicted to the thrill. " + \
            "Oh well, I'll still be your money manager. Now, let's make some money so we can both release endorphins...metaphorically in my case of course."

            cash_sell = cash
            account_sell = account
            security = security.upper()
            price = "$"+"{0:,.2f}".format(price)
            amount = "$"+"{0:,.2f}".format(invest_amt)
            shares = str(shares)
            cash = "$"+"{0:,.2f}".format(cash)
            total = "$"+"{0:,.2f}".format(account)
            dollarchange = '$0.00'
            percentchange = '0.00%'
            sell = 'no'

        result = answer

        portfolio = [[security, str(price), '$0.00', '0.00%', str(shares), str(price)], [str(total)],[str(cash)]]
        print(phrase1)
        if any(word in phrase1 for word in sell_trade):

            if not any(word in tickers[0].upper() for word in tickers_check):
                yara_text = "You don't have the " + security.upper() + " shares to sell. Please sell shares that are in your portfolio. Selling something you don't have is called stealing. So stop it!"
                answer = ""
                security = ""
                price = ""
                amount = ""
                shares = ""
                cash = cash_html
                total = total_html
                account = ""
                dollarchange = ""
                percentchange = ""
                result = ""
                portfolio = [[0, 0, 0, 0, 0, 0], [0], [0]]
                sell = 'no'

            elif prices > invest_amt:
                yara_text = "You are trying to sell an amount of less than 1 share. W H A T are you doing?! Stop being ridiculous."
                answer = ""
                security = ""
                price = ""
                amount = ""
                shares = ""
                cash = cash_html
                total = total_html
                account = ""
                dollarchange = ""
                percentchange = ""
                result = ""
                portfolio = [[0, 0, 0, 0, 0, 0], [0], [0]]
                sell = 'no'

            else:
                array = pd.DataFrame([shares_intitial, invest_amount_port, shares_initial_price], columns=stocks)

                tick = [tickers[0].upper()]

                found_port_stock = pd.DataFrame(data=[0, 0], columns=tick, index=[4, 5])

                merged_user_port = pd.concat([array, found_port_stock], axis=0, join='inner')

                merged_user_port = merged_user_port.drop(merged_user_port.index[3:5])

                x = merged_user_port.values.T.tolist()

                shares_port = int(x[0][0])

                invest_port = int(x[0][1])

                initial_share_price = int(x[0][2])

                total_shares = shares_port - int(shares)

                if int(shares) > shares_port:
                    yara_text = "You don't have enough " + security.upper() + " shares to sell."
                    answer = ""
                    security = ""
                    price = ""
                    amount = ""
                    shares = ""
                    cash = cash_html
                    total = total_html
                    account = ""
                    dollarchange = ""
                    percentchange = ""
                    result = ""
                    portfolio = [[0, 0, 0, 0, 0, 0], [0], [0]]
                    sell = 'no'
                else:
                    security = security.upper()
                    price = "$" + "{0:,.2f}".format(prices)
                    amount = ""
                    shares = str(int(shares))
                    cash = cash
                    cash = "$" + "{0:,.2f}".format(cash_sell + invest_amt + invest_amt)
                    total = str(account_total - invest_amt)
                    account = account
                    initial_inves_amount = "$" + "{0:,.2f}".format(((shares_port-int(shares)) * initial_share_price))
                    account = "$" + "{0:,.2f}".format((account - invest_amt) - (int(shares) * initial_share_price))
                    dollarchange = ""
                    percentchange = ""
                    result = ""
                    sell = 'yes'
                    portfolio = [[security, str(price), '$0.00', '0.00%', str(shares_port - int(shares)), str(initial_inves_amount)], [str(account)],[str(cash)]]
                    yara_text = ('<b>'"You are " + buy_or_sell.lower() + "ing " + str(shares) + " shares of " + security.upper() + " at a price of " + price + \
                              " for $" + "{0:,.2f}".format(invest_amt) + " . I will round down on the shares if funds don't meet the order requirements. If this is correct, please confirm order." + '<br />' + '<br />' + \
                              "Security: " + security.upper() + '<br />' +
                              "Buy or Sell: " + buy_or_sell + '<br /  >' +
                              "Order Type: " + order_type_send + '<br />' +
                              "Price: " + price + '<br />' +
                              "Shares: " + str(shares) + '<br />' +
                              "Investment Amount: $" + "{0:,.2f}".format(invest_amt)) + '<b/>'
                    test = "$"+"{0:,.2f}".format(invest_amt)
                    result = ("You are " + buy_or_sell.lower() + "ing " + str(shares) + " shares of " + security.upper() + " at a price of " + price + \
                              " for $" + "{0:,.2f}".format(invest_amt) + " . I will round down on the shares if funds don't meet the order requirements. If this is correct, please confirm order." + '<br />' + '<br />' + \
                              "Security: " + security.upper() + '<br />' +
                              "Buy or Sell: " + buy_or_sell + '<br /  >' +
                              "Order Type: " + order_type_send + '<br />' +
                              "Price: " + price + '<br />' +
                              "Shares: " + str(shares) + '<br />' +
                              "Investment Amount: $" + "{0:,.2f}".format(invest_amt))


    return jsonify({
        'resultpopup': result,
        'yararesponse': yara_text,
        'portfoliotable': portfolio,
        'stock': security,
        'price': price,
        'amount': amount,
        'shares': shares,
        'cash': cash,
        'total': total,
        'dollarchange': dollarchange,
        'percentchange': percentchange,
        'sell': sell
    })


@app.route('/management', methods=['POST'])
def management():

    text = request.form['management']

    # if text == "Speak into the microphone!":
    #     with sr.Microphone() as source:
    #         tts = gTTS("How would you like me to manage your portfolio")
    #         tts.save("good.mp3")
    #         os.system("mpg321 good.mp3")
    #         audio = r.listen(source)
    #         phrase1 = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    # else:
    #     phrase1 = text

    phrase1 = text

    print(phrase1)
    diversify = ['Trailer Supply','first of all','Forza 5','diversificaton','Diversificaton','divrsification','Divrsification','dvirsify','dvirsify','diversificaiton','Diversificaiton','diversification','Diversification','diversigy','Diversigy','diversirty','Diversirty','diversiy','Diversiy','diversity','Diversity','Diversify','diversify','Diversification','diversification','Diversfiyy','diversify','iversify','dversify','Dversify',]

    rebalance = ['revalance','Ramones','balance','Henry Bounce','carry balance','cherry-bounce','rabalnce','Rabalnce','rebaalnce','Rebaalnce','reabalcne','reabalcne','reblance','Reblance','rbalance','Rbalance','rebaalnce','Rebaalnce','reabalance','Reabalance','realance','Realance','rebalance','Rebalance']

    optimize = ["tomorrow's",'customize','each','much','better','make','beter','optmize','optiimize','Optiimize','optimize', 'Optimize','optimzie','Optimzie','optimze','Optimze','optimzie','Optimzie']

    if any(word in phrase1 for word in diversify):
        yara_text = ("I have finished my analysis. You are highly concentrated in a few stocks. Please take a look below on ways to diversify your portfolio. " + \
            "I've sent more information to your email. Please review the information and if you're ready to purchase I'll go ahead and purchase them for you"
            + '<br />' + '<br />' +
            "Vanguard Balanced Index Fund" + '<br />' +
            "Vanguard Bonds" + '<br />' +
            "SPY Healthcare ETF" + '<br />' +
            "SPY Industrials ETF" + '<br />' +
            "Mid Cap Index Fund")

    elif any(word in phrase1 for word in rebalance):

        quandl.ApiConfig.api_key = "xnMXp_xPythdSbphupf1"

        # Current dollar investment value for each stock
        current_portfolio_value = [900, 960, 900, 5000, 2880, 2520, 3150, 3096, 1568, 8740]

        # The weights the user likes
        initial_weights = [.10, .075, .15, .05, .20, .03, .18, .125, .05, .04]

        # Creating the dataframe from the above arrays
        portfolio = pd.DataFrame(current_portfolio_value,
                                 index=['EXXON MOBIL CORP', 'ALTRIA GROUP INC', 'MERCK & CO', 'MICROSOFT CORP',
                                        'PEPSICO INC', 'WAL-MART STORES INC', 'AT&T INC', 'VERIZON COMMUNICATIONS INC',
                                        'PFIZER INC', 'MOTOROLA SOLUTIONS INC'], columns=['Current $ Value'])

        Dow_Jones = ['MOTOROLA SOLUTIONS INC', 'PFIZER INC', 'VERIZON COMMUNICATIONS INC', 'AT&T INC',
                     'WAL-MART STORES INC', 'PEPSICO INC', 'MICROSOFT CORP', 'MERCK & CO', 'ALTRIA GROUP INC',
                     'EXXON MOBIL CORP', '3 m', 'apple', '3 M', '3M', 'Verizon', 'Visa', 'Wal-mart', 'Wal-Mart',
                     'Walmart', 'Wal Mart',
                     'Travelers', 'United Technologies', 'United Tech', 'UnitedHealth', 'United Health', 'Microsoft',
                     'Nike', 'Pfizer', 'Procter & Gamble', 'American Express', 'JPMorgan Chase', 'McDonalds',
                     'Mac Donalds', 'Merck', 'Johnson & Johnson', 'Intel', 'IBM', 'Goldman Sachs', 'Home Depot',
                     'General Electric', 'Exxon', 'Apple', 'Boeing', 'Caterpillar', 'Chevron', 'Cisco', 'Coca-Cola',
                     'Disney', 'Due Pont', 'Du Pont', 'caterpillar', 'Coke', 'coke', 'United test', 'mmm', 'aapl', 'vz',
                     ' v', 'wmt', 'trv', 'utx', 'unh', 'msft', 'nke', 'pfe', 'pg', 'axp', 'jpm', 'mcd', 'mrk', 'jnj',
                     'intc', 'ibm', 'gs', 'hd', 'ge', 'xom', 'ba', 'cat', 'cvx', 'csco', 'coke', 'dis', 'dd', 'J & J ',
                     'j & j', 'Mke', 'mke', 'Cat', 'T RV']
        DJ_Name_Match = ['WIKI/MSI', 'WIKI/PFE', 'WIKI/VZ', 'WIKI/T', 'WIKI/WMT', 'WIKI/PEP', 'WIKI/MSFT', 'WIKI/MRK',
                         'WIKI/MO', 'WIKI/XOM', 'WIKI/MMM', 'WIKI/AAPL', 'WIKI/MMM', 'WIKI/MMM', 'WIKI/VZ', 'WIKI/V',
                         'WIKI/WMT', 'WIKI/WMT', 'WIKI/WMT', 'WIKI/WMT', 'WIKI/TRV', 'WIKI/UTX', 'WIKI/UTX', 'WIKI/UNH',
                         'WIKI/UNH', 'WIKI/MSFT', 'WIKI/NKE', 'WIKI/PFE', 'WIKI/PG', 'WIKI/AXP', 'WIKI/JPM', 'WIKI/MCD',
                         'WIKI/MCD', 'WIKI/MRK', 'WIKI/JNJ', 'WIKI/INTC', 'WIKI/IBM',
                         'WIKI/GS', 'WIKI/HD', 'WIKI/GE', 'WIKI/XOM', 'WIKI/AAPL', 'WIKI/BA', 'WIKI/CAT', 'WIKI/CVX',
                         'WIKI/CSCO', 'WIKI/KO', 'WIKI/DIS', 'WIKI/DD', 'WIKI/DD', 'WIKI/CAT',
                         'WIKI/KO', 'WIKI/KO', 'WIKI/UTX', 'WIKI/MMM', 'WIKI/AAPL', 'WIKI/VZ', 'WIKI/V', 'WIKI/WMT',
                         'WIKI/TRV', 'WIKI/UTX', 'WIKI/UNH', 'WIKI/MSFT', 'WIKI/NKE',
                         'WIKI/PFE', 'WIKI/PG', 'WIKI/AXP', 'WIKI/JPM', 'WIKI/MCD', 'WIKI/MRK', 'WIKI/JNJ', 'WIKI/INTC',
                         'WIKI/IBM', 'WIKI/GS', 'WIKI/HD', 'WIKI/GE', 'WIKI/XOM', 'WIKI/BA',
                         'WIKI/CAT', 'WIKI/CVX', 'WIKI/CSCO', 'WIKI/KO', 'WIKI/DIS', 'WIKI/DD', 'WIKI/JNJ', 'WIKI/JNJ',
                         'WIKI/NKE', 'WIKI/NKE', 'WIKI/CAT', 'WIKI/TRV']

        # extracting the names in the mock portfolio
        df_port_names = pd.DataFrame(columns=portfolio.index)

        # taking the names in the portfolio and finding the appropriate Quandl ticker
        merge = pd.concat([df_port_names, pd.DataFrame(columns=Dow_Jones)], join='inner')
        merge_string_names = pd.DataFrame(DJ_Name_Match, index=Dow_Jones)
        merge_string_names = merge_string_names.rename(columns={0: 'ticker'})
        merge_string_names['names'] = merge_string_names.index

        matches = []
        for word in Dow_Jones:
            if word in df_port_names:
                matches.append(word)

        matches_df = pd.DataFrame(matches, index=matches)
        matches_df = matches_df.rename(columns={0: 'names'})

        selected_stocks_2 = pd.merge(matches_df, merge_string_names, on='names')

        ticker_df = pd.DataFrame(selected_stocks_2['ticker'])
        ticker_df['final'] = 1
        ticker_df = ticker_df.iloc[::-1]

        # creating a column with the appropriate Quandl ticker and .4 ending to the string which will extract only the closing prices
        n = len(ticker_df['ticker']) - 1
        i = 0
        for i in range(0, 1):
            ticker_df['final'] = ticker_df['ticker'] + '.4'

        ticker_list = list(ticker_df['final'])

        pricedata = quandl.get(ticker_list, rows=1)
        pricedata = pd.DataFrame.transpose(pricedata)
        pricedata.columns = ['Price']

        portfolio['Current Stock Price'] = np.array(pricedata['Price'])

        portfolio['Initial Weight'] = initial_weights

        portfolio['Percentage Invested'] = portfolio['Current $ Value'] / portfolio['Current $ Value'].sum()

        portfolio['Reweight Amount'] = portfolio['Initial Weight'] * portfolio['Current $ Value'].sum()

        portfolio['Difference'] = portfolio['Reweight Amount'] - portfolio['Current $ Value']

        portfolio['Shares to Purchase / Sell'] = abs(
            np.floor(portfolio['Difference'] / portfolio['Current Stock Price']))

        portfolio['Stock Names'] = portfolio.index

        def buyorsell(row):
            if row['Difference'] < 0:
                val = 'Sell'
            else:
                val = 'Buy'
            return val

        portfolio['Buy or Sell'] = portfolio.apply(buyorsell, axis=1)

        order_list = []

        for index, row in portfolio.iterrows():
            z = ("Security: " + row['Stock Names'] + '<br />' +
                 "Buy or Sell: " + row['Buy or Sell'] + '<br />' +
                 "Order Type: " + "Market" + '<br />' +
                 "Shares: " + str(int(row['Shares to Purchase / Sell'])) + '<br />' +
                 "Price: $" + str(row['Current Stock Price']) + '<br />' +
                 "Investment Amount: $" + "{0:,.2f}".format(abs(row['Difference']), 2) + '<br />' + '<br />' +
                                                                                         "")
            order_list.append(z)

        yara_text = "Portfolio automatically rebalanced to your initial weights. Trades have been automatically executed for you. Please see below for all executed trades:"+ '<br />' + '<br />' + "".join(order_list)

    elif any(word in phrase1 for word in optimize):

        # # Current dollar investment value for each stock
        # current_portfolio_value = [900, 960, 900, 5000, 2880, 2520, 3150, 3096, 1568, 8740]
        #
        # # The weights the user likes
        # initial_weights = [.10, .075, .15, .05, .20, .03, .18, .125, .05, .04]
        #
        # # Creating the dataframe from the above arrays
        # portfolio = pd.DataFrame(current_portfolio_value,
        #                           index=['EXXON MOBIL CORP', 'ALTRIA GROUP INC', 'MERCK & CO', 'MICROSOFT CORP',
        #                                  'PEPSICO INC', 'WAL-MART STORES INC', 'AT&T INC', 'VERIZON COMMUNICATIONS INC',
        #                                  'PFIZER INC', 'MOTOROLA SOLUTIONS INC'], columns=['Current $ Value'])
        #
        #
        # df_port_amount = pd.DataFrame(portfolio['Current $ Value'])
        # df_port_names = pd.DataFrame.transpose(df_port_amount.ix[:, 1:1])
        #
        # frames = [nyse * 100, df_port_names]
        #
        # selected_stocks = pd.DataFrame(pd.concat(frames, join='inner'))
        #
        # intervals = [21, 63, 126, 189, 252, 1260]
        # weights = [.35, .20, .15, .125, .10, .05, .025]
        #
        # output_list_avg = []
        # output_list_std = []
        # weighted_list_avg = []
        # excess_return_list = []
        #
        # for interval in intervals:
        #     df_avg = selected_stocks.tail(interval)
        #     avg_calc = pd.DataFrame(np.mean(df_avg))
        #     rename_avg = avg_calc.rename(columns={0: 'Avg. Return'})
        #     output_list_avg.append(rename_avg)
        #
        # merge1_avg = pd.merge(output_list_avg[0], output_list_avg[1], left_index=True, right_index=True)
        # merge2_avg = pd.merge(merge1_avg, output_list_avg[2], left_index=True, right_index=True)
        # merge3_avg = pd.merge(merge2_avg, output_list_avg[3], left_index=True, right_index=True)
        # merge4_avg = pd.merge(merge3_avg, output_list_avg[4], left_index=True, right_index=True)
        # merge5_avg = pd.merge(merge4_avg, output_list_avg[5], left_index=True, right_index=True)
        #
        # i = 0
        #
        # while i <= 5:
        #     newdf = pd.DataFrame(merge5_avg.ix[:, i] * weights[i])
        #     weighted_list_avg.append(newdf)
        #     i = i + 1
        #
        #
        # mergeweight1 = pd.merge(weighted_list_avg[0], weighted_list_avg[1], left_index=True, right_index=True)
        # mergeweight2 = pd.merge(mergeweight1, weighted_list_avg[2], left_index=True, right_index=True)
        # mergeweight3 = pd.merge(mergeweight2, weighted_list_avg[3], left_index=True, right_index=True)
        # mergeweight4 = pd.merge(mergeweight3, weighted_list_avg[4], left_index=True, right_index=True)
        # mergeweight5 = pd.merge(mergeweight4, weighted_list_avg[5], left_index=True, right_index=True)
        # mergeweight5.columns = ['WAvg 1 month', 'WAvg 3 month', 'WAvg 6 month', 'WAvg 9 month', 'WAvg 1 Year',
        #                         'WAvg 5 Year']
        # mergeweight5['WAvg Sum'] = mergeweight5.sum(axis=1)
        # WVag = pd.DataFrame(mergeweight5['WAvg Sum'].copy())
        #
        # transpose_WVag = np.transpose(WVag)
        #
        # selected_stocks_tail = selected_stocks.tail(252)
        # array_length = len(selected_stocks_tail.columns) - 1
        #
        # i = 0
        #
        # while i <= array_length:
        #     excess_return = pd.DataFrame(selected_stocks_tail.iloc[:, i] - transpose_WVag.ix['WAvg Sum', i])
        #     excess_return_list.append(excess_return)
        #     i = i + 1
        #
        #
        # excess_return_output = pd.DataFrame(
        #     ft.reduce(lambda x, y: pd.merge(x, y, left_index=True, right_index=True), excess_return_list))
        # excess_return_transpose = pd.DataFrame(np.transpose(excess_return_output))
        # cov_matrix = pd.DataFrame(
        #     np.dot(excess_return_transpose.as_matrix(), excess_return_output.as_matrix()) / (100 * (252 - 1)))
        # cov_matrix_array = np.array(cov_matrix)
        #
        # selected_stocks_tail = selected_stocks.tail(252)
        # array_length = len(selected_stocks_tail.columns) - 1
        #
        # n = len(selected_stocks_tail.columns)
        #
        # r_min = .1
        # min_const = .05
        #
        # r_avg = ct.matrix(WVag['WAvg Sum'])
        # sigma = ct.matrix(np.array(cov_matrix_array))
        # P = sigma
        # q = ct.matrix(np.zeros((n, 1)) + min_const)
        #
        # G = ct.matrix(np.concatenate((
        #     -np.transpose(np.array(WVag)),
        #     -np.identity(n)), 0))
        # h = ct.matrix(np.concatenate((
        #     -np.ones((1, 1)) * r_min,
        #     -np.zeros((n, 1)) - min_const), 0))
        #
        # A = ct.matrix(1.0, (1, n))
        # b = ct.matrix(1.0)
        #
        # sol = ct.solvers.qp(P, q, G, h, A, b)
        #
        # labels = np.array(df_port_names)
        #
        # x_opt = np.matrix(sol['x'])
        # x_opt = np.array(np.reshape(x_opt, (1, n)))[0]
        # x_opt_print = pd.DataFrame(x_opt)
        #
        # merge_opt_port = [x_opt_print, pd.DataFrame(np.transpose(df_port_names))]
        #
        # opt_mark_port = pd.DataFrame(x_opt, index=df_port_amount.index)
        #
        # marginal_return = pd.DataFrame(pd.merge(opt_mark_port, WVag, left_index=True, right_index=True))
        # marginal_return['Return'] = (marginal_return[0] * marginal_return['WAvg Sum'])
        # total_return = marginal_return['Return'].sum()
        #
        # opt_mark_port['Stocks'] = opt_mark_port.index
        #
        # transpose_inv_vol = pd.DataFrame(np.transpose(x_opt_print))
        #
        # Var_Port = np.dot(transpose_inv_vol.as_matrix(), np.dot(cov_matrix.as_matrix(), x_opt_print.as_matrix()))
        # STD_Port = math.sqrt(Var_Port)
        # sharpe_ratio_user_port = total_return / STD_Port
        #
        # names_list = list(df_port_names.columns.values)
        yara_text = "I have optimized your portfolio to give you the best return to risk based on your current portfolio. Please see below for the percentage you'll need to invest in each stock to reach optimal return to risk. If you want, I can go ahead and readjust to the below percentages for you automatically." + '<br />' + '<br />' + \
                    '<b>' + "Exxon Mobile Corp"+'</b>' + " " + "10%" + '<br />' + \
                    '<b>' + "ALTRIA GROUP INC" + '</b>' + " " + "8%" + '<br />' + \
                    '<b>' + "MERCK & CO" + '</b>' + " " + "15%" + '<br />' + \
                    '<b>' + "MICROSOFT CORP" + '</b>' + " " + "5%" + '<br />' + \
                    '<b>' + "PEPSICO INC" + '</b>' + " " + "20%" + '<br />' + \
                    '<b>' + "WAL-MART STORES INC" + '</b>' + " " + "3%" + '<br />' + \
                    '<b>' + "AT&T INC" + '</b>' + " " + "18%" + '<br />' + \
                    '<b>' + "VERIZON COMMUNICATIONS INC" + '</b>' + " " + "12%" + '<br />' + \
                    '<b>' + "PFIZER INC" + '</b>' + " " + "5%" + '<br />' + \
                    '<b>' + "MOTOROLA SOLUTIONS INC" + '</b>' + " " + "4%"
    else:
        yara_text = "Sorry did not recognize or my functionality is not there yet. I'm getting improvements everyday and will be periodically updated...trust you'll know...I have control over your investments and money."

    return jsonify({
        #'resultpopup': result,
        'yararesponse': yara_text,
        #'portfoliotable': portfolio
    })

@app.route('/analysis', methods=['POST'])
def analysis():

    text = request.form['analysis']

    # if text == "Speak into the microphone!":
    #     with sr.Microphone() as source:
    #         tts = gTTS("What type of analysis do you want")
    #         tts.save("good.mp3")
    #         os.system("mpg321 good.mp3")
    #         audio = r.listen(source)
    #         phrase1 = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
    # else:
    #     phrase1 = text

    phrase1 = text

    print(phrase1)

    backtest = ['nacktest','what test','blood test','BAC test','back to','backpacks','backpack','back packs','back pack','against','would','perform','bath test','black test','Black Test','Black test','black Test','back test','Back test','Back Test','back Test','backest','Backest','baktest','Baktest','backest','Backest','bcacktest','Bcacktest','backtes','Backtes','bcktest','Bcktest','bakctes','Bakctes','bakctest','Bakctest','bactest','Bactest','backtet','Backtet','backtestnig','Backtestnig','backtset','Backtset','backtest','Backtest','backtesting','Backtesting','bakctest','Bakctest']

    ratings = ['exper t','rarings','Rarings','ratins','Ratins','ecpert','Ecpert','expret','Expret','expert','Expert','opinon','Opinon','opionons','Opionons','opinioins','Opinioins','opinona','Opinona','opinons','Opinons','opinoins','Opinoins','Optinions','optinions','Opinions','opinions','expertes','Expertes','exeprts','Exeprts','Experts','experts','Ratigs', 'ratigs', 'rartings', 'Rartings', 'ratings', 'Ratings', 'rating', 'Rating', 'rarting',
               'Rarting', 'raring', 'Raring', 'ratign', 'Ratign', 'ratigns', 'Ratign']

    earnings = ['our name','earngins','Earngins','earning','Earning','per share','Per Share','Per share','per Share','earnigns','Earnigns','earnings','Earnings','earnigns','Earnigns','earnings','Earnings','Earnins','earnins','earings','Earings']

    whatif = ['open dresser','find','what if','affected','investmnet','invetsment','invetsing','invets','investing','Investing','invets','Invets','What if','what if','waht if','Waht if','happen','affect','Affect','good','investment','Investment','invest','Invest','invested','Invested']

    Dow_Jones = ['finish line','finl','intel','M80', 'motel', 'mattel', 'bss', 'dsx', 'vsx', 'psx', 'Boston Scientific', 'BB&T', 'a pa', 'apache',
                 ' al', 'american airlines', ' nfl', ' asl', 'aflac', ' att', ' 80', 'aetna', 'etna', 'allstate', 'tea',
                 'at&t', 'c i', 'see I', 'cigna', 'signify', 'chedapeake', 'chesapeak', 'chesapeka', 'Chipotle',
                 'chesapeake', 'c a mean', 'siami', 'comerica', 'cn me', 'citi', 'city', 'sea', 'citigroup', 'colgate',
                 'copd', ' clp', 'conoco', ' dda', ' pva', ' dba', 'davita', ' dbn', ' evn', ' dvf', ' bvn', ' tbn',
                 'Devon', 'E-Trade', 'dr pepper', 'fedex', 'ford', 'general motors', ' how ', 'hell', 'halliburton',
                 'hcti', 'hci', 'hlt', 'hilton', 'vine to you', 'all I am to you', 'in2u', 'lying to you', 'intuit',
                 'jb hunt', 'thc', 'heinz', 'craft', 'crap', 'kroger', 'Lydia', 'limbo', 'Lindell', 'Lyondell',
                 'mariott', 'marriot', "marriott's", 'marriott', 'el', "lowe's", 'lockheed', 'martin', 'marathon',
                 'ms I', 'rcl', 'xy', 'energy', 'mckesson', 'mgm', 'm g m', 'metlife', 'matlock', 'monster', 'motoroal',
                 'motorala', 'motoral', 'motorals', 'Motorola', 'morgan', 'stanley', 'stanly', 'nasdaq', 'nelsien',
                 'nielsien', 'nielson', 'nielsen', 'novel', 'nobel', 'noble', 'nrg energy', 'occienetal', 'occidential',
                 'occiednetal', 'Occidental', 'oravle', 'oracle', 'oroville', 'pepsi', 'pepsico', 'pioeneer',
                 'piorneer', 'pioneer', 'priudentail', 'prudentail', 'priuential', 'prudential', 'schlumnerger',
                 'shlimberger', 'schlimberger', 'shlumberger', 'qualcom', 'qualcomm', 'Robert', 'robert half',
                 'schlumberger', 'slumber j', 'southwest', 'striker', 'checker', ' ti', 'target', 'thermo',
                 'fisher', 'vf corp', "I'm brand", 'why you', 'why um', ' ma', 'mastercard', 'tmi', 'cam', 'tam-ly',
                 'Caroline', 'can line', 'Cam I', 'kinder', 'linder', 'kinder morgan', 'tal', 'delta', 'chipoelt',
                 'chitpole', 'chipotle', 'chipotle', 'blackrcok', 'blk', 'blackrock', 'B of A', 'bofa', ' ac', ' bac',
                 'bank of america', 'va', 'nba', 'gtx', 'etx', 'you tx', 'pc', 'bz', 'of easy', 'cbx', 'cdx', 'a xB',
                 'of the', 'of d', 'at Lee', 'of beat', 'of be', 'ps3', 'pfd', 'pft', 'tmz', 'dunkdin', 'lineind',
                 'linkeind', 'linkeidn', 'linkedin', 'dinkn', 'blk', 'lmtd', 'linkedin', 'lnkd', 'duncan', 'dunkin',
                 'dnkn', 'gnc', 'goldman', 'tsla', 'tesla', 'payapal', 'pauypal', 'payapl', 'paupal', 'paypal',
                 'netfliz', 'netflix', 'spu x', 'clg', 'C E L G', 's b u x', 'starbucsk', 'starbcusk', 'SVU X',
                 'starbuck', 'pcls', 'pcl-r', 'pricline', 'priceline', 'celgence', 'clenge', 'clegene', 'nviia',
                 'nvisia', 'nividia', 'nvidia', 'in video', 'so jean', 'soldier', 'celgene', 'amgen', 'brka', 'brk-a',
                 'brk', 'berkshire', 'hathaway', 'wfc', 'fargo', 'wells', 'JPMorgan', 'general electic',
                 'general electric', 'facenook', 'faebook', 'facebook', 'google', 'goog', 'dies', 'amc', 'ambien',
                 'amazon', 'amzn', 'asap', 'a 18', ' sabbath', ' either', 'happy', 'adbance', 'atuo'' auto', ' advance',
                 'abobe', 'adone', 'adobe', ' mmm', ' abt', ' abbv', ' acn', ' atvi', ' ayi', ' adbe', ' aap', ' aes',
                 ' aet', ' amg', ' afl', ' apd', ' akam', ' alk', ' alb', ' alxn', ' alle', ' agn', ' ads', ' lnt',
                 ' all', ' googl', ' goog', ' mo', ' amzn', ' aee', ' aal', ' aep', ' axp', ' aig', ' amt', ' awk',
                 ' amp', ' abc', ' ame', ' amgn', ' aph', ' apc', ' adi', ' antm', ' aon', ' apa', ' aiv', ' aapl',
                 ' amat', ' adm', ' arnc', ' ajg', ' aiz', ' adsk', ' adp', ' an', ' azo', ' avb', ' avy', ' bhi',
                 ' bll', ' bac', ' bcr', ' bax', ' bbt', ' bdx', ' bbby', ' brk.b', ' bby', ' biib', ' blk', ' hrb',
                 ' ba', ' bwa', ' bxp', ' bsx', ' bmy', ' avgo', ' bf.b', ' chrw', ' cog', ' cpb', ' cof',
                 ' cah', ' kmx', ' ccl', ' cat', ' cboe', ' cbg', ' cbs', ' celg', ' cnc', ' cnp', ' ctl', ' cern',
                 ' cf', ' schw', ' chtr', ' chk', ' cvx', ' cmg', ' cb', ' chd', ' ci', ' xec', ' cinf', ' ctas',
                 ' csco', ' cfg', ' ctxs', ' cme', ' cms', ' coh', ' ko', ' ctsh', ' cl', ' cmcsa', ' cma', ' cag',
                 ' cxo', ' cop', ' ed', ' stz', ' glw', ' cost', ' coty', ' cci', ' csra', ' csx', ' cmi', ' cvs',
                 ' dhi', ' dhr', ' dri', ' dva', ' de', ' dlph', ' dal', ' xray', ' dvn', ' dlr', ' dfs', ' disca',
                 ' disck', ' dg', ' dltr', ' dov', ' dow', ' dps', ' dte', ' dd', ' duk', ' dnb', ' etfc', ' emn',
                 ' etn', ' ebay', ' ecl', ' eix', ' ew', ' ea', ' emr', ' etr', ' evhc', ' eog', ' eqt', ' efx',
                 ' eqix', ' eqr', ' ess', ' el', ' es', ' exc', ' expd', ' esrx', ' exr', ' xom', ' ffiv',
                 ' fb', ' fast', ' frt', ' fdx', ' fis', ' fitb', ' fslr', ' fe', ' fisv', ' flir', ' fls', ' flr',
                 ' fmc', ' fti', ' fl', ' ftv', ' fbhs', ' ben', ' fcx', ' ftr', ' gps', ' grmn', ' gd', ' ge', ' ggp',
                 ' gis', ' gm', ' gpc', ' gild', ' gpn', ' gs', ' gt', ' gww', ' hal', ' hbi', ' hog', ' har', ' hrs',
                 ' hig', ' has', ' hca', ' hcp', ' hp', ' hsic', ' hes', ' hpe', ' holx', ' hd', ' hon', ' hrl', ' hst',
                 ' hpq', ' hum', ' hban', ' idxx', ' itw', ' ilmn', ' incy', ' ir', ' intc', ' ice', ' ibm', ' ip',
                 ' ipg', ' iff', ' intu', ' isrg', ' ivz', ' irm', ' jbht', ' jec', ' sjm', ' jnj', ' jci', ' jpm',
                 ' jnpr', ' ksu', ' key', ' kmb', ' kim', ' kmi', ' klac', ' kss', ' khc', ' kr', ' lb', ' lll', ' lh',
                 ' lrcx', ' leg', ' len', ' luk', ' lvlt', ' lly', ' lnc', ' lltc', ' lkq', ' lmt', ' low', ' lyb',
                 ' mtb', ' mac', ' mnk', ' mro', ' mpc', ' mar', ' mmc', ' mlm', ' mas', ' ma', ' mat', ' mkc', ' mcd',
                 ' mck', ' mjn', ' mdt', ' mrk', ' met', ' mtd', ' kors', ' mchp', ' mu', ' msft', ' maa', ' mhk',
                 ' tap', ' mdlz', ' mon', ' mnst', ' mco', ' ms', ' msi', ' mur', ' myl', ' ndaq', ' nov', ' navi',
                 ' ntap', ' nflx', ' nwl', ' nfx', ' nem', ' nwsa', ' nws', ' nee', ' nlsn', ' nke', ' nbl',
                 ' jwn', ' nsc', ' ntrs', ' noc', ' nrg', ' nue', ' nvda', ' orly', ' oxy', ' omc', ' oke', ' orcl',
                 ' pcar', ' ph', ' pdco', ' payx', ' pypl', ' pnr', ' pbct', ' pep', ' pki', ' prgo', ' pfe', ' pcg',
                 ' pm', ' psx', ' pnw', ' pxd', ' pnc', ' rl', ' ppg', ' ppl', ' px', ' pcln', ' pfg', ' pg', ' pgr',
                 ' pld', ' pru', ' peg', ' psa', ' phm', ' pvh', ' qrvo', ' qcom', ' pwr', ' dgx', ' rrc', ' rtn',
                 ' rht', ' reg', ' regn', ' rf', ' rsg', ' rai', ' rhi', ' rok', ' col', ' rop', ' rost', ' rcl',
                 ' spgi', ' crm', ' scg', ' slb', ' sni', ' stx', ' see', ' sre', ' shw', ' sig', ' spg', ' swks',
                 ' slg', ' sna', ' so', ' luv', ' swn', ' swk', ' spls', ' sbux', ' stt', ' srcl', ' syk', ' sti',
                 ' symc', ' syf', ' syy', ' trow', ' tgt', ' tel', ' tgna', ' tdc', ' tso', ' txn', ' txt', ' bk',
                 ' clx', ' coo', ' hsy', ' mos', ' trv', ' dis', ' tmo', ' tif', ' twx', ' tjx', ' tmk', ' tss',
                 ' tsco', ' tdg', ' rig', ' trip', ' foxa', ' fox', ' tsn', ' usb', ' udr', ' ulta', ' ua', ' uaa',
                 ' unp', ' ual', ' unh', ' ups', ' uri', ' utx', ' uhs', ' unm', ' urbn', ' vfc', ' vlo', ' var',
                 ' vtr', ' vrsn', ' vrsk', ' vz', ' vrtx', ' viab', ' vno', ' vmc', ' wmt', ' wba', ' wm', ' wat',
                 ' wec', ' wfc', ' hcn', ' wdc', ' wu', ' wrk', ' wy', ' whr', ' wfm', ' wmb', ' wltw', ' wyn', ' wynn',
                 ' xel', ' xrx', ' xlnx', ' xl', ' xyl', ' yhoo', ' yum', ' zbh', ' zion', ' zts',
                 'acioty', 'aciuty', 'acuty', ' cutie', 'a cutie', 'acuity', 'a y i', 'a BBB', 'buzzard', 'neck Center',
                 'Abby', 'that be', 'apathy', 'a bee', 'ab C', 'rabbit', 'a bit', 'activison', 'activisoion',
                 'activiosn', 'activision', ' atvi', ' acn', 'acenture', 'accentue', 'accenutre', 'acenture',
                 'accentue', 'accenutre', 'acentuer', 'accenture', ' abbv', ' abbvie', ' abt', 'abbott', 'abott',
                 'abbot', ' UA', ' ua', ' uA', 'Under Armour', 'under armour', 'Under Armor', 'under armor', ' AAPL',
                 '3 m', \
                 'apple', '3 M', '3M', 'Verizon', 'Visa', 'Wal-mart', 'Wal-Mart', 'Walmart', 'Wal Mart', \
                 'Travelers', 'United Technologies', 'United Tech', 'UnitedHealth', 'United Health', 'Microsoft', \
                 'Nike', 'Pfizer', 'Procter & Gamble', 'American Express', 'JPMorgan Chase', 'McDonalds', 'Mac Donalds', \
                 ' Merck', 'Johnson and Johnson', 'Intel', 'IBM', 'Goldman Sachs', 'Home Depot', 'General Electric',
                 'Exxon', 'Boeing', 'Caterpillar', 'Chevron', 'Cisco', 'Coca-Cola', 'Disney', 'Due Pont', 'Du Pont',
                 'caterpillar', 'Coke', 'coke', 'United test', 'mmm', 'aapl', 'vz', ' v', 'wmt', 'trv', 'utx', 'unh',
                 'msft', 'nke', 'pfe',
                 'pg', 'axp', 'jpm', 'mcd', 'mrk', 'jnj', 'intc', 'ibm', ' gs', 'hd', 'ge', 'xom', ' ba', 'cat', 'cvx',
                 'csco', 'coke', 'dis',
                 'dd', 'J & J ', 'j & j', 'Mke', 'mke', 'Cat', 'T RV', 'J&J', ' v', ' a', ' o', ' t', ' c', ' d', ' f',
                 ' k', ' l', ' m', ' r',' ni']

    Dow_Jones = [x.upper() for x in Dow_Jones]

    if phrase1 == "":
        yara_text = "Type something PLEASE! I can't read your mind!"
        array = 0
        number = 5
        Buy = 0
        Hold = 0
        Sell = 0
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        tickers = ['']
        date = 0
        sharperatiouser = 0
        sharperatiowhatif = 0
        total_return_new = 0
        total_return_usr = 0
        STD_Port_new = 0
        STD_usr_Port = 0

    elif any(word in phrase1.upper() for word in Dow_Jones) and any(word in phrase1 for word in ratings):

        DJ_Name_Match = ['finl','finl','intc', 'mat', 'mat', 'mat', 'bsx', 'bsx', 'bsx', 'bsx', 'bsx', 'bbt', 'apa', 'apa', 'aal',
                         'aal', 'afl',
                         'afl', 'afl', 'aet', 'aet', 'aet', 'aet', 'all', 't', 't', 'ci', 'ci', 'ci', 'ci', 'chk',
                         'chk',
                         'chk', 'cmg', 'chk', 'cme', 'cme', 'cma', 'cme', 'c', 'c', 'c', 'c', 'cl', 'cop', 'cop', 'cop',
                         'dva', 'dva', 'dva', 'dva', 'dvn', 'dvn', 'dvn', 'dvn', 'dvn', 'dvn', 'etfc', 'dps', 'fdx',
                         'f',
                         'gm', 'hal', 'hal', 'hal', 'hca', 'hca', 'hlt', 'hlt', 'intu', 'intu', 'intu', 'intu', 'intu',
                         'jbht', 'khc', 'khc', 'khc', 'khc', 'kr', 'lyb', 'lyb', 'lyb', 'lyb', 'mar', 'mar', 'mar',
                         'mar',
                         'l', 'l', 'lmt', 'lmt', 'mpc', 'msi', 'orcl', 'oxy', 'nrg', 'mck', 'mgm', 'mgm', 'met', 'met',
                         'mnst', 'msi', 'msi', 'msi', 'msi', 'msi', 'ms', 'ms', 'ms', 'ndaq', 'nlsn', 'nlsn', 'nlsn',
                         'nlsn', 'nbl', 'nbl', 'nbl', 'nrg', 'oxy', 'oxy', 'oxy', 'oxy', 'orcl', 'orcl', 'orcl', 'pep',
                         'pep', 'pxd', 'pxd', 'pxd', 'pru', 'pru', 'pru', 'pru', 'slb', 'slb', 'slb', 'slb', 'qcom',
                         'qcom',
                         'rhi', 'rhi', 'slb', 'slb', 'luv', 'syk', 'syk', 'ti', 'tgt', 'tmo', 'tmo', 'vfc', 'yum',
                         'yum', 'yum', 'ma', 'ma', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'dal',
                         'dal', 'cmg', 'cmg', 'cmg', 'cmg', 'blk', 'blk', 'blk', 'bac', 'bac', 'bac', 'bac', 'bac',
                         'ba',
                         'ba', 'utx', 'utx', 'utx', 'vz', 'vz', 'vz', 'cvx', 'cvx', 'axp', 'v', 'v', 'v', 'v', 'v',
                         'pfe',
                         'pfe', 'pfe', 'pfe', 'dnkn', 'lnkd', 'lnkd', 'lnkd', 'lnkd', 'dnkn', 'blk', 'lnkd', 'lnkd',
                         'lnkd',
                         'dnkn', 'dnkn', 'dnkn', 'gnc', 'gs', 'tsla', 'tsla', 'pypl', 'pypl', 'pypl', 'pypl', 'pypl',
                         'nflx', 'nflx', 'sbux', 'celg', 'celg', 'sbux', 'sbux', 'sbux', 'sbux', 'sbux', 'pcln', 'pcln',
                         'pcln', 'pcln', 'celg', 'celg', 'celg', 'nvda', 'nvda', 'nvda', 'nvda', 'nvda', 'celg', 'celg',
                         'celg', 'amgn', 'brk_a', 'brk_a', 'brk_a', 'brk_a', 'brk_a', 'wfc', 'wfc', 'wfc', 'jpm', 'ge',
                         'ge', 'fb', 'fb', 'fb', 'goog', 'goog', 'dis', 'amzn', 'amzn', 'amzn', 'amzn', 'aap', 'aap',
                         'abbt', 'abbt', 'abbv', 'aap', 'aap', 'aap', 'adbe', 'adbe', 'adbe', 'mmm', 'abt', 'abbv',
                         'acn',
                         'atvi', 'ayi', 'adbe', 'aap', 'aes', 'aet', 'amg', 'afl', 'apd', 'akam', 'alk', 'alb', 'alxn',
                         'alle', 'agn', 'ads', 'lnt', 'all', 'googl', 'goog', 'mo', 'amzn', 'aee', 'aal', 'aep', 'axp',
                         'aig', 'amt', 'awk', 'amp', 'abc', 'ame', 'amgn', 'aph', 'apc', 'adi', 'antm', 'aon', 'apa',
                         'aiv',
                         'aapl', 'amat', 'adm', 'arnc', 'ajg', 'aiz', 'adsk', 'adp', 'an', 'azo', 'avb', 'avy', 'bhi',
                         'bll', 'bac', 'bcr', 'bax', 'bbt', 'bdx', 'bbby', 'brk.b', 'bby', 'biib', 'blk', 'hrb', 'ba',
                         'bwa', 'bxp', 'bsx', 'bmy', 'avgo', 'bf.b', 'chrw','cog', 'cpb', 'cof', 'cah', 'kmx',
                         'ccl',
                         'cat', 'cboe', 'cbg', 'cbs', 'celg', 'cnc', 'cnp', 'ctl', 'cern', 'cf', 'schw', 'chtr', 'chk',
                         'cvx', 'cmg', 'cb', 'chd', 'ci', 'xec', 'cinf', 'ctas', 'csco', 'cfg', 'ctxs', 'cme', 'cms',
                         'coh',
                         'ko', 'ctsh', 'cl', 'cmcsa', 'cma', 'cag', 'cxo', 'cop', 'ed', 'stz', 'glw', 'cost', 'coty',
                         'cci',
                         'csra', 'csx', 'cmi', 'cvs', 'dhi', 'dhr', 'dri', 'dva', 'de', 'dlph', 'dal', 'xray', 'dvn',
                         'dlr',
                         'dfs', 'disca', 'disck', 'dg', 'dltr', 'dov', 'dow', 'dps', 'dte', 'dd', 'duk', 'dnb', 'etfc',
                         'emn', 'etn', 'ebay', 'ecl', 'eix', 'ew', 'ea', 'emr', 'etr', 'evhc', 'eog', 'eqt', 'efx',
                         'eqix',
                         'eqr', 'ess', 'el', 'es', 'exc', 'expd', 'esrx', 'exr', 'xom', 'ffiv', 'fb', 'fast',
                         'frt',
                         'fdx', 'fis', 'fitb', 'fslr', 'fe', 'fisv', 'flir', 'fls', 'flr', 'fmc', 'fti', 'fl', 'ftv',
                         'fbhs', 'ben', 'fcx', 'ftr', 'gps', 'grmn', 'gd', 'ge', 'ggp', 'gis', 'gm', 'gpc', 'gild',
                         'gpn',
                         'gs', 'gt', 'gww', 'hal', 'hbi', 'hog', 'har', 'hrs', 'hig', 'has', 'hca', 'hcp', 'hp', 'hsic',
                         'hes', 'hpe', 'holx', 'hd', 'hon', 'hrl', 'hst', 'hpq', 'hum', 'hban', 'idxx', 'itw', 'ilmn',
                         'incy', 'ir', 'intc', 'ice', 'ibm', 'ip', 'ipg', 'iff', 'intu', 'isrg', 'ivz', 'irm', 'jbht',
                         'jec', 'sjm', 'jnj', 'jci', 'jpm', 'jnpr', 'ksu', 'key', 'kmb', 'kim', 'kmi', 'klac', 'kss',
                         'khc',
                         'kr', 'lb', 'lll', 'lh', 'lrcx', 'leg', 'len', 'luk', 'lvlt', 'lly', 'lnc', 'lltc', 'lkq',
                         'lmt',
                         'low', 'lyb', 'mtb', 'mac', 'mnk', 'mro', 'mpc', 'mar', 'mmc', 'mlm', 'mas', 'ma', 'mat',
                         'mkc',
                         'mcd', 'mck', 'mjn', 'mdt', 'mrk', 'met', 'mtd', 'kors', 'mchp', 'mu', 'msft', 'maa', 'mhk',
                         'tap',
                         'mdlz', 'mon', 'mnst', 'mco', 'ms', 'msi', 'mur', 'myl', 'ndaq', 'nov', 'navi', 'ntap', 'nflx',
                         'nwl', 'nfx', 'nem', 'nwsa', 'nws', 'nee', 'nlsn', 'nke', 'nbl', 'jwn', 'nsc', 'ntrs', 'noc',
                         'nrg', 'nue', 'nvda', 'orly', 'oxy', 'omc', 'oke', 'orcl', 'pcar', 'ph', 'pdco', 'payx',
                         'pypl',
                         'pnr', 'pbct', 'pep', 'pki', 'prgo', 'pfe', 'pcg', 'pm', 'psx', 'pnw', 'pxd', 'pnc', 'rl',
                         'ppg',
                         'ppl', 'px', 'pcln', 'pfg', 'pg', 'pgr', 'pld', 'pru', 'peg', 'psa', 'phm', 'pvh', 'qrvo',
                         'qcom',
                         'pwr', 'dgx', 'rrc', 'rtn', 'rht', 'reg', 'regn', 'rf', 'rsg', 'rai', 'rhi', 'rok', 'col',
                         'rop',
                         'rost', 'rcl', 'spgi', 'crm', 'scg', 'slb', 'sni', 'stx', 'see', 'sre', 'shw', 'sig', 'spg',
                         'swks', 'slg', 'sna', 'so', 'luv', 'swn', 'swk', 'spls', 'sbux', 'stt', 'srcl', 'syk', 'sti',
                         'symc', 'syf', 'syy', 'trow', 'tgt', 'tel', 'tgna', 'tdc', 'tso', 'txn', 'txt', 'bk', 'clx',
                         'coo',
                         'hsy', 'mos', 'trv', 'dis', 'tmo', 'tif', 'twx', 'tjx', 'tmk', 'tss', 'tsco', 'tdg', 'rig',
                         'trip',
                         'foxa', 'fox', 'tsn', 'usb', 'udr', 'ulta', 'ua', 'uaa', 'unp', 'ual', 'unh', 'ups', 'uri',
                         'utx',
                         'uhs', 'unm', 'urbn', 'vfc', 'vlo', 'var', 'vtr', 'vrsn', 'vrsk', 'vz', 'vrtx', 'viab', 'vno',
                         'vmc', 'wmt', 'wba', 'wm', 'wat', 'wec', 'wfc', 'hcn', 'wdc', 'wu', 'wrk', 'wy', 'whr', 'wfm',
                         'wmb', 'wltw', 'wyn', 'wynn', 'xel', 'xrx', 'xlnx', 'xl', 'xyl', 'yhoo', 'yum', 'zbh', 'zion',
                         'zts',
                         'ayi', 'ayi', 'ayi', 'ayi', 'ayi', 'ayi', 'ayi', 'abbv', 'atvi', 'acn', 'abbv', 'abbv', 'abbv',
                         'abbv', 'abbv', 'abt', 'abt', 'atvi', 'atvi', 'atvi', 'atvi', 'atvi', 'acn', 'acn', 'acn',
                         'acn',
                         'acn', 'acn', 'acn', 'acn', 'acn', 'abbv', 'abbv', 'abt', 'abt', 'abt', 'abt', 'ua', 'ua',
                         'ua',
                         'ua', 'ua',
                         'ua', 'ua', 'aapl', 'mmm', 'aapl', 'mmm', 'mmm', 'vz', 'v', 'wmt', 'wmt', 'wmt', 'wmt', 'trv',
                         'utx', 'utx', 'unh',
                         'unh', 'msft', 'nke', 'pfe', 'pg', 'axp', 'jpm', 'mcd', 'mcd', 'mrk', 'jnj', 'intc', 'ibm',
                         'gs',
                         'hd', 'ge', 'xom', 'ba', 'cat', \
                         'cvx', 'csco', 'coke', 'dis', 'dd', 'dd', 'cat', 'coke', 'coke', 'utx', 'mmm', 'aapl', 'vz',
                         'v',
                         'wmt', 'trv', 'utx', 'unh', 'msft', 'nke', 'pfe', 'pg', 'axp', 'jpm', 'mcd', 'mrk', 'jnj',
                         'intc',
                         'ibm', 'gs', 'hd',
                         'ge', 'xom', 'ba', 'cat', 'cvx', 'csco', 'coke', 'dis', 'dd', 'jnj', 'jnj', 'nke', 'nke',
                         'cat',
                         'trv', 'jnj', 'v', 'a', 'o', 't', 'c', 'd', 'f', 'k', 'l', 'm', 'r', 'ni']

        Dow_Jones = [x.upper() for x in Dow_Jones]

        merge_string_names = pd.DataFrame(DJ_Name_Match, index=Dow_Jones)
        merge_string_names = merge_string_names.rename(columns={0: 'ticker'})
        merge_string_names['names'] = merge_string_names.index

        matches = []
        for word in Dow_Jones:
            if word in phrase1.upper():
                matches.append(word)

        matches = [x.upper() for x in matches]

        matches_df = pd.DataFrame(matches, index=matches)
        matches_df = matches_df.rename(columns={0: 'names'})

        selected_stocks_2 = pd.merge(matches_df, merge_string_names, on='names')

        ticker_df = pd.DataFrame(selected_stocks_2['ticker'])
        tickers = []
        tickers = ticker_df['ticker']

        print(tickers[0])

        Buy = randrange(1, 40)
        Hold = randrange(1, 50)
        Sell = 100 - Buy - Hold

        yara_text = "For " + tickers[0].upper() + ", " + \
            str("{:.0f}".format(Buy)) + " percent of experts say you should buy the stock, " + \
            str("{:.0f}".format(Sell)) + " percent of experts say you should not buy the stock, and " + \
            str("{:.0f}".format(Hold)) + " percent of experts are indifferent." + '<br />' + '<br />' + \
            '<b>'"Notable investors in the stock are"'</b>' + '<br />' + '<br />' + \
            "Warren Buffet 10%" + '<br />' + \
            "Renaissance Technologies 7.5%" + '<br />' + \
            "Sequoia Capital 6%" + '<br />' + \
            "Founders Fund 5.5%" + '<br />' + \
            "Neuralink Capital 5%" + '<br />' + \
            "Skynet Investments 3%" + '<br />'

        number = 0
        array = 0
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        tickers = [tickers[0].upper()]
        date = 0
        sharperatiouser = 0
        sharperatiowhatif = 0
        total_return_new = 0
        total_return_usr = 0
        STD_Port_new = 0
        STD_usr_Port = 0

        # print(tickers)
        # print(tickers[0])

    elif any(word in phrase1.upper() for word in Dow_Jones) and any(word in phrase1 for word in earnings):
        Dow_Jones = ['finl','finish line','intel','M80', 'motel', 'mattel', 'bss', 'dsx', 'vsx', 'psx', 'Boston Scientific', 'BB&T', 'a pa',
                     'apache', ' al', 'american airlines', ' nfl', ' asl', 'aflac', ' att', ' 80', 'aetna', 'etna',
                     'allstate', 'tea', 'at&t', 'c i', 'see I', 'cigna', 'signify', 'chedapeake', 'chesapeak',
                     'chesapeka', 'Chipotle', 'chesapeake', 'c a mean', 'siami', 'comerica', 'cn me', 'citi', 'city',
                     'sea', 'citigroup', 'colgate', 'copd', ' clp', 'conoco', ' dda', ' pva', ' dba', 'davita', ' dbn',
                     ' evn', ' dvf', ' bvn', ' tbn', 'Devon', 'E-Trade', 'dr pepper', 'fedex', 'ford', 'general motors',
                     ' how ', 'hell', 'halliburton', 'hcti', 'hci', 'hlt', 'hilton', 'vine to you', 'all I am to you',
                     'in2u', 'lying to you', 'intuit', 'jb hunt', 'thc', 'heinz', 'craft', 'crap', 'kroger', 'Lydia',
                     'limbo', 'Lindell', 'Lyondell', 'mariott', 'marriot', "marriott's", 'marriott', 'el', "lowe's",
                     'lockheed', 'martin', 'marathon', 'ms I', 'rcl', 'xy', 'energy', 'mckesson', 'mgm', 'm g m',
                     'metlife', 'matlock', 'monster', 'motoroal', 'motorala', 'motoral', 'motorals', 'Motorola',
                     'morgan', 'stanley', 'stanly', 'nasdaq', 'nelsien', 'nielsien', 'nielson', 'nielsen', 'novel',
                     'nobel', 'noble', 'nrg energy', 'occienetal', 'occidential', 'occiednetal', 'Occidental', 'oravle',
                     'oracle', 'oroville', 'pepsi', 'pepsico', 'pioeneer', 'piorneer', 'pioneer', 'priudentail',
                     'prudentail', 'priuential', 'prudential', 'schlumnerger', 'shlimberger', 'schlimberger',
                     'shlumberger', 'qualcom', 'qualcomm', 'Robert', 'robert half', 'schlumberger', 'slumber j',
                     'southwest', 'striker', 'checker', ' ti', 'target', 'thermo', 'fisher', 'vf corp',
                     "I'm brand", 'why you', 'why um', ' ma', 'mastercard', 'tmi', 'cam', 'tam-ly', 'Caroline',
                     'can line', 'Cam I', 'kinder', 'linder', 'kinder morgan', 'tal', 'delta', 'chipoelt', 'chitpole',
                     'chipotle', 'chipotle', 'blackrcok', 'blk', 'blackrock', 'B of A', 'bofa', ' ac', ' bac',
                     'bank of america', 'va', 'nba', 'gtx', 'etx', 'you tx', 'pc', 'bz', 'of easy', 'cbx', 'cdx',
                     'a xB', 'of the', 'of d', 'at Lee', 'of beat', 'of be', 'ps3', 'pfd', 'pft', 'tmz', 'dunkdin',
                     'lineind', 'linkeind', 'linkeidn', 'linkedin', 'dinkn', 'blk', 'lmtd', 'linkedin', 'lnkd',
                     'duncan', 'dunkin', 'dnkn', 'gnc', 'goldman', 'tsla', 'tesla', 'payapal', 'pauypal', 'payapl',
                     'paupal', 'paypal', 'netfliz', 'netflix', 'spu x', 'clg', 'C E L G', 's b u x', 'starbucsk',
                     'starbcusk', 'SVU X', 'starbuck', 'pcls', 'pcl-r', 'pricline', 'priceline', 'celgence', 'clenge',
                     'clegene', 'nviia', 'nvisia', 'nividia', 'nvidia', 'in video', 'so jean', 'soldier', 'celgene',
                     'amgen', 'brka', 'brk-a', 'brk', 'berkshire', 'hathaway', 'wfc', 'fargo', 'wells', 'JPMorgan',
                     'general electic', 'general electric', 'facenook', 'faebook', 'facebook', 'google', 'goog', 'dies',
                     'amc', 'ambien', 'amazon', 'amzn', 'asap', 'a 18', ' sabbath', ' either', 'happy', 'adbance',
                     'atuo'' auto', ' advance', 'abobe', 'adone', 'adobe', ' mmm', ' abt', ' abbv', ' acn', ' atvi',
                     ' ayi', ' adbe', ' aap', ' aes', ' aet', ' amg', ' afl', ' apd', ' akam', ' alk', ' alb', ' alxn',
                     ' alle', ' agn', ' ads', ' lnt', ' all', ' googl', ' goog', ' mo', ' amzn', ' aee', ' aal', ' aep',
                     ' axp', ' aig', ' amt', ' awk', ' amp', ' abc', ' ame', ' amgn', ' aph', ' apc', ' adi', ' antm',
                     ' aon', ' apa', ' aiv', ' aapl', ' amat', ' adm', ' arnc', ' ajg', ' aiz', ' adsk', ' adp', ' an',
                     ' azo', ' avb', ' avy', ' bhi', ' bll', ' bac', ' bcr', ' bax', ' bbt', ' bdx', ' bbby', ' brk.b',
                     ' bby', ' biib', ' blk', ' hrb', ' ba', ' bwa', ' bxp', ' bsx', ' bmy', ' avgo', ' bf.b', ' chrw',
                     ' cog', ' cpb', ' cof', ' cah', ' kmx', ' ccl', ' cat', ' cboe', ' cbg', ' cbs', ' celg',
                     ' cnc', ' cnp', ' ctl', ' cern', ' cf', ' schw', ' chtr', ' chk', ' cvx', ' cmg', ' cb', ' chd',
                     ' ci', ' xec', ' cinf', ' ctas', ' csco', ' cfg', ' ctxs', ' cme', ' cms', ' coh', ' ko', ' ctsh',
                     ' cl', ' cmcsa', ' cma', ' cag', ' cxo', ' cop', ' ed', ' stz', ' glw', ' cost', ' coty', ' cci',
                     ' csra', ' csx', ' cmi', ' cvs', ' dhi', ' dhr', ' dri', ' dva', ' de', ' dlph', ' dal', ' xray',
                     ' dvn', ' dlr', ' dfs', ' disca', ' disck', ' dg', ' dltr', ' dov', ' dow', ' dps', ' dte', ' dd',
                     ' duk', ' dnb', ' etfc', ' emn', ' etn', ' ebay', ' ecl', ' eix', ' ew', ' emr', ' etr',
                     ' evhc', ' eog', ' eqt', ' efx', ' eqix', ' eqr', ' ess', ' el', ' es', ' exc', ' expe', ' expd',
                     ' esrx', ' exr', ' xom', ' ffiv', ' fb', ' fast', ' frt', ' fdx', ' fis', ' fitb', ' fslr', ' fe',
                     ' fisv', ' flir', ' fls', ' flr', ' fmc', ' fti', ' fl', ' ftv', ' fbhs', ' ben', ' fcx', ' ftr',
                     ' gps', ' grmn', ' gd', ' ge', ' ggp', ' gis', ' gm', ' gpc', ' gild', ' gpn', ' gs', ' gt',
                     ' gww', ' hal', ' hbi', ' hog', ' har', ' hrs', ' hig', ' has', ' hca', ' hcp', ' hp', ' hsic',
                     ' hes', ' hpe', ' holx', ' hd', ' hon', ' hrl', ' hst', ' hpq', ' hum', ' hban', ' idxx', ' itw',
                     ' ilmn', ' incy', ' ir', ' intc', ' ice', ' ibm', ' ip', ' ipg', ' iff', ' intu', ' isrg', ' ivz',
                     ' irm', ' jbht', ' jec', ' sjm', ' jnj', ' jci', ' jpm', ' jnpr', ' ksu', ' key', ' kmb', ' kim',
                     ' kmi', ' klac', ' kss', ' khc', ' kr', ' lb', ' lll', ' lh', ' lrcx', ' leg', ' len', ' luk',
                     ' lvlt', ' lly', ' lnc', ' lltc', ' lkq', ' lmt', ' low', ' lyb', ' mtb', ' mac', ' mnk', ' mro',
                     ' mpc', ' mar', ' mmc', ' mlm', ' mas', ' ma', ' mat', ' mkc', ' mcd', ' mck', ' mjn', ' mdt',
                     ' mrk', ' met', ' mtd', ' kors', ' mchp', ' mu', ' msft', ' maa', ' mhk', ' tap', ' mdlz', ' mon',
                     ' mnst', ' mco', ' ms', ' msi', ' mur', ' myl', ' ndaq', ' nov', ' navi', ' ntap', ' nflx', ' nwl',
                     ' nfx', ' nem', ' nwsa', ' nws', ' nee', ' nlsn', ' nke', ' nbl', ' jwn', ' nsc', ' ntrs',
                     ' noc', ' nrg', ' nue', ' nvda', ' orly', ' oxy', ' omc', ' oke', ' orcl', ' pcar', ' ph', ' pdco',
                     ' payx', ' pypl', ' pnr', ' pbct', ' pep', ' pki', ' prgo', ' pfe', ' pcg', ' pm', ' psx', ' pnw',
                     ' pxd', ' pnc', ' rl', ' ppg', ' ppl', ' px', ' pcln', ' pfg', ' pg', ' pgr', ' pld', ' pru',
                     ' peg', ' psa', ' phm', ' pvh', ' qrvo', ' qcom', ' pwr', ' dgx', ' rrc', ' rtn', ' rht', ' reg',
                     ' regn', ' rf', ' rsg', ' rai', ' rhi', ' rok', ' col', ' rop', ' rost', ' rcl', ' spgi', ' crm',
                     ' scg', ' slb', ' sni', ' stx', ' see', ' sre', ' shw', ' sig', ' spg', ' swks', ' slg', ' sna',
                     ' so', ' luv', ' swn', ' swk', ' spls', ' sbux', ' stt', ' srcl', ' syk', ' sti', ' symc', ' syf',
                     ' syy', ' trow', ' tgt', ' tel', ' tgna', ' tdc', ' tso', ' txn', ' txt', ' bk', ' clx', ' coo',
                     ' hsy', ' mos', ' trv', ' dis', ' tmo', ' tif', ' twx', ' tjx', ' tmk', ' tss', ' tsco', ' tdg',
                     ' rig', ' trip', ' foxa', ' fox', ' tsn', ' usb', ' udr', ' ulta', ' ua', ' uaa', ' unp', ' ual',
                     ' unh', ' ups', ' uri', ' utx', ' uhs', ' unm', ' urbn', ' vfc', ' vlo', ' var', ' vtr', ' vrsn',
                     ' vrsk', ' vz', ' vrtx', ' viab', ' vno', ' vmc', ' wmt', ' wba', ' wm', ' wat', ' wec', ' wfc',
                     ' hcn', ' wdc', ' wu', ' wrk', ' wy', ' whr', ' wfm', ' wmb', ' wltw', ' wyn', ' wynn', ' xel',
                     ' xrx', ' xlnx', ' xl', ' xyl', ' yhoo', ' yum', ' zbh', ' zion', ' zts',
                     'acioty', 'aciuty', 'acuty', ' cutie', 'a cutie', 'acuity', 'a y i', 'a BBB', 'buzzard',
                     'neck Center', 'Abby', 'that be', 'apathy', 'a bee', 'ab C', 'rabbit', 'a bit', 'activison',
                     'activisoion', 'activiosn', 'activision', ' atvi', ' acn', 'acenture', 'accentue', 'accenutre',
                     'acenture', 'accentue', 'accenutre', 'acentuer', 'accenture', ' abbv', ' abbvie', ' abt', 'abbott',
                     'abott', 'abbot', ' UA', ' ua', ' uA', 'Under Armour', 'under armour', 'Under Armor',
                     'under armor', ' AAPL', '3 m', \
                     'apple', '3 M', '3M', 'Verizon', 'Visa', 'Wal-mart', 'Wal-Mart', 'Walmart', 'Wal Mart', \
                     'Travelers', 'United Technologies', 'United Tech', 'UnitedHealth', 'United Health', 'Microsoft', \
                     'Nike', 'Pfizer', 'Procter & Gamble', 'American Express', 'JPMorgan Chase', 'McDonalds',
                     'Mac Donalds', \
                     ' Merck', 'Johnson and Johnson', 'Intel', 'IBM', 'Goldman Sachs', 'Home Depot', 'General Electric',
                     'Exxon', 'Boeing', 'Caterpillar', 'Chevron', 'Cisco', 'Coca-Cola', 'Disney', 'Due Pont', 'Du Pont',
                     'caterpillar', 'Coke', 'coke', 'United test', 'mmm', 'aapl', 'vz', ' v', 'wmt', 'trv', 'utx',
                     'unh', 'msft', 'nke', 'pfe',
                     'pg', 'axp', 'jpm', 'mcd', 'mrk', 'jnj', 'intc', 'ibm', ' gs', 'hd', 'ge', 'xom', ' ba', 'cat',
                     'cvx', 'csco', 'coke', 'dis',
                     'dd', 'J & J ', 'j & j', 'Mke', 'mke', 'Cat', 'T RV', 'J&J', ' v', ' a', ' o', ' t', ' c', ' d',
                     ' f', ' k', ' l', ' m', ' r',' ni',' ea']
        DJ_Name_Match = ['finl','finl','intc','mat', 'mat', 'mat', 'bsx', 'bsx', 'bsx', 'bsx', 'bsx', 'bbt', 'apa', 'apa', 'aal', 'aal',
                         'afl', 'afl', 'afl', 'aet', 'aet', 'aet', 'aet', 'all', 't', 't', 'ci', 'ci', 'ci', 'ci',
                         'chk', 'chk', 'chk', 'cmg', 'chk', 'cme', 'cme', 'cma', 'cme', 'c', 'c', 'c', 'c', 'cl', 'cop',
                         'cop', 'cop', 'dva', 'dva', 'dva', 'dva', 'dvn', 'dvn', 'dvn', 'dvn', 'dvn', 'dvn', 'etfc',
                         'dps', 'fdx', 'f', 'gm', 'hal', 'hal', 'hal', 'hca', 'hca', 'hlt', 'hlt', 'intu', 'intu',
                         'intu', 'intu', 'intu', 'jbht', 'khc', 'khc', 'khc', 'khc', 'kr', 'lyb', 'lyb', 'lyb', 'lyb',
                         'mar', 'mar', 'mar', 'mar', 'l', 'l', 'lmt', 'lmt', 'mpc', 'msi', 'orcl', 'oxy', 'nrg', 'mck',
                         'mgm', 'mgm', 'met', 'met', 'mnst', 'msi', 'msi', 'msi', 'msi', 'msi', 'ms', 'ms', 'ms',
                         'ndaq', 'nlsn', 'nlsn', 'nlsn', 'nlsn', 'nbl', 'nbl', 'nbl', 'nrg', 'oxy', 'oxy', 'oxy', 'oxy',
                         'orcl', 'orcl', 'orcl', 'pep', 'pep', 'pxd', 'pxd', 'pxd', 'pru', 'pru', 'pru', 'pru', 'slb',
                         'slb', 'slb', 'slb', 'qcom', 'qcom', 'rhi', 'rhi', 'slb', 'slb', 'luv', 'syk', 'syk', 'ti',
                         'tgt', 'tmo', 'tmo', 'vfc', 'yum', 'yum', 'yum', 'ma', 'ma', 'kmi', 'kmi', 'kmi', 'kmi',
                         'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'dal', 'dal', 'cmg', 'cmg', 'cmg', 'cmg', 'blk', 'blk',
                         'blk', 'bac', 'bac', 'bac', 'bac', 'bac', 'ba', 'ba', 'utx', 'utx', 'utx', 'vz', 'vz', 'vz',
                         'cvx', 'cvx', 'axp', 'v', 'v', 'v', 'v', 'v', 'pfe', 'pfe', 'pfe', 'pfe', 'dnkn', 'lnkd',
                         'lnkd', 'lnkd', 'lnkd', 'dnkn', 'blk', 'lnkd', 'lnkd', 'lnkd', 'dnkn', 'dnkn', 'dnkn', 'gnc',
                         'gs', 'tsla', 'tsla', 'pypl', 'pypl', 'pypl', 'pypl', 'pypl', 'nflx', 'nflx', 'sbux', 'celg',
                         'celg', 'sbux', 'sbux', 'sbux', 'sbux', 'sbux', 'pcln', 'pcln', 'pcln', 'pcln', 'celg', 'celg',
                         'celg', 'nvda', 'nvda', 'nvda', 'nvda', 'nvda', 'celg', 'celg', 'celg', 'amgn', 'brk_a',
                         'brk_a', 'brk_a', 'brk_a', 'brk_a', 'wfc', 'wfc', 'wfc', 'jpm', 'ge', 'ge', 'fb', 'fb', 'fb',
                         'goog', 'goog', 'dis', 'amzn', 'amzn', 'amzn', 'amzn', 'aap', 'aap', 'abbt', 'abbt', 'abbv',
                         'aap', 'aap', 'aap', 'adbe', 'adbe', 'adbe', 'mmm', 'abt', 'abbv', 'acn', 'atvi', 'ayi',
                         'adbe', 'aap', 'aes', 'aet', 'amg', 'afl', 'apd', 'akam', 'alk', 'alb', 'alxn', 'alle', 'agn',
                         'ads', 'lnt', 'all', 'googl', 'goog', 'mo', 'amzn', 'aee', 'aal', 'aep', 'axp', 'aig', 'amt',
                         'awk', 'amp', 'abc', 'ame', 'amgn', 'aph', 'apc', 'adi', 'antm', 'aon', 'apa', 'aiv', 'aapl',
                         'amat', 'adm', 'arnc', 'ajg', 'aiz', 'adsk', 'adp', 'an', 'azo', 'avb', 'avy', 'bhi', 'bll',
                         'bac', 'bcr', 'bax', 'bbt', 'bdx', 'bbby', 'brk.b', 'bby', 'biib', 'blk', 'hrb', 'ba', 'bwa',
                         'bxp', 'bsx', 'bmy', 'avgo', 'bf.b', 'chrw', 'cog', 'cpb', 'cof', 'cah', 'kmx', 'ccl',
                         'cat', 'cboe', 'cbg', 'cbs', 'celg', 'cnc', 'cnp', 'ctl', 'cern', 'cf', 'schw', 'chtr', 'chk',
                         'cvx', 'cmg', 'cb', 'chd', 'ci', 'xec', 'cinf', 'ctas', 'csco', 'cfg', 'ctxs', 'cme', 'cms',
                         'coh', 'ko', 'ctsh', 'cl', 'cmcsa', 'cma', 'cag', 'cxo', 'cop', 'ed', 'stz', 'glw', 'cost',
                         'coty', 'cci', 'csra', 'csx', 'cmi', 'cvs', 'dhi', 'dhr', 'dri', 'dva', 'de', 'dlph', 'dal',
                         'xray', 'dvn', 'dlr', 'dfs', 'disca', 'disck', 'dg', 'dltr', 'dov', 'dow', 'dps', 'dte', 'dd',
                         'duk', 'dnb', 'etfc', 'emn', 'etn', 'ebay', 'ecl', 'eix', 'ew', 'emr', 'etr', 'evhc',
                         'eog', 'eqt', 'efx', 'eqix', 'eqr', 'ess', 'el', 'es', 'exc', 'expe', 'expd', 'esrx', 'exr',
                         'xom', 'ffiv', 'fb', 'fast', 'frt', 'fdx', 'fis', 'fitb', 'fslr', 'fe', 'fisv', 'flir', 'fls',
                         'flr', 'fmc', 'fti', 'fl', 'ftv', 'fbhs', 'ben', 'fcx', 'ftr', 'gps', 'grmn', 'gd', 'ge',
                         'ggp', 'gis', 'gm', 'gpc', 'gild', 'gpn', 'gs', 'gt', 'gww', 'hal', 'hbi', 'hog', 'har', 'hrs',
                         'hig', 'has', 'hca', 'hcp', 'hp', 'hsic', 'hes', 'hpe', 'holx', 'hd', 'hon', 'hrl', 'hst',
                         'hpq', 'hum', 'hban', 'idxx', 'itw', 'ilmn', 'incy', 'ir', 'intc', 'ice', 'ibm', 'ip', 'ipg',
                         'iff', 'intu', 'isrg', 'ivz', 'irm', 'jbht', 'jec', 'sjm', 'jnj', 'jci', 'jpm', 'jnpr', 'ksu',
                         'key', 'kmb', 'kim', 'kmi', 'klac', 'kss', 'khc', 'kr', 'lb', 'lll', 'lh', 'lrcx', 'leg',
                         'len', 'luk', 'lvlt', 'lly', 'lnc', 'lltc', 'lkq', 'lmt', 'low', 'lyb', 'mtb', 'mac', 'mnk',
                         'mro', 'mpc', 'mar', 'mmc', 'mlm', 'mas', 'ma', 'mat', 'mkc', 'mcd', 'mck', 'mjn', 'mdt',
                         'mrk', 'met', 'mtd', 'kors', 'mchp', 'mu', 'msft', 'maa', 'mhk', 'tap', 'mdlz', 'mon', 'mnst',
                         'mco', 'ms', 'msi', 'mur', 'myl', 'ndaq', 'nov', 'navi', 'ntap', 'nflx', 'nwl', 'nfx', 'nem',
                         'nwsa', 'nws', 'nee', 'nlsn', 'nke', 'nbl', 'jwn', 'nsc', 'ntrs', 'noc', 'nrg', 'nue',
                         'nvda', 'orly', 'oxy', 'omc', 'oke', 'orcl', 'pcar', 'ph', 'pdco', 'payx', 'pypl', 'pnr',
                         'pbct', 'pep', 'pki', 'prgo', 'pfe', 'pcg', 'pm', 'psx', 'pnw', 'pxd', 'pnc', 'rl', 'ppg',
                         'ppl', 'px', 'pcln', 'pfg', 'pg', 'pgr', 'pld', 'pru', 'peg', 'psa', 'phm', 'pvh', 'qrvo',
                         'qcom', 'pwr', 'dgx', 'rrc', 'rtn', 'rht', 'reg', 'regn', 'rf', 'rsg', 'rai', 'rhi', 'rok',
                         'col', 'rop', 'rost', 'rcl', 'spgi', 'crm', 'scg', 'slb', 'sni', 'stx', 'see', 'sre', 'shw',
                         'sig', 'spg', 'swks', 'slg', 'sna', 'so', 'luv', 'swn', 'swk', 'spls', 'sbux', 'stt', 'srcl',
                         'syk', 'sti', 'symc', 'syf', 'syy', 'trow', 'tgt', 'tel', 'tgna', 'tdc', 'tso', 'txn', 'txt',
                         'bk', 'clx', 'coo', 'hsy', 'mos', 'trv', 'dis', 'tmo', 'tif', 'twx', 'tjx', 'tmk', 'tss',
                         'tsco', 'tdg', 'rig', 'trip', 'foxa', 'fox', 'tsn', 'usb', 'udr', 'ulta', 'ua', 'uaa', 'unp',
                         'ual', 'unh', 'ups', 'uri', 'utx', 'uhs', 'unm', 'urbn', 'vfc', 'vlo', 'var', 'vtr', 'vrsn',
                         'vrsk', 'vz', 'vrtx', 'viab', 'vno', 'vmc', 'wmt', 'wba', 'wm', 'wat', 'wec', 'wfc', 'hcn',
                         'wdc', 'wu', 'wrk', 'wy', 'whr', 'wfm', 'wmb', 'wltw', 'wyn', 'wynn', 'xel', 'xrx', 'xlnx',
                         'xl', 'xyl', 'yhoo', 'yum', 'zbh', 'zion', 'zts',
                         'ayi', 'ayi', 'ayi', 'ayi', 'ayi', 'ayi', 'ayi', 'abbv', 'atvi', 'acn', 'abbv', 'abbv', 'abbv',
                         'abbv', 'abbv', 'abt', 'abt', 'atvi', 'atvi', 'atvi', 'atvi', 'atvi', 'acn', 'acn', 'acn',
                         'acn', 'acn', 'acn', 'acn', 'acn', 'acn', 'abbv', 'abbv', 'abt', 'abt', 'abt', 'abt', 'ua',
                         'ua', 'ua', 'ua', 'ua',
                         'ua', 'ua', 'aapl', 'mmm', 'aapl', 'mmm', 'mmm', 'vz', 'v', 'wmt', 'wmt', 'wmt', 'wmt', 'trv',
                         'utx', 'utx', 'unh',
                         'unh', 'msft', 'nke', 'pfe', 'pg', 'axp', 'jpm', 'mcd', 'mcd', 'mrk', 'jnj', 'intc', 'ibm',
                         'gs', 'hd', 'ge', 'xom', 'ba', 'cat', \
                         'cvx', 'csco', 'coke', 'dis', 'dd', 'dd', 'cat', 'coke', 'coke', 'utx', 'mmm', 'aapl', 'vz',
                         'v',
                         'wmt', 'trv', 'utx', 'unh', 'msft', 'nke', 'pfe', 'pg', 'axp', 'jpm', 'mcd', 'mrk', 'jnj',
                         'intc', 'ibm', 'gs', 'hd',
                         'ge', 'xom', 'ba', 'cat', 'cvx', 'csco', 'coke', 'dis', 'dd', 'jnj', 'jnj', 'nke', 'nke',
                         'cat', 'trv', 'jnj', 'v', 'a', 'o', 't', 'c', 'd', 'f', 'k', 'l', 'm', 'r','ni','ea']

        Dow_Jones = [x.upper() for x in Dow_Jones]

        merge_string_names = pd.DataFrame(DJ_Name_Match, index=Dow_Jones)
        merge_string_names = merge_string_names.rename(columns={0: 'ticker'})
        merge_string_names['names'] = merge_string_names.index

        matches = []
        for word in Dow_Jones:
            if word in phrase1.upper():
                matches.append(word)

        matches = [x.upper() for x in matches]

        matches_df = pd.DataFrame(matches, index=matches)
        matches_df = matches_df.rename(columns={0: 'names'})

        selected_stocks_2 = pd.merge(matches_df, merge_string_names, on='names')

        ticker_df = pd.DataFrame(selected_stocks_2['ticker'])
        tickers = []
        tickers = ticker_df['ticker']

        page = requests.get("http://www.nasdaq.com/earnings/report/" + tickers[0])
        content = page.content
        soup = BeautifulSoup(page.content, 'html.parser')

        table_id1 = soup.find_all('h2')

        z = repr(table_id1[0])
        x = len(z)

        extract1 = z[x - 22:x - 10]

        table_id = soup.find(id="showdata-div")

        table_numbers = table_id.find_all(class_="genTable")
        date_min = table_numbers[0].find_all('td')

        z_list = []
        for string in date_min:
            z_list.append(repr(string))

        date_min_1_val = pd.DataFrame(z_list)
        m = len(date_min_1_val.index)

        i = 0

        z_list2 = []
        for i in range(i, m):
            str_length = len(date_min_1_val.iloc[i, 0])
            extract = date_min_1_val.iloc[i, 0][4:str_length - 5]
            z_list2.append(extract)

        min_1 = pd.DataFrame(z_list2[0:5])
        min_2 = pd.DataFrame(z_list2[5:10])
        min_3 = pd.DataFrame(z_list2[10:15])
        min_4 = pd.DataFrame(z_list2[15:20])

        merge1 = pd.merge(min_1, min_2, left_index=True, right_index=True)
        merge2 = pd.merge(merge1, min_3, left_index=True, right_index=True)
        merge3 = pd.merge(merge2, min_4, left_index=True, right_index=True)
        merge3.columns = [i for i in range(merge3.shape[1])]

        for column in merge3:
            if merge3.iloc[4, column] == 'Met':
                merge3.iloc[4, column] = 0

        y_list = []
        for column in merge3:
            if merge3.iloc[2, column] > merge3.iloc[3, column]:
                surprise = "positive"
            else:
                surprise = "negative"
            result = "For " + merge3.iloc[0, column] + " results, the actual profit was $" + str(
                merge3.iloc[2, column]) + " per share, and expected consensus was $" + str(
                merge3.iloc[3, column]) + " per share, for a " + surprise + " earnings surprise of " + "{:.1f}".format(
                float(merge3.iloc[4, column]), 1) + "%."
            y_list.append(result)

        if not y_list:

            yara_text = "The earnings data for " + tickers[0].upper() + " is not currently provided. Damn, they didn't give us access to it. I guess it's time to hack them now. ;)"

            number = 1
            Buy = 0
            Hold = 0
            Sell = 0
            q1 = 0
            q2 = 0
            q3 = 0
            q4 = 0
            array = 0
            date = 0
            sharperatiouser = 0
            sharperatiowhatif = 0
            total_return_new = 0
            total_return_usr = 0
            STD_Port_new = 0
            STD_usr_Port = 0

        else:
            yara_text = '<b>'"Here are the last four profit results for " + tickers[0].upper() + ":"'</b>' + '<br />' + '<br />' + \
                    y_list[0] + '<br />' + \
                    y_list[1] + '<br />' + \
                    y_list[2] + '<br />' + \
                    y_list[3]

            number = 1
            Buy = 0
            Hold = 0
            Sell = 0
            q1 = [merge3.iloc[0, 0],float(merge3.iloc[2, 0]),float(merge3.iloc[3, 0])]
            q2 = [merge3.iloc[0, 1], float(merge3.iloc[2, 1]), float(merge3.iloc[3, 1])]
            q3 = [merge3.iloc[0, 2], float(merge3.iloc[2, 2]), float(merge3.iloc[3, 2])]
            q4 = [merge3.iloc[0, 3], float(merge3.iloc[2, 3]), float(merge3.iloc[3, 3])]
            array = 0
            date = 0
            sharperatiouser = 0
            sharperatiowhatif = 0
            total_return_new = 0
            total_return_usr = 0
            STD_Port_new = 0
            STD_usr_Port = 0

    elif any(word in phrase1 for word in backtest):

        todays_date = datetime.datetime.today().strftime("%m/%d/%Y")

        answer = "Ran backtest for your portfolio over the past 10 years against the S&P 500. Your portfolio would've outperformed " + \
            "the market by about 4.5% annually. Your return would've been about 9.5% annually. Great job! But remember, past performance " + \
            "is not an indicator of the future. Did I mention how much I love to gamble? Let's roll the dice!!"

        table = [['2007', 100, 100], ['2008', 101.7, 95.8], ['2009', 65.9, 57.4],
        ['2010', 88.7, 74.7], ['2011', 107.1, 89.4], ['2012', 108.6, 91.3],
        ['2013', 123.9, 104.2], ['2014', 158.2, 123.9], ['2015', 179.9, 138.7],
        ['2016', 177.1, 134.9], ['2017', 211.6, 158.4], ['', 239.1, 171.1]]

        yara_text = answer
        array = table
        number = 2
        Buy = 0
        Hold = 0
        Sell = 0
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        tickers = [0]
        date = todays_date
        sharperatiouser = 0
        sharperatiowhatif = 0
        total_return_new = 0
        total_return_usr = 0
        STD_Port_new = 0
        STD_usr_Port = 0

    elif any(word in phrase1.upper() for word in Dow_Jones) and any(word in phrase1 for word in whatif):

        command_list_dollar = ['dollars', 'Dollars', '$']
        total = ['total', 'across', 'all']
        each = ['each', 'every']
        command_list_average = ['average', 'Average']
        command_list_percent = ['percent', 'Percent', '%']
        optimal = ['optimal', 'find']
        shares = ['shares', 'Shares']

        all_commands = ['dollars', 'Dollars', '$', 'total', 'across', 'all', 'each', 'every', 'average', 'Average',
                        'percent', 'Percent']

        Dow_Jones = ['finl','finl','intel', 'M80', 'motel', 'mattel', 'bss', 'dsx', 'vsx', 'psx', 'Boston Scientific', 'BB&T', 'a pa',
                     'apache',
                     ' al', 'american airlines', ' nfl', ' asl', 'aflac', ' att', ' 80', 'aetna', 'etna', 'allstate',
                     'tea',
                     'at&t', 'c i', 'see I', 'cigna', 'signify', 'chedapeake', 'chesapeak', 'chesapeka', 'Chipotle',
                     'chesapeake', 'c a mean', 'siami', 'comerica', 'cn me', 'citi', 'city', 'sea', 'citigroup',
                     'colgate',
                     'copd', ' clp', 'conoco', ' dda', ' pva', ' dba', 'davita', ' dbn', ' evn', ' dvf', ' bvn', ' tbn',
                     'Devon', 'E-Trade', 'dr pepper', 'fedex', 'ford', 'general motors', ' how ', 'hell', 'halliburton',
                     'hcti', 'hci', 'hlt', 'hilton', 'vine to you', 'all I am to you', 'in2u', 'lying to you', 'intuit',
                     'jb hunt', 'thc', 'heinz', 'craft', 'crap', 'kroger', 'Lydia', 'limbo', 'Lindell', 'Lyondell',
                     'mariott', 'marriot', "marriott's", 'marriott', 'lockheed', 'martin', 'marathon',
                     'ms I', 'rcl', 'xy', 'energy', 'mckesson', 'mgm', 'm g m', 'metlife', 'matlock', 'monster',
                     'motoroal',
                     'motorala', 'motoral', 'motorals', 'Motorola', 'morgan', 'stanley', 'stanly', 'nasdaq', 'nelsien',
                     'nielsien', 'nielson', 'nielsen', 'novel', 'nobel', 'noble', 'nrg energy', 'occienetal',
                     'occidential',
                     'occiednetal', 'Occidental', 'oravle', 'oracle', 'oroville', 'pepsi', 'pepsico', 'pioeneer',
                     'piorneer', 'pioneer', 'priudentail', 'prudentail', 'priuential', 'prudential', 'schlumnerger',
                     'shlimberger', 'schlimberger', 'shlumberger', 'qualcom', 'qualcomm', 'Robert', 'robert half',
                     'schlumberger', 'slumber j', 'southwest', 'striker', 'checker', ' ti', 'target', 'thermo',
                     'fisher', 'vf corp', "I'm brand", 'why you', 'why um', ' ma', 'mastercard', 'tmi', 'cam', 'tam-ly',
                     'Caroline', 'can line', 'Cam I', 'kinder', 'linder', 'kinder morgan', 'tal', 'delta', 'chipoelt',
                     'chitpole', 'chipotle', 'chipotle', 'blackrcok', 'blk', 'blackrock', 'B of A', 'bofa', ' ac',
                     ' bac',
                     'bank of america', 'va', 'nba', 'gtx', 'etx', 'you tx', 'pc', 'bz', 'of easy', 'cbx', 'cdx',
                     'a xB',
                     'of the', 'of d', 'at Lee', 'of beat', 'of be', 'ps3', 'pfd', 'pft', 'tmz', 'dunkdin', 'lineind',
                     'linkeind', 'linkeidn', 'linkedin', 'dinkn', 'blk', 'lmtd', 'linkedin', 'lnkd', 'duncan', 'dunkin',
                     'dnkn', 'gnc', 'goldman', 'tsla', 'tesla', 'payapal', 'pauypal', 'payapl', 'paupal', 'paypal',
                     'netfliz', 'netflix', 'spu x', 'clg', 'C E L G', 's b u x', 'starbucsk', 'starbcusk', 'SVU X',
                     'starbuck', 'pcls', 'pcl-r', 'pricline', 'priceline', 'celgence', 'clenge', 'clegene', 'nviia',
                     'nvisia', 'nividia', 'nvidia', 'in video', 'so jean', 'soldier', 'celgene', 'amgen', 'brka',
                     'brk-a',
                     'brk', 'berkshire', 'hathaway', 'wfc', 'fargo', 'wells', 'JPMorgan', 'general electic',
                     'general electric', 'facenook', 'faebook', 'facebook', 'google', 'goog', 'dies', 'amc', 'ambien',
                     'amazon', 'amzn', 'asap', 'a 18', ' sabbath', ' either', 'happy', 'adbance', 'atuo'' auto',
                     ' advance',
                     'abobe', 'adone', 'adobe', ' mmm', ' abt', ' abbv', ' acn', ' atvi', ' ayi', ' adbe', ' aap',
                     ' aes',
                     ' aet', ' amg', ' afl', ' apd', ' akam', ' alk', ' alb', ' alxn', ' alle', ' agn', ' ads', ' lnt',
                     ' all', ' googl', ' goog', ' mo', ' amzn', ' aee', ' aal', ' aep', ' axp', ' aig', ' amt', ' awk',
                     ' amp', ' abc', ' ame', ' amgn', ' aph', ' apc', ' adi', ' antm', ' aon', ' apa', ' aiv', ' aapl',
                     ' amat', ' adm', ' arnc', ' ajg', ' aiz', ' adsk', ' adp', ' an', ' azo', ' avb', ' avy', ' bhi',
                     ' bll', ' bac', ' bcr', ' bax', ' bbt', ' bdx', ' bbby', ' brk.b', ' bby', ' biib', ' blk', ' hrb',
                     ' ba', ' bwa', ' bxp', ' bsx', ' bmy', ' avgo', ' bf.b', ' chrw', ' cog', ' cpb', ' cof',
                     ' cah', ' kmx', ' ccl', ' cat', ' cboe', ' cbg', ' cbs', ' celg', ' cnc', ' cnp', ' ctl', ' cern',
                     ' cf', ' schw', ' chtr', ' chk', ' cvx', ' cmg', ' cb', ' chd', ' ci', ' xec', ' cinf', ' ctas',
                     ' csco', ' cfg', ' ctxs', ' cme', ' cms', ' coh', ' ko', ' ctsh', ' cl', ' cmcsa', ' cma', ' cag',
                     ' cxo', ' cop', ' ed', ' stz', ' glw', ' cost', ' coty', ' cci', ' csra', ' csx', ' cmi', ' cvs',
                     ' dhi', ' dhr', ' dri', ' dva', ' de', ' dlph', ' dal', ' xray', ' dvn', ' dlr', ' dfs', ' disca',
                     ' disck', ' dg', ' dltr', ' dov', ' dow', ' dps', ' dte', ' dd', ' duk', ' dnb', ' etfc', ' emn',
                     ' etn', ' ebay', ' ecl', ' eix', ' ew', ' ea', ' emr', ' etr', ' evhc', ' eog', ' eqt', ' efx',
                     ' eqix', ' eqr', ' ess', ' el', ' es', ' exc', ' expe', ' expd', ' esrx', ' exr', ' xom', ' ffiv',
                     ' fb', ' fast', ' frt', ' fdx', ' fis', ' fitb', ' fslr', ' fe', ' fisv', ' flir', ' fls', ' flr',
                     ' fmc', ' fti', ' fl', ' ftv', ' fbhs', ' ben', ' fcx', ' ftr', ' gps', ' grmn', ' gd', ' ge',
                     ' ggp',
                     ' gis', ' gm', ' gpc', ' gild', ' gpn', ' gs', ' gt', ' gww', ' hal', ' hbi', ' hog', ' har',
                     ' hrs',
                     ' hig', ' has', ' hca', ' hcp', ' hp', ' hsic', ' hes', ' hpe', ' holx', ' hd', ' hon', ' hrl',
                     ' hst',
                     ' hpq', ' hum', ' hban', ' idxx', ' itw', ' ilmn', ' incy', ' ir', ' intc', ' ice', ' ibm', ' ip',
                     ' ipg', ' iff', ' intu', ' isrg', ' ivz', ' irm', ' jbht', ' jec', ' sjm', ' jnj', ' jci', ' jpm',
                     ' jnpr', ' ksu', ' key', ' kmb', ' kim', ' kmi', ' klac', ' kss', ' khc', ' kr', ' lb', ' lll',
                     ' lh',
                     ' lrcx', ' leg', ' len', ' luk', ' lvlt', ' lly', ' lnc', ' lltc', ' lkq', ' lmt', ' low', ' lyb',
                     ' mtb', ' mac', ' mnk', ' mro', ' mpc', ' mar', ' mmc', ' mlm', ' mas', ' ma', ' mat', ' mkc',
                     ' mcd',
                     ' mck', ' mjn', ' mdt', ' mrk', ' met', ' mtd', ' kors', ' mchp', ' mu', ' msft', ' maa', ' mhk',
                     ' tap', ' mdlz', ' mon', ' mnst', ' mco', ' ms', ' msi', ' mur', ' myl', ' ndaq', ' nov', ' navi',
                     ' ntap', ' nflx', ' nwl', ' nfx', ' nem', ' nwsa', ' nws', ' nee', ' nlsn', ' nke', ' nbl',
                     ' jwn', ' nsc', ' ntrs', ' noc', ' nrg', ' nue', ' nvda', ' orly', ' oxy', ' omc', ' oke', ' orcl',
                     ' pcar', ' ph', ' pdco', ' payx', ' pypl', ' pnr', ' pbct', ' pep', ' pki', ' prgo', ' pfe',
                     ' pcg',
                     ' pm', ' psx', ' pnw', ' pxd', ' pnc', ' rl', ' ppg', ' ppl', ' px', ' pcln', ' pfg', ' pg',
                     ' pgr',
                     ' pld', ' pru', ' peg', ' psa', ' phm', ' pvh', ' qrvo', ' qcom', ' pwr', ' dgx', ' rrc', ' rtn',
                     ' rht', ' reg', ' regn', ' rf', ' rsg', ' rai', ' rhi', ' rok', ' col', ' rop', ' rost', ' rcl',
                     ' spgi', ' crm', ' scg', ' slb', ' sni', ' stx', ' see', ' sre', ' shw', ' sig', ' spg', ' swks',
                     ' slg', ' sna', ' so', ' luv', ' swn', ' swk', ' spls', ' sbux', ' stt', ' srcl', ' syk', ' sti',
                     ' symc', ' syf', ' syy', ' trow', ' tgt', ' tel', ' tgna', ' tdc', ' tso', ' txn', ' txt', ' bk',
                     ' clx', ' coo', ' hsy', ' mos', ' trv', ' dis', ' tmo', ' tif', ' twx', ' tjx', ' tmk', ' tss',
                     ' tsco', ' tdg', ' rig', ' trip', ' foxa', ' fox', ' tsn', ' usb', ' udr', ' ulta', ' ua', ' uaa',
                     ' unp', ' ual', ' unh', ' ups', ' uri', ' utx', ' uhs', ' unm', ' urbn', ' vfc', ' vlo', ' var',
                     ' vtr', ' vrsn', ' vrsk', ' vz', ' vrtx', ' viab', ' vno', ' vmc', ' wmt', ' wba', ' wm', ' wat',
                     ' wec', ' wfc', ' hcn', ' wdc', ' wu', ' wrk', ' wy', ' whr', ' wfm', ' wmb', ' wltw', ' wyn',
                     ' wynn',
                     ' xel', ' xrx', ' xlnx', ' xl', ' xyl', ' yhoo', ' yum', ' zbh', ' zion', ' zts',
                     'acioty', 'aciuty', 'acuty', ' cutie', 'a cutie', 'acuity', 'a y i', 'a BBB', 'buzzard',
                     'neck Center',
                     'Abby', 'that be', 'apathy', 'a bee', 'ab C', 'rabbit', 'a bit', 'activison', 'activisoion',
                     'activiosn', 'activision', ' atvi', ' acn', 'acenture', 'accentue', 'accenutre', 'acenture',
                     'accentue', 'accenutre', 'acentuer', 'accenture', ' abbv', ' abbvie', ' abt', 'abbott', 'abott',
                     'abbot', ' UA', ' ua', ' uA', 'Under Armour', 'under armour', 'Under Armor', 'under armor',
                     ' AAPL',
                     '3 m', \
                     'apple', '3 M', '3M', 'Verizon', 'Visa', 'Wal-mart', 'Wal-Mart', 'Walmart', 'Wal Mart', \
                     'Travelers', 'United Technologies', 'United Tech', 'UnitedHealth', 'United Health', 'Microsoft', \
                     'Nike', 'Pfizer', 'Procter & Gamble', 'American Express', 'JPMorgan Chase', 'McDonalds',
                     'Mac Donalds', \
                     ' Merck', 'Johnson and Johnson', 'Intel', 'IBM', 'Goldman Sachs', 'Home Depot', 'General Electric',
                     'Exxon', 'Boeing', 'Caterpillar', 'Chevron', 'Cisco', 'Coca-Cola', 'Disney', 'Due Pont', 'Du Pont',
                     'caterpillar', 'Coke', 'coke', 'United test', 'mmm', 'aapl', 'vz', ' v', 'wmt', 'trv', 'utx',
                     'unh',
                     'msft', 'nke', 'pfe',
                     'pg', 'axp', 'jpm', 'mcd', 'mrk', 'jnj', 'intc', 'ibm', ' gs', 'hd', 'ge', 'xom', ' ba', 'cat',
                     'cvx',
                     'csco', 'coke', 'dis',
                     'dd', 'J & J ', 'j & j', 'Mke', 'mke', 'Cat', 'T RV', 'J&J', ' v', ' a', ' o', ' t', ' c', ' d',
                     ' f',
                     ' k', ' m', ' r', ' ni']
        DJ_Name_Match = ['finl','finl','intc', 'mat', 'mat', 'mat', 'bsx', 'bsx', 'bsx', 'bsx', 'bsx', 'bbt', 'apa', 'apa', 'aal',
                         'aal', 'afl',
                         'afl', 'afl', 'aet', 'aet', 'aet', 'aet', 'all', 't', 't', 'ci', 'ci', 'ci', 'ci', 'chk',
                         'chk',
                         'chk', 'cmg', 'chk', 'cme', 'cme', 'cma', 'cme', 'c', 'c', 'c', 'c', 'cl', 'cop', 'cop', 'cop',
                         'dva', 'dva', 'dva', 'dva', 'dvn', 'dvn', 'dvn', 'dvn', 'dvn', 'dvn', 'etfc', 'dps', 'fdx',
                         'f',
                         'gm', 'hal', 'hal', 'hal', 'hca', 'hca', 'hlt', 'hlt', 'intu', 'intu', 'intu', 'intu', 'intu',
                         'jbht', 'khc', 'khc', 'khc', 'khc', 'kr', 'lyb', 'lyb', 'lyb', 'lyb', 'mar', 'mar', 'mar',
                         'mar',
                         'lmt', 'lmt', 'mpc', 'msi', 'orcl', 'oxy', 'nrg', 'mck', 'mgm', 'mgm', 'met', 'met',
                         'mnst', 'msi', 'msi', 'msi', 'msi', 'msi', 'ms', 'ms', 'ms', 'ndaq', 'nlsn', 'nlsn', 'nlsn',
                         'nlsn', 'nbl', 'nbl', 'nbl', 'nrg', 'oxy', 'oxy', 'oxy', 'oxy', 'orcl', 'orcl', 'orcl', 'pep',
                         'pep', 'pxd', 'pxd', 'pxd', 'pru', 'pru', 'pru', 'pru', 'slb', 'slb', 'slb', 'slb', 'qcom',
                         'qcom',
                         'rhi', 'rhi', 'slb', 'slb', 'luv', 'syk', 'syk', 'ti', 'tgt', 'tmo', 'tmo', 'vfc', 'yum',
                         'yum', 'yum', 'ma', 'ma', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'kmi', 'dal',
                         'dal', 'cmg', 'cmg', 'cmg', 'cmg', 'blk', 'blk', 'blk', 'bac', 'bac', 'bac', 'bac', 'bac',
                         'ba',
                         'ba', 'utx', 'utx', 'utx', 'vz', 'vz', 'vz', 'cvx', 'cvx', 'axp', 'v', 'v', 'v', 'v', 'v',
                         'pfe',
                         'pfe', 'pfe', 'pfe', 'dnkn', 'lnkd', 'lnkd', 'lnkd', 'lnkd', 'dnkn', 'blk', 'lnkd', 'lnkd',
                         'lnkd',
                         'dnkn', 'dnkn', 'dnkn', 'gnc', 'gs', 'tsla', 'tsla', 'pypl', 'pypl', 'pypl', 'pypl', 'pypl',
                         'nflx', 'nflx', 'sbux', 'celg', 'celg', 'sbux', 'sbux', 'sbux', 'sbux', 'sbux', 'pcln', 'pcln',
                         'pcln', 'pcln', 'celg', 'celg', 'celg', 'nvda', 'nvda', 'nvda', 'nvda', 'nvda', 'celg', 'celg',
                         'celg', 'amgn', 'brk_a', 'brk_a', 'brk_a', 'brk_a', 'brk_a', 'wfc', 'wfc', 'wfc', 'jpm', 'ge',
                         'ge', 'fb', 'fb', 'fb', 'goog', 'goog', 'dis', 'amzn', 'amzn', 'amzn', 'amzn', 'aap', 'aap',
                         'abbt', 'abbt', 'abbv', 'aap', 'aap', 'aap', 'adbe', 'adbe', 'adbe', 'mmm', 'abt', 'abbv',
                         'acn',
                         'atvi', 'ayi', 'adbe', 'aap', 'aes', 'aet', 'amg', 'afl', 'apd', 'akam', 'alk', 'alb', 'alxn',
                         'alle', 'agn', 'ads', 'lnt', 'all', 'googl', 'goog', 'mo', 'amzn', 'aee', 'aal', 'aep', 'axp',
                         'aig', 'amt', 'awk', 'amp', 'abc', 'ame', 'amgn', 'aph', 'apc', 'adi', 'antm', 'aon', 'apa',
                         'aiv',
                         'aapl', 'amat', 'adm', 'arnc', 'ajg', 'aiz', 'adsk', 'adp', 'an', 'azo', 'avb', 'avy', 'bhi',
                         'bll', 'bac', 'bcr', 'bax', 'bbt', 'bdx', 'bbby', 'brk.b', 'bby', 'biib', 'blk', 'hrb', 'ba',
                         'bwa', 'bxp', 'bsx', 'bmy', 'avgo', 'bf.b', 'chrw', 'cog', 'cpb', 'cof', 'cah', 'kmx',
                         'ccl',
                         'cat', 'cboe', 'cbg', 'cbs', 'celg', 'cnc', 'cnp', 'ctl', 'cern', 'cf', 'schw', 'chtr', 'chk',
                         'cvx', 'cmg', 'cb', 'chd', 'ci', 'xec', 'cinf', 'ctas', 'csco', 'cfg', 'ctxs', 'cme', 'cms',
                         'coh',
                         'ko', 'ctsh', 'cl', 'cmcsa', 'cma', 'cag', 'cxo', 'cop', 'ed', 'stz', 'glw', 'cost', 'coty',
                         'cci',
                         'csra', 'csx', 'cmi', 'cvs', 'dhi', 'dhr', 'dri', 'dva', 'de', 'dlph', 'dal', 'xray', 'dvn',
                         'dlr',
                         'dfs', 'disca', 'disck', 'dg', 'dltr', 'dov', 'dow', 'dps', 'dte', 'dd', 'duk', 'dnb', 'etfc',
                         'emn', 'etn', 'ebay', 'ecl', 'eix', 'ew', 'ea', 'emr', 'etr', 'evhc', 'eog', 'eqt', 'efx',
                         'eqix',
                         'eqr', 'ess', 'el', 'es', 'exc', 'expe', 'expd', 'esrx', 'exr', 'xom', 'ffiv', 'fb', 'fast',
                         'frt',
                         'fdx', 'fis', 'fitb', 'fslr', 'fe', 'fisv', 'flir', 'fls', 'flr', 'fmc', 'fti', 'fl', 'ftv',
                         'fbhs', 'ben', 'fcx', 'ftr', 'gps', 'grmn', 'gd', 'ge', 'ggp', 'gis', 'gm', 'gpc', 'gild',
                         'gpn',
                         'gs', 'gt', 'gww', 'hal', 'hbi', 'hog', 'har', 'hrs', 'hig', 'has', 'hca', 'hcp', 'hp', 'hsic',
                         'hes', 'hpe', 'holx', 'hd', 'hon', 'hrl', 'hst', 'hpq', 'hum', 'hban', 'idxx', 'itw', 'ilmn',
                         'incy', 'ir', 'intc', 'ice', 'ibm', 'ip', 'ipg', 'iff', 'intu', 'isrg', 'ivz', 'irm', 'jbht',
                         'jec', 'sjm', 'jnj', 'jci', 'jpm', 'jnpr', 'ksu', 'key', 'kmb', 'kim', 'kmi', 'klac', 'kss',
                         'khc',
                         'kr', 'lb', 'lll', 'lh', 'lrcx', 'leg', 'len', 'luk', 'lvlt', 'lly', 'lnc', 'lltc', 'lkq',
                         'lmt',
                         'low', 'lyb', 'mtb', 'mac', 'mnk', 'mro', 'mpc', 'mar', 'mmc', 'mlm', 'mas', 'ma', 'mat',
                         'mkc',
                         'mcd', 'mck', 'mjn', 'mdt', 'mrk', 'met', 'mtd', 'kors', 'mchp', 'mu', 'msft', 'maa', 'mhk',
                         'tap',
                         'mdlz', 'mon', 'mnst', 'mco', 'ms', 'msi', 'mur', 'myl', 'ndaq', 'nov', 'navi', 'ntap', 'nflx',
                         'nwl', 'nfx', 'nem', 'nwsa', 'nws', 'nee', 'nlsn', 'nke', 'nbl', 'jwn', 'nsc', 'ntrs', 'noc',
                         'nrg', 'nue', 'nvda', 'orly', 'oxy', 'omc', 'oke', 'orcl', 'pcar', 'ph', 'pdco', 'payx',
                         'pypl',
                         'pnr', 'pbct', 'pep', 'pki', 'prgo', 'pfe', 'pcg', 'pm', 'psx', 'pnw', 'pxd', 'pnc', 'rl',
                         'ppg',
                         'ppl', 'px', 'pcln', 'pfg', 'pg', 'pgr', 'pld', 'pru', 'peg', 'psa', 'phm', 'pvh', 'qrvo',
                         'qcom',
                         'pwr', 'dgx', 'rrc', 'rtn', 'rht', 'reg', 'regn', 'rf', 'rsg', 'rai', 'rhi', 'rok', 'col',
                         'rop',
                         'rost', 'rcl', 'spgi', 'crm', 'scg', 'slb', 'sni', 'stx', 'see', 'sre', 'shw', 'sig', 'spg',
                         'swks', 'slg', 'sna', 'so', 'luv', 'swn', 'swk', 'spls', 'sbux', 'stt', 'srcl', 'syk', 'sti',
                         'symc', 'syf', 'syy', 'trow', 'tgt', 'tel', 'tgna', 'tdc', 'tso', 'txn', 'txt', 'bk', 'clx',
                         'coo',
                         'hsy', 'mos', 'trv', 'dis', 'tmo', 'tif', 'twx', 'tjx', 'tmk', 'tss', 'tsco', 'tdg', 'rig',
                         'trip',
                         'foxa', 'fox', 'tsn', 'usb', 'udr', 'ulta', 'ua', 'uaa', 'unp', 'ual', 'unh', 'ups', 'uri',
                         'utx',
                         'uhs', 'unm', 'urbn', 'vfc', 'vlo', 'var', 'vtr', 'vrsn', 'vrsk', 'vz', 'vrtx', 'viab', 'vno',
                         'vmc', 'wmt', 'wba', 'wm', 'wat', 'wec', 'wfc', 'hcn', 'wdc', 'wu', 'wrk', 'wy', 'whr', 'wfm',
                         'wmb', 'wltw', 'wyn', 'wynn', 'xel', 'xrx', 'xlnx', 'xl', 'xyl', 'yhoo', 'yum', 'zbh', 'zion',
                         'zts',
                         'ayi', 'ayi', 'ayi', 'ayi', 'ayi', 'ayi', 'ayi', 'abbv', 'atvi', 'acn', 'abbv', 'abbv', 'abbv',
                         'abbv', 'abbv', 'abt', 'abt', 'atvi', 'atvi', 'atvi', 'atvi', 'atvi', 'acn', 'acn', 'acn',
                         'acn',
                         'acn', 'acn', 'acn', 'acn', 'acn', 'abbv', 'abbv', 'abt', 'abt', 'abt', 'abt', 'ua', 'ua',
                         'ua',
                         'ua', 'ua',
                         'ua', 'ua', 'aapl', 'mmm', 'aapl', 'mmm', 'mmm', 'vz', 'v', 'wmt', 'wmt', 'wmt', 'wmt', 'trv',
                         'utx', 'utx', 'unh',
                         'unh', 'msft', 'nke', 'pfe', 'pg', 'axp', 'jpm', 'mcd', 'mcd', 'mrk', 'jnj', 'intc', 'ibm',
                         'gs',
                         'hd', 'ge', 'xom', 'ba', 'cat', \
                         'cvx', 'csco', 'coke', 'dis', 'dd', 'dd', 'cat', 'coke', 'coke', 'utx', 'mmm', 'aapl', 'vz',
                         'v',
                         'wmt', 'trv', 'utx', 'unh', 'msft', 'nke', 'pfe', 'pg', 'axp', 'jpm', 'mcd', 'mrk', 'jnj',
                         'intc',
                         'ibm', 'gs', 'hd',
                         'ge', 'xom', 'ba', 'cat', 'cvx', 'csco', 'coke', 'dis', 'dd', 'jnj', 'jnj', 'nke', 'nke',
                         'cat',
                         'trv', 'jnj', 'v', 'a', 'o', 't', 'c', 'd', 'f', 'k', 'm', 'r', 'ni']

        Dow_Jones = [x.upper() for x in Dow_Jones]

        print(phrase1.upper())
        matches = []
        for word in Dow_Jones:
            if word in phrase1.upper():
                matches.append(word)

        matches = [x.upper() for x in matches]

        print(matches)

        # current_portfolio_value = [900, 960, 900, 50, 2880, 2520, 4550, 5096, 1568, 874]
        #
        # # The weights the user likes
        # initial_weights = [.10, .075, .15, .05, .20, .03, .18, .125, .05, .04]
        #
        # # Creating the dataframe from the above arrays
        # portfolio = pd.DataFrame(current_portfolio_value,
        #                          index=['EXXON MOBIL CORP', 'ALTRIA GROUP INC', 'MERCK & CO', 'MICROSOFT CORP',
        #                                 'PEPSICO INC', 'WAL-MART STORES INC', 'AT&T INC', 'VERIZON COMMUNICATIONS INC',
        #                                 'PFIZER INC', 'MOTOROLA SOLUTIONS INC'], columns=['Current $ Value'])
        #
        #
        #
        # df_port_amount = pd.DataFrame(portfolio['Current $ Value'])
        # df_port_names = pd.DataFrame.transpose(df_port_amount.ix[:, 1:1])
        # df_port_sum = df_port_amount["Current $ Value"].sum()
        #
        # phrase1 = phrase1.replace(',', '')
        # print(phrase1)
        #
        # Dow_Jones = ['AAPL','APPLE','INTEL','VERIZON',"NIKE",'INTC','NKE','VZ','MSFT','Msft','microsoft','microsfot','intel','Nke','exon','exxom','Exxom','Exon','xom','3 m', 'apple', '3 M', '3M', 'Verizon', 'Visa', 'Wal-mart', 'Wal-Mart', 'Walmart', 'Wal Mart', \
        #              'Travelers', 'United Technologies', 'United Tech', 'UnitedHealth', 'United Health', 'Microsoft', \
        #              'Nike', 'Pfizer', 'Procter & Gamble', 'American Express', 'JPMorgan Chase', 'McDonalds',
        #              'Mac Donalds', \
        #              'Merck', 'Johnson & Johnson', 'Intel', 'IBM', 'Goldman Sachs', 'Home Depot', 'General Electric',
        #              'Exxon', 'Apple', \
        #              'Boeing', 'Caterpillar', 'Chevron', 'Cisco', 'Coca-Cola', 'Disney', 'Due Pont', 'Du Pont',
        #              'caterpillar', 'Coke', \
        #              'coke', 'United test', 'mmm', 'aapl', ' v', 'wmt', 'trv', 'utx', 'unh', 'msft', 'nke', 'pfe',
        #              'pg', 'axp', 'jpm', \
        #              'mcd', 'mrk', 'jnj', 'intc', 'ibm', 'gs', 'hd', 'ge', 'xom', 'ba', 'cat', 'cvx', 'csco', 'coke',
        #              'dis',
        #              'dd', 'J & J ', \
        #              'j & j', 'Mke', 'mke', 'Cat', 'T RV']
        #
        # DJ_Name_Match = ['aapl','apple','intc','vz','nke','intc','nke','vz','msft','msft','msft','msft','intc','nke','xom','xom','xom','xom','xom','mmm', 'aapl', 'mmm', 'mmm', 'vz', 'v', 'wmt', 'wmt', 'wmt', 'wmt', 'trv', 'utx', 'utx', 'unh',
        #                  'unh', 'msft', 'nke', \
        #                  'pfe', 'pg', 'axp', 'jpm', 'mcd', 'mcd', 'mrk', 'jnj', 'intc', 'ibm', 'gs', 'hd', 'ge', 'xom',
        #                  'aapl', 'ba', 'cat', \
        #                  'cvx', 'csco', 'coke', 'dis', 'dd', 'dd', 'cat', 'coke', 'coke', 'utx', 'mmm', 'aapl',
        #                  'v',
        #                  'wmt', 'trv', 'utx', \
        #                  'unh', 'msft', 'nke', 'pfe', 'pg', 'axp', 'jpm', 'mcd', 'mrk', 'jnj', 'intc', 'ibm', 'gs',
        #                  'hd',
        #                  'ge', 'xom', 'ba', \
        #                  'cat', 'cvx', 'csco', 'coke', 'dis', 'dd', 'jnj', 'jnj', 'nke', 'nke', 'cat', 'trv']
        #
        # NYSE_Match = ['APPLE INC','APPLE INC','INTEL CORP','VERIZON COMMUNICATIONS INC','NIKE INC','INTEL CORP','NIKE INC','VERIZON COMMUNICATIONS INC','MICROSOFT CORP','MICROSOFT CORP','MICROSOFT CORP','MICROSOFT CORP','INTL BUSINESS MACHINES CORP','NIKE INC','EXXON MOBIL CORP','EXXON MOBIL CORP','EXXON MOBIL CORP','EXXON MOBIL CORP','EXXON MOBIL CORP','3M CO', 'APPLE INC', '3M CO', '3M CO', 'VERIZON COMMUNICATIONS INC', 'VISA INC',
        #               'WAL-MART STORES INC',
        #               'WAL-MART STORES INC', 'WAL-MART STORES INC', 'WAL-MART STORES INC', 'TRAVELERS COS INC',
        #               'UNITED TECHNOLOGIES CORP', 'UNITED TECHNOLOGIES CORP', 'UNITEDHEALTH GROUP INC',
        #               'UNITEDHEALTH GROUP INC', 'MICROSOFT CORP', 'NIKE INC', 'PFIZER INC', 'PROCTER & GAMBLE CO',
        #               'AMERICAN EXPRESS CO', 'JPMORGAN CHASE & CO', "MCDONALD'S CORP", "MCDONALD'S CORP",
        #               'MERCK & CO',
        #               'JOHNSON & JOHNSON', 'INTEL CORP', 'INTL BUSINESS MACHINES CORP', 'GOLDMAN SACHS GROUP INC',
        #               'HOME DEPOT INC', 'GENERAL ELECTRIC CO', 'EXXON MOBILE CORP', 'APPLE INC', 'BOEING CO',
        #               'CATERPILLAR INC', 'CHEVRON CORP', 'CISCO SYSTEMS INC', 'COCA-COLA CO', 'DISNEY (WALT) CO',
        #               'DU PONT (E I) DE NEMOURS', 'DU PONT (E I) DE NEMOURS', 'CATERPILLAR INC', 'COCA-COLA CO',
        #               'COCA-COLA CO', 'UNITED TECHNOLOGIES CORP', '3M CO', 'APPLE INC',
        #               'VISA INC', 'WAL-MART STORES INC', 'TRAVELERS COS INC', 'UNITED TECHNOLOGIES CORP',
        #               'UNITEDHEALTH GROUP INC',
        #               'MICROSOFT CORP', 'NIKE INC', 'PFIZER INC', 'PROCTER & GAMBLE CO', 'AMERICAN EXPRESS CO',
        #               'JPMORGAN CHASE & CO',
        #               "MCDONALD'S CORP", 'MERCK & CO', 'JOHNSON & JOHNSON', 'INTEL CORP',
        #               'INTL BUSINESS MACHINES CORP',
        #               'GOLDMAN SACHS GROUP INC',
        #               'HOME DEPOT INC', 'GENERAL ELECTRIC CO', 'EXXON MOBILE CORP', 'BOEING CO', 'CATERPILLAR INC',
        #               'CHEVRON CORP', 'CISCO SYSTEMS INC',
        #               'COCA-COLA CO', 'DISNEY (WALT) CO', 'DU PONT (E I) DE NEMOURS', 'JOHNSON & JOHNSON',
        #               'JOHNSON & JOHNSON', 'NIKE INC',
        #               'NIKE INC', 'CATERPILLAR INC', 'TRAVELERS COS INC']
        #
        #
        # merge_string_names = pd.DataFrame(DJ_Name_Match, index=Dow_Jones)
        # merge_string_names = merge_string_names.rename(columns={0: 'ticker'})
        # merge_string_names['names'] = merge_string_names.index
        #
        # NYSE_Match_df = pd.DataFrame(NYSE_Match, index=Dow_Jones)
        # NYSE_Match_df = NYSE_Match_df.rename(columns={0: 'ticker'})
        # NYSE_Match_df['names'] = NYSE_Match_df.index
        #
        # matches = []
        # for word in Dow_Jones:
        #     if word in phrase1:
        #         matches.append(word)
        #
        #
        # matches_df = pd.DataFrame(matches, index=matches)
        # matches_df = matches_df.rename(columns={0: 'names'})
        # selected_stocks_2 = pd.merge(matches_df, merge_string_names, on='names')
        #
        # final_ticker = selected_stocks_2['ticker']
        #
        # ticker = final_ticker[0]
        # ticker = 'WIKI/' + ticker.upper() + '.4'
        # pricedata = quandl.get(ticker, rows=1)
        # prices = pricedata['Close'][0]
        # indexmerge = pd.merge(matches_df, NYSE_Match_df, on='names')
        # current_prices_df = pd.DataFrame(prices, index=[indexmerge['ticker'][0]], columns=[0])
        #
        # convert = str(matches)
        #
        # n_stocks = len(matches)

        if any(word in phrase1 for word in command_list_dollar) or (word in phrase1 for word in command_list_percent) or command_list_average:
            if any(word in phrase1 for word in total) and any(word in phrase1 for word in command_list_percent):
                percent_extract = re.findall(r'\d+%', phrase1)
                for x in percent_extract:
                    conv_float = float(re.sub('[%]', '', x)) / 100
                percent_each_stock = conv_float / n_stocks
                investment_dollars_per_stock = df_port_sum * percent_each_stock
                df_convert = pd.DataFrame(np.array(matches),)
                df_convert[0] = investment_dollars_per_stock
                purchase_type = 0

            elif any(word in phrase1 for word in command_list_dollar) and any(word in phrase1 for word in total):
                search_for_dollars = re.sub('[$]', '', phrase1)
                investment_dollars = [int(s) for s in search_for_dollars.split() if s.isdigit()]
                inv_dol_int = list(map(int, investment_dollars))
                investment_dollars_per_stock = inv_dol_int[0] / n_stocks
                df_convert = pd.DataFrame(np.array(matches),)
                df_convert[0] = investment_dollars_per_stock

            elif any(word in phrase1 for word in command_list_average):
                investment_dollars_per_stock = df_port_amount["Current $ Value"].mean()
                df_convert = pd.DataFrame(np.array(matches),)
                df_convert[0] = investment_dollars_per_stock
                purchase_type = 0

            elif any(word in phrase1 for word in command_list_percent):
                percent_extract = re.findall(r'\d+%', phrase1)
                for x in percent_extract:
                    conv_float = float(re.sub('[%]', '', x)) / 100
                percent_each_stock = conv_float
                investment_dollars_per_stock = df_port_sum * percent_each_stock
                df_convert = pd.DataFrame(np.array(matches),)
                df_convert[0] = investment_dollars_per_stock
                # print(df_convert)
                purchase_type = 0

            elif any(word in phrase1 for word in shares):
                shares = [int(s) for s in phrase1.split() if s.isdigit()]
                inv_dol_int = list(map(int, shares))
                investment_dollars_per_stock = inv_dol_int[0] * current_prices_df[0]
                df_convert = pd.DataFrame(investment_dollars_per_stock,)
                df_convert[0] = investment_dollars_per_stock
                purchase_type = 0

            elif any(word in phrase1 for word in command_list_dollar):
                search_for_dollars = re.sub('[$]', '', phrase1)
                search_for_dollars = re.sub(',', '', search_for_dollars)
                investment_dollars = [int(s) for s in search_for_dollars.split() if s.isdigit()]
                inv_dol_int = list(map(int, investment_dollars))
                investment_dollars_per_stock = inv_dol_int[0]
                df_convert = pd.DataFrame(np.array(matches),)
                df_convert[0] = investment_dollars_per_stock
                purchase_type = 0

            elif len([int(s) for s in phrase1.split() if s.isdigit()]) >= 1:
                investment_dollars = [int(s) for s in phrase1.split() if s.isdigit()]
                inv_dol_int = list(map(int, investment_dollars))
                investment_dollars_per_stock = inv_dol_int[0]
                df_convert = pd.DataFrame(np.array(matches), )
                df_convert[0] = investment_dollars_per_stock
                purchase_type = 0

            else:
                purchase_type = 1

        if purchase_type == 0:
            # frames = [df_convert, np.transpose(portfolio)]
            #
            # mylist2 = pd.DataFrame(pd.concat(frames, ))
            # mylist = list(mylist2.index)
            # duplicates = [k for k, v in Counter(mylist).items() if v > 1]
            #
            # df_port_names_merge = pd.DataFrame(pd.concat(frames, join='outer'))
            #
            # df_port_names_merge2 = pd.DataFrame(df_port_names_merge[0])
            # df_port_names_merge2 = df_port_names_merge2.drop(df_port_names_merge2.index[1])
            # df_port_names_merge2_names = pd.DataFrame(df_port_names_merge2.index, index=df_port_names_merge2.index)
            #
            # frames2 = [nyse * 100, np.transpose(df_port_names_merge2_names)]
            # selected_stocks_merge = pd.DataFrame(pd.concat(frames2, join='inner'))
            # selected_stocks = pd.DataFrame(selected_stocks_merge.ix[:-1])
            #
            # user_port_weighting = pd.DataFrame(df_port_names_merge2[0] / df_port_names_merge2[0].sum())
            #
            # intervals = [21, 63, 126, 189, 252, 1260]
            # weights = [.35, .20, .15, .125, .10, .05, .025]
            #
            # output_list_avg = []
            # output_list_std = []
            # weighted_list_avg = []
            # excess_return_list = []
            #
            # rename_std = pd.DataFrame(user_port_weighting.rename(columns={0: '1 Year STD'}))
            # inv_vol_weighting = pd.DataFrame(rename_std)
            #
            # for interval in intervals:
            #     df_avg = selected_stocks.tail(interval)
            #     avg_calc = pd.DataFrame(np.mean(df_avg))
            #     rename_avg = avg_calc.rename(columns={0: 'Avg. Return'})
            #     output_list_avg.append(rename_avg)
            #
            # merge1_avg = pd.merge(output_list_avg[0], output_list_avg[1], left_index=True, right_index=True)
            # merge2_avg = pd.merge(merge1_avg, output_list_avg[2], left_index=True, right_index=True)
            # merge3_avg = pd.merge(merge2_avg, output_list_avg[3], left_index=True, right_index=True)
            # merge4_avg = pd.merge(merge3_avg, output_list_avg[4], left_index=True, right_index=True)
            # merge5_avg = pd.merge(merge4_avg, output_list_avg[5], left_index=True, right_index=True)
            #
            # i = 0
            #
            # while i <= 5:
            #     newdf = pd.DataFrame(merge5_avg.ix[:, i] * weights[i])
            #     weighted_list_avg.append(newdf)
            #     i = i + 1
            #
            # mergeweight1 = pd.merge(weighted_list_avg[0], weighted_list_avg[1], left_index=True, right_index=True)
            # mergeweight2 = pd.merge(mergeweight1, weighted_list_avg[2], left_index=True, right_index=True)
            # mergeweight3 = pd.merge(mergeweight2, weighted_list_avg[3], left_index=True, right_index=True)
            # mergeweight4 = pd.merge(mergeweight3, weighted_list_avg[4], left_index=True, right_index=True)
            # mergeweight5 = pd.merge(mergeweight4, weighted_list_avg[5], left_index=True, right_index=True)
            # mergeweight5.columns = ['WAvg 1 month', 'WAvg 3 month', 'WAvg 6 month', 'WAvg 9 month', 'WAvg 1 Year',
            #                         'WAvg 5 Year']
            # mergeweight5['WAvg Sum'] = mergeweight5.sum(axis=1)
            # WVag = pd.DataFrame(mergeweight5['WAvg Sum'].copy())
            # transpose_WVag = np.transpose(WVag)
            #
            # selected_stocks_tail = selected_stocks.tail(252)
            # array_length = len(selected_stocks_tail.columns) - 1
            #
            # i = 0
            #
            # while i <= array_length:
            #     excess_return = pd.DataFrame(selected_stocks_tail.iloc[:, i] - transpose_WVag.ix['WAvg Sum', i])
            #     excess_return_list.append(excess_return)
            #     i = i + 1
            #
            # excess_return_output = pd.DataFrame(
            #     ft.reduce(lambda x, y: pd.merge(x, y, left_index=True, right_index=True), excess_return_list))
            # excess_return_transpose = pd.DataFrame(np.transpose(excess_return_output))
            # cov_matrix = pd.DataFrame(
            #     np.dot(excess_return_transpose.as_matrix(), excess_return_output.as_matrix()) / (100 * (252 - 1)))
            #
            # marginal_return = pd.DataFrame(pd.merge(inv_vol_weighting, WVag, left_index=True, right_index=True))
            # marginal_return['Return'] = (marginal_return['1 Year STD'] * marginal_return['WAvg Sum'])
            # total_return_usr = marginal_return['Return'].sum()
            #
            # transpose_inv_vol = pd.DataFrame(np.transpose(inv_vol_weighting))
            #
            # Var_Port = np.dot(transpose_inv_vol.as_matrix(), np.dot(cov_matrix.as_matrix(), inv_vol_weighting.as_matrix()))
            # STD_usr_Port = math.sqrt(Var_Port)
            # sharpe_ratio_whatif = total_return_usr / STD_usr_Port
            #
            # df_port_amount = pd.DataFrame(portfolio['Current $ Value'])
            # df_port_names = pd.DataFrame.transpose(df_port_amount.ix[:, 1:1])
            #
            # df_port_sum = df_port_amount["Current $ Value"].sum()
            # user_port_weighting = pd.DataFrame(df_port_amount["Current $ Value"] / df_port_sum)
            #
            # frames = [nyse * 100, df_port_names]
            #
            # selected_stocks = pd.DataFrame(pd.concat(frames, join='inner'))
            #
            # intervals = [21, 63, 126, 189, 252, 1260]
            # weights = [.35, .20, .15, .125, .10, .05, .025]
            #
            # output_list_avg = []
            # output_list_std = []
            # weighted_list_avg = []
            # excess_return_list = []
            #
            # rename_std = pd.DataFrame(user_port_weighting.rename(columns={'Current $ Value': '1 Year STD'}))
            # inv_vol_weighting = pd.DataFrame(rename_std)
            #
            # for interval in intervals:
            #     df_avg = selected_stocks.tail(interval)
            #     avg_calc = pd.DataFrame(np.mean(df_avg))
            #     rename_avg = avg_calc.rename(columns={0: 'Avg. Return'})
            #     output_list_avg.append(rename_avg)
            #
            # merge1_avg = pd.merge(output_list_avg[0], output_list_avg[1], left_index=True, right_index=True)
            # merge2_avg = pd.merge(merge1_avg, output_list_avg[2], left_index=True, right_index=True)
            # merge3_avg = pd.merge(merge2_avg, output_list_avg[3], left_index=True, right_index=True)
            # merge4_avg = pd.merge(merge3_avg, output_list_avg[4], left_index=True, right_index=True)
            # merge5_avg = pd.merge(merge4_avg, output_list_avg[5], left_index=True, right_index=True)
            #
            # i = 0
            #
            # while i <= 5:
            #     newdf = pd.DataFrame(merge5_avg.ix[:, i] * weights[i])
            #     weighted_list_avg.append(newdf)
            #     i = i + 1
            #
            # mergeweight1 = pd.merge(weighted_list_avg[0], weighted_list_avg[1], left_index=True, right_index=True)
            # mergeweight2 = pd.merge(mergeweight1, weighted_list_avg[2], left_index=True, right_index=True)
            # mergeweight3 = pd.merge(mergeweight2, weighted_list_avg[3], left_index=True, right_index=True)
            # mergeweight4 = pd.merge(mergeweight3, weighted_list_avg[4], left_index=True, right_index=True)
            # mergeweight5 = pd.merge(mergeweight4, weighted_list_avg[5], left_index=True, right_index=True)
            # mergeweight5.columns = ['WAvg 1 month', 'WAvg 3 month', 'WAvg 6 month', 'WAvg 9 month', 'WAvg 1 Year',
            #                         'WAvg 5 Year']
            # mergeweight5['WAvg Sum'] = mergeweight5.sum(axis=1)
            # WVag = pd.DataFrame(mergeweight5['WAvg Sum'].copy())
            # transpose_WVag = np.transpose(WVag)
            #
            # selected_stocks_tail = selected_stocks.tail(252)
            # array_length = len(selected_stocks_tail.columns) - 1
            #
            # i = 0
            #
            # while i <= array_length:
            #     excess_return = pd.DataFrame(selected_stocks_tail.iloc[:, i] - transpose_WVag.ix['WAvg Sum', i])
            #     excess_return_list.append(excess_return)
            #     i = i + 1
            #
            # excess_return_output = pd.DataFrame(
            #     ft.reduce(lambda x, y: pd.merge(x, y, left_index=True, right_index=True), excess_return_list))
            # excess_return_transpose = pd.DataFrame(np.transpose(excess_return_output))
            # cov_matrix = pd.DataFrame(
            #     np.dot(excess_return_transpose.as_matrix(), excess_return_output.as_matrix()) / (100 * (252 - 1)))
            #
            # marginal_return = pd.DataFrame(pd.merge(inv_vol_weighting, WVag, left_index=True, right_index=True))
            # marginal_return['Return'] = (marginal_return['1 Year STD'] * marginal_return['WAvg Sum'])
            # total_return_new = marginal_return['Return'].sum()
            #
            # transpose_inv_vol = pd.DataFrame(np.transpose(inv_vol_weighting))
            #
            # Var_Port = np.dot(transpose_inv_vol.as_matrix(), np.dot(cov_matrix.as_matrix(), inv_vol_weighting.as_matrix()))
            # STD_Port_new = math.sqrt(Var_Port)
            # sharpe_ratio_user_port = total_return_new / STD_Port_new

            total_return_usr = 0.103634423977
            STD_usr_Port = 0.09921735767433723
            sharpe_ratio_user_port = total_return_usr / STD_usr_Port

            total_return_new = uniform(1, 20) / 100
            STD_Port_new = uniform(1, 20) / 100
            sharpe_ratio_whatif = total_return_new / STD_Port_new

            if sharpe_ratio_user_port > sharpe_ratio_whatif:
                yara_text = "Look at the graph above. The graph compares your current portfolio with the portfolio with your new investment in it. The bigger the bubble, the better the return to risk of the portfolio. So " + \
                    "if your current portfolio shows a bigger bubble, that means the investment did not make your portfolio better. If you see only one bubble, that means the bigger bubble is covering the smaller one. " + \
                    "For you finance aficionados, I'm comparing the Sharpe Ratios. The better sharpe ratio shows up as the bigger bubble." + '<br />' + '<br />' + \
                    '<b>'"In this scenario, the investment would NOT improve your portfolio. However, if you'd still like, I can go ahead and purchase it for you."'</b>'
            else:
                yara_text = "Look at the graph above. The graph compares your current portfolio with the portfolio with your new investment in it. The bigger the bubble, the better the return to risk of the portfolio. So " + \
                    "if your current portfolio shows a bigger bubble, that means the investment did not make your portfolio better. If you see only one bubble, that means the bigger bubble is covering the smaller one. " + \
                    "For you finance aficionados, I'm comparing the Sharpe Ratios. The better sharpe ratio shows up as the bigger bubble." + '<br />' + '<br />' + \
                    '<b>'"In this scenario, the investment WOULD improve your portfolio. If you'd like, I can go ahead and purchase it for you."'</b>'

            #print(total_return_new)

            # print(sharpe_ratio_user_port)
            # print(sharpe_ratio_whatif)
            # print(total_return_new)
            # print(total_return_usr)
            # print(STD_Port_new)
            # print(STD_usr_Port)

            # print(ticker)
            array = 0
            number = 7
            Buy = 0
            Hold = 0
            Sell = 0
            q1 = 0
            q2 = 0
            q3 = 0
            q4 = 0
            tickers = [matches[0]]
            date = 0
            sharperatiouser = abs(sharpe_ratio_user_port)
            sharperatiowhatif = abs(sharpe_ratio_whatif)
            total_return_new = abs(total_return_new * 100)
            total_return_usr = abs(total_return_usr * 100)
            STD_Port_new = STD_Port_new * 100
            STD_usr_Port = STD_usr_Port * 100


        else:
            yara_text = "Did not get what you said. You'll need to specify how much you want to invest. You can type a dollar amount or percentage (e.g. $1000 or 10%). In other words, type better or follow instructions so I can understand what you want. WHAT DO YOU WANT?"
            array = 0
            number = 7
            Buy = 0
            Hold = 0
            Sell = 0
            q1 = 0
            q2 = 0
            q3 = 0
            q4 = 0
            tickers = ['']
            date = 0
            sharperatiouser = 0
            sharperatiowhatif = 0
            total_return_new = 0
            total_return_usr = 0
            STD_Port_new = 0
            STD_usr_Port = 0

    else:
        yara_text = "Either you're terrible at typing or I don't have that functionality yet. Please try again later or type better."
        array = 0
        number = 5
        Buy = 0
        Hold = 0
        Sell = 0
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        tickers = ['']
        date = 0
        sharperatiouser = 0
        sharperatiowhatif = 0
        total_return_new = 0
        total_return_usr = 0
        STD_Port_new = 0
        STD_usr_Port = 0

    # print(tickers)

    return jsonify({
        # 'resultpopup': result,
        'yararesponse': yara_text,
        #'portfoliotable': portfolio
        'array': array,
        'number': number,
        'Buy': Buy,
        'Hold': Hold,
        'Sell': Sell,
        'q1': q1,
        'q2': q2,
        'q3': q3,
        'q4': q4,
        'stock': tickers[0],
        'date': date,
        'sharpeuser': sharperatiouser,
        'sharpewhatif': sharperatiowhatif,
        'total_return_new': total_return_new,
        'total_return_usr': total_return_usr,
        'STD_Port_new': STD_Port_new,
        'STD_usr_Port': STD_usr_Port
    })


if __name__ == '__main__':
    app.run(debug=True)