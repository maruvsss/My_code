import requests
from bs4 import BeautifulSoup

img_url = input('Your link: ')
video_url = input('Your link: ')


# response = requests.get(video_url)
# data = BeautifulSoup(response.text,"html.parser")
# print(data.find('div',class_='x5yr21d x1uhb9sk xh8yej3'))

def download_img(url=''):
    try:
        response = requests.get(url=url)
        with open("image.jpg", "wb") as file:
            file.write(response.content)
            return "IMG download c:"
    except Exception as _ex:
        return "Upps IMG dont download :c"


def download_video(url=''):
    try:
        response = requests.get(url=url)

        with open("video_1.mp4", "wb") as file:
            file.write(response.content)
            return "VIDEO download c:"
    except Exception as _ex:
        return "Upps VIDEO dont download :c"


def main():
    print(download_img(url=img_url))
    # print(download_video(url=video_url))


if __name__ == '__main__':
    main()
