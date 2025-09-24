#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

CHEATS = {
    "1": {"title": "查看当前状态",
          "body": "查看工作区/暂存区变更：\n  git status\n\n只看简洁状态：\n  git status -sb"},
    "2": {"title": "将改动加入暂存区",
          "body": "添加所有改动：\n  git add .\n\n添加特定文件：\n  git add <file>\n\n取消暂存：\n  git restore --staged <file>"},
    "3": {"title": "提交改动（写提交信息）",
          "body": "标准提交：\n  git commit -m \"feat: 描述改动\"\n\n修改上一次提交（尚未推送时）：\n  git commit --amend"},
    "4": {"title": "推送到远程（GitHub）",
          "body": "首次推送当前分支并建立跟踪：\n  git push -u origin <branch>\n\n之后直接：\n  git push"},
    "5": {"title": "拉取远程更新（只快进）",
          "body": "避免产生意外合并提交：\n  git pull --ff-only"},
    "6": {"title": "分支：创建 / 切换",
          "body": "新建并切换到分支：\n  git switch -c feature/new-strategy\n\n切回主分支：\n  git switch main\n\n查看分支：\n  git branch"},
    "7": {"title": "合并分支（merge）",
          "body": "在 main 上合并功能分支：\n  git switch main\n  git pull --ff-only\n  git merge feature/new-strategy\n  git push"},
    "8": {"title": "变基（rebase）并解决冲突",
          "body": "让分支历史更线性：\n  git switch feature/new-strategy\n  git fetch origin\n  git rebase origin/main\n\n若有冲突：\n  git add <file>\n  git rebase --continue\n\n变基完成后合并：\n  git switch main\n  git merge --ff-only feature/new-strategy\n  git push"},
    "9": {"title": "临时搁置改动（stash）",
          "body": "暂存未完成改动：\n  git stash push -m \"WIP: 修复止盈止损边界\"\n\n查看与取回：\n  git stash list\n  git stash pop"},
    "10": {"title": "回退与撤销（谨慎）",
           "body": "创建反向提交（推荐，安全）：\n  git revert <commit-hash>\n\n强制回到某提交（危险，会改历史）：\n  git reset --hard <commit-hash>\n\n救命绳：\n  git reflog"},
    "11": {"title": "远程仓库管理（HTTPS/SSH）",
           "body": "绑定远程：\n  git remote add origin https://github.com/<你>/repo.git\n\n改远程地址：\n  git remote set-url origin <新地址>\n\n查看：\n  git remote -v"},
    "12": {"title": "标签（版本号）",
           "body": "打标签并推送：\n  git tag v0.1.0\n  git push origin v0.1.0"},
    "13": {"title": "查看历史（图形化 oneline）",
           "body": "简洁图形历史：\n  git log --oneline --graph --decorate --all"},
    "14": {"title": "比较差异（含暂存区）",
           "body": "工作区与暂存区差异：\n  git diff\n\n已暂存但未提交的差异：\n  git diff --staged"},
    "15": {"title": "换行符/跨平台设置建议（LF）",
           "body": "跨平台团队常用（保存为 LF）：\n  git config --global core.autocrlf input\n  git config --global core.eol lf"},
    "16": {"title": "HTTPS 首次推送使用 PAT",
           "body": "第一次 git push 时：\n  Username: GitHub 用户名\n  Password: Personal Access Token (PAT)\n\n生成 PAT：GitHub → Settings → Developer settings → Tokens\n至少给 repo 权限；建议配合 Git Credential Manager 保存"},
    "17": {"title": "主分支改名为 main",
           "body": "本地改名并推送：\n  git branch -M main\n  git push -u origin main"},
    "18": {"title": "本地与远程差异检查",
           "body": "查看本地 main 相对远程 origin/main 的额外提交：\n  git log origin/main..main --oneline"},
}

MENU = "\n".join([f"{k}. {v['title']}" for k, v in CHEATS.items()])

def show(item_key: str):
    item = CHEATS.get(item_key)
    if item:
        print(f"\n=== {item['title']} ===\n{item['body']}\n")
    else:
        print("无此条目编号。")

def search(keyword: str):
    found = False
    for k, v in CHEATS.items():
        if keyword.lower() in v["title"].lower() or keyword.lower() in v["body"].lower():
            print(f"\n=== {v['title']} (#{k}) ===\n{v['body']}\n")
            found = True
    if not found:
        print(f"\n没有找到包含关键词 '{keyword}' 的命令。\n")

def main():
    print("""
================== Git 交互式小抄 ==================
输入编号查看详细说明；输入关键词可搜索（push/branch/rebase 等）；
输入 all 查看全部；输入 q 退出
""".rstrip())
    print(MENU)
    while True:
        choice = input("\n选择编号或关键词 (q 退出): ").strip().lower()
        if choice in ("q", "quit", "exit"):
            print("Bye!")
            break
        if choice in ("all", "-a", "--all"):
            for k in sorted(CHEATS.keys(), key=lambda x: int(x)):
                show(k)
            continue
        if choice.isdigit():
            show(choice)
        else:
            search(choice)

if __name__ == "__main__":
    main()
