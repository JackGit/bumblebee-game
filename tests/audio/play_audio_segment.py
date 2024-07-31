from pydub import AudioSegment
import simpleaudio as sa
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np


def play_audio_segment(audio_file, start_time, end_time):
    # 读取音频文件
    audio = AudioSegment.from_file(audio_file)
    
    # 将时间转换为毫秒
    start_ms = start_time
    end_ms = end_time
    
    # 提取指定时间段的音频
    segment = audio[start_ms:end_ms]

    # 将音频数据转换为 NumPy 数组
    samples = np.array(segment.get_array_of_samples())
    
    # 标准化音频数据
    samples = samples / np.max(np.abs(samples))
    
    # 设置播放参数
    num_channels = segment.channels
    sample_rate = segment.frame_rate
    bytes_per_sample = segment.sample_width
    
    # 播放音频
    play_obj = sa.play_buffer(segment.raw_data, num_channels=num_channels,
                              bytes_per_sample=bytes_per_sample,
                              sample_rate=sample_rate)
    

    # 实时显示波形图
    fig, ax = plt.subplots()
    x = np.linspace(0, len(samples) / sample_rate, num=len(samples))
    line, = ax.plot(x, samples)
    ax.set_xlim(0, len(samples) / sample_rate)
    ax.set_ylim(-1, 1)
    
    def update(frame):
        # 计算当前播放位置
        current_sample = int(frame * sample_rate / 30)  # 假设每秒 30 帧
        if current_sample < len(samples):
            line.set_ydata(samples[current_sample:current_sample + len(samples) // 30])
        return line,
    
    ani = FuncAnimation(fig, update, frames=np.arange(0, len(samples) // sample_rate * 30),
                        blit=True, interval=1000 / 30)
    
    plt.show()


    play_obj.wait_done()


if __name__ == "__main__":
  # 示例使用
  audio_file = "../data/FCRS_audio.wav"
  start_time = 460270
  end_time = 463110

  audio_file = "../data/demo_audio_01.wav"
  start_time = 3030 
  end_time = 4650 

  play_audio_segment(audio_file, start_time, end_time)
