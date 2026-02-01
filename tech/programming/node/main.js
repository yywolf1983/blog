
const os = require('os');
const https = require('https');

const { buffer } = require('stream/consumers');

// console.log(module.paths)

// 使用c编写node 模块
const addon = require('./build/Release/hello');
console.log(addon.hello());


var foo = function () {
    var bar = function () {
        var local = "局部变量";
        return function () {
            return local;
        };
    };
    var baz = bar();
    console.log(baz());
};

var foo = foo();
foo;

var showMem = function() {
    var mem = process.memoryUsage();
    var format = function (bytes){
        return (bytes / 1024 / 1024).toFixed(2)+' MB';
    };
console.log('Process: heapTotal ' + format(mem.heapTotal) +
' heapUsed ' + format(mem.heapUsed) + ' rss ' + format(mem.rss));
console.log('-----------------------------------------------------------');
};
var useMem = function() {
    var size = 80*1024*1024;
    var buf = new Buffer.alloc(size);
    for (var i=0; i < size; i++){
        buf[i] = 0;
    }
    // console.log(buf);
    return buf;
}

var total = [];

for (var j =0; j<5; j++){
    showMem();
    total.push(useMem());
}
showMem();


// open server
var net = require('net');

var server = net.createServer(function(socket){
    socket.on('data',function(data){
        socket.write("server:world!!!\n");
        console.log(data.toString());
    });
    socket.on('end',function(){
        console.log('exit!!!');
    })
    socket.write("ok");
});

server.listen(8123, function () {
    console.log('server bound');
    setTimeout(function () {
            process.exit(1);
        }, 5000);  
});

// 模拟客户端
var client = net.connect({port: 8123}, function () { //'connect' listener
    console.log('client connected');
    client.write('client:hello');
});

client.on('data', function (data) {
    console.log(data.toString());
    client.end();
});


// open https
var options = {
    hostname: 'api.d7home.com',
    port: 443,
    path: '/ip',
    method: 'GET'
}

var req = https.request(options, function(res) {
        console.log('STATUS: ' + res.statusCode);
        console.log('HEADERS: ' + JSON.stringify(res.headers));
        res.setEncoding('utf8');
        res.on('data', function (chunk) {
                console.log(chunk);
        });
});

req.on('error', (e) => {
    console.error(e);
});

req.end();

