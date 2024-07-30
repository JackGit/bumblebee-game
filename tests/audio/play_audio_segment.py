from pydub import AudioSegment
import simpleaudio as sa

def play_audio_segment(audio_file, start_time, end_time):
    # 读取音频文件
    audio = AudioSegment.from_file(audio_file)
    
    # 将时间转换为毫秒
    start_ms = start_time
    end_ms = end_time
    
    # 提取指定时间段的音频
    segment = audio[start_ms:end_ms]
    
    # 播放提取的音频段
    play_obj = sa.play_buffer(segment.raw_data, 
                              num_channels=segment.channels,
                              bytes_per_sample=segment.sample_width, 
                              sample_rate=segment.frame_rate)
    play_obj.wait_done()


if __name__ == "__main__":
  # 示例使用
  audio_file = "../data/demo_audio_01.wav"
  start_time = 3030 
  end_time = 4650 

  audio_file = "../data/FCRS_audio.wav"
  start_time = 460270
  end_time = 463110

  play_audio_segment(audio_file, start_time, end_time)
