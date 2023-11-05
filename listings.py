import streamlit as st

# Create a list of 10 empty listings
listings = [{} for _ in range(10)]


def main():
    st.title("House Listings")
    
    # Create a search bar for zip code input
    zip_code = st.text_input("Enter Zip Code:", key="zip_code")
    
    # Create 10 empty widgets for house listings
    for i in range(10):
        st.subheader(f"Listing {i + 1}")
        # Use float values for min_value and step for consistency
        listings[i]['bathrooms'] = st.number_input(f"Number of Bathrooms for Listing {i + 1}", min_value=0.0, step=0.5, key=f"bathrooms_{i}")
        listings[i]['bedrooms'] = st.number_input(f"Number of Bedrooms for Listing {i + 1}", min_value=0.0, step=1.0, key=f"bedrooms_{i}")
        listings[i]['price'] = st.number_input(f"Price for Listing {i + 1}", min_value=0.0, step=1000.0, key=f"price_{i}")
        # Add text input for address
        listings[i]['address'] = st.text_input(f"Address for Listing {i + 1}", key=f"address_{i}")

    # Additional code for searching and filtering listings based on zip code can be added here

    # Display the listings after filtering by zip code
    filtered_listings = [listing for listing in listings if listing.get('address', '').startswith(zip_code)]
    st.write(filtered_listings)

    # Run the Streamlit app
    if __name__ == "__main__":
        st.write("Enter a zip code to filter listings.")
