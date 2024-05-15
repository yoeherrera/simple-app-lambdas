from matplotlib import pylab as plt
import nltk
from collections import Counter
nltk.download('stopwords')

stopwords = set(nltk.corpus.stopwords.words("english"))

def remove_stopwords(text):
    result = " ".join([x for x in text.split(" ") if x not in stopwords and x != " "])
    return result

def plot_word_freqs(text):
    words_freq_dict = Counter(remove_stopwords(text).split())
    return words_freq_dict


if __name__ == "__main__":
    example = """This work can be done without a doubt and can 
                always be done better, for sure!
                Thanks for doing this"""
    print(f"{remove_stopwords(example)=}")
    print(f"{plot_word_freqs(example)=}")