import requests
from tqdm import tqdm
import os

def download_video(url, save_path):
    try:
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))

        if total_size == 0:
            print("The file does not exist or the URL is incorrect.")
            return

        with open(save_path, 'wb') as file, tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading") as progress_bar:
            for data in response.iter_content(chunk_size=1024*1024):  # 1MB per chunk
                file.write(data)
                progress_bar.update(len(data))

        print("Download completed!")
    except requests.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# 获取用户输入的URL
video_url = input("Please enter the video URL: ")

# 设置保存目录和文件名
save_directory = os.path.join("Video")
os.makedirs(save_directory, exist_ok=True)
save_path = os.path.join(save_directory, "video.mp4")

# 调用函数下载视频
download_video(video_url, save_path)
