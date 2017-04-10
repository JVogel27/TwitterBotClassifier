# Twitter Bot Classifier
This program uses a Random Forrest Classifier to predict whether or not a given twitter account is controlled by a human or a bot. The data has been mined from a collection of real twitter accounts, both human and non-human, then passed to our classifier. The program will accept a twitter username as input and will return whether or not it believes that account is human or bot.

Contributors: Jesse Vogel, Harry Longwell, Zach Migliorini

**System Requirements:**
- python 3.5

**Project Dependencies:**
- numpy+mkl(will need to install via file installation if using Windows)
- scipy
- scikit-learn
- tweepy

**Usage:**
```
  python3 program.py <twitter username>
```
