from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
import random
from textblob import TextBlob

ran=[[11,30],[31,50],[51,70],[71,90],[91,110],[111,130],
    [131,150],[151,170],[171,190],[191,210],[211,230],[231,250]
    ,[251,270],[271,290],[291,310],[311,330],[331,350],[351,370],[371,390]
    ,[391,410],[411,430],[431,450],[451,470]]

title=[]
href=[]
driver = webdriver.Firefox(executable_path = r'D:\Programmes\geckodriver.exe')

sa=open('names.txt','r')
sa=list(sa)
for i in sa:
    sa[sa.index(i)]=i.rstrip()

politicians=[]

def getlist():

    url = 'https://economictimes.indiatimes.com/topic/rahul-gandhi'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    div = soup.find('div', {"id":"leftContainer"})
    div2=div.find_all('a')
    for link in div2:
        if link.find('h3') is not None:
            x=str(link.find('h3'))
            if "Rahul Gandhi" in x or "Gandhi" in x:
                check2(link['href'])

def check2(url2):
    url="https://economictimes.indiatimes.com"+str(url2)
    driver.set_page_load_timeout(5)
    try:
        driver.get(url)
    except TimeoutException:
        driver.execute_script("window.stop();")
    soup = BeautifulSoup(driver.page_source, 'lxml')
    div = soup.find('div', {"class":"Normal"})
    if div==None:
        return
    x=str(div.text)
    q=x.split("\n\n")
    for j in q:
            if j=='':
                continue
            k=0
            if ((' ' + 'said' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'tweeted' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'tweeted,' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'said,' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'said:' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'saying' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'tweeted.' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'added.' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'alleged.' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'alleged' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'said.' + ' ') in (' ' + j + ' ')):
                if '"she said' in j:
                    continue
                if 'source said' in j or 'source added' in j or 'chief minister said' in j:
                    continue
                if 'report said' in j or 'it said' in j:
                    continue
                if '"he had said' in j:
                    continue
                for s in sa:
                    if s in j:
                        if j.find('"')==-1:
                            break
                        if s+' added' in j or s+' said' in j or s+' tweeted' in j or 'tweeted ' +s in j or 'said ' +s in j or 'added ' +s in j:
                            p=j.find('"')
                            q=j.find('"',p+1)
                            politicians.append([s,j[p+1:q]])
                            k=1
                            break

                if k!=1:
                    if j.find('"')==-1:
                        continue
                    p=j.find('"')
                    q=j.find('"',p+1)
                    politicians.append([s,j[p+1:q]])
                    politicians.append(['Rahul Gandhi',j])

def getlist2():
    url = 'https://economictimes.indiatimes.com/topic/Narendra-Modi/news'
    driver.get(url)
    soup = BeautifulSoup(driver.page_source,'lxml')
    div = soup.find(id='leftContainer')
    div2=div.find_all('a')
    for link in div2:
        if link.find('h3') is not None:
            x=str(link.find('h3'))
            if "Narendra Modi" in x or "Modi" in x:
                check3(link['href'])



def check3(url2):
    url="https://economictimes.indiatimes.com"+str(url2)
    driver.set_page_load_timeout(5)
    try:
        driver.get(url)
    except TimeoutException:
        driver.execute_script("window.stop();")
    soup = BeautifulSoup(driver.page_source, 'lxml')
    div = soup.find('div', {"class":"Normal"})
    if div==None:
        return
    x=str(div.text)
    q=x.split("\n\n")
    for j in q:
            if j=='':
                continue
            k=0
            if ((' ' + 'said' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'tweeted' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'tweeted,' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'said,' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'said:' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'saying' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'tweeted.' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'added.' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'alleged.' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'alleged' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'said.' + ' ') in (' ' + j + ' ')):
                if '"she said' in j:
                    continue
                if 'source said' in j or 'source added' in j or 'chief minister said' in j:
                    continue
                if 'report said' in j or 'it said' in j:
                    continue
                if '"he had said' in j:
                    continue
                for s in sa:
                    if s in j:
                        if j.find('"')==-1:
                            break
                        if s+' added' in j or s+' said' in j or s+' tweeted' in j or 'tweeted ' +s in j or 'said ' +s in j or 'added ' +s in j:
                            p=j.find('"')
                            q=j.find('"',p+1)
                            politicians.append([s,j[p+1:q]])
                            k=1
                            break

                if k!=1:
                    if j.find('"')==-1:
                        continue
                    p=j.find('"')
                    q=j.find('"',p+1)
                    politicians.append([s,j[p+1:q]])
                    politicians.append(['Modi',j])



