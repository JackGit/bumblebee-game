from moviepy.editor import *
import os

# 指定目标文件夹
video_folder = "../data"
audio_folder = "../data"

# 遍历目标文件夹中的所有文件
for filename in os.listdir(video_folder)[:2]:
    # 检查文件是否以 .mp4 结尾
    if filename.endswith(".mp4"):
        # 加载视频文件
        video_path = os.path.join(video_folder, filename)
        video = VideoFileClip(video_path)

        # 提取音频
        audio = video.audio

        # 构建音频文件的输出路径，替换扩展名为 .wav
        audio_filename = filename.replace(".mp4", "_audio.wav")
        audio_output_path = os.path.join(audio_folder, audio_filename)

        # 保存音频文件
        audio.write_audiofile(audio_output_path)

        # 关闭视频文件，释放资源
        video.close()