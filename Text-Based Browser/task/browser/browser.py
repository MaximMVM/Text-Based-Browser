import os
import sys
import work_w_http


# write your code here
if len(sys.argv) > 1:
    name_dir = sys.argv[1]
else:
    name_dir = "dir"


def make_path(name_dir, name):
    page_path = './' + name_dir + '/' + name.replace('.com', '')
    return page_path


def create_file(name_dir, url, content):
    file_name = url.replace('.com', '')
    if not os.path.exists(name_dir):
        os.mkdir(name_dir)
    with open("./" + name_dir + '/' + file_name, 'w') as f:
        f.write(content)


def check_file(name_dir, name_file):
    file_path = make_path(name_dir, name_file)
    return os.path.exists(file_path)


def read_file(dir_name, url):
    page_path = make_path(dir_name, url)
    with open(page_path, 'r') as f:
        return f.read()


def save_and_print(name_dir, url):
    if check_file(name_dir, url):
        text = read_file(name_dir, url)
        print(text)
    else:
        content = work_w_http.parse_and_print(url)
        print(content)
        create_file(name_dir, url, content)


my_stack = []


def history(dir_name):
    url = my_stack.pop(0)
    return read_file(dir_name, url)


while True:
    url = input()
    if url == "back":
        if len(my_stack) > 0:
            print(history(name_dir))
        else:
            continue
    elif '.' in url:
        save_and_print(name_dir, url)
        my_stack.append(url)
    elif url == "exit":
        break
    else:
        print("Error: Unknown url")
