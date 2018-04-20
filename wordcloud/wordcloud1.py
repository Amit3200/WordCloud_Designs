import numpy as np # linear algebra
import pandas as pd 
import matplotlib.pyplot as plt
import collections
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from os import path
d = path.dirname(__file__)
c1 = np.array(Image.open(path.join(d, "ba1.png")))
k=['anger','hate','success','joy','destruction','war','love','challenge','broken','determined']
p=['experience','power','dream','knowledge','form','one','first','time','money','anime','nothingness','ying','yang','god','death','particle','waste','human','sword','life','version','hardwork','talent','codes','progrms','Amit Singh Sansoya']
p1=[10,20,13,14,17,14,12,15,11,12,23,12,23,12,33,12,11,19,15,16,17,18,12,16,14,1]
k.extend(p)
x=[12,15,10,16,13,11,7,18,1230,10]
x.extend(p1)
stopwords = set(STOPWORDS)
stopwords.add("said")
print(len(k))
print(len(x))
d=dict(zip(k,x))
wordcloud = WordCloud(background_color="white",stopwords=stopwords,mask=c1).generate(" ".join(k))
plt.imshow(wordcloud,interpolation='bilinear')
plt.axis('off')
plt.show()
