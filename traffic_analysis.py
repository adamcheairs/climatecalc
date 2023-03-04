import tkinter as tk
import pandas as pd

# Define a function to calculate carbon emissions
def calculate_carbon_emissions(vehicle_type, distance):
    # CO2 emissions per km for different types of vehicles (in grams)
    emissions_per_km = {'car': 120, 'hybrid': 90, 'electric': 0, 'diesel': 150}
    
    # Calculate the CO2 emissions for this vehicle and distance
    emissions = (emissions_per_km[vehicle_type] / 1000) * distance
    
    return emissions

# Define a function to handle button click event
def calculate_emissions():
    # Get input values from user
    vehicle_type = vehicle_type_input.get()
    distance = float(distance_input.get())
    
    # Calculate carbon emissions
    emissions = calculate_carbon_emissions(vehicle_type, distance)
    
    # Display results in label
    result_label.config(text="Carbon emissions: {:.2f} grams".format(emissions))

# Create a new window
window = tk.Tk()
window.title("Carbon Emissions Calculator")

# Create a label for vehicle type input
vehicle_type_label = tk.Label(window, text="Vehicle Type:")
vehicle_type_label.pack()

# Create a dropdown menu for vehicle type input
vehicle_type_options = ['car', 'hybrid', 'electric', 'diesel']
vehicle_type_input = tk.StringVar()
vehicle_type_input.set(vehicle_type_options[0])
vehicle_type_dropdown = tk.OptionMenu(window, vehicle_type_input, *vehicle_type_options)
vehicle_type_dropdown.pack()

# Create a label for distance input
distance_label = tk.Label(window, text="Distance (km):")
distance_label.pack()

# Create an entry field for distance input
distance_input = tk.Entry(window)
distance_input.pack()

# Create a button to calculate emissions
calculate_button = tk.Button(window, text="Calculate", command=calculate_emissions)
calculate_button.pack()

# Create a label to display results
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()