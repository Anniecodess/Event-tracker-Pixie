import json
from scrapers.platform_scraper import PlatformScraper
from processors.event_processor import EventProcessor
from storage.excel_storage import ExcelStorage


def load_config():
    with open("config/config.json", "r", encoding="utf-8") as f:
        return json.load(f)


def main():
    # Load configuration
    config = load_config()

    # ✅ User selects city
    city = input("Enter city name (e.g., Mumbai, Delhi, Bangalore): ").strip()

    if not city:
        print("City cannot be empty. Exiting...")
        return

    # Inject city into config at runtime
    config["predicthq"]["city"] = city

    print(f"\nFetching events for city: {city}")

    # Initialize components
    scraper = PlatformScraper(config)
    processor = EventProcessor()
    storage = ExcelStorage("data/events.xlsx")

    # Fetch → Process → Store
    raw_events = scraper.fetch_events()
    processed_events = processor.process(raw_events)
    storage.save(processed_events)

    print("\nFINAL RESULT")
    print(f"Total events stored for {city}: {len(processed_events)}")


if __name__ == "__main__":
    main()
