import os

folders = [
    "01Yin",
    "02Huan",
    "03Zhuang",
    "04Min",
    "05Xi",
    "06Wen",
    "07Xuan",
    "08Cheng",
    "09Xiang",
    "10Zhao",
    "11Ding",
    "12Ai",
    ]

def main():

    path = "../raw/generated/"
    os.makedirs(path, exist_ok=False)

    for folder in folders:
        folder_path = path + folder
        os.makedirs(folder_path, exist_ok=False)

    print("Folders created: ", folders)


    generated_folder_index = -1
    generated_file_index = 0
    all_file_index = 0
    with open("../raw/all.md", "r") as all_file:
        for line in all_file:
            all_file_index += 1
            line = line.strip()
            
            if len(line) == 0:
                continue
            
            if len(line) < 2:
                print("Error in parsing line [" + str(all_file_index) + "]: " + line)
                return

            if line == "----":
                generated_folder_index += 1
                generated_folder_path = path + folders[generated_folder_index] + "/"
                generated_file_index = 0
            elif line[:2] == "# ":
                generated_file_index += 1
                generated_file_path = generated_folder_path + folders[generated_folder_index] + str(generated_file_index).zfill(2) + ".md"
                generated_file = open(generated_file_path, "w")
                generated_file.write(line + "\n")
            else:
                generated_file.write(line + "\n\n")





if __name__ == "__main__":
    main()
