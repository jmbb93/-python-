## numpy ndarray
numpy的核心特征之一是N-维数组对象——ndarray，是Python中一个快速、灵活的大型数据集容器，可以用类似标量的操作语法做数学计算。
- 标准导入，import numpy as np
- 生成ndarray，函数有array asarray arange ones ones_like zeros zeros_like empty empty_like full full_like eye identity
- ndarray的数据类型，dtype
- numpy数组算术，可进行批量操作而无须任何for循环，即向量化
- 基础索引与切片，中括号跟冒号：
- 布尔索引，条件判断，多条件用&(and)和|(or)
- 神奇索引，使用整数数组进行数据索引
- 数组转置和换轴，transpose T属性 swapaxes

## 通用函数：快速的逐元素数组函数
也称ufunc，是一种在ndarray数据中进行逐元素操作的函数。某些简单函数接收一个或多个标量数值，并产生一个或多个标量结果，而通用函数就是对这些简单函数的向量化封装。
- 一元通用函数 P107
- 二元通用函数，P108

## 使用数组进行面向数组编程
使用numpy数组可以利用简单的数组表达式完成多种数据操作任务，而无须写些大量循环，这些利用数组表达式替代显式循环的方法成为向量化。
- 将条件逻辑作为数组操作 np.where是三元表达式x if condition else y的向量版本
- 数学和统计方法 sum mean std var min max argmin argmax cumsum cumprod
- 布尔值数组的方法，any all
- 排序，sort
- 唯一值和其他集合逻辑

## 使用数组进行文件输入和输出
numpy可以在硬盘中将数据以文本或二进制文件的格式进行存入硬盘或由硬盘载入
- np.save
- np.load
- np.savez
- np.savez_compressed

## 线性代数
比如矩阵乘法、分解、行列式等方阵数学，是所有数组类库的重要组成部分，跟MATLAB等其他语言不同的是，numpy中*是矩阵的逐元素乘积而不是矩阵的点乘积。
- .dot
- @
- linalg

## 伪随机数生成
填补了Python内建的random模块的不足，可以高效的生成多种概率分布下的完整样本值数组
- np.random.normal(size)
- normalvariate
- np.random.RandomState

## 随机漫步
- random
- 一次性模拟多次随机漫步
