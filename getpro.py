# -*- coding: utf-8 -*-


import requests
import json
from pprint import pprint
# GitHub 用户名
username = "rstg00po54"

mdfile = "github_repos.md"




def check_string_in_md(file_path, target_string):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()  # 读取文件内容
            if target_string in content:  # 检查目标字符串是否存在
                print(f"'{target_string}' found in the file.")
            else:
                print(f"'{target_string}' not found in the file.")
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

render = [
    "Atrc",
    "Hana-SoftwareRenderer",
    "PhysicallyBasedRenderer",
    "nori",
    "SDEngine",
    "thegibook",
    "TinySoftRenderer",
]
web = [
    "gatsby",
    "hexo",
    "W3C-CHM",
    "w3cschool",
    "booktools",
    "css-js-animation",
    "Raym0nade",
    "webDev-animate",
]

book = [
    "hbook",
    "modern-cpp-tutorial",
    "my-node-ejs-app",
    "fullstack-hy2020.github.io",
    "Web",
    "react-naive-book",
    "openglbook",
]

games = [
    "GAMES202",
    "Games202-OpenGL",
    "GAMES_101_202_Homework",
]

mcu = [
    "cleanflight",
    "Deng-s-foc-controller",
    "ODriveHardware",
    "Helix_Mp3",
]

cpu = [
    "AZPRcpu",
    "CPU",
    "e200_opensource",
    "Examples-in-book-write-your-own-cpu",
]
dx11 = [
    
    "DirectX-Graphics-Samples",
    "DirectX11-With-Windows-SDK",
    "DirectX11-With-Windows-SDK-Book",
]
graph = [
    "movy",
    "imgui",
    "threepp",
    "tinygl",
    "opengltest",
]
encode = [
    "h264_video_decoder_demo",
]



other = [
    "FFmpegTest1",
    "index",
    "cocos2d",
]

lists = {
    "render": render,
    "web": web,
    "book": book,
    "games": games,
    "mcu": mcu,
    "cpu": cpu,
    "dx11": dx11,
    "graph": graph,
    "encode": encode,
    "other": other

}
class Category:
    cls = []
    content = {}
    name = ""
    # 构造函数，初始化属性
    def __init__(self, name, cls):
        self.cls = cls
        self.name = name

cate = Category("render", render)

cates = {}


# 遍历字典的键值对
for key, value in lists.items():
    # print('--------------')
    print(f"Key: {key}, Value: {value}")
    if "index" in value:
        print("is in")
    for v in value:
        print(v)

def check_string_in_lists(target_string, lists):
    found = False
    for category, category_list in lists.items():
        if target_string in category_list:
            # print(f"'{target_string}' found in {category} list.")
            found = True
            break
    if not found:
        print(f"'{target_string}' not found in any list.")

# GET https://api.github.com/users/rstg00po54/repos|jq '[.[] | {name, description}]'
# "https://api.github.com/users/{username}/repos?per_page=100"
# 请求 GitHub API 获取用户的仓库信息
url = f"https://api.github.com/users/{username}/repos?per_page=100"
response = requests.get(url)
# 检查响应状态码
if response.status_code == 200:
    repos = response.json()  # 将返回的 JSON 转换为 Python 对象
    # 提取所需字段
    repo_data = [
        {
            "name": repo.get("name", ""),
            "description": repo.get("description", "No description provided"),
            "html_url": repo.get("html_url", ""),
            "user_view_type": repo.get("private", False) and "Private" or "Public"
        }
        for repo in repos
    ]
    # 转换为 Markdown 格式
    md_content = "# GitHub Repositories\n\n"
    for repo in repo_data:
        md_content += f"## [{repo['name']}]({repo['html_url']})\n"
        md_content += f"**Description:** {repo['description']}\n\n"
        md_content += f"**Type:** {repo['user_view_type']}\n\n"
        # print(repo['name'])
    for repo in repo_data:
        file_path = 'test.md'  # 你的md文件路径
        # check_string_in_md(file_path, repo['name'])
        check_string_in_lists(repo['name'], lists)
        bin = False
        # 遍历字典的键值对
        for key, value in lists.items():
            # print('--------------')
            # print(f"Key: {key}, Value: {value}")
            if repo['name'] in value:
                bin = True
                print("is in")
                cates.setdefault(key, []).append(

                        {
                    "name":repo['name'],
                    "url": repo['html_url'],
                    "description":repo['description']
                        
                })
        if bin == False:
            print(f"{repo['name']} is not in ")
            # for v in value:
            #     print(v)

        # print("\""+repo['name']+"\",")
    # 将结果写入 .md 文件
    with open(mdfile, "w", encoding="utf-8") as md_file:
        md_file.write(md_content)

    print("Markdown file "+mdfile+" has been created.")
else:
    print(f"Failed to fetch repositories: {response.status_code}")


total_count = sum(len(value) if isinstance(value, list) else 0 for value in lists.values())
print("\033[31m字典中所有列表的总个数:\033[0m", total_count)

# pprint(cates["mcu"])


lists1 = [
    "render",
    "web",
    "book",
    "games",
    "mcu",
    "cpu",
    "dx11",
    "graph",
    "encode",
    "other"

]
md_content = "# GitHub Repositories\n\n"
md_content += "<table>\n"
md_content += "  <thead>\n\
    <tr>\n\
      <th>分类</th>\n\
      <th>仓库名称与链接</th>\n\
      <th>描述</th>\n\
    </tr>\n\
  </thead>\n"
'''
    <tr>
      <td rowspan="5">Path Tracing & Graphics</td>
      <td><a href="https://github.com/rstg00po54/Atrc">Atrc</a></td>
      <td>My path tracer</td>
    </tr>
'''
md_content += "<tbody>\n"
for v in lists1:
    print(f"----{v}")
    val = cates[v]
    # pprint(val)
    md_content += f"\t<!--{v}-->\n"
    i = 0
    # print(val)
    # md_content += f"\t\t<td rowspan=\"{len(val)}\">{v}</td>\n"
    for c in val:
        des =  c["description"]
        name = c["name"]
        url = c["url"]
        print(c["name"])
        # md_content += f"#{v}# [{name}]({url})\n"
        # md_content += f"\t\t<td>{name}</td>\n"
        md_content += "\t<tr>\n"
        # md_content += f"\t\t<td rowspan=\"{len(val)}\">{v}</td>\n"
        if i == 0:
            md_content += f"\t\t<td rowspan=\"{len(val)}\">{v}</td>\n"
        
        md_content += f"\t\t<td><a href=\"{url}\">{name}</td>\n"
        md_content += f"\t\t<td>{des}</td>\n"
        md_content += "\t</tr>\n"
        i = i + 1
md_content += "</table>\n"
md_content += "</tbody>\n"
# print(md_content)
with open("README.md", "w", encoding="utf-8") as md_file:
    md_file.write(md_content)
'''
total = 0
for key, value in cates.items():
    pprint(f"Key: {key}, len {len(value)}")
    i = 0
    # pprint(value)
    for v in value:
        print(f'--{i}')
        i = i+1
        total = total+1
        pprint(v)
        pprint(v["name"])
        des =  v["description"]
        name = v["name"]
        url = v["url"]
        md_content += f"#{key}# [{name}]({url})\n"
print(md_content)
print(f"total {total} ")
''' 