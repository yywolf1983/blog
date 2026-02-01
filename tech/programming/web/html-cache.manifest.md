


<html lang='cn' manifest='cache.manifest'>

CACHE MANIFEST  
# 注释：需要缓存的文件，无论在线与否，均从缓存里读取  
chched.js  
cached.css  

# 注释：不缓存的文件，无论缓存中存在与否，均从新获取  
NETWORK:  
uncached.js  
uncached.css  

# 注释：获取不到资源时的备选路径，如index.html访问失败，则返回404页面  
FALLBACK:  
index.html 404.html
//当前文档对应的applicationCache对象  
window.applicationCache  

//当前缓存所处的状态，为0～5的整数值，分别对应一个状态，并分别对应一个常量  
window.applicationCache.status  

window.applicationCache.UNCACHED === 0    //未缓存，比如一个页面没有制定缓存清单，其状态就是UNCACHED  
window.applicationCache.IDLE === 1 //空闲，缓存清单指定的文件已经全部被页面缓存，此时状态就是IDLE  
window.applicationCache.CHECKING === 2 //页面正在检查当前离线缓存是否需要更新  
window.applicationCache.DOWNLOADING === 3 //页面正在下载需要更新的缓存文件  
window.applicationCache.UPDATEREADY === 4  //页面缓存更新完毕  
window.applicationCache.OBSOLETE === 5  //缓存过期，比如页面检查缓存是否过期时，发现服务器上的.manifest文件被删掉了  

//常用API，在后面会稍详细介绍  
window.applicationCache.update()  //update方法调用时，页面会主动与服务器通信，检查页面当前的缓存是否为最新的，如不是，则下载更新后的资源  
window.applicationCache.swapCache()  //updateready后，更新到最新的应用缓存
cache.html  

<!DOCTYPE html>
<html lang='cn' manifest='cache.manifest'>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>离线缓存</title>
</head>
<body></body>
<script type="text/javascript" src="cache.js"></script>
<script type="text/javascript">
var cache = window.applicationCache;  
conso.log('test:' + test);  //cache.js定义的一个变量，初始值为10  

function load(url, callback){  
    var script = document.createElement('script');  
    script.src = url;  
    script.onload = function(){  
        callback && callback();  
    }  
    document.body.appendChild(script);  
}  

setTimeout(function(){  
    cache.addEventListener('updateready', function(){  
        log('更新完毕');  
        //cache.swapCache();  
        load('cache.js', function(){  
            log('test:' + test);    //test: 10  
        });      
    });  
    cache.update();  

}, 20*1000);  
</script>
</html> 
