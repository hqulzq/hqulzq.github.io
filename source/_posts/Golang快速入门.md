---
title: Golang快速入门
date: 2025-02-05 20:23:46
tags:
  - 快速入门
categories:
  - Golang
---

## go语言简介

> Go（又称 Golang）是 Google 的 Robert Griesemer，Rob Pike 及 Ken Thompson 开发的一种静态强类型、编译型语言。Go 语言语法与 C 相近，但功能上有：内存安全，GC（垃圾回收），结构形态及 CSP-style 并发计算。

### go语言特点

* 背靠大厂，google背书，可靠
* 天生支持并发（最显著特点）
* 语法简单，容易上手
* 内置runtime，支持垃圾回收
* 可直接编译成机器码，不依赖其他库
* 丰富的标准库
* 跨平台编译
<!-- more -->

### go语言的应用领域

* 服务器编程
* 开发云平台
* 区块链
* 分布式系统
* 网络编程

### 那些公司（项目）在使用go语言

* Google
  * k8s
* Facebook
  * facebookgo
* 腾讯
  * 蓝鲸平台
  * 容器技术
* 百度
  * 运维项目BFE
* 京东
  * 消息推送系统、云存储、京东商城
* 小米
  * 运维监控系统、小米互娱、小米商城、小米视频、小米生态链
* 360
  * 日志搜索系统Poseidon

## go环境安装

在官网 Go：<https://golang.org/dl/>  安装过程中记得把添加到环境变量那个给勾上

```shell
 go version
```

## go开发工具

* 1.vim
* 2.sublime
* 3.atom
* 4.LiteIDE
* 5.eclipse
* 6.goland
* 7.vscode

## go常用命令

<table><thead><tr><th>命令</th><th>描述</th></tr></thead><tbody><tr><td>go bug</td><td>启动一个用于报告bug的工具。</td></tr><tr><td>go build</td><td>编译Go程序包及其依赖项。</td></tr><tr><td>go clean</td><td>删除编译生成的对象文件和缓存文件。</td></tr><tr><td>go doc</td><td>显示有关包或符号的文档。</td></tr><tr><td>go env</td><td>打印有关Go环境的信息。</td></tr><tr><td>go fix</td><td>更新包以使用新的API。</td></tr><tr><td>go fmt</td><td>使用gofmt重新格式化Go包的源代码。</td></tr><tr><td>go generate</td><td>通过处理源代码来生成Go文件。</td></tr><tr><td>go get</td><td>将依赖项添加到当前模块并安装它们。</td></tr><tr><td>go install</td><td>编译并安装包及其依赖项。</td></tr><tr><td>go list</td><td>列出包或模块的信息。</td></tr><tr><td>go mod</td><td>用于模块维护,包括初始化模块、添加和更新依赖项等。</td></tr><tr><td>go work</td><td>用于工作区维护,例如查看、清理或打印工作区信息。</td></tr><tr><td>go run</td><td>编译并运行Go程序。</td></tr><tr><td>go test</td><td>运行包的测试。</td></tr><tr><td>go tool</td><td>运行指定的Go工具。</td></tr><tr><td>go version</td><td>打印Go的版本信息。</td></tr><tr><td>go vet</td><td>检查 Go 源码并报告可疑的错误。</td></tr></tbody></table>

## Go语言中的标识符、关键字和命名规范

<h2><a name="t1"></a><a id="_3"></a>一、标识符</h2>
<p>标识符，通俗的讲，就是给变量、常量、函数、方法、结构体、数组、切片、接口起名字</p>
<h3><a name="t2"></a><a id="11__5"></a>1.1 标识符的组成</h3>
<p>在 Go 语言中，标识符的组成和其他编程语言类似，如下：</p>
<ul><li>标识符有字母、数字和下划线组成</li><li>标识符只能以字母或下划线开头，不能以数字开头</li><li>标识符区分大小写</li></ul>
<h2><a name="t3"></a><a id="_12"></a>二、关键字</h2>
<p>关键字字，就是在Go语言中内置定义了一些标识符，这些标识符已经存在固定的含义了，在自定义变量名时不能再使用关键字了，Go语言中的关键字包含25个基本关键字和36个预定义标识符</p>
<h3><a name="t4"></a><a id="21_25_14"></a>2.1 25个基本关键字</h3>
<div class="table-box"><table><thead><tr><th align="center">break</th><th align="center">default</th><th align="center">func</th><th align="center">interface</th><th align="center">select</th></tr></thead><tbody><tr><td align="center">case</td><td align="center">defer</td><td align="center">go</td><td align="center">map</td><td align="center">struct</td></tr><tr><td align="center">chan</td><td align="center">else</td><td align="center">goto</td><td align="center">package</td><td align="center">switch</td></tr><tr><td align="center">const</td><td align="center">fallthrough</td><td align="center">if</td><td align="center">range</td><td align="center">type</td></tr><tr><td align="center">continue</td><td align="center">for</td><td align="center">import</td><td align="center">return</td><td align="center">var</td></tr></tbody></table></div>
<h3><a name="t5"></a><a id="22_36_22"></a>2.2 36个预定义标识符</h3>
<div class="table-box"><table><thead><tr><th align="center">append</th><th align="center">bool</th><th align="center">byte</th><th align="center">cap</th><th align="center">close</th><th align="center">complex</th><th align="center">complex64</th><th align="center">complex128</th><th align="center">uint16</th></tr></thead><tbody><tr><td align="center">copy</td><td align="center">false</td><td align="center">float32</td><td align="center">float64</td><td align="center">imag</td><td align="center">int</td><td align="center">int8</td><td align="center">int16</td><td align="center">uint32</td></tr><tr><td align="center">int32</td><td align="center">int64</td><td align="center">iota</td><td align="center">len</td><td align="center">make</td><td align="center">new</td><td align="center">nil</td><td align="center">panic</td><td align="center">uint64</td></tr><tr><td align="center">print</td><td align="center">println</td><td align="center">real</td><td align="center">recover</td><td align="center">string</td><td align="center">true</td><td align="center">uint</td><td align="center">uint8</td><td align="center">uintptr</td></tr></tbody></table></div>
<h2><a name="t6"></a><a id="_29"></a>三、命名规范</h2>
<p>命名规则涉及变量、常量、全局函数、结构、接口、方法等的命名</p>
<h3><a name="t7"></a><a id="31__31"></a>3.1 公有私有的命名规范</h3>
<ul><li> <p>当命名（包括常量、变量、类型、函数名、结构字段等等）以一个大写字母开头，如：GetUserName，那么使用这种形式的标识符的对象就可以被外部包的代码所使用（客户端程序需要先导入这个包），这被称为导出（像面向对象语言中的 public）；</p> </li><li> <p>命名如果以小写字母开头，则对包外是不可见的，但是他们在整个包的内部是可见并且可用的（像面向对象语言中的 private ）</p> </li></ul>
<h3><a name="t8"></a><a id="32__36"></a>3.2 包名称命名规范</h3>
<ul><li>保持package的名字和目录保持一致，尽量采取有意义的包名，简短，有意义，尽量和标准库不要冲突。包名应该为小写单词，不要使用下划线或者混合大小写</li></ul>
<p>如：</p>
<pre data-index="0" class="set-code-show prettyprint"><code class="prism language-bash has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">package user
package <span class="token function">service</span>
<div class="hljs-button {2}" data-title="复制"></div></code></pre>
<h3><a name="t9"></a><a id="33__45"></a>3.3 文件命名规范</h3>
<ul><li>尽量采取有意义的文件名，简短，有意义，应该为小写单词，使用下划线分隔各个单词。</li></ul>
<p>如：</p>
<pre data-index="1" class="set-code-show prettyprint"><code class="prism language-bash has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">user_api.go
<div class="hljs-button {2}" data-title="复制"></div></code></pre>
<h3><a name="t10"></a><a id="34__53"></a>3.4 结构体命名规范</h3>
<p>结构体命名规范采用驼峰法，首字母根据是否提供外部使用决定是否使用大小写</p>
<pre data-index="2" class="set-code-show prettyprint"><code class="prism language-bash has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token builtin class-name">type</span> CustomerOrder struct <span class="token punctuation">{<!-- --></span>
    Name string
    Address string
<span class="token punctuation">}</span>
</pre>
<h3><a name="t11"></a><a id="35__63"></a>3.5 接口命名规范</h3>
<p>接口命名规范也是采用驼峰法，此外单个函数的结构名以 “er” 作为后缀，例如 Reader , Writer</p>
<pre data-index="3" class="set-code-show prettyprint"><code class="prism language-bash has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;"><span class="token builtin class-name">type</span> Reader interface <span class="token punctuation">{<!-- --></span>
     Read<span class="token punctuation">(</span>p <span class="token punctuation">[</span><span class="token punctuation">]</span>byte<span class="token punctuation">)</span> <span class="token punctuation">(</span>n int, err error<span class="token punctuation">)</span>
<span class="token punctuation">}</span>
</pre>
<h3><a name="t12"></a><a id="36__72"></a>3.6 变量名命名规范</h3>
<p>变量名称一般遵循驼峰法，首字母根据<a href="https://so.csdn.net/so/search?q=%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6&amp;spm=1001.2101.3001.7020" target="_blank" class="hl hl-1" data-report-click="{&quot;spm&quot;:&quot;1001.2101.3001.7020&quot;,&quot;dest&quot;:&quot;https://so.csdn.net/so/search?q=%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6&amp;spm=1001.2101.3001.7020&quot;,&quot;extra&quot;:&quot;{\&quot;searchword\&quot;:\&quot;访问控制\&quot;}&quot;}" data-tit="访问控制" data-pretit="访问控制">访问控制</a>原则大写或者小写，但遇到特有名词时，需要遵循以下规则：</p>
<ul><li>如果变量为私有，且特有名词为首个单词，则使用小写，如 appService</li><li>若变量类型为 bool 类型，则名称应以 Has, Is, Can 或 Allow 开头</li></ul>
<p>如：</p>
<pre data-index="4" class="set-code-show prettyprint"><code class="prism language-bash has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">var isExist bool
var hasConflict bool
var canManage bool
var allowGitHook bool
</pre>
<h3><a name="t13"></a><a id="37__86"></a>3.7 常量命名规范</h3>
<p>常量均需使用全部大写字母组成，<并使用下划></并使用下划>线分词</p>
<pre data-index="5" class="set-code-show prettyprint"><code class="prism language-bash has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">const APP_URL <span class="token operator">=</span> <span class="token string">"https://www.baidu.com"</span>
</pre>
<h3><a name="t14"></a><a id="38__92"></a>3.8 异常处理的规范</h3>
<p>错误处理的原则就是不能丢弃任何有返回err的调用，不要使用 _ 丢弃，必须全部处理。接收到错误，要么返回err，或者使用log记录下来尽早return：一旦有错误发生，马上返回，尽量不要使用panic，除非你知道你在做什么，错误描述如果是英文必须为小写，不需要标点结尾，采用独立的错误流进行处理</p>
<pre data-index="6" class="set-code-show prettyprint"><code class="prism language-bash has-numbering" onclick="mdcp.copyCode(event)" style="position: unset;">// 错误写法
<span class="token keyword">if</span> err <span class="token operator">!=</span> nil <span class="token punctuation">{<!-- --></span>
    // 错误处理
<span class="token punctuation">}</span> <span class="token keyword">else</span> <span class="token punctuation">{<!-- --></span>
    // 正常代码
<span class="token punctuation">}</span>

