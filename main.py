import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import sys

def get_csv_sheets_from_google_sheet(sheet_url: str, output_dir: str) -> None:
    scope = [
        'https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive'
    ]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        './elite-list-436513-i7-ee09acefeee5.json', 
        scope
    )
    client = gspread.authorize(creds)

    sheet = client.open_by_url(sheet_url)

    for worksheet in sheet.worksheets():
        data = worksheet.get_all_values()
        df = pd.DataFrame(data[1:], columns=data[0])
        csv_file = f"{output_dir}/{worksheet.title}.csv"
        df.to_csv(csv_file, index=False)
        print(f"Converted '{worksheet.title}' to '{csv_file}'")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py <sheet_url>")
        sys.exit(1)

    sheet_url = sys.argv[1]
    output_dir = './'
    get_csv_sheets_from_google_sheet(sheet_url, output_dir)
