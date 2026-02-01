https://ollama.com/

ollama list
ollama rm 本地模型名称
ollama run 本地模型名
ollama ps
ollama cp 本地存在的模型名 新复制模型名
ollama pull 本地/远程仓库模型名称

Modelfile
FROM ./Meta-Llama-3-8B-Instruct.Q4_K_M.gguf
或
ollama run vanilj/Phi-4

ollama create 模型名称 -f ./Modelfile


git clone https://github.com/ollama-webui/ollama-webui-lite ollama-webui


npm install
npm run dev

    OLLAMA_MODELS：模型文件存放目录，默认目录为当前用户目录（Windows 目录：C:\Users%username%.ollama\models，MacOS 目录：~/.ollama/models，Linux 目录：/usr/share/ollama/.ollama/models），如果是 Windows 系统建议修改（如：D:\OllamaModels），避免 C 盘空间吃紧
    OLLAMA_HOST：Ollama 服务监听的网络地址，默认为127.0.0.1，如果允许其他电脑访问 Ollama（如：局域网中的其他电脑），建议设置成0.0.0.0，从而允许其他网络访问
    OLLAMA_PORT：Ollama 服务监听的默认端口，默认为11434，如果端口有冲突，可以修改设置成其他端口（如：8080等）
    OLLAMA_ORIGINS：HTTP 客户端请求来源，半角逗号分隔列表，若本地使用无严格要求，可以设置成星号，代表不受限制
    OLLAMA_KEEP_ALIVE：大模型加载到内存中后的存活时间，默认为5m即 5 分钟（如：纯数字如 300 代表 300 秒，0 代表处理请求响应后立即卸载模型，任何负数则表示一直存活）；我们可设置成24h，即模型在内存中保持 24 小时，提高访问速度
    OLLAMA_NUM_PARALLEL：请求处理并发数量，默认为1，即单并发串行处理请求，可根据实际情况进行调整
    OLLAMA_MAX_QUEUE：请求队列长度，默认值为512，可以根据情况设置，超过队列长度请求被抛弃
    OLLAMA_DEBUG：输出 Debug 日志标识，应用研发阶段可以设置成1，即输出详细日志信息，便于排查问题
    OLLAMA_MAX_LOADED_MODELS：最多同时加载到内存中模型的数量，默认为1，即只能有 1 个模型在内存中
