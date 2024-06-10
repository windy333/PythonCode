from tkinter import *
from tkinter import ttk
import requests
import jsonpath
import os
from urllib.request import urlretrieve
from threading import Thread

'''网易云音乐下载后无法播放,所以隐藏了网易云的按钮'''

def song_download(download_url, title, author):
    """下载歌曲到本地目录"""
    os.makedirs("music", exist_ok=True)
    path = os.path.join('music', '{} - {}.mp3'.format(title, author))
    update_text('歌曲: {}-{}, 正在下载...'.format(title, author))
    try:
        urlretrieve(download_url, path)
        update_text('下载完毕, {}-{}, 请试听'.format(title, author))
    except Exception as e:
        update_text('下载失败, {}-{}, 错误: {}'.format(title, author, e))

def get_music_name():
    """搜索歌曲名称并下载"""
    name = entry_song.get()
    artist = entry_artist.get()
    platform = var.get()
    #调用的一个网站
    url = 'https://music.liuzhijin.cn/'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest",
    }
    params = {
        "input": name,
        "filter": "name",
        "type": platform,
        "page": 1,
    }
    try:
        response = requests.post(url=url, data=params, headers=headers)
        json_text = response.json()
        title = jsonpath.jsonpath(json_text, '$..title')
        author = jsonpath.jsonpath(json_text, '$..author')
        download_url = jsonpath.jsonpath(json_text, '$..url')
        if title and author and download_url:
            # Filter by artist if specified
            if artist:
                for i in range(len(author)):
                    if artist.lower() in author[i].lower():
                        song_download(download_url[i], title[i], author[i])
                        return
                update_text('未找到指定歌手的歌曲')
            else:
                song_download(download_url[0], title[0], author[0])
        else:
            update_text('未找到歌曲信息')
    except Exception as e:
        update_text('请求失败, 错误: {}'.format(e))

def start_search_thread():
    """启动搜索线程"""
    Thread(target=get_music_name).start()

def update_text(message):
    """更新文本框内容"""
    text.insert(END, message)
    text.see(END)
    text.update()

def setup_gui():
    """设置GUI界面"""
    root = Tk()
    root.title('全网音乐下载器')
    root.geometry('600x480+400+200')

    style = ttk.Style()
    style.theme_use('default')

    label_song = ttk.Label(root, text="歌曲名:", font=('楷体', 16))
    label_song.grid(row=0, column=0, padx=10, pady=10, sticky=E)

    global entry_song
    entry_song = ttk.Entry(root, font=('宋体', 16), width=25)
    entry_song.grid(row=0, column=1, padx=10, pady=10)

    label_artist = ttk.Label(root, text="歌手名:", font=('楷体', 16))
    label_artist.grid(row=1, column=0, padx=10, pady=10, sticky=E)

    global entry_artist
    entry_artist = ttk.Entry(root, font=('宋体', 16), width=25)
    entry_artist.grid(row=1, column=1, padx=10, pady=10)

    global var
    var = StringVar()
    #r1 = ttk.Radiobutton(root, text='网易云', variable=var, value='netease')
    #r1.grid(row=2, column=0, padx=10, pady=5)
    r2 = ttk.Radiobutton(root, text='QQ音乐', variable=var, value='qq')
    r2.grid(row=2, column=1, padx=10, pady=5)

    global text
    text = Listbox(root, font=('楷体', 14), width=50, height=10)
    text.grid(row=3, columnspan=2, padx=10, pady=10)

    button1 = ttk.Button(root, text='开始下载', command=start_search_thread)
    button1.grid(row=4, column=0, padx=10, pady=10)

    button2 = ttk.Button(root, text='退出程序', command=root.quit)
    button2.grid(row=4, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    setup_gui()
