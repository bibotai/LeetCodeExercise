# 散列表


[](https://zh.wikipedia.org/zh-hans/%E5%93%88%E5%B8%8C%E8%A1%A8#mw-head)[](https://zh.wikipedia.org/zh-hans/%E5%93%88%E5%B8%8C%E8%A1%A8#p-search)

**散列表**（**Hash table**，也叫**哈希表**），是根据[键](https://zh.wikipedia.org/wiki/%E9%8D%B5 "键")（Key）而直接访问在内存存储位置的[数据结构](https://zh.wikipedia.org/wiki/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84 "数据结构")。也就是说，它通过计算一个关于键值的函数，将所需查询的数据[映射](https://zh.wikipedia.org/wiki/%E6%98%A0%E5%B0%84 "映射")到表中一个位置来访问记录，这加快了查找速度。这个映射函数称做[散列函数](https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B0 "散列函数")，存放记录的数组称做**散列表**。

一个通俗的例子是，为了查找电话簿中某人的号码，可以创建一个按照人名首字母顺序排列的表（即建立人名)到首字母F(x)的一个[函数](https://zh.wikipedia.org/wiki/%E5%87%BD%E6%95%B0 "函数")关系），在首字母为W的表中查找“王”姓的电话号码，显然比直接查找就要快得多。这里使用人名作为[关键字](https://zh.wikipedia.org/wiki/%E9%97%9C%E9%8D%B5%E5%AD%97 "关键字")，“取首字母”是这个例子中[散列函数](https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E5%87%BD%E6%95%B0 "散列函数")的函数法则F()，存放首字母的表对应[散列表](https://zh.wikipedia.org/wiki/%E6%95%A3%E5%88%97%E8%A1%A8 "散列表")。关键字和函数法则理论上可以任意确定。