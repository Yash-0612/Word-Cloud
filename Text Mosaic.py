import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS

a = str(input("Enter the word of which you want to create word cloud : "))
title = wikipedia.search(a)[0]
page = wikipedia.page(title)
text = page.content
print(text)

mask = np.array(Image.open("Thumbs_up.png"))
unwanted_words = set(STOPWORDS)
word = WordCloud(background_color="black", max_words=500, mask=mask, stopwords=unwanted_words)
word.generate(text)
word.to_file("Mosaic.png")
