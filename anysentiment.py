#anysentiment
#Purpose : As sentiment has no language boundaries.,Python library for sentiment analysis is any language.
#Author : Arghadeep Chaudhury
#Date: 31-Aug-2020
#Example : from anysentiment import anysentimentDF,overallsentiment >> anysentimentDF('এক দিকে মস্তিষ্কে রক্তক্ষরণ এবং অস্ত্রোপচার, তার উপর করোনা সংক্রমণ— জোড়া ধাক্কা সামলাতে পারলেন না তিনি। দিল্লির আর্মি হসপিটাল রিসার্চ অ্যান্ড রেফারালেই শেষ নিশ্বাস ত্যাগ করলেন স্বাধীনতা উত্তর সর্বভারতীয় রাজনীতির সফলতম বাঙালি এবং দেশের প্রাক্তন রাষ্ট্রপতি প্রণব মুখোপাধ্যায়।') 
##Will return the complete panda dataframe with translated into english with sentiment analysis for each line.
##git: @deepstartup
from googletrans import Translator
from textblob import TextBlob
import pandas as pd
def anysentimentDF(langval):
    translator = Translator()
    d=translator.translate(langval)
    valtext=d.text
    r=0
    wiki=TextBlob(valtext)
    df=pd.DataFrame(columns=['Line','sentence','Words','SentimentVal','SubjectivityVal','Sentiment','Subjectivity'])
    for vals in wiki.sentences:
        r=r+1
        x_sen=lambda x: 'positive' if x>0 else ('negative' if x<0 else 'neutral')
        x_sub=lambda x: 'subjective' if x>=0.5 else 'objective'
        #dictVals={'Line':r,'Words':len(vals.words),'Sentiment':vals.sentiment.polarity,'Subjectivity':vals.sentiment.subjectivity}
        dictVals={'Line':r,'sentence':str(vals),'Words':len(vals.words),'SentimentVal':vals.sentiment.polarity,'SubjectivityVal':vals.sentiment.subjectivity,'Sentiment':x_sen(vals.sentiment.polarity),'Subjectivity':x_sub(vals.sentiment.subjectivity)}
        df=df.append(dictVals,ignore_index=True)
    return df
def overallsentiment(langval):
    translator = Translator()
    d=translator.translate(langval)
    valtext=d.text
    wiki=TextBlob(valtext)
    return wiki.sentiment