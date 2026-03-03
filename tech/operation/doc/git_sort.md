Zsh 通过强大的插件系统（特别是 https://ohmyz.sh/）提供了极丰富的 Git 命令简化，包括大量**单字符或短命令别名**。以下是主要的 Git 简化命令：

## 一、核心简化命令

### 1. **基础操作**
| 简化命令 | 原命令 | 功能 |
|---------|--------|------|
| `g` | `git` | 所有 git 命令的前缀 |
| `gst` | `git status` | 查看状态 |
| `ga` | `git add` | 添加文件 |
| `gaa` | `git add --all` | 添加所有文件 |
| `gc` | `git commit -v` | 提交（带详细差异） |
| `gc!` | `git commit -v --amend` | 修正上次提交 |
| `gcm` | `git commit -m` | 提交（带消息） |

### 2. **分支操作**
| 简化命令 | 原命令 | 功能 |
|---------|--------|------|
| `gb` | `git branch` | 查看分支 |
| `gbd` | `git branch -d` | 删除分支 |
| `gco` | `git checkout` | 切换分支 |
| `gcb` | `git checkout -b` | 创建并切换分支 |
| `gcm` | `git checkout main` 或 `git checkout master` | 切到主分支 |

### 3. **远程操作**
| 简化命令 | 原命令 | 功能 |
|---------|--------|------|
| `gpsup` | `git push --set-upstream origin $(git_current_branch)` | 推送并设置上游 |
| `gl` | `git pull` | 拉取更新 |
| `gp` | `git push` | 推送 |
| `gf` | `git fetch` | 获取远程更新 |

### 4. **日志与历史**
| 简化命令 | 原命令 | 功能 |
|---------|--------|------|
| `glg` | `git log --stat` | 带统计的日志 |
| `glgg` | `git log --graph` | 图形化日志 |
| `glo` | `git log --oneline --decorate` | 单行装饰日志 |
| `gsh` | `git show` | 显示提交内容 |

## 二、实用的工作流简化

### 1. **合并与变基**
```bash
# 合并当前分支到主分支
ggfl
# 等同于：git flow finish

# 变基
grb
# 等同于：git rebase

# 合并
gm
# 等同于：git merge
```

### 2. **撤销与重置**
```bash
# 撤销
grh
# 等同于：git reset HEAD

# 软重置
grhh
# 等同于：git reset HEAD --hard

# 恢复文件
gcf
# 等同于：git checkout --
```

### 3. **储藏操作**
```bash
# 储藏
gsta
# 等同于：git stash

# 储藏（带消息）
gstam
# 等同于：git stash -m

# 应用储藏
gstap
# 等同于：git stash pop
```

## 三、高级功能

### 1. **差异对比**
```bash
# 查看工作区与暂存区的差异
gd
# 等同于：git diff

# 查看暂存区与仓库的差异
gdc
# 等同于：git diff --cached
```

### 2. **清理**
```bash
# 清理未跟踪文件
gclean
# 等同于：git clean -fd

# 快速清理
gcl
# 等同于：git clone
```

## 四、如何启用

1. **确保已安装 Oh My Zsh**
   ```bash
   # 检查
   echo $ZSH
   # 安装（如果没有）
   sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
   ```

2. **启用 Git 插件**
   编辑 `~/.zshrc`：
   ```bash
   plugins=(git)
   ```
   然后刷新：
   ```bash
   source ~/.zshrc
   ```

3. **查看所有别名**
   ```bash
   alias | grep -E '^g[^=]+=' | less
   ```

## 五、自定义别名
在 `~/.zshrc` 中添加：
```bash
# 自定义 git 别名
alias gdmb='git branch --merged | grep -v "\*" | xargs -n 1 git branch -d'
# 删除已合并到当前分支的所有分支
```

## 六、生产力技巧
1. **模糊补全**：输入 `gco feat<TAB>` 可自动补全分支名
2. **状态提示**：Zsh 会在提示符显示当前分支、状态（脏/干净）
3. **自动修正**：输入 `git stauts` 会提示 `git status`

这些简化命令可大幅提升日常 Git 操作的效率，建议从最常用的开始（如 `gst`, `gco`, `gc`），逐渐扩展到其他命令。