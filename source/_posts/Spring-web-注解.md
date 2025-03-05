---
title: Spring web 注解
date: 2025-01-20 21:23:31
tags:
  - 注解
categories:
  - Spring
typora-root-url: Spring-web-注解
---

### **<font style="color:rgb(0, 0, 0);">一、Spring Web MVC 与 Spring Bean 注解</font>**

#### **<font style="color:rgb(0, 0, 0);">Spring Web MVC 注解</font>**

**<font style="color:rgb(51, 51, 51);">@RequestMapping</font>**

<font style="color:rgb(51, 51, 51);">@RequestMapping注解的主要用途是将Web请求与请求处理类中的方法进行映射。Spring MVC和Spring WebFlux都通过</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">RquestMappingHandlerMapping</font><font style="color:rgb(51, 51, 51);">和</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">RequestMappingHndlerAdapter</font><font style="color:rgb(51, 51, 51);">两个类来提供对@RequestMapping注解的支持。</font>

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RequestMapping</font><font style="color:rgb(51, 51, 51);">注解对请求处理类中的请求处理方法进行标注；</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RequestMapping</font><font style="color:rgb(51, 51, 51);">注解拥有以下的六个配置属性：</font>

+ <font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">value</font><font style="color:rgb(51, 51, 51);">:映射的请求URL或者其别名</font>
+ <font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">method</font><font style="color:rgb(51, 51, 51);">:兼容HTTP的方法名</font>
+ <font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">params</font><font style="color:rgb(51, 51, 51);">:根据HTTP参数的存在、缺省或值对请求进行过滤</font>
+ <font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">header</font><font style="color:rgb(51, 51, 51);">:根据HTTP Header的存在、缺省或值对请求进行过滤</font>
+ <font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">consume</font><font style="color:rgb(51, 51, 51);">:设定在HTTP请求正文中允许使用的媒体类型</font>
+ <font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">product</font><font style="color:rgb(51, 51, 51);">:在HTTP响应体中允许使用的媒体类型</font>

<font style="color:rgb(51, 51, 51);">提示：在使用@RequestMapping之前，请求处理类还需要使用@Controller或@RestController进行标记</font>

<font style="color:rgb(51, 51, 51);">下面是使用@RequestMapping的两个示例：</font>

![](1709106096731-61aa57df-c36c-451a-8c6a-7ea937c4c60d.png)

<font style="color:rgb(51, 51, 51);">@RequestMapping还可以对类进行标记，这样类中的处理方法在映射请求路径时，会自动将类上@RequestMapping设置的value拼接到方法中映射路径之前，如下：</font>

![](1709106096629-d7f931ea-fbd5-4c07-8a66-4ba16a806456.png)

**<font style="color:rgb(51, 51, 51);">@RequestBody</font>**

<font style="color:rgb(51, 51, 51);">@RequestBody在处理请求方法的参数列表中使用，它可以将请求主体中的参数绑定到一个对象中，请求主体参数是通过</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">HttpMessageConverter</font><font style="color:rgb(51, 51, 51);">传递的，根据请求主体中的参数名与对象的属性名进行匹配并绑定值。此外，还可以通过@Valid注解对请求主体中的参数进行校验。</font>

<font style="color:rgb(51, 51, 51);">下面是一个使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RequestBody</font><font style="color:rgb(51, 51, 51);">的示例：</font>

![](1709106096701-9d9d0d6e-2fa5-43f2-94d6-811d78ffa04d.jpeg)

**<font style="color:rgb(51, 51, 51);">@GetMapping</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@GetMapping</font><font style="color:rgb(51, 51, 51);">注解用于处理HTTP GET请求，并将请求映射到具体的处理方法中。具体来说，@GetMapping是一个组合注解，它相当于是</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RequestMapping(method=RequestMethod.GET)</font><font style="color:rgb(51, 51, 51);">的快捷方式。</font>

<font style="color:rgb(51, 51, 51);">下面是</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@GetMapping</font><font style="color:rgb(51, 51, 51);">的一个使用示例：</font>

