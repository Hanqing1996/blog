#### 教程
* [MySQL安装教程](https://mp.weixin.qq.com/s/mAO83xJcTQ5B59rmCcZaag)
* [navicat安装教程](https://mp.weixin.qq.com/s/xKDWXTfgkfEZvRtLgPK5zA)
* [练习参考](https://zhuanlan.zhihu.com/p/67130837)

#### 问题
* [windows下安装mysql ，在starting server时卡住](https://blog.csdn.net/qq_32846595/article/details/53675492)
#### 注意事项
* sql语句不区分关键字大小写
* sql语句不能用中文符号
* 数据库->查询->新建查询

* select A,B,C -- A,B,C为查询结果中的各列
* where语句中不能使用汇总函数:'where 成绩>avg(成绩)'会报错

#### 执行优先级

1. FROM
2. ON
3. JOIN
4. WHERE
5. GROUP BY
6. HAVING
7. SELECT
8. DISTINCT
9. ORDER BY
10. LIMIT（MySQL）

#### 常用函数
* 插入
```
insert into student (学号,姓名,出生日期,性别)
values('0001','猴子','1989-01-01','男');
```
* 查询指定列
```
select 姓名,性别
from student;
```
* 查找所有列
```
select *
from student;
```
* 为查询结果列设置别名
```
select 姓名 as s_name,性别 as '人类性别'
from student;
```
* 从查询结果中删除重复数据
``` 
/*
姓名,学号合起来视为一条数据
*/
select distinct 姓名,学号
from student; 
```
* 查找学生表中姓名为'猴子'的学生的所有信息
```
select *
from student
where 姓名='猴子';
```
* 为查询结果增加新列
```
select 学号,成绩,成绩/100 as '百分比成绩' 
--'百分比成绩'为score没有的列，由成绩/100生成
from score
```
* 日期比较
```
select *
from student
where 出生日期<'1990-01-01'-- 尽管出生日期是日期类型的,但在sql语句中加单引号
```
* 查找列值为空的记录
```
select *
from teacher
where 教师姓名 is null;
```
* 查找列值为不为空的记录
```
select *
from teacher
where 教师姓名 is not null;
```
* not运算符
```
select *
from score
where not 成绩 >=60; -- 查找成绩<60的学生信息
```
* and运算符
```
select 学号,成绩
from score
where 成绩>=60 and 学号!='0003';
```
* or运算符
``` 
select 学号,成绩
from student
where 性别='男' and (姓名='猴子' or 姓名='马云');
```
* between运算符(包括边界)
```
select *
from score
where 成绩 between 60 and 90;
```
* in运算符(or的简便写法,not in 表示既不是...也不是...)
```
select 姓名,性别
from student
where 姓名 in ('猴子','马云'); -- 查找姓名是猴子或马云的学生
```
* 查找姓名以"猴"开头的学生信息
```
select *
from student
where 姓名 like '猴%';
```
* 查找姓名以"子"结尾的学生信息
```
select *
from student
where 姓名 like '%子';
```
* 查找姓名包含"猴子"的学生信息
```
select *
from student
where 姓名 like '%猴子%';
```
* 查找姓名长度为三个字,切以王开头的学生信息
```
select *
from student
where 姓名 like '王__'; -- 这里有两个下划线
```
*  count函数-参数为列名
```
select count(教师姓名) -- count参数为列名时,得到的是该列非空记录数
from teacher;
```
* count函数-参数为*
```
select count(*) -- count参数为*时,得到的是所有记录数
from teacher;
```
* count函数-distinct
```
select count(distinct 姓名) -- distinct保证查询结果剔除了姓名列的重复值
from student;
```
* sum函数
```
select sum(成绩) 
from score;
```
* max,min函数
```
select max(成绩),min(成绩) 
from score;
```
#### group by
* 使用group by，select语句中只允许出现avg,sum等汇总函数、分组列名
```
/*
语句执行顺序:
1.from student
2.where 出生日期>'1990-01-01'
3.group by 性别;
4.select 性别,count(*)
*/
select 性别,count(*) -- 将学生按性别分组
from student
where 出生日期>'1990-01-01'
group by 性别;
```
* 查询各科成绩最高和最低分
```
select 课程号,max(成绩),min(成绩) -- 查询各科成绩最高和最低分
from score
group by 课程号;
```
* 指定多个列名排序
```
select *
from score
order by 成绩 asc,课程号 desc; 
-- 先按成绩顺序排列,如果成绩列值相同,则按课程号倒序排列
```
* limit -- 只返回前指定行数据
```
select *
from student
limit 3 -- 返回前3行数据
```
* 查询平均成绩大于60分的学生的学号和平均成绩
```
select 学号,avg(成绩)
from score
group by 学号
having avg(成绩)>60
/*
错误写法：
select 学号,avg(成绩)
from score
where avg(成绩)>60 -- Error
*/
```
* 计算各科平均成绩
```
select 课程号,avg(成绩)
from score
group by 课程号;
```
* 查询至少选修两门课程的学生学号
```
/*
语句执行顺序:
1.from score
2.group by 学号 -- 将一张表划分为干张表,结构与原表一致
3.having count(课程号)>2 -- 删除2中不符合要求的表
4.select 学号,avg(成绩)
-- 所有表计算avg(成绩),avg(成绩)只有一行，所有表都只有一行数据(分组学号,avg(成绩))
-- 将所有所有表合并成一张表
-- 如果select语句改为select学号, 所有表只有一行数据(分组学号)
-- 如果select语句改为select学号,课程号,得到的结果是错误的
*/
select 学号,avg(成绩)
from score
group by 学号
having count(课程号)>2;
```
* 查询同名同姓学生并统计同名人数
```
select 姓名,count(*)
from student
group by 姓名;
```
* 将平均成绩大于60分的学生按成绩升序排序
```
/*
语句执行顺序:
1.from score
2.group by 学号
3.having avg(成绩)>60
4.select 学号,avg(成绩) as 平均成绩
5.order by 平均成绩 -- 这一步建立在4的结果(平均成绩列已有的基础上)
*/
select 学号,avg(成绩) as 平均成绩
from score
group by 学号
having avg(成绩)>60
order by 平均成绩; 
-- 倒序排列:order by 平均成绩 desc
-- order by xx 的结果中,空值会被优先放在前几行显示
```
* 查询不及格的课程并按课程号从大到小排序
```
select *
from score
where 成绩<60
order by 成绩
```
* 查询每门课程的平均成绩,结果按平均成绩升序排列,平均成绩相同时,按课程号降序排列
```
select 课程号,avg(成绩) as 平均成绩
from score
group by 课程号
order by 平均成绩,课程号 desc
```
* 找出每个课程里的最低成绩
```
select 课程号,min(成绩) as 最低成绩
from score
group by 课程号
```

#### 视图
* 语法
```
create view 视图名称(视图列名1,视图列名2,视图列名3...)
as
<select 查询语句>;
```
* 创建视图
```
create view 按性别汇总(性别,人数)
as 
select 性别,count(*)
from student
group by 性别;
```
* 使用视图
```
select 性别,人数
from 按性别汇总;
```
* 为什么要使用视图?
> 查询语句封装,减少代码量
* 视图会减少数据库查询吗?
> 不会,因为视图存放的不是数据而是select语句,该执行的查询一句都不会少
#### 子查询
* 将学生按性别汇总
```
select *
from (
select 性别,count(*) as 人数
from student
group by 性别
)as 按性别汇总; -- '按性别汇总'为子查询名
```
* 哪些学生成绩比课程号为0002的任意一个成绩高?
```
select 学号,成绩
from score
where 成绩 > any( -- any同some
select 成绩
from score
where 课程号='0002'
);
```
* 哪些学生成绩比课程号为0002的所有成绩都高?
```
select 学号,成绩
from score
where 成绩 > all(
select 成绩
from score
where 课程号='0002'
);
```
#### 标量子查询(子查询返回的是一个值)
* 大于平均成绩的学生的学号,课程号和成绩
```
select 学号,课程号,成绩
from score
where 成绩>(
select avg(成绩) 
from score
);
```
* 成绩介于差生平均成绩和优等生平均成绩之间的学生有哪些？
(差生：成绩<=60，优等生：成绩>=80)
```
select 学号,成绩
from score
where 成绩 between(
select avg(成绩)
from score
where 成绩<=60
)
and(
select avg(成绩)
from score
where 成绩>=80
);
```
#### 关联子查询
* 查找出每个课程中大于对应课程平均成绩的学生
```
/*
对于
select 学号,课程号,成绩
from score as s1
的每一行数据,
将该行数据的成绩与该行课程号对应的平均成绩进行比较，
若前者大，则该行保留;
若后者大，则该行删去;
*/
select 学号,课程号,成绩
from score as s1
where 成绩 > (
select avg(成绩)
from score as s2
where s1.课程号=s2.课程号
group by 课程号
); 
```
* 找出每个课程里成绩最低的学号
```
select 学号,课程号,成绩
from score as s1
where 成绩 = (
select min(成绩)
from score as s2
where s1.课程号=s2.课程号
group by 课程号
); 
```
#### union
* union -- 去重合并
```
select 课程号,课程名称
from course
union
select 课程号,课程名称
from course1
```
* union all -- 不去重合并
```
select 课程号,课程名称
from course
union all
select 课程号,课程名称
from course1
```
#### cross join
> 若表1有n行数据,表2有m行数据。则表1和表2cross join后有n*m行数据
![](https://github.com/Hanqing1996/blog/blob/master/MySQL/pictures/cross_join.jpg)
#### inner join
```
select a.学号,a.姓名,b.课程号,b.成绩
from student1 as a inner join score1 as b
on a.学号=b.学号
```
![](https://github.com/Hanqing1996/blog/blob/master/MySQL/pictures/inner_join.jpg)
#### left join
> 以左表为主表,进行联接
![](https://github.com/Hanqing1996/blog/blob/master/MySQL/pictures/left_join.jpg)
* 查询所有学生的学号,姓名,课程号,成绩
```
select a.学号,a.姓名,b.课程号,b.成绩
from student1 as a left join score1 as b
on a.学号=b.学号
```
* 查询所有学生的学号,姓名,选课数,总成绩
```
/*
-- 对score表进行处理,按学号分组，由于count()和sum()的存在,处理后的score表每个学号只对应一行数据(count(课程号),sum(成绩))
select count(课程号) as 选课数,sum(成绩)as 选课数
from score
group by 学号

-- 将student表与上述处理过的score表进行左联接,按照交叉联结的原则,最终每个学号对应1*1行数据
select a.学号,a.姓名,count(b.课程号) as 选课数,sum(b.成绩)as 选课数
from student as a 
left JOIN score as b 
on a.学号=b.学号
group by 学号
*/
select a.学号,a.姓名,count(b.课程号) as 选课数,sum(b.成绩) as 总成绩
from student as a 
left JOIN score as b 
on a.学号=b.学号
group by 学号
```
* 查询所有平均成绩大于85的学生的学号,姓名,平均成绩
```
/*
-- 对score表进行处理,按学号分组,并只保留平均成绩大于85的组
select 学号,avg(成绩) as 平均成绩
from score
group by 学号
having avg(成绩)>85

-- 左联接
select a.学号,a.姓名,avg(b.成绩) as 平均成绩
from student as a 
left join score as b
on a.学号=b.学号
group by a.学号
having avg(b.成绩)>85;
*/
select a.学号,a.姓名,avg(b.成绩) as 平均成绩
from student as a 
left join score as b
on a.学号=b.学号
group by a.学号
having avg(b.成绩)>85;
```
* 查询所有学生的选课情况(学号,姓名,课程号,课程名称)
```
/*
三表相联接,所有学生，所以应该用left join
*/
select a.学号,a.姓名,c.课程号,c.课程名称
from student as a 
left JOIN score as b
on a.学号 = b.学号
left JOIN course as c
on b.课程号 = c.课程号
```
* 查询所有选了课的学生的选课情况(学号,姓名,课程号,课程名称)
```
/*
三表相联接,所有选了课的学生，所以应该用inner join
*/
select a.学号,a.姓名,c.课程号,c.课程名称
from student as a 
inner JOIN score as b
on a.学号 = b.学号
inner JOIN course as c
on b.课程号 = c.课程号
```

#### right join
```
select a.学号,a.姓名,b.课程号
from student as a 
RIGHT JOIN score as b 
on a.学号=b.学号
```
#### case表达式
* 判断学生成绩是否及格
```
select 学号,课程号,成绩,
(case 
when 成绩>=60 then '及格'
when 成绩<=60 then '不及格'
else null
end) as 是否及格
from score;
```
* 查询每门课程的及格人数和不及格人数
```
select 课程号,
sum(case 
when 成绩>=60 then 1
else 0
end) as 及格人数,
sum(case 
when 成绩<60 then 1
else 0
end) as 不及格人数
from score
group by 课程号;
```
* 使用分段[100-85],[85-70],[70-60],[<60]来统计各科成绩，分别统计：课程号,课程名称,各分数段人数
```
/*
-- 对score表进行处理,按学号分组,并统计各个分数段人数
select 课程号
sum(case when 成绩>=85 and 成绩<=100 then 1 else 0 end) as '[100-85]',
sum(case when 成绩>=70 and 成绩<85 then 1 else 0 end) as '[85-70]',
sum(case when 成绩>=60 and 成绩<70 then 1 else 0 end) as '[70-60]',
sum(case when 成绩<60 then 1 else 0 end) as '[<60]'
from score
group by 课程号

-- 右联结course表
*/

select a.课程号,b.课程名称,
sum(case when 成绩>=85 and 成绩<=100 then 1 else 0 end) as '[100-85]',
sum(case when 成绩>=70 and 成绩<85 then 1 else 0 end) as '[85-70]',
sum(case when 成绩>=60 and 成绩<70 then 1 else 0 end) as '[70-60]',
sum(case when 成绩<60 then 1 else 0 end) as '[<60]'
from score as a right join course as b
on a.课程号=b.课程号
group by a.课程号
```






 




