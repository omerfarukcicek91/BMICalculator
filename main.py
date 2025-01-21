from tkinter import *

#open window
window = Tk()
window.title("BMI CALCULATER")
window.minsize(300,300)
window.config(bg="light gray", padx=30, pady=30)
window.geometry('300x250')
FONT = font=("Arial", 10, "normal")

#weight text
weight_label = Label(text="Enter your weight (kg):", font=FONT)
weight_label.config(bg="light gray")
weight_label.config(pady=10,padx=10)
weight_label.pack()

#weight entry
entry_weight = Entry(window, width=10)
entry_weight.pack()


#height text
height_label = Label(text="Enter your height(m):", font=FONT)
height_label.config(bg="light gray")
height_label.config(pady=10,padx=10)
height_label.pack()
#height entry

entry_height = Entry(window,width=10)
entry_height.pack()

result_text = Label(text="Your BMI Score: ", bg="light gray")
result_text.pack()

def calculate_bmi():
    height_value = entry_height.get()
    weight_value = entry_weight.get()

    if height_value == "" or weight_value == "":
        result_text.config(text="Please fill in both fields!")
        return

    elif float(height_value) <= 0 or float(weight_value) <= 0:
        result_text.config(text="Height and weight must be positive values.")
        return
        # calculation
    else:
        try:
            height_value = float(entry_height.get())
            weight_value = float(entry_weight.get())
            bmi_score = weight_value / (height_value ** 2)
            bmi_score = round(bmi_score, 2)
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
        #Classes



#calculation button
calculate_button = Button(window,text="Calculate your BMI", command=calculate_bmi)
calculate_button.pack(padx=10, pady=10)


window.mainloop()
