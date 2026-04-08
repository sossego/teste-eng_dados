from playwright.sync_api import sync_playwright
import pandas as pd
import json
import time

def download_csv():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.datablist.com/learn/csv/download-sample-csv-files")

        time.sleep(5)
        
        with page.expect_download() as download_info:
            page.get_by_text("products-1000.csv").click()
        download = download_info.value
        
        download.save_as("products.csv")

        browser.close()
        return "products.csv"


def process_csv(csv_file):
    df = pd.read_csv(csv_file)
    
    filtered = df[df["Category"] == "Automotive"]

    filtered.sort_values(by="Price", ascending=False, inplace=True)
    top5 = filtered.head(5)

    result = top5.to_dict(orient="records")
    return result


def save_json(data):
    with open("output.json", "w") as f:
        json.dump(data, f, ensure_ascii=True)


def main():
    csv_file = download_csv()
    data = process_csv(csv_file)
    save_json(data)
    
    print("Concluído")


if __name__ == "__main__":
    main()
