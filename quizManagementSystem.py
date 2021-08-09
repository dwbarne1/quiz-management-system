import csv
from tkinter import *
from tkinter import ttk
import random


class Question:
    """Creates a new question object with nine required parameters"""
    def __init__(self, text, point_value, answer1, answer2,
                 answer3, answer4, correct_answer, correct_feedback, incorrect_feedback):
        self.__text = text
        self.__point_value = point_value
        self.__answer1 = answer1
        self.__answer2 = answer2
        self.__answer3 = answer3
        self.__answer4 = answer4
        self.__correct_answer = correct_answer
        self.__correct_feedback = correct_feedback
        self.__incorrect_feedback = incorrect_feedback

    # Properties and setters for all instance variables
    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, new_text):
        self.__text = new_text

    @property
    def point_value(self):
        return self.__point_value

    @point_value.setter
    def point_value(self, new_point_value):
        self.__point_value = new_point_value

    @property
    def answer1(self):
        return self.__answer1

    @answer1.setter
    def answer1(self, new_answer1):
        self.__answer1 = new_answer1

    @property
    def answer2(self):
        return self.__answer2

    @answer2.setter
    def answer2(self, new_answer2):
        self.__answer2 = new_answer2

    @property
    def answer3(self):
        return self.__answer3

    @answer3.setter
    def answer3(self, new_answer3):
        self.__answer3 = new_answer3

    @property
    def answer4(self):
        return self.__answer4

    @answer4.setter
    def answer4(self, new_answer4):
        self.__answer4 = new_answer4

    @property
    def correct_answer(self):
        return self.__correct_answer

    @correct_answer.setter
    def correct_answer(self, new_correct_answer):
        self.correct_answer = new_correct_answer

    @property
    def correct_feedback(self):
        return self.__correct_feedback

    @correct_feedback.setter
    def correct_feedback(self, new_correct_feedback):
        self.correct_feedback = new_correct_feedback

    @property
    def incorrect_feedback(self):
        return self.__incorrect_feedback

    @incorrect_feedback.setter
    def incorrect_feedback(self, new_incorrect_feedback):
        self.incorrect_feedback = new_incorrect_feedback


# Loading the .csv file with the questions
with open('questions.csv', 'r') as file:
    readData = csv.reader(file)
    questions = list(readData)
    questions_with_first_row = questions[0:]
    questions = questions[1:]

# Creating lists to use for the storage of .csv question objects, as well as newly created questions later on
allQuestionObjects = list()
questionNumbers = list()
questionsDict = dict()
questionsToBeSaved = list()

# Reading questions from .csv file
try:
    for i in range(len(questions)):
        temp = Question(questions[i][0], questions[i][1], questions[i][2], questions[i][3], questions[i][4],
                        questions[i][5], questions[i][6], questions[i][7], questions[i][8])
        questionNumbers.append(f'Question {i+1}')
        allQuestionObjects.append(temp)
        questionsDict[f'Question {i+1}'] = allQuestionObjects[i]
except IndexError:
    pass

# Creating a window object
win = Tk()
win.geometry('1000x700')
win.title('Quiz Management System')
win.config(bg='sky blue')

# Declaring StringVar() values to be used with Entry objects
question_text = StringVar()
point_value = StringVar()
answer1 = StringVar()
answer2 = StringVar()
answer3 = StringVar()
answer4 = StringVar()
correct_answer = StringVar()
correct_feedback = StringVar()
incorrect_feedback = StringVar()

# Declaring two other variables to be used with functions
combobox_selection_number = 0
search_text = StringVar()