// 正确写法
<span class="token keyword">if</span> err <span class="token operator">!=</span>
nil <span class="token punctuation">{<!-- --></span>
// 错误处理
<span class="token builtin class-name">return</span> // 或者继续
<span class="token punctuation">}</span>
// 正常代码

</pre>

<h3><a name="t15"></a><a id="39__112"></a>3.9 <a href="https://so.csdn.net/so/search?q=%E5%8D%95%E5%85%83%E6%B5%8B%E8%AF%95&amp;spm=1001.2101.3001.7020" target="_blank" class="hl hl-1" data-report-click="{&quot;spm&quot;:&quot;1001.2101.3001.7020&quot;,&quot;dest&quot;:&quot;https://so.csdn.net/so/search?q=%E5%8D%95%E5%85%83%E6%B5%8B%E8%AF%95&amp;spm=1001.2101.3001.7020&quot;,&quot;extra&quot;:&quot;{\&quot;searchword\&quot;:\&quot;单元测试\&quot;}&quot;}" data-tit="单元测试" data-pretit="单元测试">单元测试</a>规范</h3>
<p>单元测试文件名命名规范为 example_test.go 测试用例的函数名称必须以 Test 开头，例如：TestExample 每个重要的函数都要首先编写测试用例，测试用例和正规代码一起提交方便进行回归测试 。</p>
<p><img src="https://img-blog.csdnimg.cn/img_convert/ac608a3091d7402f5ce0b56f57c10598.png" alt=""></p>

                </div><div><div></div></div>
                <link href="https://csdnimg.cn/release/blogv2/dist/mdeditor/css/editerView/markdown_views-98b95bb57c.css" rel="stylesheet">
                <link href="https://csdnimg.cn/release/blogv2/dist/mdeditor/css/style-c216769e99.css" rel="stylesheet">
        </div>

## 如何编写go代码

```go
package user
//新建一个user目录，目录下面创建一个user.go
// Hello 如果要外部能够调用必须大写开头
func Hello() string {
  return "呵呵"
}

```

```go
package main

import (
 "awesomeProject/user"
 "fmt"
)

// 调用
func main() {
 s := user.Hello()
 fmt.Print(s)
}


```

## 声明变量

> Go语言中的变量需要声明后才能使用，同一作用域内不支持重复声明。 并且Go语言的变量声明后

声明变量的语法

```shell
var identifier type
```

* var ：声明变量关键字
* identifier：变量名称
* type ：变量类型

例如

```shell
package  main
import "fmt"
func main(){
  /*var name string
  var age int 
  var m bool*/
  
  var(
    name string
    age int 
    m bool
  )
  print(name)
  print(age)
  print(m)
}
```

#### 变量的初始化

> 语言在声明变量的时候，会自动对变量对应的内存区域进行初始化操作。每个变量会被初始化成其类型的默认
> 值，例如：整型和浮点型变量的默认值为`0`。字符串变量的默认值为空字符串""。布尔型变量默认为`false`。
> 切片、函数、指针变量的默认为`nil`

变国初始化语法

```go
var变量名类现=表达式
```

例如

```go
package main
func main() {
  var name string ="baidu"
  var site string ="www.baidu.com"
  var age int = 30
}
```

##### 类型推导

> 我们在声明变量时，可以根据初始化值进行类型推导，从而省略类型。

```go
package main
func main() {
  var name="baidu"
  var site="www.baidu.com"
  var age int = 30
}
```

##### 初始化多个变量

> 可以一次性多个变量，中间用逗号分隔

```go
package main
func main() {
  var name,site,age="baidu","www.baidu.com",30
}
```

##### 短变量声明

> 在函数内部，可以用:=运算符对变量进行声明和初始化。

```go
package main
func main() {
  name:="baidu"
  site:="www.baidu.com"
  age:= 30
}
```

> 注意这种方式只适合在函数内部，函数外部不能使用

##### 匿名变量

> 如果我们接收多个变量，有一些变量用不到，可以使用下划线_表示变量名称，这种变量叫做匿名变量。例如

```go
package main

import "fmt"

func getNameAndAge() (string, int) {
 return "小白", 14
}

func main() {
    //不需要使用的可以用匿名变量来代替
 name, _ := getNameAndAge()
 fmt.Printf("%v", name)

}

```

## 语言常量

> 常量，就是在程序编译阶段就确定下来的值，而程序在运行时则无法改变该值。在G。程序中，常量可以是数值类
> 型（包括整型、浮点型和复数类型）I布尔类型、字符串类型等。

#### 定义常量的语法

定义一个常量使用const关键字，语法格式如下:

```go
const constantName (type]= value
```

`const` :定义常量关键字

`constantName` :常量名称

`type` :常量类型

`value` :常量的值

```go
package main
func main() {
  const PI float64 = 3.14
  const PI2 = 3.1415 //可以省略类型
  const (
  width = 100
  height = 200
  )
  const w,h=200,300
```

#### iota

> iota比较特殊，可以被认为是一个可被编译器修改的常量，它默认开始值是0,每调用一次加1遇到`const`关
> 键字时被重置为0.

实例

```go
package main
import 'fmf
func main() {
  const (
  a1 = iota
  a2 = iota
  a3 = iota
  fmt.Printf("a1: %v\n",a1)
  fmt.Printf("a2: %v\n", a2)
  fmt.Printf("a3: %v\n", a3)
}
```

运行结果

```text
0
1
2
```

#### 使用`-`跳过某些值

```go
package main
import 'fmt'
func main() {
  const (
  a1 = iota
  _
  a2 = iota
  )
  fmt.Printf("a1: %v\n",a1)
  fmt.Printf("a2: %v\n", a2)
}
```

运行结果

```text
a1: 0
a2: 2
```

#### `iota`声明中间插队

```go
package main
import 'fmt'

func main() {
  const (
  a1 = iota
  a2 = 200
  a3 = iota
  )
  fmt.Printf("a1: %v\n",a1)
  fmt.Printf("a2: %v\n", a2)
  fmt.Printf("a3: %v\n", a3)
```

运行结果

```text
a1: 0
a2: 200
a3: 2
```

## go语言数据类型

在 Go 编程语言中，数据类型用于声明函数和变量。

数据类型的出现是为了把数据分成所需内存大小,不同的数据，编程的时候需要用大数据的时候才需要申请大内存，就可以充分利用内存。

Go 语言按类别有以下几种数据类型：

| 序号 |                          类型和描述                          |
| :--: | :----------------------------------------------------------: |
|  1   | 布尔型 布尔型的值只可以是常量true或者false。一个简单的例子：var b bool = true。 |
|  2   | 数字类型整型mt和浮点型float32、float64, G。语言支持整型甲浮点型数字，并且支持复数，其中位的 运算采用补码 |
|  3   | 字符串类型:字符串就是一串固定长度的字符连接起来的字符序列。G。的字符串是由单个字节连接起来 的。G。语言的字符串的字节使用@e8编码标识Unicode文本 |
|  4   | 派生类型:包括：⑵指针类型(Pointer) (b)数组类型(c)结构化类型(struct)(d) Channel类型(e)函数类型 ⑴切片类型(g)接口类型(interface) (h) Map类型 |

#### 数字类型

Go也有基于架构的类型，例如：int、Gnt和uintptr

| 序号 |                          类型和描述                          |
| :--: | :----------------------------------------------------------: |
|  1   |                  uint8 无符号8位8理(0到255)                  |
|  2   |                uint16无符号16位整型(0到65535)                |
|  3   |           uint32 无符号 32 位整型(0 到 4294967295)           |
|  4   |      uint64 无符号 64 位整型(0 到 18446744073709551615)      |
|  5   |                 int8有符号8位整型(-128到127)                 |
|  6   |              int16有符号16位整型(-32768到32767)              |
|  7   |       int32有符号 32 位整型(-2147483648 到 2147483647)       |
|  8   | int64 有符号 64 位整型(-9223372036854775808 到 9223372036854775807) |

#### 浮点型

| 序号 |          类型和描述           |
| :--: | :---------------------------: |
|  1   | float32 IEEE-754 32位浮点里数 |
|  2   | float64 IEEE-754 64位浮点型数 |
|  3   |   complex64 32位实数和虚数    |
|  4   |   complex128 64位实数和虚数   |

#### 其他数字类型

以下列出了其他更多的雅字类型:

