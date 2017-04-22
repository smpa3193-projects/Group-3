import csv
import requests
from BeautifulSoup import BeautifulSoup

urls = ["http://aaspeechesdb.oscars.org/results.aspx?AC=PREV_RECORD&XC=/results.aspx&BU=http%3A%2F%2Faaspeechesdb.oscars.org%2F&TN=aatrans&SN=AUTO195&SE=397&RN=1&MR=0&TR=0&TX=1000&ES=0&CS=0&XP=&RF=WebReportList&EF=&DF=WebReportOscars&RL=0&EL=0&DL=0&NP=255&ID=&MF=oscarsmsg.ini&MQ=&TI=0&DT=&ST=0&IR=0&NR=0&NB=0&SV=0&SS=0&BG=&FG=&QS=&OEX=ISO-8859-1&OEH=utf-8", "http://aaspeechesdb.oscars.org/results.aspx?AC=NEXT_RECORD&XC=/results.aspx&BU=http%3A%2F%2Faaspeechesdb.oscars.org%2F&TN=aatrans&SN=AUTO6273&SE=453&RN=0&MR=0&TR=0&TX=1000&ES=0&CS=0&XP=&RF=WebReportList&EF=&DF=WebReportOscars&RL=0&EL=0&DL=0&NP=255&ID=&MF=oscarsmsg.ini&MQ=&TI=0&DT=&ST=0&IR=0&NR=0&NB=0&SV=0&SS=0&BG=&FG=&QS=&OEX=ISO-8859-1&OEH=utf-8", "http://aaspeechesdb.oscars.org/results.aspx?AC=NEXT_RECORD&XC=/results.aspx&BU=http%3A%2F%2Faaspeechesdb.oscars.org%2F&TN=aatrans&SN=AUTO6273&SE=453&RN=1&MR=0&TR=0&TX=1000&ES=0&CS=0&XP=&RF=WebReportList&EF=&DF=WebReportOscars&RL=0&EL=0&DL=0&NP=255&ID=&MF=oscarsmsg.ini&MQ=&TI=0&DT=&ST=0&IR=0&NR=1&NB=0&SV=0&SS=0&BG=&FG=&QS=&OEX=ISO-8859-1&OEH=utf-8", "http://aaspeechesdb.oscars.org/results.aspx?AC=NEXT_RECORD&XC=/results.aspx&BU=http%3A%2F%2Faaspeechesdb.oscars.org%2F&TN=aatrans&SN=AUTO6273&SE=453&RN=2&MR=0&TR=0&TX=1000&ES=0&CS=0&XP=&RF=WebReportList&EF=&DF=WebReportOscars&RL=0&EL=0&DL=0&NP=255&ID=&MF=oscarsmsg.ini&MQ=&TI=0&DT=&ST=0&IR=0&NR=2&NB=0&SV=0&SS=0&BG=&FG=&QS=&OEX=ISO-8859-1&OEH=utf-8", "http://aaspeechesdb.oscars.org/results.aspx?AC=PREV_RECORD&XC=/results.aspx&BU=http%3A%2F%2Faaspeechesdb.oscars.org%2F&TN=aatrans&SN=AUTO6488&SE=455&RN=1&MR=0&TR=0&TX=1000&ES=0&CS=0&XP=&RF=WebReportList&EF=&DF=WebReportOscars&RL=0&EL=0&DL=0&NP=255&ID=&MF=oscarsmsg.ini&MQ=&TI=0&DT=&ST=0&IR=0&NR=0&NB=0&SV=0&SS=0&BG=&FG=&QS=&OEX=ISO-8859-1&OEH=utf-8", "http://aaspeechesdb.oscars.org/results.aspx?AC=NEXT_RECORD&XC=/results.aspx&BU=http%3A%2F%2Faaspeechesdb.oscars.org%2F&TN=aatrans&SN=AUTO6488&SE=455&RN=0&MR=0&TR=0&TX=1000&ES=0&CS=0&XP=&RF=WebReportList&EF=&DF=WebReportOscars&RL=0&EL=0&DL=0&NP=255&ID=&MF=oscarsmsg.ini&MQ=&TI=0&DT=&ST=0&IR=0&NR=1&NB=0&SV=0&SS=0&BG=&FG=&QS=&OEX=ISO-8859-1&OEH=utf-8", "http://aaspeechesdb.oscars.org/results.aspx?AC=NEXT_RECORD&XC=/results.aspx&BU=http%3A%2F%2Faaspeechesdb.oscars.org%2F&TN=aatrans&SN=AUTO6488&SE=455&RN=1&MR=0&TR=0&TX=1000&ES=0&CS=0&XP=&RF=WebReportList&EF=&DF=WebReportOscars&RL=0&EL=0&DL=0&NP=255&ID=&MF=oscarsmsg.ini&MQ=&TI=0&DT=&ST=0&IR=0&NR=2&NB=0&SV=0&SS=0&BG=&FG=&QS=&OEX=ISO-8859-1&OEH=utf-8", "http://aaspeechesdb.oscars.org/results.aspx?AC=NEXT_RECORD&XC=/results.aspx&BU=http%3A%2F%2Faaspeechesdb.oscars.org%2F&TN=aatrans&SN=AUTO6488&SE=455&RN=2&MR=0&TR=0&TX=1000&ES=0&CS=0&XP=&RF=WebReportList&EF=&DF=WebReportOscars&RL=0&EL=0&DL=0&NP=255&ID=&MF=oscarsmsg.ini&MQ=&TI=0&DT=&ST=0&IR=0&NR=3&NB=0&SV=0&SS=0&BG=&FG=&QS=&OEX=ISO-8859-1&OEH=utf-8"]

word_list = []

for url in urls:
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html)
    speech = soup.find("p", { "class" : "MInormal" })
    speech_words = speech.text.split(':')[1].split() # take the speech text and split it on the first colon so we can drop the actor's name and just have the speech. then split the speech on spaces to get words.
    word_list.append(speech_words)

# when done appending all the urls you want, we'll need to "flatten" word_list so that it's a single Python array, not an array of arrays.
word_list_flattened = [word for speech in word_list for word in speech]
# next, count the words in word_list_flattened. try the solution here using collections: http://stackoverflow.com/questions/20510768/python-count-frequency-of-words-in-a-list

from collections import Counter
counts = Counter(word_list_flattened)
print(counts)

outfile = open("speeches.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(counts)

 