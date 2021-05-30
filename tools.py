import re
import json
import os
from tqdm import tqdm

json_file = "rem.json"
files_path = './1/files/'
# files_path = './files/'
# root = r'C:\Users\Lenovo\remnote\xxx\files'

with open(json_file,'rb') as load_f:
    load_dict = json.load(load_f)

def write_list_to_txt(list,filename):
    f = open(filename, "w")
    for line in list:
        f.write(line + '\n')
    f.close()
def find_repeat(lst):
    set_lst = set(lst)
    # set会生成一个元素无序且不重复的可迭代对象，也就是我们常说的去重
    if len(set_lst) == len(lst):
        print('列表里的元素互不重复！')
    else:
        print('列表里有重复的元素！')
def del_file_list(root,file_list):
    import os
    for file_name in tqdm(file_list):
        try:
            # print(root + file_name)
            os.remove(root + file_name)
        except:
            pass
    print('完成!!')


def run():
    str = load_dict.__str__()
    p = re.compile("%LOCAL")

    file_list_json = []
    file_list_dir = os.listdir(files_path)
    i = 0
    for m in p.finditer(str):
        i = i + 1
        step = 12
        file_name = str[m.start()+ step : m.start() + step + 128 + 4]
        file_list_json.append(file_name)

    file_not_in_Remnote= []
    for file_name_dir in file_list_dir:
        if file_name_dir not in file_list_json:
            file_not_in_Remnote.append(file_name_dir)
            # print(file_name_dir)
    print('RemNote的files文件夹中一共有{}张图片'.format(len(file_list_dir)) )
    print('RemNote的json文件实际使用到了{}张图片'.format(len(file_list_json)))
    print('RemNote的files文件夹中一共有{}张未使用的图片'.format(len(file_not_in_Remnote)))

    write_list_to_txt(file_not_in_Remnote,'file_not_in_Remnote.txt')
    return file_not_in_Remnote

if __name__ == '__main__':
    run()