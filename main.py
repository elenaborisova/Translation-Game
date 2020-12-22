from random import randint
from num2words import num2words
import tkinter
from collections import deque
import time
import unidecode
from gtts import gTTS
import playsound
import os


def generate_random_number():
    return randint(0, 10)


def translate_number():
    return num2words(numbers[0], lang='es')


def activate_speech(correct_answer):
    language = "es"
    speech = gTTS(text=correct_answer, lang=language, slow=False)
    speech.save("audio.mp3")
    playsound.playsound("audio.mp3", True)
    os.remove('audio.mp3')


def show_correct_answer_message(correct_answer):
    correct_answer_message.place(x=270, y=240)
    correct_answer_message.config(font=("Courier", 10, "bold"), background="#EAECEE", fg="#229954")
    activate_speech(correct_answer)
    root.update()
    time.sleep(1.5)
    correct_answer_message.place_forget()


def show_wrong_answer_message():
    wrong_answer_message.place(x=255, y=240)
    wrong_answer_message.config(font=("Courier", 10, "bold"), background="#EAECEE", fg="#CB4335")
    root.update()
    time.sleep(1.5)
    wrong_answer_message.place_forget()


def show_hint(correct_answer):
    hint = correct_answer[0] + " _ " * (len(correct_answer) - 2) + correct_answer[-1]
    hint_message.place(x=300, y=220, anchor="center")
    hint_message.config(text=hint, font=("Courier", 9), background="#EAECEE", fg="#3498DB")
    button.place(x=300, y=270, anchor="center")
    button.config(activebackground="#3498DB", font="Courier")


def check_correct_answer(user_answer, numbers):
    global win_points
    global lose_points
    correct_answer = translate_number()

    if user_answer == "":
        show_hint(correct_answer)
    elif user_answer == unidecode.unidecode(correct_answer):
        win_points += 1
        numbers.popleft()
        show_correct_answer_message(correct_answer)
        main_label.config(text=f"Translate: {numbers[0]}")
    else:
        lose_points += 1
        show_wrong_answer_message()
    points_label.config(text=f"Correct numbers: {win_points}\n  Incorrect numbers: {lose_points}")


def click_button():
    correct_answer = translate_number()
    hint_message.place_forget()
    revealed_answer.place(x=300, y=220, anchor="center")
    revealed_answer.config(text=correct_answer, font=("Courier", 9), background="#EAECEE", fg="#3498DB")


def press_enter(event):
    user_answer = entry.get()
    entry.delete(0, "end")
    hint_message.place_forget()
    button.place_forget()
    revealed_answer.place_forget()

    number = generate_random_number()
    numbers.append(number)
    check_correct_answer(user_answer, numbers)


# Config root
root = tkinter.Tk()
root.title("Numbers Translation Game")
root.geometry("700x400")
root.config(bg="#D5D8DC")


# Config frame
frame = tkinter.Frame(root, background="#EAECEE")
frame.place(x=50, y=50, width=600, height=300)


# Config entry
entry = tkinter.Entry(root, bg="#F2F3F4", font=("Courier", 20), fg="#34495E")
entry.place(x=200, y=185, width=300, height=50)
entry.focus_set()


# Generate first number and points
numbers = deque()
number = generate_random_number()
numbers.append(number)

win_points = 0
lose_points = 0


# Config labels
main_label = tkinter.Label(text=f"Translate: {number}")
main_label.place(x=240, y=130)
main_label.config(font=("Courier", 20), background="#EAECEE")

points_label = tkinter.Label(text=f"Correct numbers: {win_points}\n  Incorrect numbers: {lose_points}")
points_label.place(x=-10, y=5)
points_label.config(font=("Courier", 11), background="#D5D8DC", fg="#34495E")

wrong_answer_message = tkinter.Label(text="Wrong answer! Try again!")
wrong_answer_message.place_forget()

correct_answer_message = tkinter.Label(text="Correct! Well done!")
correct_answer_message.place_forget()

hint_message = tkinter.Label(frame)
revealed_answer = tkinter.Label(frame)


# Button
button = tkinter.Button(frame, text="SHOW CORRECT ANSWER", command=click_button)


entry.bind("<Return>", press_enter)
root.mainloop()
