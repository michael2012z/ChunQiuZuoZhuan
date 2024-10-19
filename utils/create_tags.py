import os

# [BookNameEn, BookNameCn, NumOfChapters]
metaData = [
    ["01Yin", "隱", 11],
    ["02Huan", "桓", 18],
    ["03Zhuang", "莊", 32],
    ["04Min", "閔", 2],
    ["05Xi", "僖", 33],
    ["06Wen", "文", 19],
    ["07Xuan", "宣", 18],
    ["08Cheng", "成", 1],
    ["09Xiang", "襄", 31],
    ["10Zhao", "昭", 31],
    ["11Ding", "定", 15],
    ["12Ai", "哀", 27],
    ]

def main():
    input_folder_path = "../raw/"
    output_base_path = "../raw/generated/"
    os.makedirs(output_base_path, exist_ok=False)
    for book in metaData:
        BookNameEn, BookNameCn, NumOfChapters = book
        output_folder_path = output_base_path + "/" + BookNameEn
        os.makedirs(output_folder_path, exist_ok=False)
        for chapter in range(1, NumOfChapters + 1):
            input_file_path = input_folder_path + BookNameEn + "/" + BookNameEn + str(chapter).zfill(2) + ".md"
            output_file_path = output_folder_path + "/" + BookNameEn + str(chapter).zfill(2) + ".md"
            input_lines = open(input_file_path, "r").read()
            input_lines = input_lines.split("\n")
            output_lines = []
            # True if handling Jing, False if handling Zhuan
            handling_jing = False
            jing_index = 0
            zhuan_index = 0
            for line in input_lines:
                if len(line) == 0:
                    continue
                elif line[:2] == "# ":
                    output_lines.append(line)
                elif line[0] == "[":
                    output_lines.append(line)
                elif line == "## 經":
                    handling_jing = True
                    tag = " <a name=\"" + BookNameEn + str(chapter).zfill(2) + "Jing\"></a>"
                    output_lines.append(line + tag)
                elif line == "## 傳":
                    handling_jing = False
                    tag = " <a name=\"" + BookNameEn + str(chapter).zfill(2) + "Zhuan\"></a>"
                    output_lines.append(line + tag)
                else:
                    if handling_jing:
                        jing_index += 1
                        tag = "<a name=\"" + BookNameEn + str(chapter).zfill(2) + "Jing" + str(jing_index).zfill(2) + "\">[" + BookNameCn + str(chapter).zfill(2) + "經" + str(jing_index).zfill(2) + "]</a> "
                    else:
                        zhuan_index += 1
                        tag = "<a name=\"" + BookNameEn + str(chapter).zfill(2) + "Zhuan" + str(zhuan_index).zfill(2) + "\">["  + BookNameCn + str(chapter).zfill(2) + "傳" + str(zhuan_index).zfill(2) + "]</a> "
                    output_lines.append(tag + line)
                output_lines.append("\n\n")
            with open(output_file_path, "w") as output_file:
                output_file.writelines(output_lines)

if __name__ == "__main__":
    main()
