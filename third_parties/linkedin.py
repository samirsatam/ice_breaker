import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """ scrape information from linkedin profiles,
    Manually scrape the information from the linkedin profile"""

    if mock:
        linkedin_profile_url= "https://gist.githubusercontent.com/samirsatam/e0b9d14cae4e8b32edd3f2504f08d5b8/raw/b9e78b571af516e8c7685da1539dca6e63543383/samir-satam-scrapin.json"
        response = requests.get(linkedin_profile_url, timeout=10)
    else:
        api_endpoint = "https://api.scrapein.io/enrichment/profile"
        params = {
            "apiKey": os.getenv("SCRAPIN_API_KEY"),
            "linkedinUrl": linkedin_profile_url,
        }
        response = requests.get(api_endpoint, params=params, timeout=10)

    data = response.json().get("person")

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(linkedin_profile_url="https://www.linkedin.com/in/samirsatam", mock=True)
    )