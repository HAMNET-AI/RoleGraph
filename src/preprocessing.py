import re
class Chapter:
    def __init__(self, title, content):
        self.title = title
        self.content = content

def split_text_into_chapters(file_path):
    # 读取文本文件
    with open(file_path, 'r', encoding='utf-16') as file:
        content = file.read()

    # 定义匹配章节标题的正则表达式（匹配形如"第十一章"的中文标题）
    chapter_pattern = re.compile(r'第[一二三四五六七八九十百千万\d]+章', re.MULTILINE)

    # 使用正则表达式进行章节分割
    chapters = re.split(chapter_pattern, content)[1:]  # [1:]用于去掉第一个空字符串元素

    # 将匹配到的章节标题和内容对应起来
    chapter_titles = re.findall(chapter_pattern, content)

    # 处理最后一个章节的内容
    last_chapter_content = chapters[-1]
    if last_chapter_content.strip() == '':
        chapters = chapters[:-1]  # 去掉最后一个空内容的章节
        chapter_titles = chapter_titles[:-1]  # 去掉对应的章节标题

    # 创建Chapter对象的列表，将章节标题和内容存储为Chapter对象的成员变量
    chapter_objects = []
    for i in range(len(chapter_titles)):
        title = chapter_titles[i].strip()
        content = chapters[i].strip()
        chapter = Chapter(title, content)
        chapter_objects.append(chapter)

    return chapter_objects

def split_text_into_sections(content, section_length):
    sections = []
    current_section = ""
    words = content.split()  # 将章节内容按照空格分割成单词

    for word in words:
        if len(current_section) + len(word) + 1 <= section_length:  # 加1是为了考虑单词之间的空格
            if current_section:
                current_section += " "
            current_section += word
        else:
            sections.append(current_section)
            current_section = word

    if current_section:
        sections.append(current_section)

    return sections