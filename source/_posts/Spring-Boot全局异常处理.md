---
title: Spring Boot全局异常处理
date: 2025-01-22 17:26:04
tags: 
  - 异常处理
categories: 
  - Spring
---
## 为什么使用全局异常处理

在开发时，需要对可能有异常的Controller层方法增加`try-catch`逻辑，而使用Spring MVC提供的**全局异常处理**功能，可以将所有处理异常的逻辑集中起来，进而统一处理所有异常，可以使代码更容易维护。
具体用法如下，详细信息可参考[官方文档](https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-controller/ann-exceptionhandler.html)：
<!-- more -->

## 例子-尚庭公寓全局异常处理

在**common模块**中创建`com.atguigu.lease.common.exception.GlobalExceptionHandler`类，内容如下

```java
@ControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(Exception.class)
    @ResponseBody
    public Result error(Exception e){
        e.printStackTrace();
        return Result.fail();
    }
}
`
上述代码中的关键注解的作用如下
`@ControllerAdvice`用于声明处理全局Controller方法异常的类
`@ExceptionHandler`用于声明处理异常的方法，`value`属性用于声明该方法处理的异常类型
`@ResponseBody`表示将方法的返回值作为HTTP的响应体
**注意：**
全局异常处理功能由SpringMVC提供，因此需要在**common模块**的`pom.xml`中引入如下依赖
```xml
<!--spring-web-->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>
```
