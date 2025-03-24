# **Used Toyota Car Value Buy Script**

This Python script helps you quickly analyze and choose the best used Toyota car based on various 
factors like price, mileage, transmission type, and model year. It uses data from certified Toyota 
websites and evaluates cars based on your preferences and calculated "Value Buy" score.

---

## **Table of Contents**

- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [How to Run the Script](#how-to-run-the-script)
- [Directory Structure](#directory-structure)
- [Example Output](#example-output)
- [License](#license)

---

## **Installation**

### Step 1: Clone the repository

You can download or clone this repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/used-toyota-car-value-buy.git
```

### Step 2: Set up the virtual environment

For this project, it’s recommended to use a virtual environment to manage dependencies.

1. Navigate to the project directory:

```bash
cd used-toyota-car-value-buy
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

### Step 3: Install dependencies

Once the virtual environment is activated, install the required packages by running:

```bash
pip install -r requirements.txt
```

---

## **Requirements**

Ensure you have the following installed:

- Python 3.x (Recommended: 3.7 or above)
- Required Python packages (listed in `requirements.txt`)

---

## **Usage**

### Step 1: Download Used Car Listings

1. Go to [Certified Toyota's Pre-owned Car Search](https://certifiedtoyota.ca/en/search.html).
2. Enter your postal code and chose your preferred car model (if you've any).
3. Click "Load More" repeatedly until all available car listings are loaded on the page.
4. Right-click anywhere on the webpage and select Save as.
5. Save the file as `Search Results.mhtml` (Format: Webpage, Single File) inside this project folder.
     This will overwrite any existing `Search Results.mhtml` file. 
6. Alternatively, if your `Search Results.mhtml` file is saved elsewhere, use the `--webpage_path` argument to provide 
     the path to that file when running the script.


### Step 2: Run the Python Script

Now that you have saved the car listings as an HTML file, you can run the script.

1. Place the saved HTML file in the project folder.
2. Run the following command in the terminal or command prompt:

```bash
python main.py --webpage_path "path/to/your/saved/file.mhtml"
```

Replace `"path/to/your/saved/file.mhtml"` with the actual path to your saved file.

### Step 3: View the Results

After running the script, it will analyze the listings and display results such as:

- **Best Value Buy score** for each car based on its price, mileage, transmission type, and more.
- **Graphs** showing price vs mileage, transmission distribution, etc.
- Sorted car listings with information like price, mileage, and a link to the car details.

---

## **How to Run the Script**

### Example Command:

```bash
python main.py --webpage_path "path/to/your/saved/file.mhtml"
```

- `--webpage_path`: The path to the HTML file you saved earlier with the pre-owned car listings.

---


## **Example Output**

### Car Analysis

The output will be printed in the terminal and show the following:

- **Car Name with Year**: Model and Year of the car
- **Price**: Price of the car
- **Mileage**: Number of kilometers driven
- **Transmission**: Transmission type (e.g., Automatic or Manual)
- **Location (km)**: Distance from your location (in km)
- **Link**: URL to the car listing

---

### **Graphical Representation**:

The script will also generate graphs displaying:
- Price distribution of all cars.
- Mileage distribution.
- Transmission type distribution.

These graphs will automatically open and save as images in your current working directory for further reference.

---

### **How Does Output Look Like (Run Example):**:
```bash
(venv) UsedToyotaCarValueAnalyzer % python3 main.py --webpage_path "Search Results.mhtml"

Loading data from Search Results.mhtml...
Data has been saved to car_listings.csv

📌 **How to Use This Table to Pick the Best Car?**

1️⃣ **Higher Value Score** = **Better deal** (price, mileage, and year combined).  
2️⃣ **Model Year** – Newer is usually better.  
3️⃣ **Mileage** – Lower is better for longevity.  
4️⃣ **Price** – The car may be cheap, but check the score for overall value.  
5️⃣ **Compare Multiple Options** – Don’t just pick the cheapest, check the best-value deal.

| Car Name with Year         | Price  | Mileage | Model Year | Value Score | Location (km) | Link                                                                                      |
|----------------------------|--------|---------|------------|-------------|---------------|-------------------------------------------------------------------------------------------|
| 2025 RAV4 XLE AWDXLE Premium AWD | 42187.0 | 725.0   | 2025       | 100.0       | 75            | [Link](https://certifiedtoyota.ca/en/vehicle-details....)                                  |
| 2024 RAV4 LE AWDStandard Package | 35499.0 | 13124.0 | 2024       | 91.54       | 47            | [Link](https://certifiedtoyota.ca/en/vehicle-details....)                                  |
| 2024 RAV4 LE AWDStandard Package | 35500.0 | 17295.0 | 2024       | 89.02       | 33            | [Link](https://certifiedtoyota.ca/en/vehicle-details....)                                  |
| 2024 RAV4 LE AWDStandard Package | 35299.0 | 20599.0 | 2024       | 87.27       | 37            | [Link](https://certifiedtoyota.ca/en/vehicle-details....)                                  |
| 2024 RAV4 XLE AWDXLE Premium AWD | 41687.0 | 10563.0 | 2024       | 85.61       | 75            | [Link](https://certifiedtoyota.ca/en/vehicle-details....)                                  |
| ...                         | ...    | ...     | ...        | ...         | ...           | ...                                                                                       |
| 2019 RAV4 XLE FWDXLE FWD     | 26888.5 | 95471.0 | 2019       | 6.97        | 348           | [Link](https://certifiedtoyota.ca/en/vehicle-details....)                                  |
| 2021 RAV4 XLE AWDXLE Premium AWD | 31588.0 | 104087.0 | 2021     | 14.20       | 6             | [Link](https://certifiedtoyota.ca/en/vehicle-details....)                                  |
| 2019 RAV4 XLE AWDXLE AWD     | 26495.0 | 107800.0 | 2019      | 0.00        | 429           | [Link](https://certifiedtoyota.ca/en/vehicle-details....)                                  |

[87 rows x 7 columns]

✅ **Best-value cars list saved as 'best_value_cars.csv'.**  
📊 **Saved graph: best_value_cars.png**
```

---

## **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## **Conclusion**

This script provides an easy way to analyze used car listings and determine the best value buy based on key factors such as price, mileage, and model year. By following the steps outlined in the **Usage** section, you can quickly evaluate available options and make a well-informed purchase decision.

Feel free to contribute or modify the script to suit your specific needs!

---

### Let me know if you need anything else!