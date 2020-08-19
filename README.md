## 项目简介
这学期数据库原理课上，我们组复现了NL2SQL领域的一篇小论文，做了一个用自然语言查询数据库的小工具。<br>
虽然论文算法很简单，适用场景也有限，但做出来的效果还是能唬住一片人的，非常花里胡哨。<br><br>
你可以输入：siri,能不能告诉我在光彪楼活动的文艺类社团和社团社长吗？<br>
我们的小工具可以将这句自然语言转化为：<br>
SELECT 社团名称, 社长 FROM student_org_info WHERE 活动地点="光彪楼" AND 社团类型="文艺类" <br>
然后返回查询结果{"烘焙社"，"小黄"}<br><br>
还在用SQL查数据库？解放双手和大脑，用自然语言去查询数据库吧。<br>
## 目录结构
doc: 包含了本工具采用的nl2sql的算法解析和复现的论文<br>
example: 演示该工具的视频<br>
main.py: 直接右键运行即可。很可惜，由于数据库在本地，这个程序还跑不起来。等我有时间有精力了，做一个在线的数据库<br>
## nl2sql算法
流程：1. 解析输入的自然语言，提取关键词（select的对象，where后的条件）<br>
     2. 对这些关键词进行同义词替换 <br>
     3. 将关键词填入sql语句中<br>
评价：我使用的算法非常简单，可以实现基本的sql查询语句，但是算法不支持嵌套查询，而且鲁棒性不强，适用于单表数据库<br>
想了解具体算法可以阅读doc文件夹下的文档
## 技术选型
编程语言：python 3.7 <br>
中文分词工具：jieba <br>
数据库：mysql <br>
