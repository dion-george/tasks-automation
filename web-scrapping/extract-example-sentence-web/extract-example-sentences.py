from bs4 import BeautifulSoup

import csv
import urllib.request
import time


def scrape(writer, url, word, word_class_name):
    try:
        with urllib.request.urlopen(f'{url}{word}') as f:
            html_doc = f.read().decode()
            soup = BeautifulSoup(html_doc, 'html.parser')
            nodesList = soup.find("div", class_ = word_class_name)
            if(nodesList is not None):
                similarWords = [ node.string for node in nodesList ]
                print(f"similar: {similarWords}")
                for similarWord in similarWords:
                    print("writing...")
                    writer.writerow({ "word" : word, "similar": similarWord })
            else:
                print(f"similar: ABSENT")
                writer.writerow({ "word" : word, "similar": "ABSENT" })
    except:
        print(f"similar: ABSENT #NOTHINGNESS")
        writer.writerow({ "word" : word, "similar": "ABSENT" })

def main():
    fw = open('words-sentences.csv', 'w+', newline='')
    fieldnames = ['word', 'similar']
    with open('words.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        url = "https://sentence.yourdictionary.com/"
        word_class_name = "li_content"
        writer = csv.DictWriter(fw, fieldnames=fieldnames)
        writer.writeheader()
        reader_length = 630
        for row in reader:
            percentDone = (reader.line_num - 2) / reader_length
            print(f'{reader.line_num - 1}/{reader_length} | {round(percentDone*100, 4)} % DONE' )
            word = row['word']
            print(f"word: {word}")
            scrape(writer, url, word, word_class_name)
    fw.close()

if __name__ == "__main__":
    main()
