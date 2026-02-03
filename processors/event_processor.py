class EventProcessor:
    def process(self, raw_events):
        processed = []

        for event in raw_events:
            location = event.get("location", [])

            longitude = location[0] if len(location) > 0 else None
            latitude = location[1] if len(location) > 1 else None

            processed.append({
                "Event ID": event.get("id"),
                "Title": event.get("title"),
                "Category": event.get("category"),
                "Start Date": event.get("start"),
                "End Date": event.get("end"),
                "Country": event.get("country"),
                "Latitude": latitude,
                "Longitude": longitude,
                "Rank": event.get("rank")
            })

        return processed