def question_selected(event):
    """Event handler for the questions_combobox which shows the different attributes
    of each selected question in said Combobox within a Frame object"""
    global questions_combobox, display_question_box, combobox_selection_number

    # Destroy any Frames used by other functions before displaying new Frame
    try:
        display_question_box.destroy()
    except NameError:
        pass

    display_question_box = Frame(big_box, bg='orange', width=400, height=200, borderwidth=5, relief=RAISED)
    display_question_box.grid(column=0, columnspan=2)
    display_question_box.pack_propagate(0)

    # Display attributes of each question using labels
    Label(display_question_box, text='Question Text:', bg='orange').grid(row=1, column=1, sticky=W)
    Label(display_question_box, text='Points:', bg='orange').grid(row=1, column=3, sticky=W)
    Label(display_question_box, text='Choice 1:', bg='orange').grid(row=2, column=1, sticky=W)
    Label(display_question_box, text='Choice 2:', bg='orange').grid(row=3, column=1, sticky=W)
    Label(display_question_box, text='Choice 3:', bg='orange').grid(row=4, column=1, sticky=W)
    Label(display_question_box, text='Choice 4:', bg='orange').grid(row=5, column=1, sticky=W)
    Label(display_question_box, text='Correct Choice:', bg='orange').grid(row=6, column=1, sticky=W)
    Label(display_question_box, text='Correct Feedback:', bg='orange').grid(row=7, column=1, sticky=W)
    Label(display_question_box, text='Incorrect Feedback:', bg='orange').grid(row=8, column=1, sticky=W)
    Label(display_question_box, text=questionsDict[questions_combobox.get()].text, bg='orange')\
        .grid(row=1, column=2, sticky=W)
    Label(display_question_box, text=questionsDict[questions_combobox.get()].point_value, bg='orange')\
        .grid(row=1, column=4, sticky=W)
    Label(display_question_box, text=questionsDict[questions_combobox.get()].answer1, bg='orange')\
        .grid(row=2, column=2, sticky=W)
    Label(display_question_box, text=questionsDict[questions_combobox.get()].answer2, bg='orange')\
        .grid(row=3, column=2, sticky=W)
    Label(display_question_box, text=questionsDict[questions_combobox.get()].answer3, bg='orange')\
        .grid(row=4, column=2, sticky=W)
    Label(display_question_box, text=questionsDict[questions_combobox.get()].answer4, bg='orange')\
        .grid(row=5, column=2, sticky=W)
    Label(display_question_box, text=questionsDict[questions_combobox.get()].correct_answer, bg='orange')\
        .grid(row=6, column=2, sticky=W)
    Label(display_question_box, text=questionsDict[questions_combobox.get()].correct_feedback, bg='orange')\
        .grid(row=7, column=2, sticky=W)
    Label(display_question_box, text=questionsDict[questions_combobox.get()].incorrect_feedback, bg='orange')\
        .grid(row=8, column=2, sticky=W)
    combobox_selection_number = questionNumbers.index(questions_combobox.get())


