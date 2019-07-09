
## 1. 文本格式数据的读写
将表格型数据读取为DataFrame对象是pandas的重要特性。
- read_csv,read_table,names,index_col P165 P170
- 分块读入，nrows=5，chunksize=1000，
- 将数据写入文本格式，to_csv
- 使用分隔格式 P175
- JSON数据，已经成为web浏览器和其他应用通过HTTP请求发送数据的标准格式，是一种比CSV等表格文本形式更为自由的数据形式。json.load，pd.read_json
- XMLhe HTML:网络抓取，pd.read_html

## 2. 二进制格式
使用python内建的pickle序列化模块进行二进制格式操作是存储数据（也称为序列化）最高效、最方便的方式之一。
- read_pickle,to_pickle
- 使用HDF5格式
- 读取Microsoft Excel文件

## 3. 与web API交互
很多网站都有公开API，通过JSON或其他格式提供数据服务。推荐的简单易用方式是使用request包。

## 4. 与数据库交互
在业务场景中，大部分数据并不是储存在文本或Excel文件中的。基于SQL的关系型数据库（例如SQL server、PostgreSQL和WySQL）使用广泛，很多小众数据库也变得越发流行。数据库的性能取决于性能、数据完整性以及应用的可伸缩性需求。
- sqlite3
