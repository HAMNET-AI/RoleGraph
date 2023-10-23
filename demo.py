import os
from langchain.llms import OpenAI
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
os.environ["OPENAI_API_KEY"] = "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"
import csv

def kg_generate():
    llm = OpenAI(temperature=0.1)
    filepath = "F:\data\hamnet//The Gift of the Magi.txt"
    with open(filepath, 'r', encoding='utf-8') as file:
        # 读取文件内容
        text = file.read()
    content = "你现在需要概括一本小说中人物的关系，定义的关系三元组有'头实体-关系-尾实体'\n要求：1、输出格式表示为头实体-关系-尾实体;2、输出的每个结果用换行符分割;3.尽可能抽取两个人物之间的关系；4.抽取7个关系\n" + f"文本：{text}"
    s = llm(prompt=content)
    print(s)
    lines = s.split('\n')
    # 创建CSV文件并写入数据
    with open('relations.csv', 'w', newline='') as csvfile:
    # 定义CSV表头
    fieldnames = ['头实体', '关系', '尾实体']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 写入表头
    writer.writeheader()
    # 解析文本并写入CSV文件
    for line in lines:
        parts = line.split('-')
        if len(parts) == 3:
            writer.writerow({'头实体': parts[0], '关系': parts[1], '尾实体': parts[2]})
