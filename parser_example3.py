from bs4 import BeautifulSoup
from urllib.request import urlopen


def main():
    """ Вывод анонсированных событий с главной страницы 'https://www.python.org/' в консоль."""
    url = "https://www.python.org/"
    html = urlopen(url)
    bsObj = BeautifulSoup(html, "html.parser")
    for event in bsObj.find("div", id="content").find("div", class_="container").find(
            "div",class_="event-widget").find("ul", class_="menu").find_all("a"):
        print(event.text)


if __name__ == "__main__":
    main()