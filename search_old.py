
import os 
import time
while True:
    def get_file_list(directory):
        file_list = os.listdir(directory)
        files_only = [f for f in file_list if os.path.isfile(os.path.join(directory, f))]
        return files_only
    def Search_words(word ,directory,file_list , context_size=3):
        start_time = time.time() 
        found = False  # متغیر برای نشان دادن وجود یا عدم وجود کلمه
        for file in file_list:
            file_path = os.path.join(directory, file)
            with open(file_path, "r") as f:
                content = f.read().lower()  
                lines = content.splitlines()
                for i, line in enumerate(lines):
                    words = line.split()  # تقسیم خط به کلمات
                    for j, w in enumerate(words):
                        if word.lower() == w:
                            # تعیین محدوده‌ی شروع و پایان برای نمایش کلمات قبل و بعد
                            start_index = max(j - context_size, 0)
                            end_index = min(j + context_size + 1, len(words))
                            context = ' '.join(words[start_index:end_index])
                            print(f"Found '{word}' in '{file}' at line {i + 1}: {context}")
        if not found:
            print(f"'{word}' not found in any file.")
        end_time = time.time()  # زمان پایان اجرا
        execution_time = end_time - start_time  # زمان اجرا
        print(f"Search time: {execution_time:.2f} seconds")
    directory ='data\dickens'
    file_list = get_file_list(directory)
    WORD = input("Enter the word to search: ")
    # os.system('cls')    
    word = WORD.lower()
    Search_words(word, directory,file_list , )