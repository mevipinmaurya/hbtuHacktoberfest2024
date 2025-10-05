#BMI Index calculator made using Python and Customtkinter(GUI Module)
#Ensure to install customtkinter module before you run the code

#code
import customtkinter as ctk

#function to calculate BMI and related advices
def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
            advice = "It may be helpful to consult a nutritionist to ensure you are meeting your dietary needs."
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
            advice = "This suggests you have a healthy weight for your height. Keep maintaining your balanced lifestyle."
        elif 25 <= bmi < 29.9:
            category = "Overweight"
            advice = "Consider adopting a more active routine and balanced diet to move towards a healthier range."
        else:
            category = "Obese"
            advice = "It is recommended to seek medical guidance and focus on lifestyle changes for better health."

        result = f"Your BMI is {bmi:.2f}. This falls under the category '{category}'.\n\nAdvice: {advice}"
        result_label.configure(text=result)
    except:
        result_label.configure(text="Invalid input. Please enter numeric values for weight and height.")

#building GUI
#building the main page
app = ctk.CTk()
app.title("Body Mass Index Calculator")
app.geometry("850x600")
app.configure(fg_color="#241135")

#building frame
frame = ctk.CTkFrame(app, fg_color="#fffacd", corner_radius=20)
frame.pack(pady=40, padx=40, fill="both", expand=True)

#building title
title_label = ctk.CTkLabel(frame, text="Body Mass Index Calculator", font=("Helvetica", 28, "bold"), text_color="black")
title_label.pack(pady=20)

#input frame
input_frame = ctk.CTkFrame(frame, fg_color="#f0f8ff", corner_radius=15)
input_frame.pack(pady=20, padx=20, fill="x")

#labels associated
weight_label = ctk.CTkLabel(input_frame, text="Enter Weight (kg):", font=("Helvetica", 16), text_color="black")
weight_label.grid(row=0, column=0, padx=20, pady=15, sticky="w")
weight_entry = ctk.CTkEntry(input_frame, font=("Helvetica", 16), width=200)
weight_entry.grid(row=0, column=1, padx=20, pady=15)

height_label = ctk.CTkLabel(input_frame, text="Enter Height (cm):", font=("Helvetica", 16), text_color="black")
height_label.grid(row=1, column=0, padx=20, pady=15, sticky="w")
height_entry = ctk.CTkEntry(input_frame, font=("Helvetica", 16), width=200)
height_entry.grid(row=1, column=1, padx=20, pady=15)

#defining and creating button and related functions
calc_button = ctk.CTkButton(frame, text="Calculate BMI", command=calculate_bmi, font=("Helvetica", 18, "bold"), fg_color="#4d79ff", hover_color="#0096c7", corner_radius=12, text_color="black")
calc_button.pack(pady=30)

#result frames and labels
result_frame = ctk.CTkFrame(frame, fg_color="#f0f8ff", corner_radius=15)
result_frame.pack(pady=20, padx=20, fill="both", expand=True)

result_label = ctk.CTkLabel(result_frame, text="", font=("Helvetica", 18), text_color="black", wraplength=700, justify="center")
result_label.pack(pady=40, padx=20)

app.mainloop()