def add_question(event):
    """Displays a menu in which the user may enter all the necessary attributes of a new question,
    which will be submitted and transformed in the submit_question function"""
    global add_edit_search_question_box

    # Destroy any Frames used by other functions before displaying new Frame
    try:
        add_edit_search_question_box.destroy()
    except NameError:
        pass
    big_box.destroy()

    # Label and Entry objects to enter new question data
    add_edit_search_question_box = Frame(win, bg='cornsilk', borderwidth=5, relief=RAISED)
    add_edit_search_question_box.pack(pady=20)

    Label(add_edit_search_question_box, text='Enter the question text:', bg='cornsilk').grid(row=0, column=0)
    add_question_text = Entry(add_edit_search_question_box, textvariable=question_text)
    add_question_text.grid(row=0, column=1, pady=20, ipadx=100)

    Label(add_edit_search_question_box, text='Enter the point value:', bg='cornsilk').grid(row=1, column=0)
    add_point_value = Entry(add_edit_search_question_box, textvariable=point_value)
    add_point_value.grid(row=1, column=1)

    Label(add_edit_search_question_box, text='Enter the first answer choice:', bg='cornsilk').grid(row=2, column=0)
    add_answer1 = Entry(add_edit_search_question_box, textvariable=answer1)
    add_answer1.grid(row=2, column=1, pady=20)

    Label(add_edit_search_question_box, text='Enter the second answer choice:', bg='cornsilk').grid(row=3, column=0)
    add_answer2 = Entry(add_edit_search_question_box, textvariable=answer2)
    add_answer2.grid(row=3, column=1)

    Label(add_edit_search_question_box, text='Enter the third answer choice:', bg='cornsilk').grid(row=4, column=0)
    add_answer3 = Entry(add_edit_search_question_box, textvariable=answer3)
    add_answer3.grid(row=4, column=1, pady=20)

    Label(add_edit_search_question_box, text='Enter the fourth answer choice:', bg='cornsilk').grid(row=5, column=0)
    add_answer4 = Entry(add_edit_search_question_box, textvariable=answer4)
    add_answer4.grid(row=5, column=1)

    Label(add_edit_search_question_box, text='Enter the correct answer:', bg='cornsilk').grid(row=6, column=0)
    add_correct_answer = Entry(add_edit_search_question_box, textvariable=correct_answer)
    add_correct_answer.grid(row=6, column=1, pady=20)

    Label(add_edit_search_question_box, text='Enter the correct feedback:', bg='cornsilk').grid(row=7, column=0)
    add_correct_feedback = Entry(add_edit_search_question_box, textvariable=correct_feedback)
    add_correct_feedback.grid(row=7, column=1)

    Label(add_edit_search_question_box, text='Enter the incorrect feedback:', bg='cornsilk').grid(row=8, column=0)
    add_incorrect_feedback = Entry(add_edit_search_question_box, textvariable=incorrect_feedback)
    add_incorrect_feedback.grid(row=8, column=1, pady=20, padx=20)

    # Submit button executes submit_question function
    submit_button = Button(add_edit_search_question_box, text='Submit', command=lambda: submit_question(1))
    submit_button.grid(row=9, column=1, ipadx=20)


def submit_question(event):
    """Creates a new Question object from the added question and places it into some lists and a dictionary
    in order to access these objects and save them to the .csv file later"""

    # New question object using data from add_question function
    temp_question = Question(question_text.get(), point_value.get(), answer1.get(), answer2.get(), answer3.get(),
                             answer4.get(), correct_answer.get(), correct_feedback.get(), incorrect_feedback.get())

    # Add question object to lists and dictionaries for later use and saving
    allQuestionObjects.append(temp_question)
    temp_question_index = allQuestionObjects.index(temp_question)
    questionNumbers.append(f'Question {temp_question_index + 1}')
    questionsDict[f'Question {temp_question_index + 1}'] = temp_question
    questionsToBeSaved.append([temp_question.text, temp_question.point_value, temp_question.answer1,
                               temp_question.answer2, temp_question.answer3, temp_question.answer4,
                               temp_question.correct_answer, temp_question.correct_feedback,
                               temp_question.incorrect_feedback])

    # Restore StringVar() objects to default values after pressing the submit button
    question_text.set('')
    point_value.set('')
    answer1.set('')
    answer2.set('')
    answer3.set('')
    answer4.set('')
    correct_answer.set('')
    correct_feedback.set('')
    incorrect_feedback.set('')


def list_questions(event):
    """Returns to the main menu of the program to list questions in the Combobox"""
    global big_box, add_edit_search_question_box, questionNumbers, questions_combobox

    # Destroy any Frames used by other functions before displaying new Frame
    try:
        add_edit_search_question_box.destroy()
    except NameError:
        pass
    try:
       big_box.destroy()
    except NameError:
        pass

    # Display main menu with Frames and Combobox
    big_box = Frame(win, bg='cornsilk', width=600, height=500, borderwidth=5, relief=RAISED)
    big_box.pack(pady=20)
    big_box.pack_propagate(0)
    Label(big_box, text='Select Question:', bg='cornsilk').grid(row=0, column=0, pady=20, padx=10)
    questions_combobox = ttk.Combobox(big_box, values=questionNumbers)
    questions_combobox.grid(row=0, column=1, padx=10)
    questions_combobox.bind('<<ComboboxSelected>>', question_selected)