def news18blog(url2):
    url=str(url2)
    driver.set_page_load_timeout(5)
    try:
        driver.get(url)
    except TimeoutException:
        driver.execute_script("window.stop();")
    try:
        soup = BeautifulSoup(driver.page_source, 'lxml')
    except Exception as e:
        return
    div = soup.find('div', {"id":"article_body"})
    if div==None:
        return
    x=str(div.text)
    q=x.split("\n\n")
    for j in q:
            if j=='':
                continue
            if ((' ' + 'said' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'tweeted' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'tweeted,' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'said,' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'said:' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'saying' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'tweeted.' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'added.' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'alleged.' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'alleged' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'said.' + ' ') in (' ' + j + ' ')):

                for s in sa:
                    if s in j:
                        if j.find('"')==-1:
                            break
                        if s+' added' in j or s+' said' in j or s+' alleged' in j or s+' claimed' in j or s+' told' in j\
                                or s+' quipped' in j or s+' had said' in j or s+' had told' in j \
                                or s+' tweeted' in j or 'tweeted ' +s in j \
                                or 'said ' +s in j or 'says ' +s in j or 'added ' +s in j:
                            p=j.find('"')
                            q=j.find('"',p+1)
                            politicians.append([s,j[p+1:q]])
                            break



def news18get(url1):
    url = 'https://www.news18.com/politics/'+str(url1)
    driver.set_page_load_timeout(10)
    try:
        driver.get(url)
    except TimeoutException:
        driver.execute_script("window.stop();")
    soup = BeautifulSoup(driver.page_source,'lxml')
    div = soup.find('div',{'class':'blog-list'})
    if div==None:
        return
    div2=div.find_all('a')
    div2=list(div2)
    m=0
    for link in div2:
        if m%2==0:
            m=m+1
            continue
        news18blog(link['href'])
        m=m+1


def indianexpressblog(url1):
    url=str(url1)
    driver.set_page_load_timeout(5)
    try:
        driver.get(url)
    except TimeoutException:
        driver.execute_script("window.stop();")
    try:
        soup = BeautifulSoup(driver.page_source, 'lxml')
    except Exception as e:
        return
    div = soup.find('div', {"class":"full-details"})
    if div==None:
        return
    x=list(div.find_all('p'))
    for i in x:
        if i is not None:
            j=str(i.text)
            if j=='':
                continue
            if ((' ' + 'said' + ' ') in (' ' + j + ' ')) or \
                ((''+'said' + ' ') in (' ' + j + ' ')) or \
                ((' '+'said' + '') in (' ' + j + ' ')) or \
                    ((' ' + 'tweeted' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'tweeted,' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'said,' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'said:' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'saying' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'tweeted.' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'added.' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'alleged.' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'alleged' + ' ') in (' ' + j + ' ')) or \
                    ((' ' + 'said.' + ' ') in (' ' + j + ' ')):

                for s in sa:
                    if s in j:
                        if j.find('“')==-1:
                            break
                        if s+' added' in j or s+' said' in j or s+' alleged' in j or s+' claimed' in j or s+' told' in j\
                                or s+' quipped' in j or s+' had said' in j or s+' had told' in j \
                                or s+' tweeted' in j or 'tweeted ' +s in j \
                                or 'said ' +s in j or 'says ' +s in j or 'added ' +s in j:
                            p=j.find('“')
                            q=j.find('”')
                            politicians.append([s,j[p+1:q]])
                            break


def indianexpressget(url1):
    url = 'http://indianexpress.com/section/india/politics/'+url1
    driver.set_page_load_timeout(10)
    try:
        driver.get(url)
    except TimeoutException:
        driver.execute_script("window.stop();")
    soup = BeautifulSoup(driver.page_source,'lxml')
    div = soup.find('div',{'class':'nation'})
    div2=div.find_all('a')
    div2=list(div2)
    del div2[len(div2)-1]
    del div2[len(div2)-1]
    del div2[len(div2)-1]
    del div2[len(div2)-1]
    m=0
    for link in div2:
        if m%2==0:
            m=m+1
            continue
        indianexpressblog(link['href'])
        m=m+1

getlist()
getlist2()

for i in range(1,11):
     if i==1:
         news18get('')
     else:
         news18get('page-'+str(i))

for i in range(1,11):
    if i==1:
        indianexpressget(' ')
    else:
        indianexpressget('page/'+str(i)+'/')


xyz=random.choice(ran)
for i in range(xyz[0],xyz[1]):
        print(i)
        indianexpressget('page/'+str(i)+'/')

for i in range(len(politicians)):
    qw=TextBlob(politicians[i][1])
    if qw.sentiment.polarity>0.05:
        politicians[i].append('Positive')
    elif qw.sentiment.polarity<(-0.05):
        politicians[i].append('Negative')
    else:
        politicians[i].append('Neutral')
    politicians[i].append(round(qw.sentiment.subjectivity*100,2))

for i in politicians:
    print(i)

print(len(politicians))











