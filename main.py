from flask import Flask, request, render_template
from random import choice

wordList = ["QUAKE", "HACKY", "QUASH", "CHEWY", "PRIZE"]
selectedWord = choice(wordList).upper()
print(selectedWord)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/win', methods=['GET', 'POST'])
def win_page():
    return render_template('win.html')


@app.route('/wordle_page', methods=['GET', 'POST'])
def wordle_page():

    guess = [""] * len(selectedWord)
    if request.method == "POST":
        guess = [request.form.get(f"letter{i+1}", "").upper()
                 for i in range(len(selectedWord))]

        guessWord = "".join(guess)

        if len(guessWord) != len(selectedWord):
            return render_template('wordle_page.html', error="Not enough letters", word_length = len(guessWord), guess = guess)
        
        feedback = checkGuess(guessWord, selectedWord)
        if guessWord == selectedWord:
            return render_template("wordle_page.html", success = True, feedback = feedback, word_length = len(selectedWord), guess = guess)
        else:
            return render_template("wordle_page.html", feedback = feedback, word_length = len(selectedWord), guess = guess)

    return render_template('wordle_page.html', word_length = len(selectedWord), guess = [""])

def checkGuess(guess_word, selected_word):
    feedback = []
    for i in range(len(guess_word)):
        if guess_word[i] == selected_word[i]:
            feedback.append("Correct")
        elif guess_word[i] in selected_word:
            feedback.append("Wrong position")
        else:
            feedback.append("Incorrect")


    return feedback
if __name__ == '__main__':
    app.run()