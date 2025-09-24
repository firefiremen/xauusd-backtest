
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from textwrap import dedent

CHEATS = {
    "1": {
        "title": "查看当前状态",
        "body": dedent(\"\"\"
            查看工作区/暂存区变更：
              git status

            只看简洁状态：
              git status -sb
        \"\"\").strip()
    },
    "2": {
        "title": "将改动加入暂存区",
        "body": dedent(\"\"\"
            添加所有改动：
              git add .

            添加特定文件：
              git add <file>

            取消暂存：
              git restore --staged <file>
        \"\"\").strip()
    },
    "3": {
        "title": "提交改动（写提交信息）",
        "body": dedent(\"\"\"
            标准提交：
              git commit -m "feat: 描述这次改动"

            修改上一次提交（尚未推送时）：
              git commit --amend
        \"\"\").strip()
    },
    "4": {
        "title": "推送到远程（GitHub）",
        "body": dedent(\"\"\"
            首次推送当前分支并建立跟踪：
              git push -u origin <branch>

            之后直接：
              git push
        \"\"\").strip()
    },
    "5": {
        "title": "拉取远程更新（只快进）",
        "body": dedent(\"\"\"
            避免产生意外合并提交：
              git pull --ff-only
        \"\"\").strip()
    },
    "6": {
        "title": "分支：创建 / 切换",
        "body": dedent(\"\"\"
            新建并切换到分支：
              git switch -c feature/new-strategy

            切回主分支：
              git switch main

            查看分支：
              git branch
        \"\"\").strip()
    },
    "7": {
        "title": "合并分支（merge）",
        "body": dedent(\"\"\"
            在 main 上合并功能分支：
              git switch main
              git pull --ff-only
              git merge feature/new-strategy
              git push
        \"\"\").strip()
    },
    "8": {
        "title": "变基（rebase）并解决冲突",
        "body": dedent(\"\"\"
            让分支历史更线性：
              git switch feature/new-strategy
              git fetch origin
              git rebase origin/main

            若有冲突：
              # 编辑冲突文件 -> 解决后：
              git add <file>
              git rebase --continue

            变基完成后合并：
              git switch main
              git merge --ff-only feature/new-strategy
              git push
        \"\"\").strip()
    },
    "9": {
        "title": "临时搁置改动（stash）",
        "body": dedent(\"\"\"
            暂存未完成改动：
              git stash push -m "WIP: 修复止盈止损边界"

            查看与取回：
              git stash list
              git stash pop
        \"\"\").strip()
    },
    "10": {
        "title": "回退与撤销（谨慎）",
        "body": dedent(\"\"\"
            创建反向提交（推荐，安全）：
              git revert <commit-hash>

            强制回到某提交（危险，会改历史）：
              git reset --hard <commit-hash>

            救命绳：查看所有引用历史：
              git reflog
        \"\"\").strip()
    },
    "11": {
        "title": "远程仓库管理（HTTPS/SSH）",
        "body": dedent(\"\"\"
            绑定远程：
              git remote add origin https://github.com/<你>/repo.git

            改远程地址：
              git remote set-url origin <新地址>

            查看：
              git remote -v
        \"\"\").strip()
    },
    "12": {
        "title": "标签（版本号）",
        "body": dedent(\"\"\"
            打标签并推送：
              git tag v0.1.0
              git push origin v0.1.0
        \"\"\").strip()
    },
    "13": {
        "title": "查看历史（图形化 oneline）",
        "body": dedent(\"\"\"
            简洁图形历史：
              git log --oneline --graph --decorate --all
        \"\"\").strip()
    },
    "14": {
        "title": "比较差异（含暂存区）",
        "body": dedent(\"\"\"
            工作区与暂存区差异：
              git diff

            查看已暂存但未提交的差异：
              git diff --staged
        \"\"\").strip()
    },
    "15": {
        "title": "换行符/跨平台设置建议（LF）",
        "body": dedent(\"\"\"
            跨平台团队常用（保存为 LF）：
              git config --global core.autocrlf input
              git config --global core.eol lf
        \"\"\").strip()
    },
    "16": {
        "title": "HTTPS 首次推送使用 PAT",
        "body": dedent(\"\"\"
            第一次 git push 时：
              Username: 你的 GitHub 用户名
              Password: Personal Access Token (PAT)  # 不是登录密码

            生成 PAT：GitHub → Settings → Developer settings → Personal access tokens
            给至少 repo 权限；用 Git Credential Manager 保存。
        \"\"\").strip()
    },
    "17": {
        "title": "主分支改名为 main",
        "body": dedent(\"\"\"
            本地改名并推送：
              git branch -M main
              git push -u origin main
        \"\"\").strip()
    },
    "18": {
        "title": "本地与远程差异检查",
        "body": dedent(\"\"\"
            查看本地 main 相对远程 origin/main 的额外提交：
              git log origin/main..main --oneline
        \"\"\").strip()
    },
}

MENU = "\\n".join([f"{k}. {v['title']}" for k, v in CHEATS.items()])

def show(item_key: str):
    item = CHEATS.get(item_key)
    if not item:
        print("无此条目编号。")
        return
    print(f"\\n=== {item['title']} ===\\n{item['body']}\\n")

def main():
    if len(sys.argv) > 1 and sys.argv[1].lower() in ("all", "-a", "--all"):
        for k in sorted(CHEATS.keys(), key=lambda x: int(x)):
            show(k)
        return

    print(dedent(\"\"\"
        ================== Git 交互式小抄 ==================
        请输入编号查看详细说明（输入 q 退出，all 查看全部）：
    \"\"\").rstrip())
    print(MENU)
    while True:
        try:
            choice = input("\\n选择编号 (q 退出): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print("\\nBye!")
            break
        if choice in ("q", "quit", "exit"):
            print("Bye!")
            break
        if choice in ("all", "-a", "--all"):
            for k in sorted(CHEATS.keys(), key=lambda x: int(x)):
                show(k)
            continue
        show(choice)
        print("\\n（再次输入编号继续查看，或输入 q 退出）")

if __name__ == "__main__":
    main()