| 序号 |             类型和描述              |
| :--: | :---------------------------------: |
|  1   |           byte 类似 uint8           |
|  2   |            rune类型int32            |
|  3   |            uint32或64位             |
|  4   |          int与uint一样大小          |
|  5   | uintptr无符号整型，用于存放一个指针 |

## 语言布尔类型

> go 语言中的布尔类型有两个常量值：true和false.布尔类型经常用在*条件判断*语句，或者*循环语句*，也可以用在*逻辑表达式*中。

#### 布尔类型

```go
package main

import "fmt"

func main() {
 var b1 bool = true
 var b2 bool = false
 var b3 = true
 var b4 = false
 b5 := true
 b6 := false
 fmt.Printf("b1: %v\n", b1)
 fmt.Printf("b2: %v\n", b2)
 fmt.Printf("b3: %v\n", b3)
 fmt.Printf("b4: %v\n", b4)
 fmt.Printf("b5: %v\n", b5)
 fmt.Printf("b6: %v\n", b6)
}

```

运行结果

```text
b1: true
b2: false
b3: true
b4: false
b5: true
b6: false
```

## go语言数字类型

Go语言支持整型和浮点型数字，并且原生支持复数，其中位的运算采用不H马。<br>
Go也有基于架构的类型，例如：`int`、`uint`和`uintptr` 。<br>
这些类型的长度都是根据运行程序所在的操作系统类型所决定的：<br>

* `int`和`uint`在32位操作系统上，它们均使用32位(4个字节)，在64位操作系统上，它们均使用64位(8个字节)。
* `uintptr`的长度被设定为足够存放一个指针即可。

Go语言中没有`float`类型。(Go语言中只有`float32`和`float64` )没有double类型。<br>
与操作系统架构无关的类型都有固定的大小，并在类型的名称中就可以看出来：<br>
整数：

* jnt8 (-128 -> 127)
* intl6 (-32768 -> 32767)
* int32 (-2,147,483,648 -> 2,147,483,647)
* int64 (-9,223,372,036,854,775,808 -> 9,223,372,036,854,775,807)

无符号整数：

* uint8 (0 -> 255)
* uintl6 (0 -> 65,535)
* Uint32 (0 -> 4,294,967,295)
* uint64 (0 -> 18,446,744,073,709,551,615)

浮点型(IEEE-754标准)：

* float32 (+- le-45 -> +-3.4 * le38)
* float64 (+- 5 *le-324 -> 107* le308)

int类型是计算最快的一种类型<br>
整型的零值是0，浮点型的零值是0.0

###### 实例

下面实例演示了，各个数字类型的长度和取值范围

```go
package main

import (
 "fmt"
 "math"
 "unsafe"
)

func main() {
 var i8 int
 var i16 int16
 var i32 int32
 var i64 int64
 var ui8 uint8
 var ui16 uint16
 var ui32 uint32
 var ui64 uint64
 fmt.Printf("%T %dB %v~%v\n", i8, unsafe.Sizeof(i8), math.MinInt8, math.MaxInt8)
 fmt.Printf("%T %dB %v~%v\n", i16, unsafe.Sizeof(i16), math.MinInt16, math.MaxInt16)
 fmt.Printf("%T %dB %v~%v\n", i32, unsafe.Sizeof(i32), math.MinInt32, math.MaxInt32)
 fmt.Printf("%T %dB %v~%v\n", i64, unsafe.Sizeof(i64), math.MinInt64, math.MaxInt64)
 fmt.Printf("%T %dB %v~%v\n", ui8, unsafe.Sizeof(ui8), 0, math.MaxUint8)
 fmt.Printf("%T %dB %v~%v\n", ui16, unsafe.Sizeof(ui16), 0, math.MaxUint16)
 fmt.Printf("%T %dB %v~%v\n", ui32, unsafe.Sizeof(ui32), 0, math.MaxUint32)
 fmt.Printf("%T %dB %v~%v\n", ui64, unsafe.Sizeof(ui64), 0, uint64(math.MaxUint64))

 var f32 float32
 var f64 float64

 fmt.Printf("%T %dB %v~%v\n", f32, unsafe.Sizeof(f32), -math.MaxFloat32, math.MaxFloat32)
 fmt.Printf("%T %dB %v~%v\n", f64, unsafe.Sizeof(f64), -math.MaxFloat64, math.MaxFloat64)

 var ui uint
 ui = uint(math.MaxUint64) //在+1会导致overflows错误
 fmt.Printf("%T %dB %v~%v\n", ui, unsafe.Sizeof(ui), 0, ui)

 var imax, imin int
 imax = int(math.MaxInt64) //在+1会导致overflows错误
 imin = int(math.MinInt64) //在+1会导致overflows错误
 fmt.Printf("%T %dB %v~%v\n", imax, unsafe.Sizeof(imax), imin, imax)
}

```

运行结果

```text
int 8B -128~127
int16 2B -32768~32767
int32 4B -2147483648~2147483647
int64 8B -9223372036854775808~9223372036854775807
uint8 1B 0~255
uint16 2B 0~65535
uint32 4B 0~4294967295
uint64 8B 0~18446744073709551615
float32 4B -3.4028234663852886e+38~3.4028234663852886e+38
float64 8B -1.7976931348623157e+308~1.7976931348623157e+308
uint 8B 0~18446744073709551615
int 8B -9223372036854775808~9223372036854775807
```

#### 以二进制.八进制或十六进制浮点数的格式定义数字

```go
package main

import (
 "fmt"
)

func main() {
 //十进制
 var a int = 10
 fmt.Printf("%d \n", a) //10
 fmt.Printf("%b \n", a) //1010 占位符%b表示二进制
 //八进制以0开头
 var b int = 077
 fmt.Printf("%o \n", b) // 77
 //十六进制以0x开头
 var c int = 0xff
 fmt.Printf("%x \n", c) // ff
 fmt.Printf("%X \n", c) // FF
}

```

运行结果

```text
10
1010
77
ff
FF
```

#### 浮点型

GO语言支持两种浮点型数：`float32`和`float64`。这两种浮点型数据格式遵循`IEEE 754`标准：`float32`的浮
点数的最大范围约为`3.4e38`,可以使用常量定义：`math.MaxFloat32`。`float64`的浮点数的最大范围约为
`1.8e308` ,可以使用一个常量定义：`math.MaxFloat64`

打印浮点数时，可以使用`fmt`包配合动词%f ,代码如下:

```go
package main

import (
 "fmt"
 "math"
)

func main() {
 fmt.Printf("%f\n", math.Pi)
 fmt.Printf("%.2f\n", math.Pi)
}

```

#### 复数

complex64 和 complex128

```go
package main

import (
 "fmt"
)

func main() {
 var c1 complex64
 c1 = 1 + 2i
 var c2 complex128
 c2 = 2 + 3i
 fmt.Println(c1)
 fmt.Println(c2)
}

```

复数有实部和虚部，complex64的实部和虚部为32位，complex128的实部和虚部为64位。

## golang字符串

Go语言字符串是任意*字节常量序号*

#### go语言字符串字面量

> 在GO语言中，字符串字面量使用双引号 或者反引号 来创建.双引号用来创建可解析的字符串，支持转义，<br>
> 但不能用来引用多行；反引号用来创建原生的字符串字面量，可能由多行组成，但不支持转义，并且可以包含除了<br>
> 反引号外其他所有字符.双引号创建可解析的字符串应用最广泛，反引号用来创建原生的字符串则多用于书写多行<br>
> 消息，HTML以及正则表达式<br>

```go
package main

import (
 "fmt"
)

func main() {
 var str1 string = "hello world"
 var html string = `
 <html>
   <head><title>hello golang</title>
 </html>`
 fmt.Printf("str1: %v\n", str1)
 fmt.Printf("html: %v\n", html)
}

```

运行结果

```text
str1: hello world
html:
        <html>
          <head><title>hello golang</title>
        </html>
```

#### GO语言字符串连接

使用加号

虽然Go语言中的字符串是不可变的，但是字符串支持+级联操作和+二追加操作，例如:

```go
package main

import (
 "fmt"
)

func main() {
 name := "tom"
 age := "20"
 msg := name + age
 fmt.Printf("msg: %v\n", msg)
 fmt.Println("-------------")
 msg = ""
 msg += name
 msg += ""
 msg += age
 fmt.Printf("msg： %v\n", msg)
}

```

golang里面的字符串都是不可变的,每次运算都会产生一个新的字符串，所以会产生很多临时的无用的字符
串，不仅没有用，还会给gc带来额外的负担，所以性能比较差

###### 使用`fmt.Sprintf()`函数

```go
package main

import (
 "fmt"
)

func main() {
 name := "tom"
 age := "20"
 msg := fmt.Sprintf("%s,%s", name, age)
 fmt.Printf("msg： %v\n", msg)
}

```

运行结果

```text
msg： tom,20
```

内部使用[]byte实现，不像直接运算符这种产生很多临时的字符串，但是内部的逻辑比较复杂，有很多额外的判断，还用到了interface，所以性能也不是很好

###### `strings.Join()`

```go
package main

import (
 "fmt"
 "strings"
)

func main() {
 name := "tom"
 age := "20"
 msg := strings.Join([]string{name, age}, ",")
 fmt.Printf("msg： %v\n", msg)
}

```

> join会先根据字符串数组的内容，计算出一个拼接之后的长度，然后申请对应大小的内存，一个一个字符串填
> 入，在已有一个数组的情况下，这种效率会很高，但是本来没有，去构造这个数据的代价也不小

###### `buffer.WriteString()`

```go
package main

import (
 "bytes"
 "fmt"
)

func main() {
 var buffer bytes.Buffer
 buffer.WriteString("tom")
 buffer.WriteString(",")
 buffer.WriteString("20")
 fmt.Printf("msg： %v\n", buffer.String())
}

```

> 这个比较理想，可以当成可变字符使用，对内存的增长也有优化，如果能预估字符串的长度，还可以用 buffer.Grow()接口来设置
> capacity

#### 语言字符串转义字符