def edit_question_menu(event):
    """Display list_questions with an edit button, which executes edit_question_button_press function"""
    global big_box, add_edit_search_question_box, questionNumbers, questions_combobox

    # Destroy any Frames used by other functions before displaying new Frame
    try:
        add_edit_search_question_box.destroy()
    except NameError:
        pass
    try:
        big_box.destroy()
    except NameError:
        pass

    # Display main menu with Frames and Combobox
    big_box = Frame(win, bg='cornsilk', width=600, height=500, borderwidth=5, relief=RAISED)
    big_box.pack(pady=20)
    big_box.pack_propagate(0)
    Label(big_box, text='Select Question:', bg='cornsilk').grid(row=0, column=0, pady=20, padx=10)
    questions_combobox = ttk.Combobox(big_box, values=questionNumbers)
    questions_combobox.grid(row=0, column=1, padx=10)
    questions_combobox.bind('<<ComboboxSelected>>', question_selected)
    edit_button = Button(big_box, text='Edit Question', command=edit_question_button_press)
    edit_button.grid(row=1, column=1)


def edit_question_button_press():
    """Displays a new frame resembling that of add_question, which allows the user to edit the question
    currently selected in the Combobox"""
    global add_edit_search_question_box, questions_combobox

    # Destroy any Frames used by other functions before displaying new Frame
    try:
        add_edit_search_question_box.destroy()
    except NameError:
        pass

    # Label and Entry objects to enter question data
    add_edit_search_question_box = Frame(win, bg='cornsilk', borderwidth=5, relief=RAISED)
    add_edit_search_question_box.pack(pady=10)

    Label(add_edit_search_question_box, text='Enter the question text:', bg='cornsilk').grid(row=0, column=0)
    add_question_text = Entry(add_edit_search_question_box, textvariable=question_text)
    add_question_text.grid(row=0, column=1, pady=10, ipadx=100)

    Label(add_edit_search_question_box, text='Enter the point value:', bg='cornsilk').grid(row=1, column=0)
    add_point_value = Entry(add_edit_search_question_box, textvariable=point_value)
    add_point_value.grid(row=1, column=1)

    Label(add_edit_search_question_box, text='Enter the first answer choice:', bg='cornsilk').grid(row=2, column=0)
    add_answer1 = Entry(add_edit_search_question_box, textvariable=answer1)
    add_answer1.grid(row=2, column=1, pady=10)

    Label(add_edit_search_question_box, text='Enter the second answer choice:', bg='cornsilk').grid(row=3, column=0)
    add_answer2 = Entry(add_edit_search_question_box, textvariable=answer2)
    add_answer2.grid(row=3, column=1)

    Label(add_edit_search_question_box, text='Enter the third answer choice:', bg='cornsilk').grid(row=4, column=0)
    add_answer3 = Entry(add_edit_search_question_box, textvariable=answer3)
    add_answer3.grid(row=4, column=1, pady=10)

    Label(add_edit_search_question_box, text='Enter the fourth answer choice:', bg='cornsilk').grid(row=5, column=0)
    add_answer4 = Entry(add_edit_search_question_box, textvariable=answer4)
    add_answer4.grid(row=5, column=1)

    Label(add_edit_search_question_box, text='Enter the correct answer:', bg='cornsilk').grid(row=6, column=0)
    add_correct_answer = Entry(add_edit_search_question_box, textvariable=correct_answer)
    add_correct_answer.grid(row=6, column=1, pady=10)

    Label(add_edit_search_question_box, text='Enter the correct feedback:', bg='cornsilk').grid(row=7, column=0)
    add_correct_feedback = Entry(add_edit_search_question_box, textvariable=correct_feedback)
    add_correct_feedback.grid(row=7, column=1)

    Label(add_edit_search_question_box, text='Enter the incorrect feedback:', bg='cornsilk').grid(row=8, column=0)
    add_incorrect_feedback = Entry(add_edit_search_question_box, textvariable=incorrect_feedback)
    add_incorrect_feedback.grid(row=8, column=1, pady=10, padx=20)

    # Submit button executes submit_edited_question function
    submit_button = Button(add_edit_search_question_box, text='Submit', command=lambda: submit_edited_question(1))
    submit_button.grid(row=9, column=1, ipadx=10)


