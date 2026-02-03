import pandas as pd
import os

class ExcelStorage:
    def __init__(self, file_path):
        self.file_path = os.path.abspath(file_path)
        os.makedirs(os.path.dirname(self.file_path), exist_ok=True)

    def save(self, events):
        if not events:
            print("No events to save.")
            return

        df = pd.DataFrame(events)

        with pd.ExcelWriter(
            self.file_path,
            engine="openpyxl",
            mode="w"
        ) as writer:
            df.to_excel(writer, index=False, sheet_name="Events")

        print(f"Saved {len(events)} events to {self.file_path}")

        # ✅ Auto-open Excel safely (Windows)
        self.open_excel()

    def open_excel(self):
        try:
            os.startfile(self.file_path)  # 🔥 correct Windows method
            print("Excel file opened automatically.")
        except Exception as e:
            print("Could not auto-open Excel:", e)
