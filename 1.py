import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature():
    try:
        temp = float(entry_temp.get())
        unit = unit_var.get()
        
        if unit == "C":
            result = f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F\n{temp}°C = {celsius_to_kelvin(temp):.2f}K"
        elif unit == "F":
            result = f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C\n{temp}°F = {fahrenheit_to_kelvin(temp):.2f}K"
        elif unit == "K":
            result = f"{temp}K = {kelvin_to_celsius(temp):.2f}°C\n{temp}K = {kelvin_to_fahrenheit(temp):.2f}°F"
        else:
            result = "Invalid unit. Please select C, F, or K."
        
        messagebox.showinfo("Conversion Result", result)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# GUI Setup
root = tk.Tk()
root.title("Temperature Converter")

tk.Label(root, text="Enter Temperature:").grid(row=0, column=0, padx=10, pady=10)
entry_temp = tk.Entry(root)
entry_temp.grid(row=0, column=1, padx=10, pady=10)

unit_var = tk.StringVar(value="C")
tk.Label(root, text="Select Unit:").grid(row=1, column=0, padx=10, pady=10)
tk.OptionMenu(root, unit_var, "C", "F", "K").grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Convert", command=convert_temperature).grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