def submit_edited_question(event):
    """Submits the edited question from edit_question_button_press and replaces all the old data of it
    in the various containers in which it was stored"""
    global combobox_selection_number
    try:
        # New question object using data from edit_question_button_press function
        temp_question = Question(question_text.get(), point_value.get(), answer1.get(), answer2.get(), answer3.get(),
                                 answer4.get(), correct_answer.get(), correct_feedback.get(), incorrect_feedback.get())

        # Replace the old question object in the lists and dictionaries
        allQuestionObjects[combobox_selection_number] = temp_question
        questionNumbers[combobox_selection_number] = f'Question {combobox_selection_number + 1}'
        questionsDict[f'Question {combobox_selection_number + 1}'] = temp_question
        questions_with_first_row[combobox_selection_number + 1] = [temp_question.text, temp_question.point_value,
                                                                   temp_question.answer1, temp_question.answer2,
                                                                   temp_question.answer3, temp_question.answer4,
                                                                   temp_question.correct_answer,
                                                                   temp_question.correct_feedback,
                                                                   temp_question.incorrect_feedback]
    except IndexError:
        pass

    # Restore StringVar() objects to default values after pressing the submit button
    question_text.set('')
    point_value.set('')
    answer1.set('')
    answer2.set('')
    answer3.set('')
    answer4.set('')
    correct_answer.set('')
    correct_feedback.set('')
    incorrect_feedback.set('')


def delete_question_menu(event):
    """Same display as list_questions, but with a delete button to delete a question"""
    global big_box, add_edit_search_question_box, questionNumbers, questions_combobox

    # Destroy any Frames used by other functions before displaying new Frame
    try:
        add_edit_search_question_box.destroy()
    except NameError:
        pass
    try:
        big_box.destroy()
    except NameError:
        pass

    # Display main menu with Frames and Combobox
    big_box = Frame(win, bg='cornsilk', width=600, height=500, borderwidth=5, relief=RAISED)
    big_box.pack(pady=20)
    big_box.pack_propagate(0)
    Label(big_box, text='Select Question:', bg='cornsilk').grid(row=0, column=0, pady=20, padx=10)
    questions_combobox = ttk.Combobox(big_box, values=questionNumbers)
    questions_combobox.grid(row=0, column=1, padx=10)
    questions_combobox.bind('<<ComboboxSelected>>', question_selected)
    delete_button = Button(big_box, text='Delete Question', command=delete_question_button_press)
    delete_button.grid(row=1, column=1)


def delete_question_button_press():
    """Deletes the selected question in the Combobox in delete_question_menu from all its containers"""
    global combobox_selection_number
    try:
        questionNumbers.pop(combobox_selection_number)
        allQuestionObjects.pop(combobox_selection_number)
        questionsDict.pop(f'Question {combobox_selection_number + 1}')
        questions_with_first_row.pop(combobox_selection_number + 1)
    except KeyError:
        pass
    except IndexError:
        pass


def search_question(event):
    """Allows the user to enter text into an entry box to be searched using search_question_button_press"""
    global add_edit_search_question_box, big_box

    # Destroy any Frames used by other functions before displaying new Frame
    try:
        add_edit_search_question_box.destroy()
    except NameError:
        pass
    try:
        big_box.destroy()
    except NameError:
        pass

    add_edit_search_question_box = Frame(win, bg='cornsilk', borderwidth=5, relief=RAISED)
    add_edit_search_question_box.pack(pady=10)

    Label(add_edit_search_question_box, text='Enter the text you would like to search:', bg='cornsilk')\
        .grid(row=0, column=0)
    add_question_text = Entry(add_edit_search_question_box, textvariable=search_text)
    add_question_text.grid(row=0, column=1, pady=10, ipadx=100)
    search = Button(add_edit_search_question_box, text='Search',
                    command=lambda: search_question_button_press(search_text))
    search.grid(row=1, column=1, pady=10)


