import requests

img_url = "https://pancakeswap.finance/_next/image?url=%2Fimages%2Fdecorations%2F3d-pan-bunny.png&w=384&q=75"
video_url = "https://p16-sign-va.tiktokcdn.com/tos-maliva-p-0068/2225608ee65742489313ce8e727a04b3_1691162906~tplv-f5insbecw7-1:480:480.jpeg?x-expires=1692853200&x-signature=pgoWQR5RfzordBrmiaMJCQ6mro0%3D"
def download_img(url=''):
    try:
        response = requests.get(url=url)

        with open("image.jpg","wb") as file:
            file.write(response.content)
            return "IMG download c:"
    except Exception as _ex:
        return "Upps IMG dont download :c"


def download_video(url=''):
    try:
        response = requests.get(url=url)

        with open("video_1.mp4","wb") as file:
            file.write(response.content)
            return "VIDEO download c:"
    except Exception as _ex:
        return "Upps VIDEO dont download :c"

def main():
    # print(download_img(url=img_url))
    print(download_video(url=video_url))

if __name__ == '__main__':
    main()