# College Student Spending Behavior Analysis

基于大学生消费数据的行为分析项目，使用 Python 对学生消费结构、影响因素以及消费模式进行探索分析。

## 项目简介

本项目基于 1000 条大学生消费数据，利用 Python 数据分析方法，对学生消费行为进行探索。

主要完成：

- 数据清洗与预处理
- 描述性统计分析
- 消费结构分析
- 收入与消费关系分析
- 年级消费差异分析
- K-Means 聚类分析
- 学生消费画像构建

---

## 技术栈

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- SciPy

---

## 项目流程
数据读取
    ↓
数据清洗
    ↓
探索性数据分析（EDA）
    ↓
统计检验
    ↓
K-Means聚类
    ↓
消费画像分析

---

# 分析结果

## 1. 消费结构分析

分析不同消费类别的平均支出情况。

主要发现：

- 学费和住宿是主要支出来源；
- 日常消费中食品支出占比较高。

结果示例：

![Daily Spending](images/daily_spending.png)


---

## 2. 收入与消费关系分析

采用：

- Pearson相关分析
- 散点图

分析学生月收入与非学费消费之间的关系。

结果：

- 相关系数约为 0.002
- 数据中未观察到明显线性关系

![Income Spending](images/income_vs_spending.png)


---

## 3. 年级消费差异分析

采用：

- 单因素方差分析（ANOVA）

结果：

- p-value = 0.032

说明不同年级学生消费水平存在统计差异。

---

## 4. 消费画像分析

采用：

- StandardScaler标准化
- K-Means聚类算法

通过肘部法选择：

K = 4


最终得到4类消费群体：

|类别|特点|
|-|-|
|Cluster 0|学习与科技投入型|
|Cluster 1|生活保障型|
|Cluster 2|低支出理性消费型|
|Cluster 3|生活品质型|


聚类结果：

![Cluster Heatmap](images/cluster_heatmap.png)


---

## 项目文件结构
college-student-consumption-analysis
├── data
│ └── student_spending.csv
│
├── images
│ ├── daily_spending.png
│ ├── income_vs_spending.png
│ ├── elbow_method.png
│ └── cluster_heatmap.png
│
├── analysis.py
└── README.md

---

## 如何运行

安装依赖：

```bash
pip install -r requirements.txt
python analysis.py