def search_question_button_press(event):
    """Uses a for loop to search for questions that contain the search text from search_question,
    then allows these questions to be viewed in a new Frame object using another Combobox"""
    global search_text, big_box, questions_combobox

    # Destroy any Frames used by other functions before displaying new Frame
    try:
        big_box.destroy()
    except NameError:
        pass

    # Loops through all the attributes of each question to find questions that contain the search text
    counter = 1
    questions_found_in_search = []
    for question in allQuestionObjects:
        if search_text.get().casefold() in question.text.casefold() \
                or search_text.get().casefold() in question.answer1.casefold() \
                or search_text.get().casefold() in question.answer2.casefold() \
                or search_text.get().casefold() in question.answer3.casefold() \
                or search_text.get().casefold() in question.answer4.casefold() \
                or search_text.get().casefold() in question.correct_feedback.casefold() \
                or search_text.get().casefold() in question.incorrect_feedback.casefold():
            temp = f'Question {counter}'
            questions_found_in_search.append(temp)
        counter += 1
    counter = 1

    # Display main menu with Frames and Combobox
    big_box = Frame(win, bg='cornsilk', width=600, height=500, borderwidth=5, relief=RAISED)
    big_box.pack(pady=20)
    big_box.pack_propagate(0)
    Label(big_box, text='Questions Matching Search:', bg='cornsilk').grid(row=0, column=0, pady=20, padx=10)
    # Using a list comprehension below to get only those question numbers that match the search text
    questions_combobox = ttk.Combobox(big_box, values=[q for q in questionNumbers if q in questions_found_in_search])
    questions_combobox.grid(row=0, column=1, padx=10)
    questions_combobox.bind('<<ComboboxSelected>>', question_selected)

    questions_found_in_search = []


# Declaring variables to be used with the quiz game functions
quiz_points_earned = 0
total_quiz_points = 0
quiz_question_counter = 0
questions_seen = []
selected_answer = ''


def quiz_selection(event):
    """Event handler tied to the radio buttons used for quiz answer choices"""
    global num, selected_answer
    selected_answer = event


def quiz_submit_question():
    """Submits a question in the quiz game; it changes the points and question number
    and provides feedback accordingly"""
    global selected_answer, allQuestionObjects, question_random_value, display_question_box, big_box, \
        quiz_question_counter, total_quiz_points, quiz_points_earned

    # Checking if the answer was correct in order to adjust points and provide feedback
    if selected_answer == allQuestionObjects[question_random_value].correct_answer:
        # Handles exception if the points value for the question cannot be converted to an int (i.e. Points: f)
        try:
            total_quiz_points += int(allQuestionObjects[question_random_value].point_value)
            quiz_points_earned += int(allQuestionObjects[question_random_value].point_value)
        except ValueError:
            total_quiz_points += 0
            quiz_points_earned += 0
        Label(display_question_box, text=f'Points earned: {quiz_points_earned} / {total_quiz_points}', bg='orange')\
            .grid(row=7, column=1, sticky=W, pady=10)
        Label(display_question_box, text=allQuestionObjects[question_random_value].correct_feedback,
              bg='orange').grid(row=8, column=1, pady=10, sticky=W)
        Label(display_question_box, text=f'Correct Answer: {allQuestionObjects[question_random_value].correct_answer}',
              bg='orange').grid(row=9, column=1, sticky=W, pady=10)
    elif selected_answer != allQuestionObjects[question_random_value].correct_answer:
        try:
            total_quiz_points += int(allQuestionObjects[question_random_value].point_value)
        except ValueError:
            total_quiz_points += 0
        Label(display_question_box, text=f'Points earned: {quiz_points_earned} / {total_quiz_points}', bg='orange') \
            .grid(row=7, column=1, sticky=W, pady=10)
        Label(display_question_box, text=allQuestionObjects[question_random_value].incorrect_feedback,
             bg='orange').grid(row=8, column=1, pady=10, sticky=W)
        Label(display_question_box, text=f'Correct Answer: {allQuestionObjects[question_random_value].correct_answer}',
              bg='orange').grid(row=9, column=1, sticky=W, pady=10)
    next_button = Button(display_question_box, text='Next Question', command=lambda: play_quiz_game(1))
    next_button.grid(row=11, column=1, pady=10, ipadx=20)
    quiz_question_counter += 1


