from scrap import final_version_li as text
from stopWords import stopwords as ignore
dic={}
for i in text:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
cleaned_dic={}
for word,count in dic.items():
    if word.lower() not in ignore:
        cleaned_dic[word]=count
most_word_used=sorted(cleaned_dic.items(),key=lambda x:x[1],reverse=True)
first_word,used=most_word_used[0]
print(f"the President of america used word {first_word} {used} times!")
