# -*- coding: utf-8 -*-


import requests
import json

# GitHub 用户名
username = "rstg00po54"

# 请求 GitHub API 获取用户的仓库信息
url = f"https://api.github.com/users/{username}/repos"
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
    
    # 将结果写入 .md 文件
    with open("github_repos.md", "w", encoding="utf-8") as md_file:
        md_file.write(md_content)

    print("Markdown file 'github_repos.md' has been created.")
else:
    print(f"Failed to fetch repositories: {response.status_code}")
