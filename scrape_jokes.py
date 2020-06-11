import csv

from bs4 import BeautifulSoup
import requests


def main():
    for i in range(0, 19841, 20):
        url = f"https://schlechtewitze.com/kurze-witze?skip={i}"
        print(f"Parsing {url}")

        response = requests.get(url)
        soup = BeautifulSoup(response.content, features="html.parser")
        jokes = soup.findAll("section", {"class": "Article__content"})

        with open('data.csv', mode='a+', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for joke in jokes:
                csv_writer.writerow([joke.get_text().encode('utf-8')])


if __name__ == "__main__":
    main()