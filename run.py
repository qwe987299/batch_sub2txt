import os
import re

# 設定讀取和輸出的目錄
src_dir = 'src'
build_dir = 'build'

# 批次讀取 src 目錄下的 .srt 檔案
for filename in os.listdir(src_dir):
    if filename.endswith('.srt'):
        # 讀取檔案
        with open(os.path.join(src_dir, filename), 'r', encoding='utf-16 le') as f:
            text = f.read()

        # 使用正規表達式進行批次尋找取代的動作
        text = re.sub(r'\s\n[0-9][0-9][0-9]', '', text)
        text = re.sub(r'\s\n[0-9][0-9]', '', text)
        text = re.sub(r'\s\n[0-9]', '', text)
        text = re.sub(r',[0-9][0-9][0-9] --> .*\n', ' ', text)
        text = re.sub(r',[0-9][0-9] --> .*\n', ' ', text)
        text = re.sub(r',[0-9] --> .*\n', ' ', text)

        # 刪除第一行
        text = text.split('\n', 1)[1]

        # 新增第一行
        text = '00:00:00 片頭\n' + text

        # 將結果寫入新檔案
        output_filename = os.path.splitext(filename)[0] + '.txt'
        output_path = os.path.join(build_dir, output_filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(text)

        # 將結果輸出到終端機
        with open(output_path, 'r', encoding='utf-8') as f:
            output_text = f.read()
            print(f'======== {output_filename} ========')
            print(output_text)
