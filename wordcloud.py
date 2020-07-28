# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 20:52:35 2020

@author: NIKHIL YADAV
"""


#pip install wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt
 
# Create a list of word
text = ("Ayushi Aditi Ayushi Askhsay Nikhil nikhil nikhil nikhil nikhil Alex Ankita Ankita Shweta Shewta")
# Create the wordcloud object
wordcloud = WordCloud(width=480, height=480, margin=0).generate(text)
# Display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
