import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns


# Load data function
def load_data_from_csv(file_path):
    """Loads car data, cleans it, and filters out hybrids."""
    df = pd.read_csv(file_path)

    # Convert price and mileage to numerical values
    df['Price'] = df['Price'].replace({r'\$': '', r',': ''}, regex=True).astype(float)
    df['Mileage'] = df['Mileage'].replace({' km': '', r',': ''}, regex=True).astype(float)

    # Extract model year
    df['Model Year'] = df['Car Name'].apply(
        lambda x: int(re.match(r'(\d{4})', x).group(1)) if re.match(r'(\d{4})', x) else None)

    # Remove hybrid cars
    df = df[~df['Car Name'].str.contains("Hybrid", case=False, na=False)]

    # Add car name with year for display
    df['Car Name with Year'] = df['Car Name']

    # Extract distance in km from Location
    df['Location (km)'] = df['Location'].apply(
        lambda x: re.search(r'(\d+)', x).group(1) if re.search(r'(\d+)', x) else None)

    return df


# Compute Value Score
def compute_value_score(df):
    """Calculates a value score based on price, mileage, and model year."""
    df['Value Score'] = (df['Model Year'] * 1.5) - (df['Price'] / 5000) - (df['Mileage'] / 10000)

    # Normalize scores between 0-100 (for better readability)
    df['Value Score'] = ((df['Value Score'] - df['Value Score'].min()) /
                         (df['Value Score'].max() - df['Value Score'].min())) * 100

    return df


# Display results with instructions
def display_best_value_cars(df):
    """Sorts cars by value score and prints them with instructions."""
    df_sorted = df.sort_values(by='Value Score', ascending=False)

    instructions = """
    📌 **How to Use This Table to Pick the Best Car?**
    1️⃣ Higher **Value Score** = **Better deal** (price, mileage, and year combined).
    2️⃣ **Model Year** – Newer is usually better.
    3️⃣ **Mileage** – Lower is better for longevity.
    4️⃣ **Price** – The car may be cheap, but check the score for overall value.
    5️⃣ **Compare Multiple Options** – Don’t just pick the cheapest, check the best-value deal.
    """

    print(instructions)
    # print(df_sorted[['Car Name with Year', 'Price', 'Mileage', 'Model Year', 'Value Score', 'Location (km)', 'Link']])
    df_sorted = df_sorted[['Car Name with Year', 'Price', 'Mileage', 'Model Year', 'Value Score', 'Location (km)', 'Link']]
    print(df_sorted)

    return df_sorted


# Generate a scatter plot
def plot_best_value_graph(df):
    """Creates a scatter plot of price vs. mileage, highlighting the best-value car."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=df['Mileage'], y=df['Price'], hue=df['Value Score'], size=df['Value Score'], sizes=(50, 200),
                    palette="coolwarm")

    best_car = df.iloc[0]  # Best value car (highest score)
    plt.scatter(best_car['Mileage'], best_car['Price'], color='red', s=250, label="Best Value Buy", edgecolors='black')

    plt.xlabel("Mileage (km)")
    plt.ylabel("Price ($)")
    plt.title("Car Price vs. Mileage (Best Value Highlighted)")
    plt.legend()

    file_name = "best_value_cars.png"
    plt.savefig(file_name)
    print(f"📊 Saved graph: {file_name}")

    plt.show()


# # Sample execution
# file_path = "car_listings_copy.csv"
# df = load_data(file_path)
# df = compute_value_score(df)
# df_sorted = display_best_value_cars(df)
#
# # Save the sorted data for reference
# df_sorted.to_csv("best_value_cars.csv", index=False)
# print("✅ Best-value cars list saved as 'best_value_cars.csv'.")
#
# # Generate and show graph
# plot_best_value_graph(df_sorted)
