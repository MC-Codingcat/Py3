#!/usr/bin/env python
# coding: utf-8

# In[ ]:


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
# Get rid of punctuation
def strip_punctuation(str):
    for char in str:
        if char in punctuation_chars:
            str = str.replace(char, '')
    return str

# Count positive words
def get_pos(str):
    str_list = strip_punctuation(str).strip().lower().split()
    count = 0
    for word in str_list:
        if word in positive_words:
            count += 1
    return count

# Count negative words
def get_neg(str):
    str_list = strip_punctuation(str).strip().lower().split()
    count = 0
    for word in str_list:
        if word in negative_words:
            count += 1
    return count

# Read data
with open('project_twitter_data.csv') as prj_d:
    lines = prj_d.readlines()

# Process calculation & write to CSV
with open('resulting_data.csv', 'w') as prj_w:
    prj_w.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    prj_w.write('\n')
    for line in lines[1:]:
        d_lst = line.strip().split(',')
        net = get_pos(d_lst[0]) - get_neg(d_lst[0])
        prj_w.write(f'{d_lst[1]}, {d_lst[2]}, {get_pos(d_lst[0])}, {get_neg(d_lst[0])}, {net}\n')
        
        

