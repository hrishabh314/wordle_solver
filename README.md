# wordle solver
This is a Python program to solve the online word puzzle, wordle : https://www.powerlanguage.co.uk/wordle/

# How to set up: (Tested on Anaconda Jupyter Notebook)
-> Download zip and extract.
-> Launch the notebook nb2.ipynb using Jupyter Notebook etc. method may vary.

# How to use:
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
