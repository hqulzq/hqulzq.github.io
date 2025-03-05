---
title: Mybatis-Plus快速入门
date: 2025-01-22 17:34:22
tags:
  - Mybatis-Plus
  - 快速入门
categories:
  - Java工具
typora-root-url: Mybatis-Plus快速入门
---

# MyBatis Plus快速入门

## 1、概述

MyBatis-Plus（简称 MP）是一个MyBatis 的增强工具，在 MyBatis 的基础上只做增强不做改变，为简化开发、提高效率而生。其突出的特性如下：

- **无侵入**：只做增强不做改变，引入它不会对现有工程产生影响，如丝般顺滑
- **强大的 CRUD 操作**：内置通用 Mapper、通用 Service，提供了大量的通用的CRUD方法，因此可以省去大量手写sql的语句的工作。
- **条件构造器**：提供了强大的条件构造器，可以构造各种复杂的查询条件，以应对各种复杂查询。
- **内置分页插件**：配置好插件之后，写分页等同于普通 List 查询，无需关注分页逻辑。

下面通过一个简单案例快速熟悉MyBatis Plus的基本使用
<!-- more -->

## 2、数据库准备

首先在数据库中准备一张表，为后序的学习做准备。

1. **创建数据库**

   在MySQL中创建一个数据库`hello_mp`

   ```sql
   CREATE DATABASE hello_mp CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
   ```

2. **创建表**

   在`hello-mp`库中创建一个表`user`

   ```sql
   DROP TABLE IF EXISTS user;
   CREATE TABLE user
   (
       id BIGINT(20) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
       name VARCHAR(30) NULL DEFAULT NULL COMMENT '姓名',
       age INT(11) NULL DEFAULT NULL COMMENT '年龄',
       email VARCHAR(50) NULL DEFAULT NULL COMMENT '邮箱',
       PRIMARY KEY (id)
   );
   ```

3. **插入数据**

   ```bash
   INSERT INTO user (id, name, age, email) VALUES
   (1, 'Jone', 18, 'test1@baomidou.com'),
   (2, 'Jack', 20, 'test2@baomidou.com'),
   (3, 'Tom', 28, 'test3@baomidou.com'),
   (4, 'Sandy', 21, 'test4@baomidou.com'),
   (5, 'Billie', 24, 'test5@baomidou.com');
   ```

## 3 与SpringBoot集成

Mybatis Plus与SpringBoot的集成十分简单，具体操作如下

1. **引入Maven 依赖**

   提前创建好一个SpringBoot项目，然后在项目中引入MyBatis Plus依赖

   ```xml
   <dependency>
       <groupId>com.baomidou</groupId>
       <artifactId>mybatis-plus-boot-starter</artifactId>
       <version>3.5.3.2</version>
   </dependency>
   ```

   本案例完整的`pom.xml`文件如下

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd">
       <modelVersion>4.0.0</modelVersion>
       <parent>
           <groupId>org.springframework.boot</groupId>
           <artifactId>spring-boot-starter-parent</artifactId>
           <version>3.0.9</version>
           <relativePath/> <!-- lookup parent from repository -->
       </parent>
       <groupId>com.atguigu</groupId>
       <artifactId>hello-mp</artifactId>
       <version>0.0.1-SNAPSHOT</version>
       <name>hello-mp</name>
       <description>hello-mp</description>
       <properties>
           <java.version>17</java.version>
       </properties>
       <dependencies>
           <dependency>
               <groupId>org.springframework.boot</groupId>
               <artifactId>spring-boot-starter-web</artifactId>
           </dependency>
   
           <dependency>
               <groupId>com.mysql</groupId>
               <artifactId>mysql-connector-j</artifactId>
               <scope>runtime</scope>
           </dependency>
           <dependency>
               <groupId>org.projectlombok</groupId>
               <artifactId>lombok</artifactId>
               <optional>true</optional>
           </dependency>
           <dependency>
               <groupId>org.springframework.boot</groupId>
               <artifactId>spring-boot-starter-test</artifactId>
               <scope>test</scope>
           </dependency>
           <dependency>
               <groupId>com.baomidou</groupId>
               <artifactId>mybatis-plus-boot-starter</artifactId>
               <version>3.5.3.2</version>
           </dependency>
       </dependencies>
   
       <build>
           <plugins>
               <plugin>
                   <groupId>org.springframework.boot</groupId>
                   <artifactId>spring-boot-maven-plugin</artifactId>
               </plugin>
           </plugins>
       </build>
   
   </project>
   ```

2. **配置`application.yml`文件**

   配置数据库相关内容如下

   ```yml
   spring:
     datasource:
       driver-class-name: com.mysql.cj.jdbc.Driver
       username: root
       password: Atguigu.123
       url: jdbc:mysql://192.168.10.101:3306/hello_mp?useUnicode=true&characterEncoding=utf-8&serverTimezone=GMT%2b8
   ```

## 4 创建实体类

创建与`user`表相对应的实体类，如下

```java
@Data
@TableName("user")
public class User {

