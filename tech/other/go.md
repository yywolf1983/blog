
https://github.com/SabakiHQ/Sabaki/releases

## lalee-zero

-g -t4（这个数字4是线程数） -w daonao.txt（这个是权重文件名） --noponder（对手只在对方回合思考） --playouts 3000（每一步棋考虑变化数）
time_settings 0 30 1  (三十秒一步) 


[权重文件下载](https://zero.sjeng.org/best-network)

## katago


gtp -model /Users/yy/Downloads/kata1-b40c256-s11840935168-d2898845681.bin.gz -config /Users/yy/Downloads/gtp_example.cfg time_settings 0 15 1

time_settings 0 15 1
上面这个意思就是无保留时间，15秒一步

[权重文件下载](https://katagotraining.org/networks/)


cpu 模式
analysis -config C:\Users\yy\Downloads\katago-v1.15.2-eigen-windows-x64\analysis_example.cfg -model C:\Users\yy\Downloads\kata1-b28c512nbt-s7332806912-d4357057652.bin.gz -override-config "engine: max-threads=4


生成配置文件
.\katago.exe genconfig -model .\权重文件名.bin.gz -output .\gtp_custom.cfg

.\katago.exe genconfig -model ..\kata1-b18c384nbt-s9131461376-d4087399203.bin.gz -output gtp_3070.cfg