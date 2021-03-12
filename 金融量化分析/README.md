#### TuShare
[简介](https://github.com/Hanqing1996/TuShare)<br>
[官方文档](http://tushare.org/)<br>
[如何设置token](https://www.zhihu.com/search?type=content&q=Tushare%20token)<br>

#### 概念
[参考](https://www.ricequant.com/api/python/chn#backtest-results-factors)
* 量化策略：通过一套固定逻辑来分析、判断和决策，自动化地进行股票交易
* 回测：利用历史数据验证投资效果
* 20日均线：当前交易日与其之前19个交易日之盘价的平均值为当日平均值，最后将一段时间内的所有平均值点相连，可得到20日均线
* 仓位：比如你有10万用于投资基金，现用了4万元买基金或股票，你的仓位是40％。如你全买了基金或股票，你就满仓了。如你全部赎回基金卖出股票，你就空仓了。
* 滑点：一笔交易或挂单交易中所要求的价格和实际订单执行或成交价格之间的差异。
* 挂单：交易是指由客户指定交易币种、金额以及交易目标价格后，一旦报价达到或优于客户指定的价格，即执行客户的指令，完成交易，成交价格为该银行的即时报价。
* 夏普率：策略所获得风险溢价的度量——即如果策略额外承担一单位的风险，可以获得多少单位的收益作为补偿。
#### 单因子（宏观）
* 油价（英国北海布伦特油价）：[数据源](https://cn.investing.com/commodities/brent-oil-historical-data)
* 汇率（人民币对美元汇率）：[数据源](https://tushare.pro/document/2?doc_id=179)
* 利率（根据十年国债收益率计算，可参考[这里](http://bond.jrj.com.cn/2017/10/24072123274433.shtml)）
* PMI（采购经理人指数）
#### 资产
* 股票（中证指数500）：[数据源](http://tushare.org/classifying.html#id10)
* 债券（十年期国债）：[数据源](https://cn.investing.com/rates-bonds/china-10-year-bond-yield-historical-data)
* 期货（不要黄金）：[数据源](https://tushare.pro/document/2?doc_id=134)
#### 单因子对资产的影响
相关性|股票 | 债券|期货
---- | ----|----|----|
油价 | 负|-|正|
汇率 | 正|-|负
利率 |负|负|负
PMI |正|-|正
#### 前端要求
1. 时间序列（坐标点间距即为时间单元）上资本总值（股票总市值+债券总市值+期货总市值）变化曲线
2. 时间序列各资产仓位配比变化曲线


#### 通过智能计算可以调整什么
* 各项因子权重
* 时间单元

---
#### python 常用代码
* 读取csv内容，转为DataFrame格式并遍历
```python
def getCodeList():

    tmp_lst = []
    with open('./stocksWeight.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            tmp_lst.append(row)
    df = pd.DataFrame(tmp_lst[1:], columns=tmp_lst[0])

    res=[]
    for index, data in df.iterrows():
        res.append(data['交易所Exchange'][0].lower()+data['交易所Exchange'][2].lower()+'.'+data['成分券代码Constituent Code'].zfill(6))
    return  res[:3]
```
* 将 DataFrame 内容写入 csv
```python
summaryTable.to_csv('./summaryTable/300274_summaryTable.csv',index=False)
```
* 字符串转日期
```python
dateStr='2011-01-02'
date=datetime.datetime.strptime(originalDateStr, '%Y-%m-%d')
print(date)
```
* 获取目录下各个文件名
```python
for root, dirs, files in os.walk('./CSVdata'):
    print(files)
```

