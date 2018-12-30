import requests
from bs4 import BeautifulSoup
import sys
def getQuestions(error):
    stacklink=r'https://stackoverflow.com'
    toQuery=lambda x:'/search?q='+'+'.join(x.split())

    # error='unicode error'

    url=stacklink+toQuery(error)
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    questionList=soup.find_all(class_='question-hyperlink')
    questionDict={}

    for question in questionList:
        if question.get('title'): # if it's not none
            questionDict[question.get('title')] = stacklink+question.get('href')
    return questionDict

importname=sys.argv[1] if '.py' not in sys.argv[1] else sys.argv[1][:-3] # remove .py extension if it's there
try:
    exec('import '+importname)
    print('No Errors!')
except Exception as e:
    error= e.__class__.__name__+' '+ str(e) # str() calls the __str__ method of class which gives exeption description
    print(error)
    questionDict=getQuestions(error)
    print('Questions:\n')
    for q in questionDict:
        print('Q:{}\nL:{}\n'.format(q,questionDict[q]))