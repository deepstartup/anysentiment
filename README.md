# anysentiment
Python Lib For doing sentiment Analysis in Any Language
# anysentiment Package

This is a  package for sentiment analysis in any language . You can use for overall sentiment for a entire paragraph or a sentence in anylanguage.
Languages as per : https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
Example :
>>from anysentiment import anysentimentDF,overallsentiment
>>anysentimentDF('এক দিকে মস্তিষ্কে রক্তক্ষরণ এবং অস্ত্রোপচার, তার উপর করোনা সংক্রমণ— জোড়া ধাক্কা সামলাতে পারলেন না তিনি। দিল্লির আর্মি হসপিটাল রিসার্চ অ্যান্ড রেফারালেই শেষ নিশ্বাস ত্যাগ করলেন স্বাধীনতা উত্তর সর্বভারতীয় রাজনীতির সফলতম বাঙালি এবং দেশের প্রাক্তন রাষ্ট্রপতি প্রণব মুখোপাধ্যায়।') 
output :
 Line                                           sentence Words  SentimentVal  \
0    1  On the one hand, bleeding in the brain and sur...    21        0.0000   
1    2  Pranab Mukherjee, the most successful Bengali ...    28        0.3125   

   SubjectivityVal Sentiment Subjectivity  
0         0.000000   neutral    objective  
1         0.379167  positive    objective  

[Github-flavored Markdown](https://github.com/deepstartup/anysentiment/)
