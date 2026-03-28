import pandas as pd
from analysis import most_word_used as words
datafram=pd.DataFrame(words,columns=["word","count"])
datafram.to_csv("Speech_word_count.csv",index=False)