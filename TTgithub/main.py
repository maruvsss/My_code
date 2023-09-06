from tiktok_scraper import TikTokScraper

# URL видео с TikTok
video_url = "https://www.tiktok.com/@username/video/1234567890123456789"

# Создайте экземпляр TikTokScraper
scraper = TikTokScraper()

# Получите информацию о видео
video_info = scraper.get_tiktok_by_url(video_url)

if video_info:
    # URL видео без водяного знака
    download_url = video_info["video_url"]

    # Скачайте видео
    import requests
    response = requests.get(download_url)

    if response.status_code == 200:
        with open("downloaded_video.mp4", "wb") as video_file:
            video_file.write(response.content)
        print("Видео успешно скачано и сохранено в файле 'downloaded_video.mp4'")
    else:
        print("Ошибка при скачивании видео.")
else:
    print("Не удалось получить информацию о видео.")
