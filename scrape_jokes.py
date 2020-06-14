from bs4 import BeautifulSoup
import requests


def main():
    for i in range(0, 19841, 20):
        url = f"https://schlechtewitze.com/kurze-witze?skip={i}"
        print(f"Parsing {url}")

        response = requests.get(url)
        soup = BeautifulSoup(response.content, features="html.parser")
        jokes = soup.findAll("section", {"class": "Article__content"})

        with open('joke_sentences.txt', 'a') as txt_file:
            for joke in jokes:
                joke_text = joke.get_text()
                joke_text = joke_text.replace("\n", " ")
                txt_file.write(joke_text + '\n')


if __name__ == "__main__":
    main()