![](1709106096688-c0398558-79fb-4f6f-9ec4-7100c77dbd3b.jpeg)

<!-- more -->

**<font style="color:rgb(51, 51, 51);">@PostMapping</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@PostMapping</font><font style="color:rgb(51, 51, 51);">注解用于处理HTTP POST请求，并将请求映射到具体的处理方法中。@PostMapping与@GetMapping一样，也是一个组合注解，它相当于是</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RequestMapping(method=HttpMethod.POST)</font><font style="color:rgb(51, 51, 51);">的快捷方式。</font>

<font style="color:rgb(51, 51, 51);">下面是使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@PostMapping</font><font style="color:rgb(51, 51, 51);">的一个示例：</font>

![](1709106096618-3550ddca-8fa3-4a10-8faf-698b32c6ea68.jpeg)

<

**<font style="color:rgb(51, 51, 51);">@PutMapping</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@PutMapping</font><font style="color:rgb(51, 51, 51);">注解用于处理HTTP PUT请求，并将请求映射到具体的处理方法中，@PutMapping是一个组合注解，相当于是</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RequestMapping(method=HttpMethod.PUT)</font><font style="color:rgb(51, 51, 51);">的快捷方式。</font>

<font style="color:rgb(51, 51, 51);">下面是使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@PutMapping</font><font style="color:rgb(51, 51, 51);">的一个示例：</font>

![](1709106097163-681e9f87-039d-44b6-b272-9026ace93a00.jpeg)

<

**<font style="color:rgb(51, 51, 51);">@DeleteMapping</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@DeleteMapping</font><font style="color:rgb(51, 51, 51);">注解用于处理HTTP DELETE请求，并将请求映射到删除方法中。@DeleteMapping是一个组合注解，它相当于是</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RequestMapping(method=HttpMethod.DELETE)</font><font style="color:rgb(51, 51, 51);">的快捷方式。</font>

<font style="color:rgb(51, 51, 51);">下面是使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@DeleteMapping</font><font style="color:rgb(51, 51, 51);">的一个示例：</font>

![](1709106097302-924c0ec0-a8ea-41d6-8458-7ee7deaf5254.jpeg)

<

**<font style="color:rgb(51, 51, 51);">@PatchMapping</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@PatchMapping</font><font style="color:rgb(51, 51, 51);">注解用于处理HTTP PATCH请求，并将请求映射到对应的处理方法中。@PatchMapping相当于是</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RequestMapping(method=HttpMethod.PATCH)</font><font style="color:rgb(51, 51, 51);">的快捷方式。</font>

<font style="color:rgb(51, 51, 51);">下面是一个简单的示例：</font>

![](1709106097261-f0eb3826-f449-46b0-9a2f-9bb4aef3888a.jpeg)

**<font style="color:rgb(51, 51, 51);">@ControllerAdvice</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ControllerAdvice</font><font style="color:rgb(51, 51, 51);">是@Component注解的一个延伸注解，Spring会自动扫描并检测被@ControllerAdvice所标注的类。</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ControllerAdvice</font><font style="color:rgb(51, 51, 51);">需要和</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ExceptionHandler</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@InitBinder</font><font style="color:rgb(51, 51, 51);">以及</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ModelAttribute</font><font style="color:rgb(51, 51, 51);">注解搭配使用，主要是用来处理控制器所抛出的异常信息。</font>

<font style="color:rgb(51, 51, 51);">首先，我们需要定义一个被</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ControllerAdvice</font><font style="color:rgb(51, 51, 51);">所标注的类，在该类中，定义一个用于处理具体异常的方法，并使用@ExceptionHandler注解进行标记。</font>

<font style="color:rgb(51, 51, 51);">此外，在有必要的时候，可以使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@InitBinder</font><font style="color:rgb(51, 51, 51);">在类中进行全局的配置，还可以使用@ModelAttribute配置与视图相关的参数。使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ControllerAdvice</font><font style="color:rgb(51, 51, 51);">注解，就可以快速的创建统一的，自定义的异常处理类。</font>

