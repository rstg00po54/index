import requests
from pprint import pprint
def get_repo_count(username):
    url = f"https://api.github.com/users/{username}/repos?per_page=100"  # 每页返回最多 100 个仓库
    repo_count = 0
    while url:
        print("get" + url)
        response = requests.get(url)
        if response.status_code == 200:
            repos = response.json()
            # pprint(repos)
            print(type(repos))
            repo_count += len(repos)
            print(repo_count)
            pprint(repos[0])
            # 查找分页链接
            if 'Link' in response.headers:
                links = response.headers['Link']
                # 查找 'rel="next"'，并更新 URL 以请求下一页
                if 'rel="next"' in links:
                    url = links.split(';')[0][1:-1]  # 提取 URL
                else:
                    url = None  # 没有下一页
            else:
                url = None  # 没有分页链接
        else:
            print(f"Failed to fetch repositories for {username}. Status code: {response.status_code}")
            break
    return repo_count

# 使用示例
username = "rstg00po54"  # 替换为你想查询的 GitHub 用户名
repo_count = get_repo_count(username)
print(f"{username} has {repo_count} repositories.")
