import tkinter as tk

class Diet:
    def __init__(self, breakfast_calories, lunch_calories, dinner_calories, exercise, bmr):
        self.breakfast_calories=breakfast_calories
        self.lunch_calories=lunch_calories
        self.dinner_calories=dinner_calories
        self.exercise=exercise
        self.bmr=bmr
    def calorie_deficit(self):
        deficit=self.bmr+self.exercise-(self.breakfast_calories+self.lunch_calories+self.dinner_calories)
        return deficit

def calculate():
    breakfast_calories=int(breakfast_entry.get())
    lunch_calories=int(lunch_entry.get())
    dinner_calories=int(dinner_entry.get())
    exercise=int(exercise_entry.get())
    bmr=int(bmr_entry.get())
    fitness = Diet(breakfast_calories,lunch_calories, dinner_calories, exercise, bmr)
    weekly_deficit=7*fitness.calorie_deficit()

    if weekly_deficit>0:
        result_label.config(text=f"You will lose {round(weekly_deficit/3600, 2)} lbs. per week")
    elif weekly_deficit==0:
        result_label.config(text='Your weight will stay the same.')
    else:
        result_label.config(text=f"You will gain {round(-1 * weekly_deficit/3600, 2)} lbs. per week.")

# Create the GUI window
window = tk.Tk()
window.geometry("500x250")
window.configure(bg="lightblue")
window.title('Diet Calculator')

# Create the input labels and entry widgets
breakfast_label = tk.Label(window, text='Breakfast Calories:')
breakfast_entry = tk.Entry(window)
lunch_label = tk.Label(window, text='Lunch Calories:',padx=10,pady=10)
lunch_entry = tk.Entry(window)
dinner_label = tk.Label(window, text='Dinner Calories:')
dinner_entry = tk.Entry(window)
exercise_label = tk.Label(window, text='Exercise Calories:')
exercise_entry = tk.Entry(window)
bmr_label = tk.Label(window, text='Basic Metabolic Rate:',pady=10,padx=10)
bmr_entry = tk.Entry(window)

# Create the calculate button and result label
calculate_button = tk.Button(window, text='Calculate', command=calculate)
result_label = tk.Label(window, text='')

# Add the widgets to the window
breakfast_label.grid(row=0, column=0)
breakfast_entry.grid(row=0, column=1)
lunch_label.grid(row=1, column=0)
lunch_entry.grid(row=1, column=1)
dinner_label.grid(row=2, column=0)
dinner_entry.grid(row=2, column=1)
exercise_label.grid(row=3, column=0)
exercise_entry.grid(row=3, column=1)
bmr_label.grid(row=4, column=0)
bmr_entry.grid(row=4, column=1)
calculate_button.grid(row=5, column=0, columnspan=2, pady=10)
result_label.grid(row=6, column=0, columnspan=2)

# Start the event loop
window.mainloop()
