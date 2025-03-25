import os, sys

current_dir = os.getcwd()

# Add the current directory to the Python path
sys.path.append(current_dir)

from data_analysis import *
from create_csv import create_car_listing_csv

# Instructions to Follow:
#
# Visit https://certifiedtoyota.ca/en/search.html to view the list of pre-owned cars.
#
# Enter your postal code and desired model.
#
# Click “Load More” until all results are loaded.
#
# Once all results are displayed, right-click on the page and select Save as.
#
# Save the entire webpage as a single HTML file.
#
# Provide the path to this saved HTML file as input to this program.

import argparse
import os


# Function to load the webpage file
def load_webpage(webpage_path, fetch_new_data=True):

    if fetch_new_data:
        if not os.path.exists(webpage_path):
            raise FileNotFoundError(f"The specified file does not exist: {webpage_path}")
        print(f"Loading data from {webpage_path}...")

        # logic to process the .mhtml file starts here
        create_car_listing_csv(mhtml_file='Search Results.mhtml') # this function will create 'car_listings.csv'.

    source_csv_path = "car_listings.csv"
    df = load_data_from_csv(source_csv_path)
    df = compute_value_score(df)
    df_sorted = display_best_value_cars(df)

    # Save the sorted data for reference
    df_sorted.to_csv("best_value_cars.csv", index=False)
    print("✅ Best-value cars list saved as 'best_value_cars.csv'.")

    # Generate and show graph
    plot_best_value_graph(df_sorted)


# Main function to parse arguments and run the script
def main():
    parser = argparse.ArgumentParser(description="Process the used car listings.")

    # Optional argument for webpage path
    parser.add_argument(
        "--webpage_path",
        type=str,
        default="Search Results.mhtml", # file path
        help="Path to the saved webpage file. Default is 'Search Results.mhtml' in the project folder."
    )

    # Optional argument for 'fetch_from_webpage_and_store_in_csv' (what if we just want to manually add items in "car_listings.csv"
    # and see where my new car info lies in value score
    parser.add_argument(
        "--fetch_new_data",
        action="store_true",
        help="Set this flag if you want to fetch new data. If omitted, it defaults to False."
    )
    args = parser.parse_args()
    print(args)

    # If the --webpage_path argument is provided, use that; otherwise, use the default
    try:
        load_webpage(args.webpage_path, args.fetch_new_data)
    except FileNotFoundError as e:
        print(e)


if __name__ == "__main__":
    main()

