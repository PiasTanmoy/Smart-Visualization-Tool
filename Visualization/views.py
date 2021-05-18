from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import numpy as np
import pandas as pd
from json import dumps

# Create your views here.




global_username = ''
global_password = ''

global_from_date = ''
global_to_date = ''

global_file_name = ''


def check_user(request):
    global global_username
    global global_password
    if global_username != "mercadante" or global_password != "smartfeed":
        print('1')
        return redirect('credentials')
    print('2')
    return True



def csv_data_read(request):
    return render(request, 'JS-learn.html')

def bar(request):
    return render(request, 'bar.html')

def multiple_chart(request):
    return render(request, 'multiple_chart.html')

def smartScale(request):
    return render(request, 'smartScaleData.html')

def smartScale2(request):
    return render(request, 'smartScaleData2.html')

def dataSelection(request):
    return render(request, 'data_selection.html')

def dataSelection2(request):

    #############################################################
    global global_username
    global global_password
    if global_username != "mercadante" or global_password != "smartfeed":
        print('1')
        return redirect('credentials')
    ########################################################################


    x = 0

    if request.method == "POST":
        x = request.POST.get("title")
        x = x.replace('[', '')
        x = x.replace(']', '')
        x = list(x.split(" "))
        x = int(x[0])
        print(x, type(x))

    dataset = pd.read_csv('media/data/AnimalWeights_3.csv')

    datanumpy = np.array(dataset)


    datanumpy = enumerate(datanumpy)

    dataJSON = dumps({'val': 555})

    context = {
        'dataset': dataset,
        'datanumpy': list(datanumpy),
        'val': 5,
        'dataJSON': dataJSON,
        'single': x

    }


    return render(request, 'data_selection2.html', context=context)

def dataSelection2single(request):
    #############################################################
    global global_username
    global global_password
    if global_username != "mercadante" or global_password != "smartfeed":
        print('1')
        return redirect('credentials')
    ########################################################################

    x = 0

    if request.method == "POST":
        x = request.POST.get("title")
        x = x.replace('[', '')
        x = x.replace(']', '')
        x = list(x.split(" "))
        x = int(x[0])
        print(x, type(x))

    dataset = pd.read_csv('media/data/AnimalWeights_3.csv')

    datanumpy = np.array(dataset)

    nColumn = np.arange(datanumpy.shape[1]-2)
    nRows = np.arange(datanumpy.shape[0])


    datanumpy = enumerate(datanumpy)

    dataJSON = dumps({'val': 555})



    context = {
        'dataset': dataset,
        'datanumpy': list(datanumpy),
        'val': 5,
        'dataJSON': dataJSON,
        'single': x,
        'nColumn': nColumn,
        'nRows': nRows

    }


    return render(request, 'data_selection2-single.html', context=context)



def dataSelection2singleCol(request):
    #############################################################
    global global_username
    global global_password
    if global_username != "mercadante" or global_password != "smartfeed":
        print('1')
        return redirect('credentials')
    ########################################################################


    x = 0

    if request.method == "POST":
        x = request.POST.get("title")
        x = x.replace('[', '')
        x = x.replace(']', '')
        x = list(x.split(" "))
        x = int(x[0])


    dataset = pd.read_csv('media/data/AnimalWeights_3.csv')

    datanumpy = np.array(dataset)

    nColumn = np.arange(datanumpy.shape[1]-2)
    nRows = np.arange(datanumpy.shape[0])


    datanumpy = enumerate(datanumpy)

    dataJSON = dumps({'val': 555})




    context = {
        'dataset': dataset,
        'datanumpy': list(datanumpy),
        'val': 5,
        'dataJSON': dataJSON,
        'single': x,
        'nColumn': nColumn,
        'nRows': nRows

    }


    return render(request, 'data_selection2-single-col.html', context=context)







def getCredentials(request):
    wrong_credentials = False

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        wrong_credentials = True

        if username == "mercadante" and password == "smartfeed":
            global global_username
            global global_password

            global_password = password
            global_username = username

            print(global_username)

            return redirect('getDataset')

    context = {'wrong_credentials': wrong_credentials}

    return render(request, 'get_credentials.html', context)


def getDataSet(request):
    #############################################################
    global global_username
    global global_password
    if global_username != "mercadante" or global_password != "smartfeed":
        print('1')
        return redirect('credentials')
    ########################################################################

    successful = False
    if request.method == "POST":
        from_date = request.POST.get('from_date')
        to_date = request.POST.get('to_date')

        global global_from_date
        global global_to_date

        global_from_date = from_date
        global_to_date = to_date

        donwloadDataset()
        successful = True

        print(global_from_date, global_to_date)

    context = {'successful': successful}

    return render(request, 'date_range.html', context)