<font style="color:rgb(51, 51, 51);">下面是一个使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ControllerAdvice</font><font style="color:rgb(51, 51, 51);">的示例代码：</font>

![](1709106097273-f1dc8409-761a-4579-8d4d-4bddafc6047f.jpeg)

**<font style="color:rgb(51, 51, 51);">@ResponseBody</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ResponseBody</font><font style="color:rgb(51, 51, 51);">会自动将控制器中方法的返回值写入到HTTP响应中。特别的，</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ResponseBody</font><font style="color:rgb(51, 51, 51);">注解只能用在被</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Controller</font><font style="color:rgb(51, 51, 51);">注解标记的类中。如果在被</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RestController</font><font style="color:rgb(51, 51, 51);">标记的类中，则方法不需要使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ResponseBody</font><font style="color:rgb(51, 51, 51);">注解进行标注。</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RestController</font><font style="color:rgb(51, 51, 51);">相当于是</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Controller</font><font style="color:rgb(51, 51, 51);">和</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ResponseBody</font><font style="color:rgb(51, 51, 51);">的组合注解。</font>

<font style="color:rgb(51, 51, 51);">下面是使用该注解的一个示例</font>

![](1709106097309-d7108a06-e6bc-4b04-b442-41cc24e8ddf8.png)

**<font style="color:rgb(51, 51, 51);">@ExceptionHandler</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ExceptionHander</font><font style="color:rgb(51, 51, 51);">注解用于标注处理特定类型异常类所抛出异常的方法。当控制器中的方法抛出异常时，Spring会自动捕获异常，并将捕获的异常信息传递给被</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ExceptionHandler</font><font style="color:rgb(51, 51, 51);">标注的方法。</font>

<font style="color:rgb(51, 51, 51);">下面是使用该注解的一个示例：</font>

![](1709106097716-f9cc78a3-b126-457a-a6f3-b1336fe0924e.jpeg)

**<font style="color:rgb(51, 51, 51);">@ResponseStatus</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ResponseStatus</font><font style="color:rgb(51, 51, 51);">注解可以标注请求处理方法。使用此注解，可以指定响应所需要的HTTP STATUS。特别地，我们可以使用HttpStauts类对该注解的value属性进行赋值。</font>

<font style="color:rgb(51, 51, 51);">下面是使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ResponseStatus</font><font style="color:rgb(51, 51, 51);">注解的一个示例：</font>

![](1709106097942-28ba45a1-6ac0-4fe7-8447-19efe8bdd12c.jpeg)

**<font style="color:rgb(51, 51, 51);">@PathVariable</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@PathVariable</font><font style="color:rgb(51, 51, 51);">注解是将方法中的参数绑定到请求URI中的模板变量上。可以通过</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RequestMapping</font><font style="color:rgb(51, 51, 51);">注解来指定URI的模板变量，然后使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@PathVariable</font><font style="color:rgb(51, 51, 51);">注解将方法中的参数绑定到模板变量上。</font>

<font style="color:rgb(51, 51, 51);">特别地，</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@PathVariable</font><font style="color:rgb(51, 51, 51);">注解允许我们使用value或name属性来给参数取一个别名。下面是使用此注解的一个示例：</font>

![](1709106097865-e8ed68eb-0fea-4e35-bb37-2d52bea49b21.jpeg)

<font style="color:rgb(51, 51, 51);">模板变量名需要使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">{ }</font><font style="color:rgb(51, 51, 51);">进行包裹，如果方法的参数名与URI模板变量名一致，则在</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@PathVariable</font><font style="color:rgb(51, 51, 51);">中就可以省略别名的定义。</font>

<font style="color:rgb(51, 51, 51);">下面是一个简写的示例：</font>

![](1709106097968-dcbf7dc8-e1d2-412c-9639-fdfba9e545ae.jpeg)

<font style="color:rgb(51, 51, 51);">提示：如果参数是一个非必须的，可选的项，则可以在</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@PathVariable</font><font style="color:rgb(51, 51, 51);">中设置</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">require = false</font>

