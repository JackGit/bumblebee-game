from funasr import AutoModel
# paraformer-zh is a multi-functional asr model
# use vad, punc, spk or not as you need
model = AutoModel(model="paraformer-zh",  vad_model="fsmn-vad",  punc_model="ct-punc", 
                  # spk_model="cam++", 
                  )
res = model.generate(input=f"../data/demo_audio_01.wav", 
                     batch_size_s=300, 
                     hotword='魔搭',
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
        'end': end
    })

# sentences into json string
import json
text_content = json.dumps(sentences, ensure_ascii=False)

# 将拼接后的字符串保存到txt文件中
with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(text_content)