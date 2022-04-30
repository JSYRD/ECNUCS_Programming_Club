Java不是C

消除抵触情绪



多继承？

[c++面向对象和java面向对象的区别_百度知道 (baidu.com)](https://zhidao.baidu.com/question/811224577184531092.html)

[Java 为什么不支持多继承？ - 知乎 (zhihu.com)](https://www.zhihu.com/question/24317891)

描述，抽象，对象之间的交互

* 为什么是OOP？

  * 代码复用

  * 封装

  * 更方便地解决实际问题（实际问题往往是对对象进行操作）

  * 要素

    > 1.任何事物都是对象 
    >
    > 2.“ 程序”是一些对象间的相互协作  
    >
    > 3.一个对象可以包含另一个对象 
    >
    > 4.每个对象都有类型 
    >
    > 5.同一类型的对象接收相同类型的消息 , 提供相同类型的服务

  * 状态，行为，类型（归根到底，只不过是利用面对对象**尽力**将复杂的细节隐藏起来，只提供给使用者**抽象**的使用接口。）

  * getter/setter

    > **的确可以暴露，如果1. 所有内外代码都是你自己写；2. 这个模块再也不改了；3. 不会继承它，或者继承但不改变语义。**
    >
    > David John Wheeler有一句名言：
    >
    > “All problems in computer science can be solved by another level of indirection.”
    >
    > getter、setter就是个很好的中间层。
    >
    > 直接摘录stackoverflow上一个不错的总结：
    >
    > [oop - Why use getters and setters?](https://link.zhihu.com/?target=http%3A//stackoverflow.com/questions/1568091/why-use-getters-and-setters)
    >
    > 1. 这两个方法可以方便增加额外功能（比如验证）。
    > 2. 内部存储和外部表现不同。
    > 3. 可以保持外部接口不变的情况下，修改内部存储方式和逻辑。
    > 4. 任意管理变量的生命周期和内存存储方式。
    > 5. 提供一个debug接口。
    > 6. 能够和模拟对象、序列化乃至WPF库等融合。
    > 7. 允许继承者改变语义。
    > 8. 可以将getter、setter用于lambda表达式。（大概即作为一个函数，参与函数传递和运算）
    > 9. getter和setter可以有不同的访问级别。
    >
    > 的回答，但是这里还想从另外一个更宏观的角度，以我的理解做一点补充。
    >
    > 对于OOP，**宏观上来说，设计者都在试图做到的一件事情就是如何当好程序中的上帝。**通过设计良好的接口（这里的良好指的是不多也不少）来对外暴露一个对象的能力，使得使用者只需要充分了解接口，就可以了解这个对象所能提供的能力。
    >
    > 而使用“方法”来表达对象的能力，同使用“变量”相比，从宏观上来说，没有什么区别，只是形式上的不同。但**使用“方法”来表达接口，更容易体现OOP的一个核心理念“隐藏细节”**

* 类型（Java 优点之跨平台）
  * 声明和创建的区别
  * 基本类型的封装：如int->Integer（为了提供更多与整数相关的功能）
  * 定义类型
  * 创建对象
  * 使用对象
  * Static
  * 引用和对象，引用和指针
  * 可变和不可变(String, Stringbuilder, StringBuffer)



foreach

static 

override

overload

```java
int []A = new int[10];
for(int i=0;i<10;i++){
    System.out.println(i);
}
for(int i: A){
    System.out.println(i);
}
```

