from bs4 import BeautifulSoup

import csv
import urllib.request
import time


def scrape(writer, url, word, word_class_name):
    try:
        with urllib.request.urlopen(f'{url}{word}') as f:
            html_doc = f.read().decode()
            soup = BeautifulSoup(html_doc, 'html.parser')
            nodesList = soup.find("span", class_ = word_class_name)
            if(nodesList is not None):
                meanings = [ node.string for node in nodesList ]
                print(f"meaning: {meanings}")
                for meaning in meanings:
                    print("writing...")
                    writer.writerow({ "word" : word, "meaning": meaning})
            else:
                print(f"similar: ABSENT")
                writer.writerow({ "word" : word, "meaning": "ABSENT"})
    except:
        print(f"similar: ABSENT #NOTHINGNESS")
        writer.writerow({ "word" : word, "meaning": "ABSENT"})

def main():
    fw = open('final-words-meaning-2.csv', 'w+', newline='')
    fieldnames = ['word', 'meaning']
    with open('final-gre-words-2.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        url = "https://en.oxforddictionaries.com/definition/"
        word_class_name = "ind"
        writer = csv.DictWriter(fw, fieldnames=fieldnames)
        writer.writeheader()
        reader_length = 1134
        for row in reader:
            percentDone = (reader.line_num - 2) / reader_length
            print(f'{reader.line_num - 1}/{reader_length} | {round(percentDone*100, 4)} % DONE' )
            word = row['word']
            print(f"word: {word}")
            scrape(writer, url, word, word_class_name)
    fw.close()

if __name__ == "__main__":
    main()
