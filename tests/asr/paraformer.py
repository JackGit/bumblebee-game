from funasr import AutoModel
# paraformer-zh is a multi-functional asr model
# use vad, punc, spk or not as you need
model = AutoModel(model="paraformer-zh",  vad_model="fsmn-vad",  punc_model="ct-punc", 
                  # spk_model="cam++", 
                  )

audio_file = '../data/demo_audio_01.wav'
audio_file = '../data/FCRS_audio.wav'


res = model.generate(input=audio_file, 
                     batch_size_s=300, 
                     sentence_timestamp=True
                    )
print(res)

res = res[0]
file_name = res['key']
sentence_info = res['sentence_info'] # { text, timestamp[] }
sentences = []

for i in range(len(sentence_info)):
    text = sentence_info[i]['text']
    timestamp = sentence_info[i]['timestamp']
    start = timestamp[0][0]
    end = timestamp[len(timestamp) - 1][1]
    sentences.append({
        'text': text,
        'start': start,
        'end': end,
        'file': file_name
    })

# sentences into json string
import json
text_content = json.dumps(sentences, ensure_ascii=False)

# 将拼接后的字符串保存到txt文件中
with open('output_FCRS_sentences.js', 'w', encoding='utf-8') as file:
    file.write(text_content)