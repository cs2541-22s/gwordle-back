from flask import Flask, render_template, request, session, redirect

app = Flask('app')
app.secret_key = "secret key!"

word = "ultra"
letters = list(word)

MISS = "MISS"    # not in the word
HIT = "HIT"      # in the right spot
CLOSE = "CLOSE"  # in the word, but wrong spot
solved = False

# guesses = a list with words that have been guessed
# results = a list, where each element is another list specifying if the corresponding letter in a guess was a hit, miss, or close

@app.route('/', methods=['GET', 'POST'])
def index():
  # Initialize session variables if needed
  if 'guesses' not in session :
    session['guesses'] = list()
  if 'results' not in session :
    session['results'] = list()

  if request.method == 'POST' :
    # TODO: save the guess to the session
    # check the result for each letter
    # see wordle.py for sample game logic
    pass
  return render_template("index.html")

@app.route('/reset', methods=['GET', 'POST'])
def reset():
  # TODO: reset the game board and the session 
  return 

app.run(host='0.0.0.0', port=8080)
