#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
import os


# In[6]:


ones = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 
        'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19}

tens = {'twenty': 2, 'thirty': 3, 'forty': 4, 'fifty': 5, 'sixty': 6, 'seventy': 7, 'eighty': 8, 'ninety': 9}


# In[18]:


dates = []
casesList = []

location = 'Cases'
directory = os.fsencode(location)

intNumberofCases = 0

for file in sorted(os.listdir(directory)):
     filename = os.fsdecode(file)
     
     date = filename.replace('-22 NHS COVID Communication.txt', '').strip().replace('-','/')
     dates.append(date)
     
     fileLocation = location + "/" + filename
     
     with open(fileLocation, encoding="utf8") as f:
        lines = f.read()
    
        endofCaseNumber = lines.find("confirmed")
        numberofCases = lines[228:endofCaseNumber]

        if(numberofCases.find('(') != -1):
            numberStart = numberofCases.find('(')
            numberEnd = numberofCases.find(')')
            intNumberofCases = int(numberofCases[numberStart+1 : numberEnd])
            casesList.append(intNumberofCases)
    
        else:
            numberofCases = numberofCases.lower().strip()
            if numberofCases in ones:
                casesList.append(ones[numberofCases])
            elif numberofCases in tens:
                casesList.append(tens[numberofCases] * 10)
            else:
                numberofCases = numberofCases.replace('-',' ')
                division = numberofCases.find(' ')
                firstPt = numberofCases[0:division].strip().lstrip()
                secondPt = numberofCases[division:len(numberofCases)].strip().lstrip()
                
                intNumberofCases = int(str(tens[firstPt]) + str(ones[secondPt]))
                casesList.append(intNumberofCases)
                
                
dataDict = dict(zip(dates,casesList))


# In[19]:


#function for key
def sortKey(inputdate):
    divide = inputdate.find('/')
    month = inputdate[0:divide]
    day = int(inputdate[divide+1:len(inputdate)])
    schoolMonth = {'9':1, '10':2, '11':3, '12':4,'1':5,'2':6,'3':7,'4':8,'5':9,'6':10}
    return (schoolMonth[month]*100) + day
    
#sorting the dictionary by date
sorted_dates = sorted(dataDict.items(), key = lambda date: sortKey(date[0]))
final_dict = dict(sorted_dates)



# In[20]:


df = pd.DataFrame(final_dict.items(), columns=['Date', 'Cases'])


