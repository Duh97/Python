import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}

r = requests.get('https://ani.gamer.com.tw/', headers=headers)
if r.status_code == 200:
    print(f'請求成功：{r.status_code}')
    
    soup = BeautifulSoup(r.text,'html.parser') #網頁原始碼傳入內建的'html.parser'解析器
    newanime_item = soup.select_one('.timeline-ver > .newanime-block')#抓一個元素
    anime_items = newanime_item.select('.newanime-date-area:not(.premium-block)')#抓全部的動畫元素

    for anime_item in anime_items:
        anime_name = anime_item.select_one('.anime-name > p').text.strip() #名稱
        print(anime_name)
        anime_watch_number = anime_item.select_one('.anime-watch-number > p').text.strip() #觀看人數
        print(anime_watch_number)
        anime_episode = anime_item.select_one('.anime-episode').text.strip()#集數
        print(anime_episode)
        anime_href = anime_item.select_one('a.anime-card-block').get('href')
        print('https://ani.gamer.com.tw/'+anime_href)

        #時間日期縮圖
        anime_date = anime_item.select_one('.anime-date-info').contents[-1].string.strip()
        anime_time = anime_item.select_one('.anime-hours').text.strip() #時間
        print(anime_date,anime_time)
        anime_img = anime_item.select_one('img.lazyload').get('src')
        print(anime_img)
        print('----------')
else:
    print(f'請求失敗：{r.status_code}')