**<font style="color:rgb(51, 51, 51);">@RequestParam</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RequestParam</font><font style="color:rgb(51, 51, 51);">注解用于将方法的参数与Web请求的传递的参数进行绑定。使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RequestParam</font><font style="color:rgb(51, 51, 51);">可以轻松的访问HTTP请求参数的值。</font>

<font style="color:rgb(51, 51, 51);">下面是使用该注解的代码示例：</font>

![](1709106097953-35ae1da2-6935-4b59-9d9e-f2486c6a1410.png)

<font style="color:rgb(51, 51, 51);">该注解的其他属性配置与</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@PathVariable</font><font style="color:rgb(51, 51, 51);">的配置相同，特别的，如果传递的参数为空，还可以通过defaultValue设置一个默认值。示例代码如下：</font>

![](1709106098321-68f40df0-3918-4a04-b5d2-e6c490901228.jpeg)

**<font style="color:rgb(51, 51, 51);">@Controller</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Controller</font><font style="color:rgb(51, 51, 51);">是</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Component</font><font style="color:rgb(51, 51, 51);">注解的一个延伸，</font>

[Spring](https://cloud.tencent.com/developer/tools/blog-entry?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzg2MjEwMjI1Mg%3D%3D%26mid%3D2247488534%26idx%3D1%26sn%3D109a9ecbc8784fb71b5b92809d04449a%26chksm%3Dce0da395f97a2a83513f039a1b9f47ccd12701cdffac8bb0f3b24bbab13033338b6f9898a518%26scene%3D21%23wechat_redirect&source=article&objectId=1885299)

<font style="color:rgb(51, 51, 51);">会自动扫描并配置被该注解标注的类。此注解用于标注Spring MVC的控制器。下面是使用此注解的示例代码：</font>

![](1709106098485-28e2a725-d479-46de-8ee5-8d0d6a948c72-173752061337520.jpeg)

**<font style="color:rgb(51, 51, 51);">@RestController</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RestController</font><font style="color:rgb(51, 51, 51);">是在Spring 4.0开始引入的，这是一个特定的控制器注解。此注解相当于</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Controller</font><font style="color:rgb(51, 51, 51);">和</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ResponseBody</font><font style="color:rgb(51, 51, 51);">的快捷方式。当使用此注解时，不需要再在方法上使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ResponseBody</font><font style="color:rgb(51, 51, 51);">注解。</font>

<font style="color:rgb(51, 51, 51);">下面是使用此注解的示例代码：</font>

![](1709106098549-b33d3134-a3c4-47b8-a619-05bb6d59c989.jpeg)

**<font style="color:rgb(51, 51, 51);">@ModelAttribute</font>**

<font style="color:rgb(51, 51, 51);">通过此注解，可以通过模型索引名称来访问已经存在于控制器中的model。下面是使用此注解的一个简单示例：</font>

![](1709106098636-fa91e056-bf59-441a-92fa-bd64be4cdf4e.png)

<font style="color:rgb(51, 51, 51);">与</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@PathVariable</font><font style="color:rgb(51, 51, 51);">和</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@RequestParam</font><font style="color:rgb(51, 51, 51);">注解一样，如果参数名与模型具有相同的名字，则不必指定索引名称，简写示例如下：</font>

![](1709106098498-e16ba5df-5360-4215-b3e5-6136ce06c65d.png)

<font style="color:rgb(51, 51, 51);">特别地，如果使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ModelAttribute</font><font style="color:rgb(51, 51, 51);">对方法进行标注，Spring会将方法的返回值绑定到具体的Model上。示例如下：</font>

![](1709106099007-048d51af-6468-4eb1-be6e-b89897316399.png)

<font style="color:rgb(51, 51, 51);">在Spring调用具体的处理方法之前，被</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ModelAttribute</font><font style="color:rgb(51, 51, 51);">注解标注的所有方法都将被执行。</font>

**<font style="color:rgb(51, 51, 51);">@CrossOrigin</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@CrossOrigin</font><font style="color:rgb(51, 51, 51);">注解将为请求处理类或请求处理方法提供跨域调用支持。如果我们将此注解标注类，那么类中的所有方法都将获得支持跨域的能力。使用此注解的好处是可以微调跨域行为。使用此注解的示例如下：</font>

![](1709106099056-67c9795b-60ca-4d33-9d90-79a306495b19.jpeg)

**<font style="color:rgb(51, 51, 51);">@InitBinder</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@InitBinder</font><font style="color:rgb(51, 51, 51);">注解用于标注初始化</font>**<font style="color:rgb(51, 51, 51);">WebDataBinider</font>**<font style="color:rgb(51, 51, 51);">的方法，该方法用于对Http请求传递的表单数据进行处理，如时间格式化、字符串处理等。下面是使用此注解的示例：</font>

![](1709106099162-0494d48f-cdf6-450d-b1bf-3a2c258d425f.png)

### **<font style="color:rgb(0, 0, 0);">二、Spring Bean 注解</font>**

<font style="color:rgb(51, 51, 51);">在本小节中，主要列举与Spring Bean相关的4个注解以及它们的使用方式。</font>

**<font style="color:rgb(51, 51, 51);">@ComponentScan</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ComponentScan</font><font style="color:rgb(51, 51, 51);">注解用于配置Spring需要扫描的被组件注解注释的类所在的包。可以通过配置其basePackages属性或者value属性来配置需要扫描的包路径。value属性是basePackages的别名。此注解的用法如下：</font>

**<font style="color:rgb(51, 51, 51);">@Component</font>**

<font style="color:rgb(51, 51, 51);">@Component注解用于标注一个普通的组件类，它没有明确的业务范围，只是通知Spring被此注解的类需要被纳入到Spring Bean</font>[容器](https://cloud.tencent.com/product/tke?from_column=20065&from=20065)<font style="color:rgb(51, 51, 51);">中并进行管理。此注解的使用示例如下：</font>

![](1709106099168-8db7425c-413b-4d4c-9700-09a9a481651a.png)

**<font style="color:rgb(51, 51, 51);">@Service</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Service</font><font style="color:rgb(51, 51, 51);">注解是</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Component</font><font style="color:rgb(51, 51, 51);">的一个延伸（特例），它用于标注业务逻辑类。与</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Component</font><font style="color:rgb(51, 51, 51);">注解一样，被此注解标注的类，会自动被Spring所管理。下面是使用</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Service</font><font style="color:rgb(51, 51, 51);">注解的示例：</font>

![](1709106099385-1480782a-ea36-4b65-9937-2f39030e0aaa.jpeg)

**<font style="color:rgb(51, 51, 51);">@Repository</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Repository</font><font style="color:rgb(51, 51, 51);">注解也是</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Component</font><font style="color:rgb(51, 51, 51);">注解的延伸，与</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Component</font><font style="color:rgb(51, 51, 51);">注解一样，被此注解标注的类会被Spring自动管理起来，</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Repository</font><font style="color:rgb(51, 51, 51);">注解用于标注DAO层的数据持久化类。此注解的用法如下：</font>

![](1709106099679-4f026999-4d2d-44b4-b837-df76e8fcd3cc.jpeg)

### **<font style="color:rgb(0, 0, 0);">三、Spring Dependency Inject 与 Bean Scops注解</font>**

#### **<font style="color:rgb(0, 0, 0);">Spring DI注解</font>**

**<font style="color:rgb(51, 51, 51);">@DependsOn</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@DependsOn</font><font style="color:rgb(51, 51, 51);">注解可以配置Spring IoC容器在初始化一个Bean之前，先初始化其他的Bean对象。下面是此注解使用示例代码：</font>

![](1709106099765-fd8e6bbc-fd54-4788-9913-3844e0e4a45c.jpeg)

**<font style="color:rgb(51, 51, 51);">@Bean</font>**

<font style="color:rgb(51, 51, 51);">@Bean注解主要的作用是告知Spring，被此注解所标注的类将需要纳入到Bean管理工厂中。@Bean注解的用法很简单，在这里，着重介绍@Bean注解中</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">initMethod</font><font style="color:rgb(51, 51, 51);">和</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">destroyMethod</font><font style="color:rgb(51, 51, 51);">的用法。示例如下：</font>

![](1709106099732-f5c0ee38-7ef5-44f3-9f0f-cf19fcbe287f.jpeg)

#### **<font style="color:rgb(0, 0, 0);">Scops注解</font>**

**<font style="color:rgb(51, 51, 51);">@Scope</font>**

<font style="color:rgb(51, 51, 51);">@Scope注解可以用来定义@Component标注的类的作用范围以及@Bean所标记的类的作用范围。@Scope所限定的作用范围有：</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">singleton</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">prototype</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">request</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">session</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">globalSession</font><font style="color:rgb(51, 51, 51);">或者其他的自定义范围。这里以prototype为例子进行讲解。</font>

<font style="color:rgb(51, 51, 51);">当一个Spring Bean被声明为prototype（原型模式）时，在每次需要使用到该类的时候，Spring IoC容器都会初始化一个新的改类的实例。在定义一个Bean时，可以设置Bean的scope属性为</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">prototype：scope=“prototype”</font><font style="color:rgb(51, 51, 51);">,也可以使用@Scope注解设置，如下：</font>

```javascript
@Scope(value=ConfigurableBeanFactory.SCOPE_PROPTOTYPE)
```

<font style="color:rgb(51, 51, 51);">下面将给出两种不同的方式来使用@Scope注解，示例代码如下：</font>

![](1709106099941-81a1117f-f25b-451f-8b48-d5b6a748b83e.jpeg)

**<font style="color:rgb(51, 51, 51);">@Scope 单例模式</font>**

<font style="color:rgb(51, 51, 51);">当@Scope的作用范围</font>[设置成Singleton时](https://cloud.tencent.com/developer/tools/blog-entry?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI4Njc5NjM1NQ%3D%3D%26mid%3D2247493542%26idx%3D2%26sn%3D43a97be735b81408b35a00d0adaf75bf%26chksm%3Debd5d88adca2519cd66108625b1561983a5a40b476d377b24b6c7f8c5af4331d5d790a76be07%26scene%3D21%23wechat_redirect&source=article&objectId=1885299)<font style="color:rgb(51, 51, 51);">，被此注解所标注的类只会被Spring IoC容器初始化一次。在默认情况下，Spring IoC容器所初始化的类实例都为singleton。同样的原理，此情形也有两种配置方式，示例代码如下：</font>

![](1709106099945-cbf8cf90-1120-4b8d-b52e-98e023a9e162.png)

### **<font style="color:rgb(0, 0, 0);">四、容器配置注解</font>**

#### **<font style="color:rgb(0, 0, 0);">@Autowired</font>**

<font style="color:rgb(51, 51, 51);">@Autowired注解用于标记Spring将要解析和注入的依赖项。此注解可以作用在构造函数、字段和setter方法上。</font>

**<font style="color:rgb(51, 51, 51);">作用于构造函数</font>**

<font style="color:rgb(51, 51, 51);">下面是@Autowired注解标注构造函数的使用示例：</font>

![](1709106100372-d6898280-8259-431e-a6d7-668708a02ef7.png)

**<font style="color:rgb(51, 51, 51);">作用于setter方法</font>**

<font style="color:rgb(51, 51, 51);">下面是@Autowired注解标注setter方法的示例代码：</font>

![](1709106100395-d14606e1-09a8-48e5-a7c8-c6bcb4d9364e.png)

**<font style="color:rgb(51, 51, 51);">作用于字段</font>**

<font style="color:rgb(51, 51, 51);">@Autowired注解标注字段是最简单的，只需要在对应的字段上加入此注解即可，示例代码如下：</font>

![](1709106100526-8d32a439-9a2f-4313-8c08-d905e1f673b8.png)

#### **<font style="color:rgb(0, 0, 0);">@Primary</font>**

<font style="color:rgb(51, 51, 51);">当系统中需要配置多个具有相同类型的bean时，@Primary可以定义这些Bean的优先级。下面将给出一个实例代码来说明这一特性：</font>

![](1709106100512-76f86389-942f-484b-8ab4-4ee1d3e03fb5.png)

<font style="color:rgb(51, 51, 51);">输出结果：</font>

```javascript
this is send DingDing method message.
```

#### **<font style="color:rgb(0, 0, 0);">@PostConstruct与@PreDestroy</font>**

<font style="color:rgb(51, 51, 51);">值得注意的是，这两个注解不属于Spring,它们是源于JSR-250中的两个注解，位于</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">common-annotations.jar</font><font style="color:rgb(51, 51, 51);">中。@PostConstruct注解用于标注在Bean被Spring初始化之前需要执行的方法。@PreDestroy注解用于标注Bean被销毁前需要执行的方法。下面是具体的示例代码：</font>

![](1709106100654-4f6b2adb-b033-42c6-8af9-ae4724aff9f5.png)

#### **<font style="color:rgb(0, 0, 0);">@Qualifier</font>**

<font style="color:rgb(51, 51, 51);">当系统中存在同一类型的多个Bean时，@Autowired在进行依赖注入的时候就不知道该选择哪一个实现类进行注入。此时，我们可以使用@Qualifier注解来微调，帮助</font>[@Autowired选择正确的依赖项](https://cloud.tencent.com/developer/tools/blog-entry?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI4Njc5NjM1NQ%3D%3D%26mid%3D2247508834%26idx%3D1%26sn%3Dccf444814b629a320c3b979c71df2bc0%26chksm%3Debd59c4edca21558b045a819b4d03500164ae7bea099af4725ea1f0d6bd795ef2b03fd509fcd%26scene%3D21%23wechat_redirect&source=article&objectId=1885299)<font style="color:rgb(51, 51, 51);">。下面是一个关于此注解的代码示例：</font>

![](1709106101078-632fad2d-dbeb-4aa4-a3dd-2d80766d7adb.png)

### **<font style="color:rgb(0, 0, 0);">五、Spring Boot注解</font>**

**<font style="color:rgb(51, 51, 51);">@SpringBootApplication</font>**

<font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@SpringBootApplication</font><font style="color:rgb(51, 51, 51);">注解是一个快捷的配置注解，在被它标注的类中，可以</font>[定义一个或多个Bean](https://cloud.tencent.com/developer/tools/blog-entry?target=http%3A%2F%2Fmp.weixin.qq.com%2Fs%3F__biz%3DMzI4Njc5NjM1NQ%3D%3D%26mid%3D2247499001%26idx%3D2%26sn%3Da4e94719a95f22171efd8ff2907fa95a%26chksm%3Debd5c3d5dca24ac3f620be051883c784f062eeee41ac89b53fbd09a8c145c0c0e0d08cdcfc4b%26scene%3D21%23wechat_redirect&source=article&objectId=1885299)<font style="color:rgb(51, 51, 51);">，并自动触发自动配置Bean和自动扫描组件。此注解相当于</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@Configuration</font><font style="color:rgb(51, 51, 51);">、</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@EnableAutoConfiguration</font><font style="color:rgb(51, 51, 51);">和</font><font style="color:rgb(10, 191, 91);background-color:rgb(243, 245, 249);">@ComponentScan</font><font style="color:rgb(51, 51, 51);">的组合。</font>

<font style="color:rgb(51, 51, 51);">在</font><font style="color:rgb(0, 82, 217);">Spring Boot</font><font style="color:rgb(51, 51, 51);">应用程序的主类中，就使用了此注解。示例代码如下：</font>

```javascript
@SpringBootApplication
public class Application{
 public static void main(String [] args){
   SpringApplication.run(Application.class,args);
 }
}
```

**<font style="color:rgb(51, 51, 51);">@EnableAutoConfiguration</font>**

<font style="color:rgb(51, 51, 51);">@EnableAutoConfiguration注解用于通知Spring，根据当前类路径下引入的依赖包，自动配置与这些依赖包相关的配置项。</font>

**<font style="color:rgb(51, 51, 51);">@ConditionalOnClass与@ConditionalOnMissingClass</font>**

<font style="color:rgb(51, 51, 51);">这两个注解属于类条件注解，它们根据是否存在某个类作为判断依据来决定是否要执行某些配置。下面是一个简单的示例代码：</font>

```javascript
@Configuration
@ConditionalOnClass(DataSource.class)
class MySQLAutoConfiguration {
 //...
}
```

**<font style="color:rgb(51, 51, 51);">@ConditionalOnBean与@ConditionalOnMissingBean</font>**

<font style="color:rgb(51, 51, 51);">这两个注解属于对象条件注解，根据是否存在某个对象作为依据来决定是否要执行某些配置方法。示例代码如下：</font>

```javascript
@Bean
@ConditionalOnBean(name="dataSource")
LocalContainerEntityManagerFactoryBean entityManagerFactory(){
 //...
}
@Bean
@ConditionalOnMissingBean
public MyBean myBean(){
 //...
}
```

**<font style="color:rgb(51, 51, 51);">@ConditionalOnProperty</font>**

<font style="color:rgb(51, 51, 51);">@ConditionalOnProperty注解会根据Spring配置文件中的配置项是否满足配置要求，从而决定是否要执行被其标注的方法。示例代码如下：</font>

```javascript
@Bean
@ConditionalOnProperty(name="alipay",havingValue="on")
Alipay alipay(){
 return new Alipay();
}
```

**<font style="color:rgb(51, 51, 51);">@ConditionalOnResource</font>**

<font style="color:rgb(51, 51, 51);">此注解用于检测当某个配置文件存在使，则触发被其标注的方法，下面是使用此注解的代码示例：</font>

```javascript
@ConditionalOnResource(resources = "classpath:website.properties")
Properties addWebsiteProperties(){
 //...
}
```

**<font style="color:rgb(51, 51, 51);">@ConditionalOnWebApplication与@ConditionalOnNotWebApplication</font>**

<font style="color:rgb(51, 51, 51);">这两个注解用于判断当前的应用程序是否是Web应用程序。如果当前应用是Web应用程序，则使用Spring WebApplicationContext,并定义其会话的生命周期。下面是一个简单的示例：</font>

```javascript
@ConditionalOnWebApplication
HealthCheckController healthCheckController(){
 //...
}
```

**<font style="color:rgb(51, 51, 51);">@ConditionalExpression</font>**

<font style="color:rgb(51, 51, 51);">此注解可以让我们控制更细粒度的基于表达式的配置条件限制。当表达式满足某个条件或者表达式为真的时候，将会执行被此注解标注的方法。</font>

```javascript
@Bean
@ConditionalException("${localstore} && ${local == 'true'}")
LocalFileStore store(){
 //...
}
```

**<font style="color:rgb(51, 51, 51);">@Conditional</font>**

<font style="color:rgb(51, 51, 51);">@Conditional注解可以控制更为复杂的配置条件。在Spring内置的条件控制注解不满足应用需求的时候，可以使用此注解定义自定义的控制条件，以达到自定义的要求。下面是使用该注解的简单示例：</font>

```javascript
@Conditioanl(CustomConditioanl.class)
CustomProperties addCustomProperties(){
 //...
}
```

### **<font style="color:rgb(0, 0, 0);">总结</font>**

<font style="color:rgb(51, 51, 51);">本次课程总结了Spring Boot中常见的各类型注解的使用方式，让大家能够统一的对Spring Boot常用注解有一个全面的了解。另外，关注</font><font style="color:rgb(0, 82, 217);">Java</font><font style="color:rgb(51, 51, 51);">知音公众号，回复“后端面试”，送你一份面试题宝典！</font>

<font style="color:rgb(51, 51, 51);">由于篇幅的原因，关于Spring Boot不常用的一些注解，将在下一次分享中进行补充和说明。</font>
