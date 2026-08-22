#Problem #1
#Tells your zodiac, chinese zodiac, traits and forecast

import tkinter as tk
from tkinter import messagebox

WESTERN_ZODIAC_DATA = [
    [1, 20, "Capricorn", "Ambitious, organized, practical, patient."],
    [2, 19, "Aquarius", "Innovative, independent, humanitarian, original."],
    [3, 21, "Pisces", "Compassionate, artistic, intuitive, empathetic."],
    [4, 20, "Aries", "Eager, dynamic, quick, competitive."],
    [5, 21, "Taurus", "Strong, dependable, sensual, creative."],
    [6, 21, "Gemini", "Versatile, expressive, curious, kind."],
    [7, 23, "Cancer", "Intuitive, sentimental, compassionate, protective."],
    [8, 23, "Leo", "Dramatic, outgoing, fiery, self-assured."],
    [9, 23, "Virgo", "Practical, loyal, analytical, gentle."],
    [10, 23, "Libra", "Diplomatic, artistic, intelligent, hospitable."],
    [11, 22, "Scorpio", "Passionate, stubborn, resourceful, brave."],
    [12, 22, "Sagittarius", "Extraverted, optimistic, funny, generous."],
    [12, 31, "Capricorn", "Ambitious, organized, practical, patient."]
]

CHINESE_ANIMALS = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
CHINESE_FORECASTS = [
    "A year of new networking opportunities and career growth.",
    "Steady progress rewarded by consistent effort and discipline.",
    "Bold moves will bring great returns; stay adaptable.",
    "A peaceful year favoring self-care and emotional balance.",
    "High energy brings strong leadership and breakthrough ideas.",
    "Wisdom and strategy will turn challenges into victories.",
    "Fast-paced changes bring excitement and fresh adventures.",
    "Creativity flourishes; focus on personal growth and arts.",
    "Sharp problem-solving opens doors to unexpected rewards.",
    "Attention to detail pays off in your professional life.",
    "Loyalty and honesty lead to strong, lasting partnerships.",
    "Good fortune and contentment follow good choices."
]

def find_western_zodiac(month, day):
    for item in WESTERN_ZODIAC_DATA:
        cutoff_month = item[0]
        cutoff_day = item[1]
        
        if month < cutoff_month or (month == cutoff_month and day <= cutoff_day):
            return item[2], item[3]
            
    return "Capricorn", "Ambitious, organized, practical, patient."

def find_chinese_zodiac(year):
    target_index = (year - 4) % 12
    
    matched_animal = ""
    matched_forecast = ""
    
    for idx in range(len(CHINESE_ANIMALS)):
        if idx == target_index:
            matched_animal = CHINESE_ANIMALS[idx]
            matched_forecast = CHINESE_FORECASTS[idx]
            break
            
    return matched_animal, matched_forecast

def calculate_horoscope():
    try:
        mm = int(entry_month.get().strip())
        dd = int(entry_day.get().strip())
        yyyy = int(entry_year.get().strip())

        if not (1 <= mm <= 12 and 1 <= dd <= 31 and yyyy > 0):
            raise ValueError

        w_sign, traits = find_western_zodiac(mm, dd)
        c_sign, forecast = find_chinese_zodiac(yyyy)

        lbl_w_sign_val.config(text=w_sign)
        lbl_traits_val.config(text=traits)
        lbl_c_sign_val.config(text=c_sign)
        lbl_forecast_val.config(text=forecast)

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values for Month (1-12), Day (1-31), and Year.")

root = tk.Tk()
root.title("Zodiac & Chinese Zodiac Finder")
root.geometry("750x580")
root.resizable(False, False)

lbl_title = tk.Label(root, text="Zodiac Finder", font=("Helvetica", 23, "bold"))
lbl_title.pack(pady=15)

frame_input = tk.Frame(root)
frame_input.pack(pady=5)

tk.Label(frame_input, text="MM:", font=("Helvetica", 16)).grid(row=0, column=0, padx=2)
entry_month = tk.Entry(frame_input, width=4, font=("Helvetica", 16))
entry_month.grid(row=0, column=1, padx=8)

tk.Label(frame_input, text="DD:", font=("Helvetica", 16)).grid(row=0, column=2, padx=2)
entry_day = tk.Entry(frame_input, width=4, font=("Helvetica", 16))
entry_day.grid(row=0, column=3, padx=8)

tk.Label(frame_input, text="YYYY:", font=("Helvetica", 16)).grid(row=0, column=4, padx=2)
entry_year = tk.Entry(frame_input, width=6, font=("Helvetica", 16))
entry_year.grid(row=0, column=5, padx=8)

btn_calc = tk.Button(root, text="Calculate Zodiac", command=calculate_horoscope, bg="#4CAF50", fg="white", font=("Helvetica", 16, "bold"), padx=10, pady=5)
btn_calc.pack(pady=15)

frame_results = tk.LabelFrame(root, text=" Results ", font=("Helvetica", 17, "bold"), padx=15, pady=15)
frame_results.pack(padx=30, pady=10, fill="both", expand=True)

tk.Label(frame_results, text="Zodiac Sign:", font=("Helvetica", 16, "bold")).grid(row=0, column=0, sticky="w", pady=6)
lbl_w_sign_val = tk.Label(frame_results, text="-", font=("Helvetica", 16), fg="#1E88E5")
lbl_w_sign_val.grid(row=0, column=1, sticky="w", pady=6, padx=10)

tk.Label(frame_results, text="Traits:", font=("Helvetica", 16, "bold")).grid(row=1, column=0, sticky="nw", pady=6)
lbl_traits_val = tk.Label(frame_results, text="-", font=("Helvetica", 16), wraplength=480, justify="left")
lbl_traits_val.grid(row=1, column=1, sticky="w", pady=6, padx=10)

tk.Label(frame_results, text="Chinese Zodiac:", font=("Helvetica", 16, "bold")).grid(row=2, column=0, sticky="w", pady=6)
lbl_c_sign_val = tk.Label(frame_results, text="-", font=("Helvetica", 16), fg="#D81B60")
lbl_c_sign_val.grid(row=2, column=1, sticky="w", pady=6, padx=10)

tk.Label(frame_results, text="Forecast:", font=("Helvetica", 16, "bold")).grid(row=3, column=0, sticky="nw", pady=6)
lbl_forecast_val = tk.Label(frame_results, text="-", font=("Helvetica", 16), wraplength=480, justify="left")
lbl_forecast_val.grid(row=3, column=1, sticky="w", pady=6, padx=10)

root.mainloop()
