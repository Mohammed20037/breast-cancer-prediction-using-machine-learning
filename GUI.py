import tkinter as tk
from tkinter import messagebox
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from tkinter import ttk

# Load the dataset
data = pd.read_csv("data.csv", index_col=False)
data['diagnosis'] = data['diagnosis'].apply(lambda x: '1' if x == 'M' else '0')
data = data.set_index('id')
del data['Unnamed: 32']

# Split the data into predictor variables and target variable
Y = data['diagnosis'].values
X = data.drop('diagnosis', axis=1).values

# Standardize the input data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the SVM model
model = SVC(C=2.0, kernel='rbf')
model.fit(X_scaled, Y)

def predict():
    try:
        # Retrieve input values from the GUI
        input_values = []
        for entry in entry_list:
            input_values.append(float(entry.get()))

        # Standardize the input values
        input_scaled = scaler.transform([input_values])

        # Make the prediction
        prediction = model.predict(input_scaled)[0]

        # Display the prediction
        if prediction == '1':
            messagebox.showinfo("Prediction", "Breast cancer is predicted.")
        else:
            messagebox.showinfo("Prediction", "No breast cancer is predicted.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the GUI
window = tk.Tk()
window.title("Breast Cancer Prediction")

# Create a scrollable frame
scrollable_frame = ttk.Frame(window)
scrollable_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Create a canvas and a scrollbar for the scrollable frame
canvas = tk.Canvas(scrollable_frame)
scrollbar = ttk.Scrollbar(scrollable_frame, orient="vertical", command=canvas.yview)
canvas.configure(yscrollcommand=scrollbar.set)

# Pack the scrollbar to the right of the canvas
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a frame inside the canvas to hold the grid layout
grid_frame = tk.Frame(canvas)

# Configure the canvas to scroll the grid frame
canvas.create_window((0, 0), window=grid_frame, anchor="nw")

# Add the grid frame to the canvas
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Bind the scrollbar to the canvas
canvas.configure(scrollregion=canvas.bbox("all"), yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

label_list = [
    "Mean radius:", "Mean texture:", "Mean perimeter:", "Mean area:",
    "Mean smoothness:", "Mean compactness:", "Mean concavity:",
    "Mean concave points:", "Mean symmetry:", "Mean fractal dimension:",
    "Radius error:", "Texture error:", "Perimeter error:", "Area error:",
    "Smoothness error:", "Compactness error:", "Concavity error:",
    "Concave points error:", "Symmetry error:", "Fractal dimension error:",
    "Worst radius:", "Worst texture:", "Worst perimeter:", "Worst area:",
    "Worst smoothness:", "Worst compactness:", "Worst concavity:",
    "Worst concave points:", "Worst symmetry:",  "Worst fractal dimension:"
]

entry_list = []

# Create labels and entry fields for input values using the grid layout
for i, label_text in enumerate(label_list):
    label = tk.Label(grid_frame, text=label_text)
    entry = tk.Entry(grid_frame)
    label.grid(row=i, column=0, sticky="w")
    entry.grid(row=i, column=1, padx=10, pady=5)
    entry_list.append(entry)

# Create the predict button
predict_button = tk.Button(window, text="Predict", command=predict)
predict_button.pack(pady=10)

window.mainloop()
