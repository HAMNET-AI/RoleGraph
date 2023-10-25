from src.preprocessing import split_text_into_chapters,split_text_into_sections
import os
from langchain.llms import OpenAI
os.environ["http_proxy"] = "http://127.0.0.1:7890"
os.environ["https_proxy"] = "http://127.0.0.1:7890"
os.environ["OPENAI_API_KEY"] = "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"
import csv

if __name__ == '__main__':
    file_path = r'F:\code\python\RoleGragh\novel\Animal-Farm.txt'
    chapters = split_text_into_chapters(file_path=file_path)
    llm = OpenAI(temperature=0.1)
    chunks = split_text_into_sections(content=chapters[0].content,section_length=1500)
    #for chapter in chapters:
    print(chunks[0])
    content = "你是一名文学鉴赏家\n 你现在需要判断出一本小说中某段章节的主要角色 \n 要求：1、输出格式表示为角色名或者角色名-身份;2、输出的每个结果用换行符分割;3角色名必须是在小说里出现；\n" + f"小说：{chunks[0]}"
    s = llm(prompt=content)

    print(s)

