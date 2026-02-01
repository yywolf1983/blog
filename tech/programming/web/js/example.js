function test(){
   //var message = "hi"; // 局部变量 
   message = "hi"; // 全局变量 
}
test();

num1 = 077  //八进制
num2 = 078  //十进制 八进制无法大于8
num3 = 0x16 //十六进制

num4 = ~num2  //按位非

// & and   | or   ^   XOR

num5 = num4 >> 5 //右移

num6 = num5 >>> 4 //无符号位移 无法无符号左移


var result = ("55" === 55); //false，因为不同的数据类型不相等
re = result?"a1":"a2"

// 定义 with 语句的目的主要是为了简化多次编写同一个对象的工作，如下面的例子所示:
    var qs = location.search.substring(1);
    var hostName = location.hostname;
    var url = location.href;
// 上面几行代码都包含 location 对象。如果使用 with 语句，可以把上面的代码改写成如下所示:
with(location){
    var qs = search.substring(1);
    var hostName = hostname;
    var url = href;
}


//函数
function sayHi(name, message) {
    console.log("Hello " + name + "," + message);
}

//变参函数
function doAdd() {
  if(arguments.length == 1) {
    console.log(arguments[0] + 10);
   } else if (arguments.length == 2) {
    console.log(arguments[0] + arguments[1]);
  }
}
doAdd(10);         //20
doAdd(30, 20);     //50


var colors = ["red", "blue", "green"];
console.log(colors.toString());
console.log(colors.valueOf());
console.log(colors);

var d = Date.now();
console.log("now time:"+d);


var person = new Object();
person.name = "Nicholas";
person.sayName = function(){
        alert(this.name);
};

//面向对象
var person = {
    name: "Nicholas",
    age: 29,
    job: "Software Engineer",

    sayName:function(){
        console.log(this.name);
    }
};

person.sayName()

//原型模式
 function Person(){
 }
 
Person.prototype.name = "Nicholas";
Person.prototype.age = 29;
Person.prototype.job = "Software Engineer";
Person.prototype.sayName = function(){
    console.log(this.name);
};
//所有属性直接添加到了 Person 的 prototype 属性中
var person1 = new Person();
person1.sayName();   //"Nicholas"

//闭包
var name = "The Window";
var object = {
    name : "My Object",
    getNameFunc : function(){
         var that = this;
         return function(){
             return that.name;
         }; 
    }
};

//闭包控制变量不越界
console.log(object.getNameFunc()());  //"My Object"

//window 当前窗口全局
console.log(window.name);
//本地信息
console.log(document.location);
//浏览器信息
console.log(window.navigator);
//像素信息
console.log(window.screen);
//历史记录
console.log(window.history);


function loadappString(lable,id,code){
    var script = document.createElement(lable);
    script.id = id;
    try {
        script.appendChild(document.createTextNode(code));
    } catch (ex){
        script.text = code;
    }
    document.body.appendChild(script);
}

var id = "csd"
loadappString("h1",id,"fun");

var selected = document.querySelector("#"+id);
console.log(selected);

var btn = document.getElementById(id);
btn.onclick = function(){
    console.log(this.id);    //"myBtn"
    btn.onclick = null;
};

//模拟事件


//绘图
var drawing = document.getElementById("drawing");
drawing.width=100;
drawing.height=100;
//确定浏览器支持<canvas>元素 
if (drawing.getContext){
    var context = drawing.getContext("2d");
    //绘制红色矩形
    context.fillStyle = "#ff0000"; 
    context.fillRect(10, 10, 50, 50);
    //绘制半透明的蓝色矩形
    context.fillStyle = "rgba(0,0,255,0.5)"; 
    context.fillRect(30, 30, 50, 50);
    
    //在两个矩形重叠的地方清除一个小矩形
    context.fillStyle = "rgba(0,0,255,0.5)"; 
    context.clearRect(40, 40, 10, 10);
}

