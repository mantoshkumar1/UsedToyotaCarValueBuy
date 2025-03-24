from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup
import csv

# # Path to your MHTML file
# mhtml_file = 'Search Results.mhtml'


def create_car_listing_csv(mhtml_file='Search Results.mhtml'):
    # Open and parse the MHTML file
    with open(mhtml_file, 'rb') as file:
        msg = BytesParser(policy=policy.default).parse(file)

    # Get the HTML content from the MHTML
    html_content = ''
    for part in msg.iter_parts():
        if part.get_content_type() == 'text/html':
            charset = part.get_content_charset() or 'utf-8'
            html_content = part.get_payload(decode=True).decode(charset)

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all car listings
    car_listings = soup.find_all('div', class_='cmp-search-results__each-result')

    # Open CSV file for writing (this will overwrite the old content)
    with open('car_listings.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow(['Car Name', 'Price', 'Mileage', 'Transmission', 'Location', 'Link'])

        # Extract and write car information
        for listing in car_listings:
            # 1. Car Name
            car_name = listing.find('div', class_='cmp-search-results__car-name').get_text(strip=True)

            # 2. Price
            price = listing.find('div', class_='cmp-search-results__car-price').get_text(strip=True)

            # 3. Mileage
            mileage_element = listing.find('div', class_='cmp-search-results__info-value', string=lambda text: text and 'km' in text)
            mileage = mileage_element.get_text(strip=True) if mileage_element else 'N/A'

            # 4. Transmission
            transmission_element = listing.find('div', class_='cmp-search-results__info-value', string='Automatic')
            transmission = transmission_element.get_text(strip=True) if transmission_element else 'N/A'

            # 5. Location
            location = listing.find('div', class_='cmp-search-results__info-value-address').get_text(strip=True)

            # 6. Link to the car details
            link = listing.find('a', class_='cmp-image__link')['href']

            # # Print the extracted data to the screen
            # print(f"Car Name: {car_name}")
            # print(f"Price: {price}")
            # print(f"Mileage: {mileage}")
            # print(f"Transmission: {transmission}")
            # print(f"Location: {location}")
            # print(f"Link: {link}")
            # print("-" * 40)

            # Write the data to CSV
            writer.writerow([car_name, price, mileage, transmission, location, link])

    print("Data has been saved to car_listings.csv")
