import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../DataSets/CARS.csv")

# Set page title
st.title("Car Brand Horsepower Viewer")

# Show available brands
brands = df['Make'].unique()
selected_brand = st.selectbox("Select a Car Brand", options=brands)

# Filter dataframe based on selected brand
filtered_df = df[df['Make'] == selected_brand]

# Plotting
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=filtered_df['Model'], y=filtered_df['Horsepower'], ax=ax)
plt.xticks(rotation=90)
plt.title(f"Horsepower of {selected_brand} Models")
plt.xlabel("Model")
plt.ylabel("Horsepower")
st.pyplot(fig)
