import requests

class PlatformScraper:
    def __init__(self, config):
        phq = config["predicthq"]

        self.api_token = phq["api_token"]
        self.base_url = phq["base_url"]
        self.country = phq["country"]
        self.city = phq.get("city", "")
        self.limit = phq["limit"]
       

    def fetch_events(self):
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Accept": "application/json"
        }

        params = {
            "country": self.country,
            "q":self.city,
            "limit": self.limit
        }

        print("Requesting PredictHQ API...")
        print("URL:", self.base_url)

        response = requests.get(
            self.base_url,
            headers=headers,
            params=params
        )

        print("Status Code:", response.status_code)

        if response.status_code != 200:
            print("❌ API request failed")
            print(response.text)
            return []

        data = response.json()
        events = data.get("results", [])

        print(f"Events received: {len(events)}")

        if events:
            print("Sample Event:", events[0]["title"])

        return events