Go语言的字符串常见专义符包含回车、换行、单双引号、制表符等，如下表所示。

| 转义符 |                含义                |
| :----: | :--------------------------------: |
|   \r   |         回车符（返回行首）         |
|   \n   | 换行符（直接跳到下一行的同列位置） |
|   \t   |               制表符               |
|   \'   |               单引号               |
|   \"   |               双引号               |
|   \\   |               反斜杠               |

#### GO语言字符串切片操作

```go
package main

import (
 "fmt"
)

func main() {
 str := "hello world"
 n := 3
 m := 5
 fmt.Println(str[n])   //获取字符串索引位置为n的原始字节
 fmt.Println(str[n:m]) //鼓取得字符串索引位置为n到m-1的字符串
 fmt.Println(str[n:])  //鼓取得字符串索引位置为n到len(s)-1的字符串
 fmt.Println(str[:m])  //裁取得字符串索引位置为0到m-1的字符串
}

```

运行结果

```text
108
lo
lo world
hello
```

#### go语言字符串常用方法

|                方法                 |      介绍      |
| :---------------------------------: | :------------: |
|              len (str)              |     求长度     |
|           +或fmt.Sprintf            |   拼接字符串   |
|            strings.Split            |      分割      |
|          strings.Contains           |  判断是否包含  |
| strings.HasPrefix,strings.HasSuffix | 前缀/后缀判断  |
| strings.Index(),strings.LastIndex() | 子串出现的位置 |
| strings.Join(a[]string,sep string)  |    join操作    |

实例

```go
package main

import (
 "fmt"
 "strings"
)

func main() {
 s := "hello world!"
 fmt.Printf("len(s): %v\n", len(s))
 fmt.Printf("strings.Split(s, \"\"): %v\n", strings.Split(s, ""))
 fmt.Printf("strings.Contains(s, \"hello\"): %v\n", strings.Contains(s, "hello"))
 fmt.Printf("strings.HasPrefix(s, \"hello\"): %v\n", strings.HasPrefix(s, "hello"))
 fmt.Printf("strings.HasSuffix(s, \"world! \"): %v\n", strings.HasSuffix(s, "world!"))
 fmt.Printf("strings.Index(s, \"1\"): %v\n", strings.Index(s, "l"))
 fmt.Printf("strings.Lastlndex(s, \"1\"): %v\n", strings.LastIndex(s, "l"))
}

```

运行结果

```text
strings.Split(s, ""): [h e l l o   w o r l d !]
strings.Contains(s, "hello"): true
strings.HasPrefix(s, "hello"): true
strings.HasSuffix(s, "world! "): true
strings.Index(s, "1"): 2
strings.Lastlndex(s, "1"): 9
```

## golang格式化输出

下面实例使用到的结构体

```go
type Website struct {
  Name string
}
  //定义结构体变量
  var site = Webslte{Name: "duoke360"}
```

#### 占位符

* 普通占位符