    @TableId(value = "id", type = IdType.AUTO)
    private Long id;

    @TableField("name")
    private String name;

    @TableField("age")
    private Integer age;

    @TableField("email")
    private String email;
}
```

**知识点**：

实体类中的三个注解的含义如下

- `@TableName`：表名注解，用于标识实体类所对应的表
  - `value`：用于声明表名

- `@TableId`：主键注解，用于标识主键字段
  - `value`：用于声明主键的字段名
  - `type`：用于声明主键的生成策略，常用的策略有`AUTO`、`ASSIGN_UUID`、`INPUT`等等

- `@TableField`：普通字段注解，用于标识属性所对应的表字段
  - `value`：用于声明普通字段的字段名


## 5 通用Mapper

通用Mapper提供了通用的CRUD方法，使用它可以省去大量编写简单重复的SQL语句的工作，具体用法如下

1. **创建Mapper接口**

   创建`UserMapper`接口，并继承由Mybatis Plus提供的`BaseMapper<T>`接口，如下

   ```java
   @Mapper
   public interface UserMapper extends BaseMapper<User> {
   }
   ```

   **知识点**：

   若Mapper接口过多，可不用逐一配置`@Mapper`注解，而使用`@MapperScan`注解指定包扫描路径进行统一管理，例如

   ```java
   @SpringBootApplication
   @MapperScan("com.atguigu.hellomp.mapper")
   public class HelloMpApplication {
   
       public static void main(String[] args) {
           SpringApplication.run(HelloMpApplication.class, args);
       }
   }
   ```

2. **测试通用Mapper**

   创建`userMapperTest`测试类型，内容如下

   ```java
   @SpringBootTest
   class UserMapperTest {
   
       @Autowired
       private UserMapper userMapper;
   
       @Test
       public void testSelectList() {
           List<User> users = userMapper.selectList(null);
           users.forEach(System.out::println);
       }
   
       @Test
       public void testSelectById() {
           User user = userMapper.selectById(1);
           System.out.println(user);
       }
   
       @Test
       public void testInsert() {
           User user = new User();
           user.setName("zhangsan");
           user.setAge(11);
           user.setEmail("test@test.com");
           userMapper.insert(user);
       }
   
       @Test
       public void testUpdateById() {
           User user = userMapper.selectById(1);
           user.setName("xiaoming");
           userMapper.updateById(user);
       }
       
       @Test
       public void testDeleteById() {
           userMapper.deleteById(1);
       }
   }
   ```

## 6 通用Service

通用Service进一步封装了通用Mapper的CRUD方法，并提供了例如`saveOrUpdate`、`saveBatch`等高级方法。

1. **创建Service接口**

   创建`UserService`，内容如下

   ```java
   public interface UserService extends IService<User> {
   }
   ```

2. **创建Service实现类**

   创建`UserServiceImpl`，内容如下

   ```java
   @Service
   public class UserServiceImpl extends ServiceImpl<UserMapper, User> implements UserService {
   }
   ```

3. **测试通用Service**

   创建`UserServiceImplTest`测试类，内容如下

   ```java
   @SpringBootTest
   class UserServiceImplTest {
   
   
       @Autowired
       private UserService userService;
   
       @Test
       public void testSaveOrUpdate() {
           User user1 = userService.getById(2);
           user1.setName("xiaohu");
   
           User user2 = new User();
           user2.setName("lisi");
           user2.setAge(27);
           user2.setEmail("lisi@email.com");
           userService.saveOrUpdate(user1);
           userService.saveOrUpdate(user2);
       }
   
   
       @Test
       public void testSaveBatch() {
           User user1 = new User();
           user1.setName("dongdong");
           user1.setAge(49);
           user1.setEmail("dongdong@email.com");
   
           User user2 = new User();
           user2.setName("nannan");
           user2.setAge(29);
           user2.setEmail("nannan@email.com");
   
           List<User> users = List.of(user1, user2);
           userService.saveBatch(users);
       }
   }
   ```

## 7 条件构造器

条件构造器用于构造复杂的查询条件，例如获取`name='zhangsan'`的用户。MyBatis Plus共提供了两类构造器，分别是`QueryWrapper`和`UpdateWrapper`。其中`QueryWrapper`主要用于查询、删除操作，`UpdateWrapper`主要用于更新操作，下面通过几个案例学习条件构造器的基础用法。

1. 创建`WrapperTest`测试类，内容如下

   ```java
   @SpringBootTest
   public class WrapperTest {
   
       @Autowired
       private UserService userService;
   
       @Test
       public void testQueryWrapper() {
   
           //查询name=Tom的所有用户
           QueryWrapper<User> queryWrapper1 = new QueryWrapper<>();
           queryWrapper1.eq("name", "Tom");
   
           //查询邮箱域名为baomidou.com的所有用户
           QueryWrapper<User> queryWrapper2 = new QueryWrapper<>();
           queryWrapper2.like("email", "baomidou.com");
   
           //查询所有用户信息并按照age字段降序排序
           QueryWrapper<User> queryWrapper3 = new QueryWrapper<>();
           queryWrapper3.orderByDesc("age");
           
           //查询age介于[20,30]的所有用户
           QueryWrapper<User> queryWrapper4 = new QueryWrapper<>();
           queryWrapper4.between("age", 20, 30);
           
           //查询age小于20或大于30的用户
           QueryWrapper<User> queryWrapper5 = new QueryWrapper<>();
           queryWrapper5.lt("age", 20).or().gt("age", 30);
   
           //邮箱域名为baomidou.com且年龄小于30或大于40且的用户
           QueryWrapper<User> queryWrapper6 = new QueryWrapper<>();
           queryWrapper6.like("email", "baomidou.com").and(wrapper -> wrapper.lt("age", 30).or().gt("age", 40));
           
           List<User> list = userService.list(queryWrapper6);
           list.forEach(System.out::println);
       }
   
       @Test
       public void testUpdateWrapper() {
   
           //将name=Tom的用户的email改为Tom@baobidou.com
           UpdateWrapper<User> updateWrapper = new UpdateWrapper<>();
           updateWrapper.eq("name", "Tom");
           updateWrapper.set("email", "Tom@baobidou.com");
   
           userService.update(updateWrapper);
       }
   }
   ```

2. 创建`LambdaWrapperTest`测试类，内容如下

   上述的`QueryWrapper`和`UpdateWrapper`均有一个`Lambda`版本，也就是`LambdaQueryWrapper`和`LambdaUpdateWrapper`，`Lambda`版本的优势在于，可以省去字段名的硬编码，具体案例如下：

   ```java
   @SpringBootTest
   public class LambdaWrapperTest {
   
       @Autowired
       private UserService userService;
   
       @Test
       public void testLambdaQueryWrapper() {
           //查询name=Tom的所有用户
           LambdaQueryWrapper<User> lambdaQueryWrapper = new LambdaQueryWrapper<>();
           lambdaQueryWrapper.eq(User::getName, "Tom");
   
           List<User> list = userService.list(lambdaQueryWrapper);
           list.forEach(System.out::println);
   
       }
   
       @Test
       public void testLambdaUpdateWrapper() {
           //将name=Tom的用户的邮箱改为Tom@tom.com
           LambdaUpdateWrapper<User> lambdaUpdateWrapper = new LambdaUpdateWrapper<>();
           lambdaUpdateWrapper.eq(User::getName, "Tom");
           lambdaUpdateWrapper.set(User::getEmail, "Tom@Tom.com");
   
           userService.update(lambdaUpdateWrapper);
       }
   }
   ```

## 8 分页插件

分页查询是一个很常见的需求，故Mybatis-Plus提供了一个分页插件，使用它可以十分方便的完成分页查询。下面介绍Mybatis-Plus分页插件的用法，详细信息可参考[官方文档](https://baomidou.com/pages/97710a/)。

- 配置分页插件

  创建`com.atguigu.hellomp.config.MPConfiguration`配置类，增加如下内容

  ```java
  @Configuration
  public class MPConfiguration {
  
      @Bean
      public MybatisPlusInterceptor mybatisPlusInterceptor() {
          MybatisPlusInterceptor interceptor = new MybatisPlusInterceptor();
          interceptor.addInnerInterceptor(new PaginationInnerInterceptor(DbType.MYSQL));
          return interceptor;
      }
  }
  ```

- 分页插件使用说明

  - 构造分页对象

    分页对象包含了分页的各项信息，其核心属性如下：


    | 属性名  | 类型 | 默认值    | 描述                   |
    | ------- | ---- | --------- | ---------------------- |
    | records | List | emptyList | 查询数据列表           |
    | total   | Long | 0         | 查询列表总记录数       |
    | size    | Long | 10        | 每页显示条数，默认`10` |
    | current | Long | 1         | 当前页                 |
    
    分页对象既作为分页查询的参数，也作为分页查询的返回结果，当作为查询参数时，通常只需提供`current`和`size`属性，如下
    
    ```java
    IPage<T> page = new Page<>(current, size);
    ```
    
    注：`IPage`为分页接口，`Page`为`IPage`接口的一个实现类。`Page` 类是具体的实现类，主要用于创建分页对象、传递分页参数以及接收分页结果。`IPage` 接口是抽象的接口，用于定义分页的通用行为和属性，提升代码的灵活性与可扩展性。在实际开发中，通常先用 `Page` 类创建分页对象，再用 `IPage` 接口来接收和处理分页结果。


  - 分页查询

    Mybatis Plus的`BaseMapper`和`ServiceImpl`均提供了常用的分页查询的方法，例如：

    - `BaseMapper`的分页查询：

      ```java
      IPage<T> selectPage(IPage<T> page,Wrapper<T> queryWrapper);
      ```

    - `ServiceImpl`的分页查询：

      ```java
      // 无条件分页查询
      IPage<T> page(IPage<T> page);
      // 条件分页查询
      IPage<T> page(IPage<T> page, Wrapper<T> queryWrapper);
      ```

    - 自定义Mapper

      对于自定义SQL，也可以十分方便的完成分页查询，如下

      `Mapper`接口：

      ```java
      IPage<UserVo> selectPageVo(IPage<?> page, Integer state);
      ```

      `Mapper.xml`：

      ```java
      <select id="selectPageVo" resultType="xxx.xxx.xxx.UserVo">
          SELECT id,name FROM user WHERE state=#{state}
      </select>
      ```

      **注意**：`Mapper.xml`中的SQL只需实现查询`list`的逻辑即可，无需关注分页的逻辑。

- 案例实操

  分页查询案例如下：

  创建`PageTest`测试类，内容如下

  ```java
  @SpringBootTest
  public class PageTest {
  
      @Autowired
      private UserService userService;
  
      @Autowired
      private UserMapper userMapper;
  
      //通用Service分页查询
      @Test
      public void testPageService() {
          Page<User> page = new Page<>(2, 3);
          Page<User> userPage = userService.page(page);
          userPage.getRecords().forEach(System.out::println);
      }
  
      //通用Mapper分页查询
      @Test
      public void testPageMapper() {
          IPage<User> page = new Page<>(2, 3);
          IPage<User> userPage = userMapper.selectPage(page, null);
          userPage.getRecords().forEach(System.out::println);
      }
  
      //自定义SQL分页查询
      @Test
      public void testCustomMapper() {
          IPage<User> page = new Page<>(2, 3);
          IPage<User> userPage = userMapper.selectUserPage(page);
          userPage.getRecords().forEach(System.out::println);
      }
  }
  ```

  在UserMapper中声明分页查询方法如下

  ```java
  IPage<User> selectUserPage(IPage<User> page);
  ```

  创建`resources/mapper/UserMapper.xml`文件，内容如下

  ```xml
  <?xml version="1.0" encoding="UTF-8"?>
  <!DOCTYPE mapper
          PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
          "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
  <mapper namespace="com.atguigu.hellomp.mapper.UserMapper">
      <select id="selectUserPage" resultType="com.atguigu.hellomp.entity.User">
          select *
          from user
      </select>
  </mapper>
  ```

  **注意**：

  Mybatis-Plus中`Mapper.xml`文件路径默认为：`classpath*:/mapper/**/*.xml`，可在`application.yml`中配置以下参数进行修改

     ```yml
  mybatis-plus:
    mapper-locations: classpath*:/mapper/**/*.xml
     ```

## 9 MyBatisX插件

MyBatis Plus提供了一个IDEA插件——`MybatisX`,使用它可根据数据库快速生成`Entity`、`Mapper`、`Mapper.xml`、`Service`、`ServiceImpl`等代码，使用户更专注于业务。

下面演示具体用法

1. **安装插件**

   在IDEA插件市场搜索`MyBatisX`，进行在线安装

   ![image-20250122173825745](image-20250122173825745.png)

2. **配置数据库连接**

   在IDEA中配置数据库连接

   ![image-20250122173835578](image-20250122173835578.png)

   

3. **生成代码**

   首先将之前编写的`User`、`UserMapper`、`UserServcie`、`UserServiceImpl`全部删除，然后按照下图指示使用插件生成代码

   ![image-20250122173844446](image-20250122173844446.png)

   配置实体类相关信息

   ![image-20250122173850326](image-20250122173850326.png)

   配置代码模版信息

   ![image-20250122173901559](image-20250122173901559.png)

   点击Finish然后查看生成的代码。