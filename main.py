from flask import Flask, request, render_template
from random import randint

listofWords = ["QUAKE", "HACKY", "QUASH", "CHEWY", "PRIZE"]
def chooseWord(WordList):
    wordListLength = len(WordList)
    
    chosen_word_index = randint(0, wordListLength-1)
    chosen_word = WordList[chosen_word_index]

    return chosen_word
turn = 1
input_turn1 = ""
input_turn2 = ""
input_turn3 = ""
input_turn4 = ""
input_turn5 = ""
input_turn6 = ""

color1 = ""
color2 = ""
color3 = ""
color4 = ""
color5 = ""
color6 = ""
color7 = ""
color8 = ""
color9 = ""
color10 = ""
color11 = ""
color12 = ""
color13 = ""
color14 = ""
color15 = ""
color16 = ""
color17 = ""
color18 = ""
color19 = ""
color20 = ""
color21 = ""
color22 = ""
color23 = ""
color24 = ""
color25 = ""
color26 = ""
color27 = ""
color28 = ""
color29 = ""
color30 = ""

return_command = "'"


goal_word = chooseWord(listofWords)
goal_word_data = ""
print(goal_word)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/win', methods=['GET', 'POST'])
def win_page():
    return render_template('win.html')


@app.route('/wordle', methods=['GET', 'POST'])
def wordle():
    global goal_word
    global turn

    global input_turn1
    global input_turn2
    global input_turn3
    global input_turn4
    global input_turn5
    global input_turn6

    global return_command

    global color1 
    global color2 
    global color3 
    global color4 
    global color5 
    global color6 
    global color7 
    global color8
    global color9
    global color10
    global color11 
    global color12 
    global color13 
    global color14 
    global color15 
    global color16 
    global color17 
    global color18 
    global color19 
    global color20 
    global color21 
    global color22 
    global color23 
    global color24 
    global color25 
    global color26 
    global color27 
    global color28 
    global color29 
    global color30

    global goal_word_data

    if request.method == 'POST':
        input_gotten = request.form.get('inputGotten')
        input_gotten_upper = input_gotten.upper()
        if input_gotten_upper.isalpha():
            if turn == 1:
                input_turn1 = input_gotten_upper
                if len(input_turn1) < 5:
                    return render_template('wordle.html', input = "Please enter at least 5 characters")
                else:
                    for i in range(5):
                        if input_turn1[i] == goal_word[i]:
                            if i == 0:
                                color1 = "correct"
                            elif i == 1:
                                color2 = "correct"
                            elif i == 2:
                                color3 = "correct"
                            elif i == 3:
                                color4 = "correct"
                            elif i == 4:
                                color5 = "correct"
                        elif input_turn1[i] in goal_word:
                            if i == 0:
                                color1 = "present"
                            elif i == 1:
                                color2 = "present"
                            elif i == 2:
                                color3 = "present"
                            elif i == 3:
                                color4 = "present"
                            elif i == 4:
                                color5 = "present"
                        else:
                            if i == 0:
                                color1 = "absent"
                            elif i == 1:
                                color2 = "absent"
                            elif i == 2:
                                color3 = "absent"
                            elif i == 3:
                                color4 = "absent"
                            elif i == 4:
                                color5 = "absent"

                if color1 == "correct" and color2 == "correct" and color3 == "correct" and color4 == "correct" and color5 == "correct":
                    turn = 1
                    color1 = ""
                    color2 = ""
                    color3 = ""
                    color4 = ""
                    color5 = ""
                    goal_word_data = goal_word
                    goal_word = chooseWord(listofWords)
                    print(goal_word)
                    return render_template("win.html")
                
                turn = 2
                return render_template('wordle.html', input=input_gotten_upper, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5)

            elif turn == 2:
                input_turn2 = input_gotten_upper
                if len(input_turn2) < 5:
                    return render_template('wordle.html', input = "Please enter at least 5 characters", letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5)
                else:
                    for i in range(5):
                        if input_turn2[i] == goal_word[i]:
                            if i == 0:
                                color6 = "correct"
                            elif i == 1:
                                color7 = "correct"
                            elif i == 2:
                                color8 = "correct"
                            elif i == 3:
                                color9 = "correct"
                            elif i == 4:
                                color10 = "correct"
                        elif input_turn2[i] in goal_word:
                            if i == 0:
                                color6 = "present"
                            elif i == 1:
                                color7 = "present"
                            elif i == 2:
                                color8 = "present"
                            elif i == 3:
                                color9 = "present"
                            elif i == 4:
                                color10 = "present"
                        else:
                            if i == 0:
                                color6 = "absent"
                            elif i == 1:
                                color7 = "absent"
                            elif i == 2:
                                color8 = "absent"
                            elif i == 3:
                                color9 = "absent"
                            elif i == 4:
                                color10 = "absent"

                if color6 == "correct" and color7 == "correct" and color8 == "correct" and color9 == "correct" and color10 == "correct":
                    turn = 1
                    color1 = ""
                    color2 = ""
                    color3 = ""
                    color4 = ""
                    color5 = ""
                    color6 = ""
                    color7 = ""
                    color8 = ""
                    color9 = ""
                    color10 = ""
                    goal_word_data = goal_word
                    goal_word = chooseWord(listofWords)
                    print(goal_word)
                    return render_template("win.html")
                
                turn = 3
                return render_template(
                    'wordle.html', input=input_gotten_upper, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10       
                )
            
            elif turn == 3:
                input_turn3 = input_gotten_upper
                if len(input_turn3) < 5:
                    return render_template(
                    'wordle.html', input = "Please enter at least 5 characters", letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10       
                )
                else:
                    for i in range(5):
                        if input_turn3[i] == goal_word[i]:
                            if i == 0:
                                color11 = "correct"
                            elif i == 1:
                                color12 = "correct"
                            elif i == 2:
                                color13 = "correct"
                            elif i == 3:
                                color14 = "correct"
                            elif i == 4:
                                color15 = "correct"
                        elif input_turn3[i] in goal_word:
                            if i == 0:
                                color11 = "present"
                            elif i == 1:
                                color12 = "present"
                            elif i == 2:
                                color13 = "present"
                            elif i == 3:
                                color14 = "present"
                            elif i == 4:
                                color15 = "present"
                        else:
                            if i == 0:
                                color11 = "absent"
                            elif i == 1:
                                color12 = "absent"
                            elif i == 2:
                                color13 = "absent"
                            elif i == 3:
                                color14 = "absent"
                            elif i == 4:
                                color15 = "absent"

                if color11 == "correct" and color12 == "correct" and color13 == "correct" and color14 == "correct" and color15 == "correct":
                    turn = 1
                    color1 = ""
                    color2 = ""
                    color3 = ""
                    color4 = ""
                    color5 = ""
                    color6 = ""
                    color7 = ""
                    color8 = ""
                    color9 = ""
                    color10 = ""
                    color11 = ""
                    color12 = ""
                    color13 = ""
                    color14 = ""
                    color15 = ""
                    goal_word_data = goal_word
                    goal_word = chooseWord(listofWords)
                    print(goal_word)
                    return render_template("win.html")
                
                turn = 4
                return render_template(
                    'wordle.html', input=input_gotten_upper, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10,
                                                             letter11=input_turn3[0], letter12=input_turn3[1], letter13=input_turn3[2], letter14=input_turn3[3], letter15=input_turn3[4], color11=color11, color12=color12, color13=color13, color14=color14, color15=color15,
                )
            
            elif turn == 4:
                input_turn4 = input_gotten_upper
                if len(input_turn4) < 5:
                    return render_template(
                    'wordle.html', input=input_gotten_upper, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10,
                                                             letter11=input_turn3[0], letter12=input_turn3[1], letter13=input_turn3[2], letter14=input_turn3[3], letter15=input_turn3[4], color11=color11, color12=color12, color13=color13, color14=color14, color15=color15,
                )
                else:
                    for i in range(5):
                        if input_turn4[i] == goal_word[i]:
                            if i == 0:
                                color16 = "correct"
                            elif i == 1:
                                color17 = "correct"
                            elif i == 2:
                                color18 = "correct"
                            elif i == 3:
                                color19 = "correct"
                            elif i == 4:
                                color20 = "correct"
                        elif input_turn4[i] in goal_word:
                            if i == 0:
                                color16 = "present"
                            elif i == 1:
                                color17 = "present"
                            elif i == 2:
                                color18 = "present"
                            elif i == 3:
                                color19 = "present"
                            elif i == 4:
                                color20 = "present"
                        else:
                            if i == 0:
                                color16 = "absent"
                            elif i == 1:
                                color17 = "absent"
                            elif i == 2:
                                color18 = "absent"
                            elif i == 3:
                                color19 = "absent"
                            elif i == 4:
                                color20 = "absent"

                if color16 == "correct" and color17 == "correct" and color18 == "correct" and color19 == "correct" and color20 == "correct":
                    turn = 1
                    color1 = ""
                    color2 = ""
                    color3 = ""
                    color4 = ""
                    color5 = ""
                    color6 = ""
                    color7 = ""
                    color8 = ""
                    color9 = ""
                    color10 = ""
                    color11 = ""
                    color12 = ""
                    color13 = ""
                    color14 = ""
                    color15 = ""
                    color16 = ""
                    color17 = ""
                    color18 = ""
                    color19 = ""
                    color20 = ""
                    goal_word_data = goal_word
                    goal_word = chooseWord(listofWords)
                    print(goal_word)
                    return render_template("win.html")
                
                turn = 5
                return render_template(
                    'wordle.html', input=input_gotten_upper, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10,
                                                             letter11=input_turn3[0], letter12=input_turn3[1], letter13=input_turn3[2], letter14=input_turn3[3], letter15=input_turn3[4], color11=color11, color12=color12, color13=color13, color14=color14, color15=color15,
                                                             letter16=input_turn4[0], letter17=input_turn4[1], letter18=input_turn4[2], letter19=input_turn4[3], letter20=input_turn4[4], color16=color16, color17=color17, color18=color18, color19=color19, color20=color20,
                )
            elif turn == 5:
                input_turn5 = input_gotten_upper
                if len(input_turn5) < 5:
                    return render_template(
                    'wordle.html', input=input_gotten_upper, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10,
                                                             letter11=input_turn3[0], letter12=input_turn3[1], letter13=input_turn3[2], letter14=input_turn3[3], letter15=input_turn3[4], color11=color11, color12=color12, color13=color13, color14=color14, color15=color15,
                                                             letter16=input_turn4[0], letter17=input_turn4[1], letter18=input_turn4[2], letter19=input_turn4[3], letter20=input_turn4[4], color16=color16, color17=color17, color18=color18, color19=color19, color20=color20,
                )
                else:
                    for i in range(5):
                        if input_turn5[i] == goal_word[i]:
                            if i == 0:
                                color21 = "correct"
                            elif i == 1:
                                color22 = "correct"
                            elif i == 2:
                                color23 = "correct"
                            elif i == 3:
                                color24 = "correct"
                            elif i == 4:
                                color25 = "correct"
                        elif input_turn5[i] in goal_word:
                            if i == 0:
                                color21 = "present"
                            elif i == 1:
                                color22 = "present"
                            elif i == 2:
                                color23 = "present"
                            elif i == 3:
                                color24 = "present"
                            elif i == 4:
                                color25 = "present"
                        else:
                            if i == 0:
                                color21 = "absent"
                            elif i == 1:
                                color22 = "absent"
                            elif i == 2:
                                color23 = "absent"
                            elif i == 3:
                                color24 = "absent"
                            elif i == 4:
                                color25 = "absent"

                if color21 == "correct" and color22 == "correct" and color23 == "correct" and color24 == "correct" and color25 == "correct":
                    turn = 1
                    color1 = ""
                    color2 = ""
                    color3 = ""
                    color4 = ""
                    color5 = ""
                    color6 = ""
                    color7 = ""
                    color8 = ""
                    color9 = ""
                    color10 = ""
                    color11 = ""
                    color12 = ""
                    color13 = ""
                    color14 = ""
                    color15 = ""
                    color16 = ""
                    color17 = ""
                    color18 = ""
                    color19 = ""
                    color20 = ""
                    color21 = ""
                    color22 = ""
                    color23 = ""
                    color24 = ""
                    color25 = ""
                    goal_word_data = goal_word
                    goal_word = chooseWord(listofWords)
                    print(goal_word)
                    return render_template("win.html")
                
                turn = 6
                return render_template(
                    'wordle.html', input=input_gotten_upper, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10,
                                                             letter11=input_turn3[0], letter12=input_turn3[1], letter13=input_turn3[2], letter14=input_turn3[3], letter15=input_turn3[4], color11=color11, color12=color12, color13=color13, color14=color14, color15=color15,
                                                             letter16=input_turn4[0], letter17=input_turn4[1], letter18=input_turn4[2], letter19=input_turn4[3], letter20=input_turn4[4], color16=color16, color17=color17, color18=color18, color19=color19, color20=color20,
                                                             letter21=input_turn5[0], letter22=input_turn5[1], letter23=input_turn5[2], letter24=input_turn5[3], letter25=input_turn5[4], color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,
                )
            elif turn == 6:
                input_turn6 = input_gotten_upper
                if len(input_turn6) < 5:
                    return render_template(
                    'wordle.html', input=input_gotten_upper, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10,
                                                             letter11=input_turn3[0], letter12=input_turn3[1], letter13=input_turn3[2], letter14=input_turn3[3], letter15=input_turn3[4], color11=color11, color12=color12, color13=color13, color14=color14, color15=color15,
                                                             letter16=input_turn4[0], letter17=input_turn4[1], letter18=input_turn4[2], letter19=input_turn4[3], letter20=input_turn4[4], color16=color16, color17=color17, color18=color18, color19=color19, color20=color20,
                                                             letter21=input_turn5[0], letter22=input_turn5[1], letter23=input_turn5[2], letter24=input_turn5[3], letter25=input_turn5[4], color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,
                )
                else:
                    for i in range(5):
                        if input_turn6[i] == goal_word[i]:
                            if i == 0:
                                color26 = "correct"
                            elif i == 1:
                                color27 = "correct"
                            elif i == 2:
                                color28 = "correct"
                            elif i == 3:
                                color29 = "correct"
                            elif i == 4:
                                color30 = "correct"
                        elif input_turn6[i] in goal_word:
                            if i == 0:
                                color26 = "present"
                            elif i == 1:
                                color27 = "present"
                            elif i == 2:
                                color28 = "present"
                            elif i == 3:
                                color29 = "present"
                            elif i == 4:
                                color30 = "present"
                        else:
                            if i == 0:
                                color26 = "absent"
                            elif i == 1:
                                color27 = "absent"
                            elif i == 2:
                                color28 = "absent"
                            elif i == 3:
                                color29 = "absent"
                            elif i == 4:
                                color30 = "absent"

                if color26 == "correct" and color27 == "correct" and color28 == "correct" and color29 == "correct" and color30 == "correct":
                    turn = 1
                    color1 = ""
                    color2 = ""
                    color3 = ""
                    color4 = ""
                    color5 = ""
                    color6 = ""
                    color7 = ""
                    color8 = ""
                    color9 = ""
                    color10 = ""
                    color11 = ""
                    color12 = ""
                    color13 = ""
                    color14 = ""
                    color15 = ""
                    color16 = ""
                    color17 = ""
                    color18 = ""
                    color19 = ""
                    color20 = ""
                    color21 = ""
                    color22 = ""
                    color23 = ""
                    color24 = ""
                    color25 = ""
                    color26 = ""
                    color27 = ""
                    color28 = ""
                    color29 = ""
                    color30 = ""
                    goal_word_data = goal_word
                    goal_word = chooseWord(listofWords)
                    print(goal_word)
                    return render_template("win.html")
                
                turn = "end"
                return render_template(
                    'wordle.html', input="You lose (type 'rtn' to exit)", letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10,
                                                             letter11=input_turn3[0], letter12=input_turn3[1], letter13=input_turn3[2], letter14=input_turn3[3], letter15=input_turn3[4], color11=color11, color12=color12, color13=color13, color14=color14, color15=color15,
                                                             letter16=input_turn4[0], letter17=input_turn4[1], letter18=input_turn4[2], letter19=input_turn4[3], letter20=input_turn4[4], color16=color16, color17=color17, color18=color18, color19=color19, color20=color20,
                                                             letter21=input_turn5[0], letter22=input_turn5[1], letter23=input_turn5[2], letter24=input_turn5[3], letter25=input_turn5[4], color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,
                                                             letter26=input_turn6[0], letter27=input_turn6[1], letter28=input_turn6[2], letter29=input_turn6[3], letter30=input_turn6[4], color26=color26, color27=color27, color28=color28, color29=color29, color30=color30,
                )

            elif turn == "end":
                if input_gotten == "rtn":
                    return render_template("index.html")
                else:
                    return render_template(
                        'wordle.html', input="You lose (type 'rtn' to exit)", letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                                letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10,
                                                                letter11=input_turn3[0], letter12=input_turn3[1], letter13=input_turn3[2], letter14=input_turn3[3], letter15=input_turn3[4], color11=color11, color12=color12, color13=color13, color14=color14, color15=color15,
                                                                letter16=input_turn4[0], letter17=input_turn4[1], letter18=input_turn4[2], letter19=input_turn4[3], letter20=input_turn4[4], color16=color16, color17=color17, color18=color18, color19=color19, color20=color20,
                                                                letter21=input_turn5[0], letter22=input_turn5[1], letter23=input_turn5[2], letter24=input_turn5[3], letter25=input_turn5[4], color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,
                                                                letter26=input_turn6[0], letter27=input_turn6[1], letter28=input_turn6[2], letter29=input_turn6[3], letter30=input_turn6[4], color26=color26, color27=color27, color28=color28, color29=color29, color30=color30,
                    )
                       

        else:
            message = "Please enter only alphabet characters (with no spaces)"
            if turn == 1:
                return render_template('wordle.html', input=message)
            elif turn == 2:
                return render_template('wordle.html', input = message, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5)
            elif turn == 3:
               return render_template(
                    'wordle.html', input = message, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10       
                )
            elif turn == 4:
                return render_template(
                    'wordle.html', input=message, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10,
                                                             letter11=input_turn3[0], letter12=input_turn3[1], letter13=input_turn3[2], letter14=input_turn3[3], letter15=input_turn3[4], color11=color11, color12=color12, color13=color13, color14=color14, color15=color15,
                )
            elif turn == 5:
                return render_template(
                    'wordle.html', input=message, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10,
                                                             letter11=input_turn3[0], letter12=input_turn3[1], letter13=input_turn3[2], letter14=input_turn3[3], letter15=input_turn3[4], color11=color11, color12=color12, color13=color13, color14=color14, color15=color15,
                                                             letter16=input_turn4[0], letter17=input_turn4[1], letter18=input_turn4[2], letter19=input_turn4[3], letter20=input_turn4[4], color16=color16, color17=color17, color18=color18, color19=color19, color20=color20,
                )
            elif turn == 6:
                return render_template(
                    'wordle.html', input=message, letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10,
                                                             letter11=input_turn3[0], letter12=input_turn3[1], letter13=input_turn3[2], letter14=input_turn3[3], letter15=input_turn3[4], color11=color11, color12=color12, color13=color13, color14=color14, color15=color15,
                                                             letter16=input_turn4[0], letter17=input_turn4[1], letter18=input_turn4[2], letter19=input_turn4[3], letter20=input_turn4[4], color16=color16, color17=color17, color18=color18, color19=color19, color20=color20,
                                                             letter21=input_turn5[0], letter22=input_turn5[1], letter23=input_turn5[2], letter24=input_turn5[3], letter25=input_turn5[4], color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,
                )
            
            elif turn == "end":
                return render_template(
                    'wordle.html', input="You lose (type 'rtn' to exit)", letter1=input_turn1[0], letter2=input_turn1[1], letter3=input_turn1[2], letter4=input_turn1[3], letter5=input_turn1[4], color1=color1, color2=color2, color3=color3, color4=color4, color5=color5,
                                                             letter6=input_turn2[0], letter7=input_turn2[1], letter8=input_turn2[2], letter9=input_turn2[3], letter10=input_turn2[4], color6=color6, color7=color7, color8=color8, color9=color9, color10=color10,
                                                             letter11=input_turn3[0], letter12=input_turn3[1], letter13=input_turn3[2], letter14=input_turn3[3], letter15=input_turn3[4], color11=color11, color12=color12, color13=color13, color14=color14, color15=color15,
                                                             letter16=input_turn4[0], letter17=input_turn4[1], letter18=input_turn4[2], letter19=input_turn4[3], letter20=input_turn4[4], color16=color16, color17=color17, color18=color18, color19=color19, color20=color20,
                                                             letter21=input_turn5[0], letter22=input_turn5[1], letter23=input_turn5[2], letter24=input_turn5[3], letter25=input_turn5[4], color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,
                                                             letter26=input_turn6[0], letter27=input_turn6[1], letter28=input_turn6[2], letter29=input_turn6[3], letter30=input_turn6[4], color26=color26, color27=color27, color28=color28, color29=color29, color30=color30,
                )

    return render_template('wordle.html', input=None)

if __name__ == '__main__':
    app.run()