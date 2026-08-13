# goose 速查手册


## 配置管理

goose configure      # 重新配置模型/密钥
goose update

goose info -v

添加到 zsh 配置中
eval "$(goose completion zsh)"

添加到 powershell 配置中
goose completion powershell | Out-String | Invoke-Expression
. $PROFILE

## 常用配置

任意目录/.goosehints  # 可以在任意目录下生效

## session 管理

goose session list       # 查看所有会话

goose session --resume --name 20260429_1
goose session -r -n 20260429_1

goose session remove -r "20260429_*"


## 简化命令

goose run -t "你好"
goose run --text "帮我解释一下当前目录"

goose run -i instructions.md

echo "2+2=?" | goose run -i -

goose run -t "先总结代码" -s
goose run -t "继续刚才的分析" -s -r --name 20260429_1

-s, --interactive    # 初始输入处理完后，继续停留在交互模式

## 常用环境变量 

export GOOSE_AUTO_COMPACT_THRESHOLD=0.6 压缩会话

### LiteLLM proxy with custom model name
export GOOSE_PROVIDER="openai"
export GOOSE_MODEL="my-custom-gpt4-proxy"
export GOOSE_CONTEXT_LIMIT=200000  # Override the 32k default


export GOOSE_MOIM_MESSAGE_FILE="~/.goose/guardrails.md"
### Always run tests before committing1
export GOOSE_MOIM_MESSAGE_TEXT="IMPORTANT: Always run tests before committing changes."


## 内部命令

/recipe   持久化 可以指定命令
goose recipe list

## 内部系统

命令历史	~/.config/goose/history.txt
            %APPDATA%\Block\goose\data\history.txt
会话记录	~/.local/share/goose/sessions/sessions.db	
            %APPDATA%\Block\goose\data\sessions\sessions.db
系统日志	~/.local/state/goose/logs/
            %APPDATA%\Block\goose\data\logs\


## 忽略系统

.gooseignore 


## 使用浏览器

npx skills add https://github.com/microsoft/playwright-cli --skill playwright-cli

https://goose-docs.ai/docs/mcp/playwright-mcp
