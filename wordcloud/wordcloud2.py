import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random
from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)


mask = np.array(Image.open(path.join(d, "do.png")))
k=['anger','hate','success','joy','destruction','war','love','challenge','broken','determined']
p=['experience','power','dream','knowledge','form','one','first','time','money','anime','nothingness','ying','yang','god','death','particle','waste','human','sword','life','version','hardwork','talent','codes','progrms','Amit Singh Sansoya']
p1=[10,20,13,14,17,14,12,15,11,12,23,12,23,12,33,12,11,19,15,16,17,18,12,16,14,1]
k.extend(p)
x=[12,15,10,16,13,11,7,18,1230,10]
x.extend(p1)
stopwords = set(STOPWORDS)
stopwords.add("kill")
wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10,
               random_state=1).generate(" ".join(k))
default_colors = wc.to_array()
plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")
wc.to_file("apple.png")
plt.axis("off")
plt.figure()
plt.title("Default colors")
plt.imshow(default_colors, interpolation="bilinear")
plt.axis("off")
plt.show()
