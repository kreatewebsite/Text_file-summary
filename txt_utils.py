import os

def find_and_read_txt_files(root_dir):
    txt_files = []

    for root, d_, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".txt"):
                txt_path = os.path.join(root, file)
                with open(txt_path, 'r', encoding='utf-8') as txt_file:
                    content = txt_file.read()
                    txt_files.append((txt_path, content))

    return txt_files

def single_file(txt_path):
    
    with open(txt_path, 'r', encoding='utf-8') as txt_file:
        content = txt_file.read()
    
    return [(txt_path, content)]

     