| 占位符 |                             说明                             |                      举例                      |             输出              |
| :----: | :----------------------------------------------------------: | :--------------------------------------------: | :---------------------------: |
|   %v   | 相应值的默认格式.在打印结构体时."加号"标汜（%+v）会添加字段名 | fmt.Printf("%v", site) fmt.Printf("%+v", site) |   duoke360} {Name:duoke360    |
|  %#v   |                         相应值和类型                         |            fmt.Printf("%#v", site)             | main.Webslte{Name:"duoke360"} |
|   %T   |                         相应值的类型                         |             fmt.Printf("%T", site)             |         main.Webslte          |
|   %%   |                字面上的百分号，并非值的占位符                |                fmt.Printf("%%")                |               %               |

* 布尔占位符

| 占位符 |      说明       |          举例          | 输出 |
| :----: | :-------------: | :--------------------: | :--: |
|   %t   | 单词true和false | fmt.Printf("%t", true) | true |

* 整数占位符

| 占位符 |                    说明                    |           举例           |  输出  |
| :----: | :----------------------------------------: | :----------------------: | :----: |
|   %b   |                   二进制                   |   fmt.Printf("%b", 5)    |  101   |
|   %c   |              相应的Unicode码               | fmt.Printf("%c", 0x4E2D) |   中   |
|   %d   |                   十进制                   |  fmt.Printf("%d", 0x12)  |   18   |
|   %o   |                   八进制                   |   fmt.Printf("%o", 10)   |   12   |
|   %q   | 单引号围绕的字符字面值，由go语言安全的专义 | fmt.Printf("%q", 0x4E2D) |  '中'  |
|   %x   |        十六进制，字母形式为小写 a-f        |   fmt.Printf("%x", 13)   |   d    |
|   %X   |        十六进制，字母形式为大写 A-F        |   fmt.Printf("%X", 13)   |   D    |
|   %U   |    Unicode格式，U+1234，等同于"U+%04X"     |  fmt.Printf("%t", true)  | U+4E2D |

* 浮点数和复数的组成部分（实部和虚部）

| 占位符 |                             说明                             |            举例            |     输出     |
| :----: | :----------------------------------------------------------: | :------------------------: | :----------: |
|   %b   | 无小数部分的，指数为2的幂的科学计数法，与strconv.FormatFloat的'b'转换格式一致例如-123456p-78 |                            |              |
|   %e   |                科学计数法，例如-1234.456e+78                 |   fmt.Printf("%e", 10.2)   | 1.020000e+01 |
|   %E   |                科学计数法，例如-1234.456E+78                 |   fmt.Printf("%E", 10.2)   | 1.020000E+01 |
|   %f   |                有小数点而无指数，例如123.456                 |   fmt.Printf("%f", 10.2)   |  10.200000   |
|   %g   |         根据情况选择%e或%f以产生更紧凑的(无末尾的0)          |  fmt.Printf("%g", 10.20)   |     10.2     |
|   %G   |         根据情况选择%E或%f以产生更紧凑的(无末尾的0)          | fmt.Printf("%G", 10.20+2i) |   10.20+2i   |

* 字符串与字节切片

| 占位符 |                  说明                  |                举例                |     输出     |
| :----: | :------------------------------------: | :--------------------------------: | :----------: |
|   %s   |   输出字符串表示(string类型或[]byte)   | fmt.Printf("%s", []byte("多课网")) |    多课网    |
|   %q   | 双引号围绕的字符串，由Go语法安全地转义 |     fmt.Printf("%q", "多课网")     |   "多课网"   |
|   %x   |   十六进制，小写字母，每字节两个字符   |     fmt.Printf("%x", "golang")     | 676f6c616e67 |
|   %X   |   十六进制，小写字母，每字节两个字符   |     fmt.Printf("%X", "golang")     | 676F6C616E67 |

* 指针

| 占位符 |         说明         |          举例          |   输出   |
| :----: | :------------------: | :--------------------: | :------: |
|   %p   | 十六进制表示，前缀θx | fmt.Printf("%p",&site) | 0x4f57f0 |

## GO语言运算符

Go语言内置的运算符有:

* 1.算术运算符
* 2.关系运算符
* 3.逻辑运算符
* 4.位运算符
* 5.赋值运算符

#### 算术运算符

| 运算符 | 描述 |
| :----: | :--: |
|   +    | 相加 |
|   -    | 相减 |
|   *    | 相乘 |
|   /    | 相除 |
|   %    | 取余 |

注意: `++` (自增) 和`--` (自减) 在Go语言中是单独的语句，并不是运算符。

实例

```go
package main

import "fmt"

func main() {
 a := 100
 b := 10
 fmt.Printf("(a + b): %V\n", (a + b))
 fmt.Printf("(a一b): %V\n", (a - b))
 fmt.Printf("(a★b): %v\n", (a * b))
 fmt.Printf("(a / b): %V\n", (a / b))
 fmt.Printf("(a %% b): %V\n", (a % b))
 a++
 fmt.Printf("a: %V\n", a)
 b--
 fmt.Printf("b: %V\n", b)
}

```

#### 关系运算符

| 运算符 |                            描述                             |
| :----: | :---------------------------------------------------------: |
|   ==   |     检查两个值是否相等,如果相等返回True否则返回False。      |
|   !=   |   检查两个值是否不相等，如果不相等返回True否则返回False.    |
|   \>   |   检查左边值是否大于右边值，如果是返回True否则返回False。   |
|  \>=   | 检查左边值是否大于等于右边值，如果是返回True否则返回False。 |
|   <    |   检查左边值是否小于右边值，如果是返回True否则返回False。   |
|   <=   | 检查左边值是否小于等于右边值，如果是返回True否则返回False。 |

实例

```go
package main

import "fmt"

func main() {
 a := 1
 b := 2
 fmt.Printf("(a > b): %V\n", (a > b))
 fmt.Printf("(a < b): %V\n", (a < b))
 fmt.Printf("(a >= b): %V\n", (a >= b))
 fmt.Printf("(a <= b): %V\n", (a <= b))
 fmt.Printf("(a == b): %V\n", (a == b))
 fmt.Printf("(a != b): %V\n", (a != b))
}

```

#### 逻辑运算符

| 运算符 |                             描述                             |
| :----: | :----------------------------------------------------------: |
|   &&   | 逻辑AND运算符。如果两边的操作数都是True,则为True,否则为False。 |
|  \|\|  | 逻辑OR运算符。如果两边的操作数有一个True,则为True,否则为False。 |
|   !    |     逻辑NOT运算符。如果条件为True,则为False,否则为True。     |

实例

```go
package main

import "fmt"

func main() {
 a := true
 b := false
 fmt.Printf("(a && b): %V\n", (a && b))
 fmt.Printf("(a 11 b): %V\n", (a || b))
 fmt.Printf("(!a): %V\n", (!a))
 fmt.Printf("(!b): %V\n", (!b))
}

```

#### 位运算符

位运算符对整数在内存中的二进制位进行操作。

| 运算符 |                             描述                             |
| :----: | :----------------------------------------------------------: |
|   &    |     参与运算的两数各对应的二进位相与。(两位均为1才为1)。     |
|   \|   |  参与运算的两数各对应的二进位相或。(两位有一 个为1就为1)。   |
|   ^    | 参与运算的两数各对应的_进位相异或，当两对应的二进位相异时，结果为1。(两位不- 样则为。 |
|   <<   | 左移n位就是乘以2的n次方。“a<<b"是把a的各 二进位全部左移b位，高位丢弃，低位补0。 |
|  \>>   | 右移n位就是除以2的n次方。“a>>b”是把a的各二 进位全部右移b位。 |

实例

```go
package main

import "fmt"

func main() {
 a := 4 //二进制100
 fmt.Printf("I: %b\n", a)
 b := 8 //二进制1000
 fmt.Printf("b: %b\n", b)
 fmt.Printf("(a & b): %V， %b \n", (a & b), (a & b))
 fmt.Printf("(a | b): %V，%b\n", (a | b), (a | b))
 fmt.Printf("(a ^ b): %v，%b\n", (a ^ b), (a ^ b))
 fmt.Printf("(a << 2): %V，%b\n", (a << 2), (a << 2))
 fmt.Printf("(b >> 2): %V，%b\n", (b >> 2), (b >> 2))
}

```

#### 赋值运算符

| 运算符 |                      描述                      |
| :----: | :--------------------------------------------: |
|   =    | 简单的赋值运算符，将一个表达式的值赋给一个左值 |
|   +=   |                  相加后再赋值                  |
|   -=   |                  相减后再赋值                  |
|   *=   |                  相乘后再赋值                  |
|   /=   |                  相除后再赋值                  |
|   %=   |                  求余后再赋值                  |
|  <<=   |                   左移后赋值                   |
|  \>>=  |                   右移后赋值                   |
|  \|=   |                  按位与后赋值                  |
|   ^=   |                 按位异或后赋值                 |

实例

```go
package main

import "fmt"

func main() {
 var a int
 a = 100
 fmt.Printf("a: %v\n", a)
 a += 1 //a=a+1
 fmt.Printf("a: %v\n", a)
 a -= 1 //a=a-1
 fmt.Printf("a: %V\n", a)
 a *= 2 //a=a*2
 fmt.Printf("a: %V\n", a)
 a /= 2 //a=a/2
 fmt.Printf("a: %V\n", a)
}

```

## go语言中的流程控制

#### go语言中的条件

> 条件语句是用来判断给定的条件是否满足(表达式值是否为true或者false ),并根据判断的结果(真或假)决定执行的语句，go语言中的条件语句也是这样的。

###### go语言中的条件语句包含如下几种情况

1. if语句: if语句由一个布尔表达式后紧跟一 个或多个语句组成。<br>
2. ...else 语句: if语句后可以使用可选的else 语句，else 语句中的表达式在布尔表达式为false 时执行<br>
3. if 嵌套语句:你可以在if或else if语句中嵌入一个或多个if或else if语句。<br>
4. switch 语句: switch 语句用于基于不同条件执行不同动作。<br>
5. select 语句: select语句类似于switch
   语句，但是select会随机执行一个可运行的case.如果没有case可运行，它将阻塞，直到有case可运行。<br>

#### go语言中的循环语句

go语言中的循环只有for循环，去除了while、do while 循环，使用起来更加简洁。

1. for循环。<br>
2. for range循环。<br>

go语言中的流程控制关键字

1. break<br>
2. continue<br>
3. goto<br>

## go语言if语句语法

```go
if布尔表达式{
  /*在布尔表达式为true 时执行*/
}
```

> 注意:在go语言中布尔表达式不用使用括号。

go语言if语句实例演示

```go
package main

import "fmt"

func main() {
 var flag = true
 if flag {
  fmt.Print("flag is true")
 }
 fmt.Print("程序结束")
}

```

运行结果

```text
flag is true
程序结束
```

> 初始变量可以声明在布尔表达式里面， 注意它的作用域

```go
package main

import "fmt"

func main() {
 if age := 20; age > 18 {
  fmt.Println("flag is true")
 }
 fmt.Println("程序结束")
}
```

`注意:不能使用0或非0表示真假`

```go
func test4() {
  var i=1
  if i {//编译失败
    fmt.Println("here")
    }
  fmt.Printf("程序运行结束")
}
```

go语言if语句使用提示:

* 1.不需使用括号将条件包含起来
* 2.大括号{}必须存在，即使只有一行语句
* 3.左括号必须在if或else的同- -行
* 4.在if之后，条件语句之前，可以添加变量初始化语句，使用;进行分隔

## golang中的if else语句

go语言中的if else语句可以根据给定条件*二选一*。

#### go语言的if else语句语法

```go
if 布尔表达式 {
    /*在布尔表达式为true 时执行*/
}else{
    /* 在布尔表达式为 false时执行*/
}
```

go语言if else语句实例

```go
package main

func main() {
 a := 1
 b := 2
 if a > b {
  println("a大于b")
 } else {
  println("a小于等于b")
 }
}

```

###### 特殊语法

```go
package main

import "fmt"

func main() {
 if age := 20; age >= 18 {
  fmt.Println("你是成年人")
 } else {
  fmt.Println("你还未成年")
 }
}

```

go语言if语句使用提示:

* 1.不需使用括号将条件包含起来
* 2.大括号{}必须存在，即使只有一行语句
* 3.左括号必须在if或else的同一行
* 4.在if之后，条件语句之前，可以添加变量初始化语句，使用:进行分隔
* 5.在有返回值的函数中，最终的return不能在条件语句中

## golang中的if else if语句

go语言if语句可以进行多重嵌套使用，进行多重判断。

#### go语言中的if else if语法

```go
if 布尔表达式1 {
  // do something
} else if 布尔表达式2 {
  // do something else
}else {
  // catch-all or default
}
```

go语言中的if else if语法实例

```go
package main

func main() {
 score := 80
 if score >= 60 && score <= 70 {
  println("C")
 } else if score > 70 && score <= 90 {
  println("B")
 } else {
  println("A")
 }
}

```

###### 特殊语法

```go
package main

func main() {
 if score := 80;score >= 60 && score <= 70 {
  println("C")
 } else if score > 70 && score <= 90 {
  println("B")
 } else {
  println("A")
 }
}

```

## golang switch语句

go语言中的`switch`语句，可以非常容易的判断多个值的情况。

#### go语言中switch语句的语法

```go
switch var1 {
  case val1:
    ...
  case va12 :
    ...
   default:
    ...
}
```

go语言中switch语句实例

```go
package main

import "fmt"

func main() {
 grade := "A"
 switch grade {
 case "A":
  fmt.Println("优秀")
 case "B":
  fmt.Println("良好")
 default:
  fmt.Println("一般")
 }
}

```

###### 多条件匹配

```go
package main

import "fmt"

func main() {
 day := 3
 switch day {
 case 1,2,3,4,5:
  fmt.Println("z工作日")
 case 6,7:
  fmt.Println("休息日")
 default:
  fmt.Println("非法输入")
 }
}

```

###### case可以是条件表达式

```go
package main

import "fmt"

func main() {
 score := 90
 switch {
 case score >= 90:
  fmt.Println("享受假期")
 case score < 90 && score >= 80:
  fmt.Println("好好学习吧!")
 default:
  fmt.Println("玩命学习! ")
 }
}
```

###### `fallthrough`可以可以执行满足条件的下一个`case`

```go
package main

import "fmt"

func main() {
 a := 100
 switch a {
 case 100:
  fmt.Println("100")
  fallthrough
 case 200:
  fmt.Println("200")
 case 300:
  fmt.Println("300")
 default:
  fmt.Println("other")
 }
}

```

运行结果

```text
100
200
```

## golang for循环语句

go语言中的`for`循环，只有`for`关键字，去除了像其他语言中的`while`和`do while` .

#### go语言for循环语法

```go
for 初始语句;条件表达式;结束语句{
  循环体语句
}
```

> 注意: for表达式不用加括号

go语言for循环实例

```go
package main

func main() {
 for i := 0; i < 10; i++ {
  println(i)
 }
}

```

###### 初始条件,可以写到外面

```go
package main

func main() {
    i := 0
 for ; i < 10; i++ {
  println(i)
 }
}
```

###### 初始条件和结束条件都可以省略

```go
package main

func main() {
    i :=1 //初始条件
 for i <= 10{
  println(i)
  i++
 }
}
```

###### 这种情况类似其他语言中的`while`循环

```go
package main

func main() {
 for{
  println("我一直在执行~")
 }
}
```

###### for循环可以通过`break`、`goto`、 `return`、 `panic` 语句强制退出循环

## golang for range循环

Go语言中可以使用`for range` 遍历数组、切片、字符串、map 及通道(channel) 。通过`for range` 遍历的返回值有以下规律:

* 1.数组、切片I字符串返回索弓和值。
* 2.map返回键和值。
* 3.通道(channel) 只返回通道内的值。

go语言for range实例

```go
package main

import "fmt"

func main() {
 var a = [5]int{1, 2, 3, 4, 5}
 for i, v := range a {
  fmt.Printf("1: %d，v: %V\n", i, v)
 }
  //匿名变量用来表示不需要使用
 //for _, v := range a {
 // fmt.Printf(v)
 //}
}

```

## golang流程控制关键字break

`break`语句可以结束`for`、`switch` 和`select`的代码块。

#### go语言使用break注意事项

* 1.单独在`select`中使用break和不使用break没有啥区别。
* 2.单独在表达式`switch`语询,并且没有`fallthough`,使用`break`和不使用`break`没有啥区别。
* 3.单独在表达式`switch`语句,并且有`fallthough`，使用`break`能够终止`fallthough`后面的`case`语句的执行
* 4.带标签的`break`，可以跳出多层`select`/`switch` 作用域。让`break`更加灵活,写法更加简单灵活，不需要使用控制变量- -层-
  层跳出循环,没有带`break`的只能跳出当前语句块。

go语言break关键字实例

```go
package main

func main() {
 for i := 0; i < 10; i++ {
  if i == 5 {
   break
  }
  println(i)
 }
}
```

## golang关键字continue

`continue`只能用在循环中，在go中只能用在`for`循环中，它可以终止本次循环，进行下一-次循环。

在`continue`语句后添加际签时，表示开始标签对应的循环。

#### go语言continue实例

```go
package main

func main() {
 for i := 0; i < 10; i++ {
  if i%2 == 0 {
  } else {
   continue
  }
  println(i)
 }
}
```

## golang流程控制关键字goto

`goto`语句通过标签进行代码间的无条件跳转。`goto` 语句可以在快速跳出循环、避免重复退出上有-定的帮助。Go语言中使用goto语句能简化一些代码的实现过程。
例如双层嵌套的for循环要退出时:

go语言关键字goto实例

```go
package main

func main() {
 a := 0
 if a == 1 {
  goto LABEL
 } else {
  println("aaaa")
 }
LABEL:
 println("LABEL")
}

```

## golang数组

数组是相同数据类型的一组数据的集合,数组-定义长度不能修改，数组可以通过下标(或者叫索引)来访问元素。

#### go语言数组的定义

```go
var variable_ name [SIZE] variable_type
variable_name: 数组名称
SIZE :数组长度,必须是常量
variabl_type :数组保存元素的类型
```

```go
package main

import "fmt"

func main() {
 var a [3]int    //定义一个int类型的数组a.长度是3
 var s [2]string //定义一个字符串类型的数组s，长度是2

 fmt.Printf("a: %T\n", a)
 fmt.Printf("s: %T\n", s)
}

```

###### 使用初始化列表

```go
package main

import "fmt"

func main() {
 var a = [3]int{1, 2, 3}
 var b = [2]string{"tom", "kite"}
 var c = [2]bool{true, false}
 a1 := [2]int{1, 2} //类型推断
 fmt.Printf("a: %T\n", a)
 fmt.Printf("b: %T\n", b)
 fmt.Printf("c: %T\n", c)
 fmt.Printf("a1: %T\n", a1)
}

```

运行结果

```text
a: [3]int
b: [2]string
c: [2]bool
a1: [2]int
```

使用初始化列表，就是将值写在*大括号*里面。

###### 省略数组长度

> 数组长度可以省略,使用`...`代替,加初始化值得数量自动推断，例如:

```go
package main

import "fmt"

func main() {
 var a = [...]int{1, 2, 3}
 var b = [...]string{"tom", "kite"}
 var c = [...]bool{true, false}
 a1 := [2]int{1, 2} //类型推断
 fmt.Printf("a: %T\n", a)
 fmt.Printf("b: %T\n", b)
 fmt.Printf("c: %T\n", c)
 fmt.Printf("a1: %T\n", a1)
}
```

运行结果

```text
a: [3]int
b: [2]string
c: [2]bool
a1: [2]int
```

###### 指定索引值的方式来初始化

> 可以通过指定所有的方式来初始化,未指定所有的默认未零值。

```go
package main

import "fmt"

func main() {
 var a = [...]int{0: 1, 2: 2}
 var b = [...]string{1: "tom", 2: "kite"}
 var c = [...]bool{2: true, 5: false}
 a1 := [2]int{1, 2} //类型推断
 fmt.Printf("a: %T\n", a)
 fmt.Printf("b: %T\n", b)
 fmt.Printf("c: %T\n", c)
 fmt.Printf("a1: %T\n", a1)
}

```

运行结果

```text
a: [3]int
b: [3]string
c: [6]bool
a1: [2]int
```

#### go语言访问数组元素

可以通过下标的方式，来访问数组元索。数组的最大下标为数组长度1,于这个下标会发生数组越界。

```go
package main

import "fmt"

func main() {
 var a [2]int
 a[0] = 100
 a[1] = 200
 fmt.Printf("a[0]: %V\n", a[0])
 fmt.Printf("a[1]: %V\n", a[1])

 //修改a[e] a[1]
 a[0] = 1
 a[1] = 2
 fmt.Println("-----------")
 fmt.Printf("a[0]: %V\n", a[0])
 fmt.Printf("a[0]: %V\n", a[1])
}

```

运行结果

```text
a[0]: %!V(int=100)
a[1]: %!V(int=200)
-----------
a[0]: %!V(int=1)
a[0]: %!V(int=2)
```

#### 根据数组长度遍历数组

可以根据数组长度，通过for循环的方式来遍历数组,数组的长度可以使用len函数获得。

实例

```go
package main

func main() {
 a := [...]int{1, 2, 3, 4, 5, 6}
 for i := 0; i < len(a); i++ {
  println(a[i])
 }
}

```

运行结果

```text
1
2
3
4
5
6
```

###### 使用`for range` 数组

还可以使用`for range` 循环来遍历数组, range返回数组 下标和对应的值

实例

```go
package main

func main() {
 a := [...]int{1, 2, 3, 4, 5, 6}
 for i,v:=range a{
  println(v)
 }
}

```

## golang切片

> 前面我们学习了数组,数组是固定长度，可以容纳相同数据类型的元素的集合。当长度固定时，使用还是带来一些限制，比如:
> 我们申请的长度太大浪费内存，太小又不够用。

鉴于.上述原因,我们有了go语言的切片，可以把切片理解为,可变长度的数组,其实它底层就是使用数组实现的，增加了自动扩容功能。切片(
Slice) 是一个拥有相同类型元素的可变长度的序列。

#### go语言切片的语法

声明一个切片和声明一个数组类似，只要不添加长度就可以了

```text
var identifier []type

切片是引用类型，可以使用make函数来创建切片:

var slice1 []type = make([]type, 1en)

也可以简写为

slice1 = make([]type，1en)

也可以指定容量，其中capacity为可选参数。

make([]T，length, capacity)

这里len是数组的长度并且也是切片的初始长度。
```

go语言切片实例

```go
package main

import "fmt"

func main() {
 var names []string
 var numbers []int
 fmt.Printf("names: %V\n", names)
 fmt.Printf("numbers: %v\n", numbers)
 fmt.Println(names == nil)
 fmt.Println(numbers == nil)
}

```

运行结果

```text
names: []
numbers: []
true
true
```

#### go语言切片的长度和容量

切片拥有自己的长度和容量,我们可以通过使用内置的len()函数求长度,使用内置的cap()函数求切片的容量。

实例

```go
package main

import "fmt"

func main() {
 var names = []string{"tom", "kite"}
 var numbers = []int{1, 2, 3}
 fmt.Printf("names: %V\n", names)
 fmt.Printf("numbers: %v\n", numbers)
 fmt.Printf("len: %d cap: %d\n", len(names), cap(names))
 fmt.Printf("len: %d cap: %d\n", len(numbers), cap(numbers))
 var s1 = make([]string, 2, 3)
 fmt.Printf("len: %d cap: %d\n", len(s1), cap(s1))
}

```

运行结果

```text
names: [%!V(string=tom) %!V(string=kite)]
numbers: [1 2 3]
len: 2 cap: 2
len: 3 cap: 3
len: 2 cap: 3
```

#### golang切片的初始化

切片的初始化方法很多，可以直接初始化，也可以使用数组初始化等。

###### 直接初始化

```go
package main

import "fmt"

func main() {
 s := []int{1, 2, 3}
 fmt.Printf("s: %V\n", s)
}
```

###### 使用数组初始化

```go
package main

import "fmt"

func main() {
 arr := [...]int{1, 2, 3}
 s1 := arr
 fmt.Printf("s: %v\n", s1)
}

```

###### 使用数组的部分元素初始化(切片表达式)

切片的底层就是一个数组, 所以我们可以基于数组通过切片表达式得到切片。切片表达式中的low和high表示一个索引范围(
左包含,右不包含)，得到的切片 长度=high-low,容量等于得到的切片的底层数组的容量。

```go
package main

import "fmt"

func main() {
 arr := [...]int{1, 2, 3, 4, 5, 6}
 s1 := arr[2:5]
 fmt.Printf("s1: %v\n", s1)
 s2 := arr[2:]
 fmt.Printf("s2: %v\n", s2)
 s3 := arr[:3]
 fmt.Printf("s3: %v\n", s3)
}

```

运行结果

```text
s1: [3 4 5]
s2: [3 4 5 6]
s3: [1 2 3]
```

###### 空(nil)切片

一个切片在末初始化之前默认为nil,长度为0,容量为0.

```go
package main

import "fmt"

func main() {
 var s1 []int
 fmt.Println(s1 == nil)
 fmt.Printf("len: %d，cap: %d\n", len(s1), cap(s1))
}

```

运行结果

```text
true
len: 0，cap: 0
```

#### go语言切片的遍历

切片的遍历和数组的遍历非常类似，可以使用for循环索弓|遍历，或者for range循环。

###### for循环索引遍历

```go
package main

import "fmt"

func main() {
 s1 := []int{1, 2, 3, 4, 5}
 for i := 0; i < len(s1); i++ {
  fmt.Printf("s1[%d]: %v\n", i, s1[i])
 }
}

```

运行结果

```text
s1[0]: 1
s1[1]: 2
s1[2]: 3
s1[3]: 4
s1[4]: 5
```

###### for range循环

```go
package main

import "fmt"

func main() {
 s1 := []int{1, 2, 3, 4, 5}
 for i, v := range s1 {
  fmt.Printf("s1[%d]: %v\n", i, v)
 }
}

```

运行结果

```text
s1[0]: 1
s1[1]: 2
s1[2]: 3
s1[3]: 4
s1[4]: 5
```

## go语言切片元素的添加和删除copy

切片是一个动态数组，可以使用append()函数添加元素，go语言中并没有删除切片元素的专用方法，我们可以使用切片本身的特性来删除元素。由于，切片是引用类型，通过赋值的方式，会修改原有内容，go提供了
copy()函数来拷贝切片

#### 添加元素

```go
package main

import "fmt"

func main() {
 s1 := []int{}
 s1 = append(s1, 1)
 s1 = append(s1, 2)
 s1 = append(s1, 3, 4, 5) //添加多个元素
 fmt.Printf("s1: %v\n", s1)

 s3 := []int{3, 4, 5}
 s4 := []int{1, 2}
 s4 = append(s4, s3...) //添加另外一个切片
 fmt.Printf("s4: %v\n", s4)
}

```

运行结果

```text
s1: [1 2 3 4 5]
s4: [1 2 3 4 5]
```

#### 删除元素

```go
package main

import "fmt"

func main() {
 s1 := []int{1, 2, 3, 4, 5}
 //删除索引为2的元素
 s1 = append(s1[:2], s1[3:]...)
 fmt.Printf("s1: %v\n", s1)
}

```

运行结果

```text
s1: [1 2 4 5]
```

公式:要从切片a中删除索引为`index`的元素,操作方法是`a = append(a[ :index]，a[index+1:]...)`

#### 修改元素

```go
package main

import "fmt"

func main() {
 s1 := []int{1, 2, 3, 4, 5}
 s1[1] = 100
 fmt.Printf("s1: %v\n", s1)
}

```

运行结果

```text
s1: [1 100 3 4 5]
```

#### 查询元素

```go
package main

func main() {
 s1 := []int{1, 2, 3, 4, 5}
 key := 2
 for i := 0; i < len(s1); i++ {
  if i == key {
   println(s1[i])
  }
 }
}

```

运行结果

```text
3
```

#### 拷贝切片

```go
package main

import "fmt"

func main() {
 s1 := []int{1, 2, 3}
 s2 := s1
 s1[0] = 100
 fmt.Printf("s1: %v\n", s1)
 fmt.Printf("s2: %v\n", s2)
 fmt.Println("---------")

 s3 := make([]int, 3)
 copy(s3, s1)
 s1[0] = 1

 fmt.Printf("s1: %v\n", s1)
 fmt.Printf("s3: %v\n", s3)
}

```

运行结果

```text
s1: [100 2 3]
s2: [100 2 3]
---------
s1: [1 2 3]
s3: [100 2 3]
```

## golang map

map是一种`key:value`键值对的数据结构容器。map内部实现是哈希表( `hash` )。

map最重要的一点是通过key来快速检索数据，key 类似于索引，指向数据的值。

map是引用类型的。

#### map的语法格式

可以使用内建函数make也可以使用map关键字来定义map

```go
/*声明变量，默认map是nil */
var map_variable map[ key_data_type ]value.data_type
/*使用make函数*/
map_variable = make(map[key_data_type ]value_data_type)
```

* `map_variable` : map变量名称
* `key_data_type` : key的数据类型
* `value_data_type` :值得数据类型

实例

```go
package main

import "fmt"

func main() {
 m1 := make(map[string]string)
 m1["name"] = "tom"
 m1["age"] = "20"
 fmt.Printf("m1: %v\n", m1)

 m2 := map[string]string{"name": "tom", "age": "20"}
 fmt.Printf("m2: %v\n", m2)
}

```

运行结果

```text
m1: map[age:20 name:tom]
m2: map[age:20 name:tom]
```

#### 访问map

```go
package main

import "fmt"

func main() {

 m1 := map[string]string{"name": "tom", "age": "20"}

 fmt.Printf("m2: %v\n", m1["name"])
}

```

#### 判断某个键是否存在

go语言中有个判断map中键是否存在的特殊写法，格式如下:

```go
value,ok := map[key]

如果ok为true，存在;否则，不存在。

```

```go
package main

import "fmt"

func main() {

 m1 := map[string]string{"name": "tom", "age": "20"}
 name, ok := m1["name"]
 fmt.Printf("m2: %v,%v\n", name, ok)
}

```

运行结果

```text
m2: tom,true
```

#### go语言遍历map

可以使用`for range`循环进行map遍历，得到key和value值。

###### 遍历key

```go
package main

func main() {

 m1 := map[string]string{"name": "tom", "age": "20"}
 for key := range m1 {
  println(key)
 }
}

```

运行结果

```text
name
age
```

###### 遍历key和value

```go
package main

func main() {

 m1 := map[string]string{"name": "tom", "age": "20"}
 for key, value := range m1 {
  println(key, value)
 }
}

```

运行结果

```text
age 20
name tom

```

## golang函数

> 函数的go语言中的*一级公民*， 我们把所有的功能单元都定义在函数中，
> 可以重复使用。函数包含函数的名称、参数列表和返回值类型，这些构成了函数的签名(signature) 。

#### go语言中函数特性

* 1.go语言中有3种函数:普通函数、匿名函数(没有名称的函数)、方法(定义在struct.上的函数)。
* 2.go语言中不允许函数重载(overload), 也就是说不允许函数同名。
* 3.go语言中的函数不能嵌套函数,但可以嵌套匿名函数。
* 4.函数是一个值,可以将函数赋值给变量,使得这个变量也成为函数。
* 5.函数可以作为参数传递给另一个函数。
* 6.函数的返回值可以是一个函数。
* 7.函数调用的时候，如果有参数传递给函数，则先拷贝参数的副本，再将副本传递给函数。
* 8.函数参数可以没有名称。

#### go语言中函数的定义和调用

函数在使用之前必须先定义，可以调用函数来完成某个任务。函数可以重复调用，从而达到代码重用。

###### go语言函数定义语法

```go
func function. name( [parameter list] ) [return_types]
{
    函数体
}
```

*语法解析:*

* func :函数由func 开始声明
* function. name :函数名称，函数名和参数列表-起构成了函数签名。
* \[parameter list] :参数列表，参数就像一个占位符，当函数被调用时,你可以将值传递给参数,这个值被称为实际参数。参数列表指定的是参数类型、顺序、及参数个数。参数是可选的，也就是说函数也可以不包含参数。
* return. types :返回类型，函数返回- -列值。 return. types 是该列值的数据类型。有些功能不需要返回值，这种情况下return.
* types不是必须的。
* 函数体:函数定义的代码集合。

#### go语言函数定义实例

###### 定义一个求和函数

```go
func sum(a int, b int) (ret int) {
  ret=a+b
  return ret
}
```

###### 定义一个比较两个数大小的函数

```go
func compare(a int, b int) (max int) {
  if a>b{
      max=a
  } else {
      max=b
  }
  return max
}
```

#### golang函数的返回值

函数可以有0或多个返回值，返回值需要指定数据类型，返回值通过return关键字来指定。

return可以有参数,也可以没有参数,这些返回值可以有名称,也可以没有名称。go中的函数可以有多个返回值。

1.return 关键字中指定了参数时，返回值可以不用名称。如果return省略参数，则返回值部分必须带名称
2.当返回值有名称时，必须使用括号包围，逗号分隔，即使只有一个返回值
3.但即使返回值命名了，return 中也可以强制指定其它返回值的名称，也就是说return的优先级更高
4.命名的返回值是预先声明好的， 在函数内部可以直接使用，无需再次声明。命名返回值的名称不能和函数参数名称相同，否则报错提示变量重复定义
5.return中可以有表达式，但不能出现赋值表达式，这和其它语言可能有所不同。例如return a+b是正确的，但return c=a+b 是错误的。

###### go语言函数返回值实例

###### 没有返回值

```go
func f1() {
  fmt.Printf("我没有返回值，只是进行一些计算")
}
```

###### 有一个返回值

```go
func sum(a int，b int) (ret int) {
  ret=a+b
  return ret
}
```

###### 多个返回值，且在return中指定返回的内容

```go
func f2() (name string, age int) {
  name ="小白"
  age = 30
  return name, age
}
```

###### 多个返回值,返回值名称没有被使用

```go
func f3() (name string, age int) {
  name ="小白"
  age = 30
  return //等价于return name, age 
}
```

###### return覆盖命名返回值，返回值名称没有被使用

```go
func f4() (name string, age int) {
  n :="小白"
  a:=30
  return n,a
}
```

> Go中经常会使用其中一个返回值作为函数是否执行成功、是否有错误信息的判断条件。
> 例如`return value, exists、return value,ok、 return value,err`等。

> 当函数的返回值过多时，例如有4个以上的返回值，应该将这些返回值收集到容器中，然后以返回容器的方式去返回。例如，同类型的返回值可以放进slice中，不同类型的返回值可以放进map中。

> 但函数有多个返回值时，如果其中某个或某几个返回值不想使用，可以通过下划线_来丢弃这些返回值。
> 例如下面的f1函数两个返回值，调用该函数时，丢弃了第二个返回值b，只保留了第一个返回值a赋值给 了变量a。

```go
package main

func f1() (int, int) {
 return 1, 2
}

func main() {
 _, x := f1()
 println(x)
}

```

运行结果

```text
2
```

#### golang函数的参数

go语言函数可以有0或多个参数，参数需要指定数据类型。

声明函数时的参数列表叫做形参，调用时传递的参数叫做实参。

go语言是通过传值的方式传参的，意味着传递给函数的是拷贝后的副本，所以函数内部访问、修改的也是这个副本。

go语言可以使用变长参数，有时候并不能确定参数的个数,可以使用变长参数,可以在函数定义语句的参数部分使用ARGS...
TYPE的方式。这时会将... 代表的参数全部保存到一个名为ARGS的slice中，注意这些参数的数据类型都是TYPE。

go语言函数的参数实例

```go
package main

func f1(a int, b int) int {
 //形参列表
 if a > b {
  return a
 } else {
  return b
 }
}

func main() {
 x := f1(1, 2)
 println(x)
}

```

###### 演示参数传递，按值传递

```go
func f1(a int) {
  a=200
  fmt.Printf("a1: %v\n", a)
}

func main() {
  a := 100
  f1(a)
  fmt.Printf("a: %v\n", a)
}
```

运行结果

```text
a1: 200
a: 100
```

`从运行结果可以看到，调用函数1后，a的值并没有被改变，说明参数传递是拷贝了一个副本，也就是拷贝了1份新的内容进行运算。`

> `map、slice、 interface、 channel` 这些数据类型本身就是指针类型的， 所以就算是拷贝传值也是拷贝的指针，拷贝后的参数仍然指向底层数据结构，所以修改它们可能会影响外部数据结构的值。

```go
package main

import "fmt"

func f1(a []int) {
 a[0] = 200
 fmt.Printf("a1: %v\n", a)
}

func main() {
 a := []int{100}
 f1(a)
 fmt.Printf("a: %v\n", a)
}

```

输出结果

```text
a1: [200]
a: [200]
```

#### golang函数类型与函数变量

可以使用`type` 关键字来定义一个函数类型,语法格式如下:

上面语句定义了一个fun函数类型,它是一种函数类型, 这种函数接收两个int类型的参数并且返回一个int类型的返回值。

###### 下面我们定义两个这样结构的两个函数,一个求和，一个比较大小

```go
func sum(a int, b int) int {
  return a + b
}

func max(a int, b int) int {
  if a> b{
    return a
  } else {
    return b
  }
}
```

###### 下面定义一个fun函数类型,把sum和max赋值给它

```go
package main

func sum(a int, b int) int {
 return a + b
}

func max(a int, b int) int {
 if a > b {
  return a
 } else {
  return b
 }
}

type fun func(int, int) int

func main() {
 var f fun
 f = sum
 s := f(1, 2)
 println(s)
 f = max
 m := f(3, 4)
 println(m)
}

```

运行结果

```text
3
4
```

## golang高阶函数

go语言的函数，可以作为函数的参数，传递给另外一个函数,可以可以作为,另外一个函数的返回值返回。

#### go语言函数作为参数

```go
package main

func sayHello(name string) {
 println(name)
}

func f1(name string, f func(string)) {
 f(name)
}

func main() {
 f1("tom", sayHello)
}

```

运行结果

```text
tom
```

#### go语言函数作为返回值

```go
package main

func add(x, y int) int {
 return x + y
}

func sub(x, y int) int {
 return x - y
}

func cal(s string) func(int, int) int {
 switch s {
 case "+":
  return add
 case "-":
  return sub
 default:
  return nil
 }
}

func main() {
 add := cal("+")
 println(add(1, 5))

 sub := cal("-")
 println(sub(1, 5))
}

```

运行结果

```text
6
-4
```

## golang匿名函数

go语言函数不能嵌套，但是在函数内部可以定义匿名函数，实现一下简单功能调用。

所谓匿名函数就是,没有名称的函数。

语法格式如下:

```go
fubc (参 数列表)(返回值)
```

> 当然可以既没有参数，可以没有返回值

匿名函数实例

```go
package main

func main() {
 max := func(a int, b int) int {
  if a > b {
   return a
  } else {
   return b
  }
 }
 i := max(1, 2)
 println(i)
}

```

运行结果

```text
2
```

## golang闭包

闭包可以理解成定义在一个函数内部的函数。在本质上，闭包是将函数内部和函数外部连接起来的桥梁。或者说是函数和其引用环境的组合体。

闭包指的是一个函数和与其相关的引用环境组合而成的实体。 简单来说，闭包=函 数+引用环境。首先我们来看一个例子:

```go
package main

func add() func(int) int {
 var x int
 return func(y int) int {
  x += y
  return x
 }
}

func main() {
 var f = add()
 println(f(10))
 println(f(20))
 println(f(30))

 f1 := add()
 println(f1(40))
 println(f1(50))
}
```

运行结果

```text
10
30
60
40
90
```

变量`f`是一个函数并且它引用了其外部作用域中的x变量，此时f就是一个闭包。在f的生命周期内，*变量x也一直有效*。闭包进阶示例1:

闭包其实并不复杂，只要牢记`闭包=雨数+引用环境`。

## golang递归

函数内部调用函数自身的函数称为递归函数。

使用递归函数最重要的三点:

* 1.递归就是自己调用自己。
* 2.必须先定义函数的退出条件，没有退出条件,递归将成为死循环。
* 3.go语言递归函数很可能会产性一大堆的goroutine, 也很可能会出现栈空间内存溢出问题。

go语言递归实例

```go
package main

func a(n int) int {
 //返回条件
 if n == 1 {
  return 1
 } else {
  //自己调用自己
  return n * a(n-1)
 }
}

func main() {
 s := a(5)
 println(s)
}

```

运行结果

```text
120
```

*斐波那契数列*
它的计算公式为`f(n)=f(n-1)+f(n-2)且f(2)=f(1)=1`

```go
package main

func f(n int) int {
 //退出点判断
 if n == 1 || n == 2 {
  return 1
 }
 //递归表达式
 return f(n-1) + f(n-2)
}

func main() {
 s := f(5)
 println(s)
}

```

```text
5
```

## golang defer语句

go语言中的`defer`语句会将其后面跟随的语句进行*延迟*处理。在`defer`归属的函数即将返回时，将延迟处理的语句按`defer`定义的
*逆序*进行执行，也就是说，先被`defer`的语句最后被执行，最后被`defer`的语句，最先被执行。

#### defer特性

* 1.关键字defer用于注册延迟调用。
* 2.这些调用直到return 前才被执。因此，可以用来做资源清理。
* 3.多个defer语句，按先进后出的方式执行。
* 4.defer 语句中的变量,在defer声明时就决定了。

#### defer用途

* 1.关闭文件句柄
* 2.锁资源释放
* 3.数据库连接释放

go语言defer语句实例

```go
package main

func main() {
 println("start")
 defer println("step1")
 defer println("step2")
 defer println("step3")
 println("end")
}

```

运行结果

```text
start
end
step3
step2
step1
```

## golang init函数

golang有一个特殊的函数`init`函数，先于`main`函数执行，实现包级别的一些*初始化*操作。

#### init函数的主要特点

* init函数先于mpin函数自动执行,不能被其他函数调用;
* init函数没有输入参数、 返回值;
* 每个包可以有多个init函数;
* 包的每个源文件也可以有多个init函数，这点比较特殊;
* 同一个包的init执行顺序, golang没有明确定义,编程时要注意程序不要依赖这个执行顺序。
* 不同包的init函数按照包导入的依赖关系决定执行顺序。

#### golang初始化顺序

初始化顺序:变量初始化->init()->main()

实例

```go
package main

var i int = initValue()

func initValue() int {
 println("initValue")
 return 1
}

func init() {
 println("init")
}

func main() {
 println("main")
}

```

运行结果

```text
initValue
init
main
```

## golang指针

Go语言中的函数传参都是值拷贝，当我们想要修改某个变量的时候，我们可以创建一个 指向该变量地址的指针变量。传递数据使用指针，而无须拷贝数据。

类型指针不能进行偏移和运算。

Go语言中的指针操作非常简单，只需要记住两个符号: `&` (取地址) 和`*` (根据地址取值) 。

#### 指针地址和指针类型

每个变量在运行时都拥有一个地址，
这个地址代表变量在内存中的位置。Go语言中使用&字符放在变量前面对变量进行取地址操作。Go语言中的值类型`(int、 float. bool.
string、 array、 struct)`都有对应的指针类型,如: `*int、 *int64、 *string` 等。

#### 指针语法

一个指针变量指向了一个值的内存地址。(也就是我们声明了一 个指针之后，可以像变量赋值一样,把一个值的内存地址放入到指针当中。)

类似于变量和常量，在使用指针前你需要声明指针。指针声明格式如下:

```go
var var_name *var-type
```

* var-type :为指针类型
* var_name :为指针变量名
* *:用于指定变量是作为一个指针。

#### 指针声明实例

```go
var ip *int     /*指向整型*/
var fp *float32 /*指向浮点型*/
```

#### 指针使用实例

```go
package main

import "fmt"

func main() {
 var a int = 20 /*声明实际变量*/
 var ip *int    /*声明指针变量*/
 ip = &a        /* 指针变量的存储地址*/
 fmt.Printf("a变量的地址是: %x\n", &a)
 /*指针变量的存储地址*/
 fmt.Printf("ip变量储存的指针地址: %x\n", ip)
 /*使用指针访问值*/
 fmt.Printf("*ip变量的值: %d\n", *ip)
}

```

运行结果

```text
a变量的地址是: c00000a0d8
ip变量储存的指针地址: c00000a0d8
*ip变量的值: 20

```

#### golang指向数组的指针

###### 定义语法

```go
var ptr [MAX]*int;
```

实例演示

```go
package main

import "fmt"

const MAX int = 3

func main() {
 a := []int{1, 3, 5}
 var i int
 var ptr [MAX]*int
 fmt.Println(ptr) //这个打印出来是[<n1l> <nil> <nil> ]
 for i = 0; i < MAX; i++ {
  ptr[i] = &a[i] /*整数地址赋值给指针数组*/
 }
 for i = 0; i < MAX; i++ {
  fmt.Printf("a[%d] = %d\n", i, *ptr[i]) //*ptr[i]就是打印出相关指针的值了 。
 }
}

```

```text
[<nil> <nil> <nil>]
a[0] = 1
a[1] = 3
a[2] = 5
```

## golang类型定义和类型别名

在介绍*结构体*之前，我们先来看看什么是类型定义和类型别名。

#### go语言类型定义

类型定义的语法

```go
type NewType Type
```

实例.

```go
package main

import "fmt"

func main() {
 //类型定义
 type MyInt int
 // i为MyInt类型
 var i MyInt
 i = 100
 fmt.Printf("i: %v i: %T\n", i, i)
}

```

运行结果

```text
i: 100 i: main.MyInt
```

###### go语言类型定义和类型别名的区别

* 1.类型定义相当于定义了一个全新的类型，与之前的类型不同;但是类型别名并没有定义一个新的类型,而是使用一个别名来替换之前的类型
* 2.类型别名只会在代码中存在,在编译完成之后并不会存在该别名
* 3.因为类型别名和原来的类型是一致的，所以原来类型所拥有的方法，类型别名中也可以调用，但是如果是重新定义的一个类型，那么不可以调用之前的任何方法
