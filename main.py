from bs4 import BeautifulSoup
import requests
import settings
import csv


def parse_content(content):
    soup = BeautifulSoup(content, "html.parser")
    boxes = soup.findAll('article', class_="box")
    page = []

    # print(boxes)

    if boxes:
        with open('source'+'.txt', 'w', encoding='utf-8') as f:
            f.write(str(boxes))

    for box in boxes:
        if not box.find('a', class_="article-link"):
            if not box.find('h4', class_="top-posts__header"):
                return page

        if box.find('h4', class_="top-posts__header"):
            continue
        else:
            data = {

            'link': box.find('a', class_="article-link").attrs['href'],
            'title': box.find('h2', class_="entry-title").get_text(strip=True),
            'text': box.find('div', class_='entry-content').get_text(strip=True),

        }
        page.append(data)
    return page


def save_to_csv(file_path, data):
    with open(file_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(
            file,
            skipinitialspace=True,
            fieldnames=['link', 'title', 'text'],
            quoting=csv.QUOTE_MINIMAL,
            delimiter=',',


        )

        writer.writeheader()
        for elem in data:
            writer.writerow(elem)


def parse_request(tag_name, page_number, data=None):
    url = settings.BASE_URL.format(tag=tag_name, page_number=page_number)
    response = requests.get(url)

    page = parse_content(response.content)

    if page:
        data.extend(page)
        parse_request(tag_name, page_number+1, data)
    else:
        print(data)
        print(len(data))
        save_to_csv(tag_name + ".csv", data)








if __name__ == "__main__":
    for name in settings.PAGES_NAMES:


        parse_request(name, 1, [])
