# wordle solver
This is a Python program to solve the online word puzzle, wordle : https://www.powerlanguage.co.uk/wordle/

nb2.ipynb is the jupyter notebook for the program.
wordle_solver.py is the same program as a python script.
data contains word2.csv which is a dataset of all 5-letter words.

# How to set up: (Tested on Anaconda Jupyter Notebook)
-> Download zip and extract.
-> Launch the notebook nb2.ipynb using Jupyter Notebook etc. method may vary.

# How to use:
![e12a4a57-53e7-49a7-81ad-1d0370caf12a](https://user-images.githubusercontent.com/74061616/148730510-6a0aa419-b771-46df-99b6-7e0e3f2d64c6.jpg)

-> Outputs:
  -> guess <guess_number> <guess_string>
      eg. guess 3 lover
      Enter these guess outputs as wordle guesses

-> Inputs:
  -> <wordle_info_string>
      This 5-letter string consists of only the letters 'g' for green, 'b' for black/grey and 'y' 
      for yellow outputs from wordle.
      
      eg. Say your guess is the string 'lover', and say 'l', 'o' exactly matches (green), 'v' is
          present somewhere but not at 3rd position (yellow) and 'e' & 'r' are nowhere (black)
          then enter the string 'ggybb' into the program.
   
   -> 'x'
      Enter this if wordle says the guessed string is not in its word list.
   
   -> 'done'
      Enter this to terminate program after winnning. :)
