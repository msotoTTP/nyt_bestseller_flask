from bs4 import BeautifulSoup
import requests

def getBestsellersForDate(date):
    year = date.year
    month = str(date.month).zfill(2)
    day = str(date.day).zfill(2)

    url = f"https://www.nytimes.com/books/best-sellers/{year}/{month}/{day}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    bookTitles = [bookElement.text for bookElement in soup.find_all("h3", itemprop="name")]
    authors = [authorElement.text for authorElement in soup.find_all(itemprop="author")]
    descriptions = [descriptionElement.text for descriptionElement in soup.find_all(itemprop="description")]
    categories = [categoryElement.text for categoryElement in soup.find_all(class_="css-nzgijy")]

    bestsellers = []
    for i, category in enumerate(categories):
        books = []
        for j in range(5*i, 5*(i+1)):
            title = bookTitles[j]
            author = authors[j]
            description = descriptions[j]
            book = {"title": title, "author": author, "description": description}
            books.append(book)
        bestsellers.append({"category": category, "books": books})
        
    return bestsellers
