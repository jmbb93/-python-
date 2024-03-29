
# 1. pandas数据结构介绍

## 1.1 Series
一种一维的数组型对象，包含一个值序列（与numpy中的类型相似），并包含了数据标签即索引（index）。
- 交互式环境中，索引在左边，值在右边，默认的索引是从0到N-1（N是数据长度），可通过values和index属性分别获取Series对象的值和索引
- 通常会创建一个索引序列，用标签标识每个数据点
- 可认为Series是一个长度固定且有序的字典，因为它将索引值跟数据值按位置配对
- NaN(not a number)标记缺失值或NA值的方式，使用isnull跟notnull来检查缺失数据
- Series对象和其索引都有name属性

## 1.2 DataFrame
表述矩阵的数据表，包含已排序的列集合，每一列可以是不同的值类型（数值/字符串/布尔值等）。既有行索引也有列索引，可以被视为一个共享相同索引的Series的字典。
- 有多种方式可以创建DataFrame，最常用的是利用包含等长度或numpy数组的字典来形成DataFrame
- 构造函数 p134
- 索引对象，是用于存储横轴标签和其他元数据的（例如轴名称或标签），其不可变性使得在多种数据结构中分享对象更为安全，索引对象可重复 P135

# 2. 基本功能
了解Series和DataFrame中数据交互的基础机制

- 重建索引，reindex,method='ffill'会将值前向填充 P137
- 轴向上删除条目，drop方法
- 索引/选择/过滤，loc iloc P144
- 整数索引
- 算术和数据对齐
- 函数应用和映射
- 排名和排序
- 含有重复标签的轴索引

# 3. 描述性统计的概述和计算
pandas对象装配了一个常用数学/统计学方法的集合，其中大部分属于归约或汇总统计的类别，这些方法从DataFrame的行或列中抽取一个Series或一系列值的单个值（如总和或平均值）。
- 归约方法 P158
- 积累型方法
- 既不是归约也不是积累，如describe
- 相关性和协方差 pandas-datareader
- 唯一值/计数/成员属性
