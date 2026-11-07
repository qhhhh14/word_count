# 打开 sample.txt 文件，读取全部内容
with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 把文本全部变成小写，这样 Hello 和 hello 会被算成同一个词
text = text.lower()

# 按空格把文本切分成一个个单词
words = text.split()

# 创建一个空字典，用来存“单词 → 出现次数”
counts = {}

# 遍历每一个单词
for word in words:
    if word in counts:
        counts[word] = counts[word] + 1  # 已经出现过，次数加1
    else:
        counts[word] = 1                 # 第一次出现，次数设为1

# 按出现次数从高到低排序，然后打印
with open("result.txt", "w", encoding="utf-8") as f:
    for word, count in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        f.write(f"{word}: {count}\n")