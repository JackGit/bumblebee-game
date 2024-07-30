from pydub import AudioSegment
import simpleaudio as sa

def play_audio_segment(audio_file, start_time, end_time):
    # 读取音频文件
    audio = AudioSegment.from_file(audio_file)
    
    # 将时间转换为毫秒
    start_ms = start_time * 1000
    end_ms = end_time * 1000
    
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
  start_time = 3030/1000  # 开始时间，单位为秒, sentence_info[i].timestamp[0][0]
  end_time = 4650/1000   # 结束时间，单位为秒, sentence_info[i].timestamp[n][1]

  play_audio_segment(audio_file, start_time, end_time)
