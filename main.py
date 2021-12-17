from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #


def trigger():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        count_down(short_break_min)
        time_label.config(text="BREAK", fg=PINK)
    elif reps % 8 == 0:
        count_down(long_break_min)
        time_label.config(text="WORK", fg=RED)
    else:
        count_down(work_sec)
        time_label.config(text="WORK", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(clock, text=f"{count_min}:{count_sec}")
    if count > 0:
        canvas.after(1000, count_down, count - 1)
    else:
        trigger()
        if reps % 2 == 0:
            marks = ""
            work_sessions = math.floor(reps/2)
            for n in range(work_sessions):
                marks += "✔"
            check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Amaterasu")
window.config(padx=100, pady=50, bg=YELLOW)

#timer label
time_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "bold"))
time_label.grid(column=1, row=0)


#tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
clock = canvas.create_text(100, 110, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#start button
start_button = Button(text="Start", command=trigger)
start_button.grid(column=0, row=2)

#reset button
reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

#checkmark
check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
check_mark.grid(column=1, row=3)


window.mainloop()
