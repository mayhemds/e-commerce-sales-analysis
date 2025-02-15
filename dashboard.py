import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Data set
df = pd.read_excel("../../Datasets/real_world_datasets/ecommerce_sales.xlsx")


# Convert Date Columns
df["Date"] = pd.to_datetime(df["Date"])


# Calculate Revenue
df["Revenue"] = df["Quantity Sold"] * df["Price"]


# Sidebar Filters
st.sidebar.header("Filters")
selected_category = st.sidebar.selectbox("Select Product Category", ["All"] + list(df["Product Category"].unique()))


# Apply Filters
if selected_category != 'All':
    df = df[df["Product Category"] == selected_category]


# Dashboard Title
st.title(" E-commerce Sales Dashboard")

# --- Top-Selling Products ---
st.subheader("Top 5 Best-Selling Products")
top_products = df.groupby("Product Name")["Quantity Sold"].sum().sort_values(ascending=False).head(5)

# Plot Bar Chart
fig, ax = plt.subplots()
top_products.plot(kind="bar", color="skyblue", ax=ax)
ax.set_ylabel("Total Quantity Sold")
st.pyplot(fig)

# --- Sales Trend Over Time ---
st.subheader("Sales Trend Over Time")
fig, ax = plt.subplots()
df.groupby("Date")['Revenue'].sum().plot(figsize=(10,9), color="green", ax=ax)
ax.set_ylabel("Revenue")
st.pyplot(fig)



# --- Revenue by Product Category ---
st.subheader("Revenue by Breakdown by Category")
fig, ax = plt.subplots()
df.groupby("Product Category")["Revenue"].sum().plot(kind="pie", autopct="%1.1f%%", ax=ax)
ax.set_ylabel("")
st.pyplot(fig)


# --- Total Revenue ---

total_revenue = df["Revenue"].sum()
st.subheader(f"Total Revenue: ${total_revenue:.2f}")