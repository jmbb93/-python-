
# 数据规整：连接、联合与重塑
在很多应用中，数据可能分布在多个文件或数据库中，亦或以某种不易于分析的格式进行排列。本章首先介绍pandas中的分层索引，然后再深入介绍特定的数据操作。

## 1. 分层索引
pandas的重要特性，允许你在一个轴向上拥有多个（两个或两个以上）索引层级，笼统地说，分层索引提供了一种在更低维度的形式中处理更高维度数据的方式。
- 部分索引，可在内部选择
- 在重塑数据和数组透视表等分组操作中扮演了重要角色，unstack()  stack()
- MultiIndex可使用其自身的构造函数创建并复用
- 重排序和层级排序，swaplevel接收两个层级序号或层级名称，返回一个进行了层级变换的新对象
- sort_index只能在单一层级上排序，sort_index(level=0)
- sum(level='key2')按层级进行汇总
- 使用DF的列进行索引，set_index()  reset_index()

## 2. 联合与合并数据集
包含在pandas对象中的数据可以通过多种方式联合在一起：
- pandas.merge 根据一个或多个键将行进行连接，即数据库的连接操作
- pandas.concat 使对象在轴向上进行粘合或“堆叠”
- combine_first 实例方法允许将重叠的数据拼接在一起，以使一个对象中的值填充另一个对象中的缺失值

### 2.1 数据库风格的DataFrame连接
合并或连接操作通过一个或多个键连接来联合数据集。这些操作是关系型数据库的核心内容，pandas中的merge函数主要用于将各种join操作算法运用在你的数据上。
- merge会自动将重叠列名作为连接的键，merge(df1,df2,on='key')on用来显式地指定连接键
- merge默认做内连接（inner join），可用how指定left/right/outer
- 多对多是行的笛卡尔积
- suffixes指定重叠的列名

### 2.2 根据索引合并
- left_index=True right_index=True
- 默认的合并方法是连接键相交，可以用外连接来合并，how='outer'
- 简单的索引-索引合并，可以向join方法传入一个DataFrame列表，该方法可以替代下一节中的concat

### 2.3 沿轴向连接
可互换地成为拼接、绑定或堆叠。
- numpy.concatenate
- pandas.concat，axis默认为0，axis=1是列
- concat(keys=['','',''...]区分合并结果中的各部分
- concat字典时，字典的键会用于keys选项
- ignore_index=True 行索引中不包含任何相关数据

### 2.4 联合重叠数据
既不是数据联合，也不是合并操作
- numpy.where面向数组的if-else等价操作
- Series.combine_first()等价于pandas常见数据对齐逻辑的轴向操作，可认为是根据你传入的对象来“修补”调用对象的缺失值

## 3. 重塑和透视
重排列表格型数据的基础操作
- 使用多层索引 stack(堆叠)  unstack(拆堆)
- 将“长”透视为“宽”，PeriodIndex---pivot---set_index---unstack
- 将“宽”透视为“长”，pivot的反操作是melt，必须指定哪些列是分组指标key

学会了pandas的数据导入、清洗以及按照你自己的想法来重新组织数据，接下来就可以使用matplotlib进行数据可视化了。