def play_quiz_game(event):
    """Plays quiz game, which gives three unique questions in one game; four answer choices possible"""
    global add_edit_search_question_box, big_box, num, question_random_value, display_question_box, \
        quiz_question_counter, total_quiz_points, quiz_points_earned, questions_seen

    # Restart score when the game is accessed from the menu bar
    if event == 5:
        total_quiz_points = 0
        quiz_points_earned = 0
        questions_seen = []

    # Destroy any Frames used by other functions before displaying new Frame
    try:
        add_edit_search_question_box.destroy()
    except NameError:
        pass
    big_box.destroy()

    big_box = Frame(win, bg='cornsilk', width=650, height=400, borderwidth=5, relief=RAISED)
    big_box.pack(pady=20)
    big_box.pack_propagate(0)
    Label(big_box, text='Quiz Game', bg='cornsilk').pack(anchor=N)
    display_question_box = Frame(big_box, bg='orange', width=400, height=200, borderwidth=5, relief=RAISED)
    display_question_box.pack()
    display_question_box.pack_propagate(0)

    # while loop runs until the random question number is unique and has not been seen in the same game
    while True:
        question_random_value = random.randint(0, len(allQuestionObjects) - 1)
        if question_random_value not in questions_seen:
            questions_seen.append(question_random_value)
            break
        else:
            continue

    # Displays question number out of 3, question text, and points value
    Label(display_question_box, text=f'Question {quiz_question_counter + 1} / 3', bg='orange')\
        .grid(row=0, column=1, sticky=W, pady=10)
    Label(display_question_box, text=allQuestionObjects[question_random_value].text, bg='orange')\
        .grid(row=2, column=1, sticky=W)
    Label(display_question_box, text='Points:', bg='orange').grid(row=2, column=3, sticky=W)
    Label(display_question_box, text=allQuestionObjects[question_random_value].point_value, bg='orange')\
        .grid(row=2, column=4, sticky=W)

    # Creating IntVar for radio buttons and a default selection for each question
    num = IntVar()
    num.set(1)
    selected_answer = '1 - ' + allQuestionObjects[question_random_value].answer1
    quiz_selection(selected_answer)

    # Displays radio buttons for answer choices
    question_choice1 = Radiobutton(display_question_box, variable=num,
                                   text=allQuestionObjects[question_random_value].answer1, value=1, indicatoron=1,
                                   bg='orange',
                                   command=lambda:
                                   quiz_selection('1 - ' + allQuestionObjects[question_random_value].answer1))
    question_choice1.grid(row=3, column=1, sticky=W)
    question_choice2 = Radiobutton(display_question_box, variable=num,
                                   text=allQuestionObjects[question_random_value].answer2,
                                   value=2, indicatoron=1, bg='orange',
                                   command=lambda:
                                   quiz_selection('2 - ' + allQuestionObjects[question_random_value].answer2))
    question_choice2.grid(row=4, column=1, sticky=W)
    question_choice3 = Radiobutton(display_question_box, variable=num,
                                   text=allQuestionObjects[question_random_value].answer3,
                                   value=3, indicatoron=1, bg='orange',
                                   command=lambda:
                                   quiz_selection('3 - ' + allQuestionObjects[question_random_value].answer3))
    question_choice3.grid(row=5, column=1, sticky=W)
    question_choice4 = Radiobutton(display_question_box, variable=num,
                                   text=allQuestionObjects[question_random_value].answer4,
                                   value=4, indicatoron=1, bg='orange',
                                   command=lambda:
                                   quiz_selection('4 - ' + allQuestionObjects[question_random_value].answer4))
    question_choice4.grid(row=6, column=1, sticky=W)

    # Display total points earned
    Label(display_question_box, text=f'Points earned: {quiz_points_earned} / {total_quiz_points}',
          bg='orange').grid(row=7, column=1, sticky=W, pady=10)

    # Submit button executes quiz_submit_question function
    answer_submit_button = Button(display_question_box, text='Submit Answer', command=quiz_submit_question)
    answer_submit_button.grid(row=11, column=1, pady=10)

    # Once three questions have been asked, the results are shown by executing show_quiz_results
    if quiz_question_counter == 3:
        show_quiz_results()


