import os
from funasr import AutoModel

model = AutoModel(model="paraformer-zh", model_revision="v2.0.4",
                  vad_model="fsmn-vad", vad_model_revision="v2.0.4",
                  punc_model="ct-punc-c", punc_model_revision="v2.0.4")

input_dir = "../extract-audios/audios"
output_dir = "./txt"

for file_name in os.listdir(input_dir):
    if file_name.endswith(".wav"):
        input_path = os.path.join(input_dir, file_name)
        output_path = os.path.join(output_dir, os.path.splitext(file_name)[0] + ".txt")
        
        if os.path.exists(output_path):
            continue
        
        res = model.generate(input_path, batch_size_s=300)
        text_content = ''.join([item['text'] for item in res])

        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(text_content)