import tkinter as tk
import pandas as pd

def calculate_carbon_emissions(vehicle_type, distance):
    emissions_per_km = {'car': 120, 'hybrid': 90, 'electric': 0, 'diesel': 150}
    
    emissions = (emissions_per_km[vehicle_type] / 1000) * distance
    
    return emissions

def calculate_emissions():
    vehicle_type = vehicle_type_input.get()
    distance = float(distance_input.get())
    
    emissions = calculate_carbon_emissions(vehicle_type, distance)
    
    result_label.config(text="Carbon emissions: {:.2f} grams".format(emissions))

window = tk.Tk()
window.title("Carbon Emissions Calculator")

vehicle_type_label = tk.Label(window, text="Vehicle Type:")
vehicle_type_label.pack()

vehicle_type_options = ['car', 'hybrid', 'electric', 'diesel']
vehicle_type_input = tk.StringVar()
vehicle_type_input.set(vehicle_type_options[0])
vehicle_type_dropdown = tk.OptionMenu(window, vehicle_type_input, *vehicle_type_options)
vehicle_type_dropdown.pack()

distance_label = tk.Label(window, text="Distance (km):")
distance_label.pack()

distance_input = tk.Entry(window)
distance_input.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_emissions)
calculate_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
