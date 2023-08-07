import zipfile
from collections import Counter
import os
import shutil



M1 = {'a', 'e', 'i', 'o', 'u', 'y'}
M2 = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'w', 'x', 'z'}
src_directory = 'task01_2'
dest_directory = 'files'


def copy_txt_files(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith('.txt'):
                src_path = os.path.join(root, file)
                dest_path = os.path.join(dest_dir, file)
                shutil.copy2(src_path, dest_path)  

def count_files(files):

    count_matching_files = 0

    for file_name in files:

        with open(f"files/{file_name}", "r",) as file:
            content = file.read()
            print(content)
            
            content = content.lower()  
            char_count = Counter(content)
            
            
            m1_count = sum(char_count[char] for char in M1)
            m2_count = sum(char_count[char] for char in M2)
            
            
            if m1_count == m2_count:
                count_matching_files += 1
    
    return count_matching_files


if __name__ == '__main__':

    copy_txt_files(src_directory, dest_directory)
    files = os.listdir(dest_directory)
    count = count_files(files=files)
    print(count)
    


