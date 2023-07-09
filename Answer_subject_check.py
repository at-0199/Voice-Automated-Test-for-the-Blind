import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
stopwords = stopwords.words('english')


def clean_string(text):
    text = ''.join([word for word in text if word not in string.punctuation])
    text = text.lower()
    text = ' '.join([word for word in text.split() if word not in stopwords])

    return text

def subj_ans(ans):
#Magnetic
# ans_1 = 'electricity is the flow of electric charges.' 
#Electric
    ans_2 = 'electricity is the phenomenon associated with stationary or moving electric charges.'


    sentences = [ans,ans_2]



    clean_str = list(map(clean_string,sentences))

    print(clean_str)

    vectorizer = CountVectorizer().fit_transform(clean_str)

    vectors = vectorizer.toarray()

    print(vectors)

    cos_sim = cosine_similarity(vectors)

    if (('not' in ans and 'not' not in ans_2) or ('not' in ans_2 and 'not' not in ans) and cos_sim[0][1] > 0.5):
        print(round((1 - cos_sim[0][1])*5))
        return round((1 - cos_sim[0][1])*5)

    else:
        print(round(cos_sim[0][1]*5))
        return round(cos_sim[0][1]*5)