def show_quiz_results():
    """Displays quiz results, namely the earned points out of the total points, and allows user to play again
    or return to the questions list"""
    global add_edit_search_question_box, big_box, display_question_box, quiz_question_counter, total_quiz_points, \
        quiz_points_earned, questions_seen

    # Destroy any Frames used by other functions before displaying new Frame
    try:
        add_edit_search_question_box.destroy()
    except NameError:
        pass
    big_box.destroy()

    big_box = Frame(win, bg='cornsilk', width=650, height=250, borderwidth=5, relief=RAISED)
    big_box.pack(pady=20)
    big_box.pack_propagate(0)
    Label(big_box, text='Quiz Game', bg='cornsilk').pack(anchor=N)
    display_question_box = Frame(big_box, bg='orange', width=400, height=200, borderwidth=5, relief=RAISED)
    display_question_box.pack()
    display_question_box.pack_propagate(0)
    Label(display_question_box, text=f'Your total score was {quiz_points_earned} out of {total_quiz_points}.',
          bg='orange').grid(row=0, column=0, sticky=W)

    # Reset variables used during the quiz
    quiz_question_counter = 0
    quiz_points_earned = 0
    total_quiz_points = 0
    questions_seen = []

    # Allows user to play again or return to questions list with "Yes" and "No" buttons, respectively
    Label(display_question_box, text='Would you like to play the Quiz Game again?', bg='orange')\
        .grid(row=1, column=0, sticky=W)
    yes_button = Button(display_question_box, text='Yes', command=lambda: play_quiz_game(0))
    yes_button.grid(row=2, column=0, sticky=W, padx=50, pady=15, ipadx=25)
    no_button = Button(display_question_box, text='No', command=lambda: list_questions(0))
    no_button.grid(row=2, column=1, sticky=W, padx=50, ipadx=25)


# Menu Bar and Menus to execute the respective functions
menu_bar = Menu(win)
win.config(menu=menu_bar)
file_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='List Questions', command=lambda: list_questions(0))
file_menu.add_command(label='Add Question', command=lambda: add_question(1))
file_menu.add_command(label='Edit Question', command=lambda: edit_question_menu(2))
file_menu.add_command(label='Delete Question', command=lambda: delete_question_menu(3))
file_menu.add_command(label='Search Question', command=lambda: search_question(4))
file_menu.add_command(label='Exit', command=win.quit)
play_menu = Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label='Play', menu=play_menu)
play_menu.add_command(label='Quiz Game', command=lambda: play_quiz_game(5))

# Frame object runs on main menu of the window to display questions and their attributes by the Combobox
big_box = Frame(win, bg='cornsilk', width=600, height=500, borderwidth=5, relief=RAISED)
big_box.pack(pady=20)
big_box.pack_propagate(0)
Label(big_box, text='Select Question:', bg='cornsilk').grid(row=0, column=0, pady=20, padx=10)
questions_combobox = ttk.Combobox(big_box, values=questionNumbers)
questions_combobox.grid(row=0, column=1, padx=10)
questions_combobox.bind('<<ComboboxSelected>>', question_selected)

# Run window
win.mainloop()

# Saving old and new questions to the .csv file after the window closes
with open('questions.csv', 'w', newline='') as file:
    writeData = csv.writer(file)
    for row in questions_with_first_row:
        writeData.writerow(row)

with open('questions.csv', 'a', newline='') as file:
    writeData = csv.writer(file)
    for row in questionsToBeSaved:
        writeData.writerow(row)
