import pandas as pd
import numpy as np

df = pd.read_csv('data/word2.csv')

guess_cnt = 0
found = [False, False, False, False, False]

while True:
    guess_cnt = guess_cnt + 1
    
    shifter = 0
    res = 'x'
    while res == 'x':
        guess = df.iloc[shifter]['0'] + df.iloc[shifter]['1'] + df.iloc[shifter]['2'] + df.iloc[shifter]['3'] + df.iloc[shifter]['4']
        shifter = shifter + 1
        
        print('guess', guess_cnt, ':', guess)
        res = input('enter response: ')
    
    if res == 'done':
        break
    
    for i in range(5):
        if res[i] == 'g':
            df = df[df[str(i)] == guess[i]]
            found[i] = True
    
    for i in range(5):
        if res[i] == 'y':
            df = df[df[str(i)] != guess[i]]
            df = df[(df['0'] == guess[i]) | (df['1'] == guess[i]) | (df['2'] == guess[i]) | (df['3'] == guess[i]) | (df['4'] == guess[i])]
    
    for i in range(5):
        if res[i] == 'b':
            if (not found[0]):
                df = df[df['0'] != guess[i]]
            if (not found[1]):
                df = df[df['1'] != guess[i]]
            if (not found[2]):
                df = df[df['2'] != guess[i]]
            if (not found[3]):
                df = df[df['3'] != guess[i]]
            if (not found[4]):
                df = df[df['4'] != guess[i]]

    
    df = df.reset_index(drop = True)