def donwloadDataset():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    import time
    import getpass

    global global_from_date
    global global_to_date

    global global_username
    global global_password

    # Create a automated Chrome window
    PATH = '/home/tanmoy/PycharmProjects/djangoProject/media/chromedriver'
    driver = webdriver.Chrome(PATH)

    # Go to the website with a link
    driver.get("https://greenfeed.c-lockinc.com/GreenFeed/home.php")
    #browser.get("https://greenfeed.c-lockinc.com/GreenFeed/home.php")


    username_input = "mercadante"
    password_input = "smartfeed"

    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    # username.send_keys(username_input)  # "mercadante"
    username.send_keys(global_username)  # "mercadante"
    # password.send_keys(password_input)  # "smartfeed"
    password.send_keys(global_password)  # "smartfeed"
    time.sleep(2)
    username.send_keys(Keys.RETURN)

    #time.sleep(5)

    # https://greenfeed.c-lockinc.com/GreenFeed/sfanimals.php

    # Negivate to the "Feed & Gain" page
    driver.get("https://greenfeed.c-lockinc.com/GreenFeed/sfanimals.php")

    # click on the tab "Animal Weight"
    link = driver.find_element_by_link_text("Animal Weight")
    link.click()

    # Select date
    WeightDateFrom = driver.find_element_by_id("WeightDateFrom")
    WeightDateFrom.clear()
    # WeightDateFrom.send_keys("10-05-2020")
    WeightDateFrom.send_keys(global_from_date)

    WeightDateTo = driver.find_element_by_id("WeightDateTo")
    WeightDateTo.clear()
    # WeightDateTo.send_keys('11-30-2020')
    WeightDateTo.send_keys(global_to_date)

    time.sleep(2)

    # Click "Go" button
    go = driver.find_element_by_id("AnimalWeightsButton")
    go.click()

    time.sleep(5)

    # Click "Download" button
    download = driver.find_element_by_id("AnimalWeightsDLButton")
    download.click()

    time.sleep(5)

    driver.close()
    driver.quit()

    file_downloaded = r'/home/tanmoy/Downloads/AnimalWeights_' \
                + global_from_date[-4:] + '-' + global_from_date[:-5] \
                + "-" \
                + global_to_date[-4:] + '-' + global_to_date[:-5] \
                + '.csv'

    from shutil import copy

    global file_name
    file_name = 'AnimalWeights_' \
                + global_from_date[-4:] + '-' + global_from_date[:-5] \
                + "-" \
                + global_to_date[-4:] + '-' + global_to_date[:-5] \
                + '.csv'

    file_path = '/home/tanmoy/PycharmProjects/djangoProject/media/data'

    import shutil
    import os

    os.rename(file_downloaded, r'/home/tanmoy/PycharmProjects/djangoProject/media/data/AnimalWeights_3.csv')
    #shutil.move(file_downloaded, r'/home/tanmoy/PycharmProjects/djangoProject/media/data/AnimalWeights_3.csv')
    #os.replace(file_downloaded, r'/home/tanmoy/PycharmProjects/djangoProject/media/data/AnimalWeights_3.csv')

    #copy(file_downloaded, r'/home/tanmoy/PycharmProjects/djangoProject/media/data/AnimalWeights_3.csv')


    #df = pd.read_csv(r'/home/tanmoy/PycharmProjects/djangoProject/media/data/AnimalWeights_3.csv')
    #df.to_csv(r'/home/tanmoy/PycharmProjects/djangoProject/media/data/AnimalWeights_3.csv', index=False)




def getDashboard(request):
    # moveDataset()
    return render(request, 'dashboard.html')

def logout(request):
    # moveDataset()
    global global_username
    global global_password
    global_username = ''
    global_password = ''
    return redirect('credentials')


def testGroud(request):

    import os
    os.rename('/home/tanmoy/PycharmProjects/djangoProject/media/data/AnimalWeights_2020-10-05-2020-10-20.csv',
              '/home/tanmoy/PycharmProjects/djangoProject/media/data/AnimalWeights.csv')

    global global_from_date
    global global_to_date

    x = '10-05-2020'

    yyyy = x[-4:]
    dd_mm = x[:-5]

    print(x)
    print(yyyy + '-' + dd_mm)

    return redirect('test')

