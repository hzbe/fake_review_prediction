from sklearn.model_selection import train_test_split
from sklearn.utils import resample

import pandas as pd


def balanced(df):
    '''
    Performs a majority undersampling and creates a 50:50 majority to minority split
    in the training data. Returns a balanced train/test split for classification models and NLP.
    '''
    df.reset_index(drop=True, inplace=True)
    features = ['review_text','rating','filtered','review_length','biz_rvws','user_rvws', 'avg_rating', 'past_filt', 'percent_filt', 'avg_rev_len', 'word_count', 'avg_word', 'stopwords', 'numbers', 'upper', 'Friday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
    #features = ['review_text','rating','filtered','review_length','biz_rvws','user_rvws', 'avg_rating', 'past_filt', 'percent_filt', 'avg_rev_len', 'word_count', 'avg_word', 'stopwords', 'numbers', 'upper', 'Friday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
    df = df[features]
    X_train, X_test = train_test_split(df, test_size=0.15, random_state=0)
    classN = X_train[X_train.filtered == 0]
    classY = X_train[X_train.filtered == 1]
    classY_count = len(classY)
    sub_classN = resample(classN, n_samples=classY_count)
    frames = [sub_classN,classY]
    X_train = pd.concat(frames)
    X_train = resample(X_train, n_samples=classY_count*2)
    y_train = X_train.pop('filtered')
    X_train_tfidf = X_train.pop('review_text')
    y_test = X_test.pop('filtered')
    X_test_tfidf = X_test.pop('review_text')
    return X_train, X_train_tfidf, X_test, X_test_tfidf, y_train, y_test

def unbalanced():
    '''
    Creates a normal unbalanced traintest split for both classification models and NLP.
    '''
    df = pd.read_csv("Data/train_set.csv" , sep="\t")
    df.reset_index(drop=True, inplace=True)
    features = ['review_text','rating','filtered','review_length','biz_rvws','user_rvws', 'avg_rating', 'past_filt', 'percent_filt', 'avg_rev_len', 'word_count', 'avg_word', 'stopwords', 'numbers', 'upper', 'Friday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
    df = df[features]
    X_train, X_test = train_test_split(df, test_size=0.15, random_state=0)
    y_train = X_train.pop('filtered')
    X_train_tfidf = X_train.pop('review_text')
    y_test = X_test.pop('filtered')
    X_test_tfidf = X_test.pop('review_text')
    return X_train, X_train_tfidf, X_test, X_test_tfidf, y_train, y_test


#for holdout
def holdout():
    '''
    Readies the final holdout set for classification model.
    '''
    df = pd.read_csv("Data/holdout.csv" , sep="\t")
    df.reset_index(drop=True, inplace=True)
    features = ['review_text','rating','filtered','review_length','biz_rvws','user_rvws', 'avg_rating', 'past_filt', 'percent_filt', 'avg_rev_len', 'word_count', 'avg_word', 'stopwords', 'numbers', 'upper', 'Friday', 'Saturday', 'Sunday', 'Thursday', 'Tuesday', 'Wednesday']
    X_final = df[features]
    y_final= X_final.pop('filtered')
    X_final_tfidf = X_final.pop('review_text')
    return X_final, X_final_tfidf, y_final
