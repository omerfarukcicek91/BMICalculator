from tkinter import *


#open window
window = Tk()
window.title("BMI CALCULATER")
window.minsize(300,300)
window.config(bg="light gray")
window.geometry('300x250')
FONT = font=("Arial", 10, "normal")

#weight text
text1 = Label(text="Enter your weight (kg):", font=FONT)
text1.config(bg="light gray")
text1.config(pady=10,padx=10)
text1.pack()

#weight entry
entry_weight = Entry(window)
entry_weight.pack()


#height text
text2 = Label(text="Enter your height(m):", font=FONT)
text2.config(bg="light gray")
text2.config(pady=10,padx=10)
text2.pack()
#height entry

entry_height = Entry(window)
entry_height.pack()

result_text = Label(text="Your BMI Score: ", bg="light gray")
result_text.pack()

def calculate_bmi():
    try:
        height_value = entry_height.get()
        weight_value = entry_weight.get()

        if not height_value.strip() or not weight_value.strip():
            result_text.config(text="Please fill in both fields!")
            return
        height_value = float(entry_height.get())
        weight_value = float(entry_weight.get())


        if height_value <= 0 or weight_value <=0:
            result_text.config(text="Height and weight must be positive values.")
            return
        #calculation
        bmi_score = weight_value / (height_value ** 2)
        bmi_score = round(bmi_score, 2)

        #Classes
        if bmi_score < 18.5:
            result_text2 = "You're Underweighted"
        elif 18.5 <= bmi_score < 24.9:
            result_text2 = "You're Normal weighted"
        elif 25 <= bmi_score < 29.9:
            result_text2 = "You're Overweighted"
        else:
            result_text2 = "You're Obese"

        result_text.config(text=f"Your BMI: {bmi_score}({result_text2})")
    except ValueError as e:
        result_text.config(text="Invalid input! Please enter valid numbers.")

#calculation button
calculate_button = Button(window, text="Calculate your BMI", command=calculate_bmi)
calculate_button.pack(padx=10, pady=10)


window.mainloop()


