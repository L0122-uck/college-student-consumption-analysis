import pandas as pd

# 读取数据
df = pd.read_csv("data/student_spending (1).csv")

# 删除无意义的行编号
df = df.drop(columns=["Unnamed: 0"])

# 各项支出的字段
spending_columns = [
    "tuition",
    "housing",
    "food",
    "transportation",
    "books_supplies",
    "entertainment",
    "personal_care",
    "technology",
    "health_wellness",
    "miscellaneous"
]

# 计算各项支出的平均值
average_spending = df[spending_columns].mean().sort_values(ascending=False)

print("=== 各项支出平均值 ===")
print(average_spending)
import matplotlib.pyplot as plt

# 排除学费，分析日常消费
daily_spending = average_spending.drop("tuition")

# 绘制柱状图
plt.figure(figsize=(10, 6))
daily_spending.sort_values().plot(kind="barh")

plt.title("Average Daily Spending by Category")
plt.xlabel("Average Spending")
plt.ylabel("Spending Category")

plt.tight_layout()
plt.savefig("daily_spending.png", dpi=300, bbox_inches="tight"
)
plt.show()

# ==============================
# 第二部分：收入与消费关系
# ==============================

# 计算每个学生的非学费总支出
df["total_spending"] = df[spending_columns].drop(columns=["tuition"]).sum(axis=1)

print("\n=== 总消费统计 ===")
print(df["total_spending"].describe())
# ==============================
# 第三部分：收入与消费关系
# ==============================

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.scatter(
    df["monthly_income"],
    df["total_spending"],
    alpha=0.6
)

plt.title("Monthly Income vs Total Spending")
plt.xlabel("Monthly Income")
plt.ylabel("Total Spending")

plt.tight_layout()
plt.savefig(
    "income_vs_spending.png"
,
    dpi=300
,
    bbox_inches="tight"
)

plt.show()
# ==============================
# 第四部分：相关性分析
# ==============================

correlation = df["monthly_income"].corr(df["total_spending"])

print("\n=== 收入与消费相关系数 ===")
print(round(correlation, 3))
# ==============================
# 第五部分：不同收入水平的消费差异
# ==============================

# 按月收入分成三组
df["income_group"] = pd.qcut(
    df["monthly_income"],
    q=3,
    labels=["Low Income", "Middle Income", "High Income"]
)

# 计算不同收入组的平均消费
income_spending = df.groupby(
    "income_group",
    observed=True
)["total_spending"].mean()

print("\n=== 不同收入组的平均消费 ===")
print(income_spending)
# ==============================
# 第六部分：收入组之间的差异检验
# ==============================

from scipy.stats import f_oneway

low_income = df[df["income_group"] == "Low Income"]["total_spending"]
middle_income = df[df["income_group"] == "Middle Income"]["total_spending"]
high_income = df[df["income_group"] == "High Income"]["total_spending"]

f_stat, p_value = f_oneway(
    low_income,
    middle_income,
    high_income
)

print("\n=== 单因素方差分析（ANOVA） ===")
print("F-statistic:", round(f_stat, 3))
print("p-value:", round(p_value, 3))
# ==============================
# 第七部分：不同年级的消费情况
# ==============================

year_spending = df.groupby(
    "year_in_school"
)["total_spending"].mean().sort_values(ascending=False)

print("\n=== 不同年级的平均消费 ===")
print(year_spending)
# ==============================
# 第八部分：不同年级消费差异检验
# ==============================

freshman = df[df["year_in_school"] == "Freshman"]["total_spending"]
sophomore = df[df["year_in_school"] == "Sophomore"]["total_spending"]
junior = df[df["year_in_school"] == "Junior"]["total_spending"]
senior = df[df["year_in_school"] == "Senior"]["total_spending"]

f_stat_year, p_value_year = f_oneway(
    freshman,
    sophomore,
    junior,
    senior
)

print("\n=== 不同年级消费的 ANOVA 检验 ===")
print("F-statistic:", round(f_stat_year, 3))
print("p-value:", round(p_value_year, 3))
# ==============================
# 第九部分：不同年级消费可视化
# ==============================

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

year_spending.plot(
    kind="bar"
)

plt.title("Average Spending by Year in School")
plt.xlabel("Year in School")
plt.ylabel("Average Total Spending")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()
# ==============================
# 第十部分：学生消费画像 - KMeans聚类
# ==============================

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 选择消费特征
cluster_features = [
    "food",
    "housing",
    "transportation",
    "books_supplies",
    "entertainment",
    "personal_care",
    "technology",
    "health_wellness",
    "miscellaneous"
]

X = df[cluster_features]

# 标准化
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("聚类数据准备完成")
# ==============================
# 第十一部分：确定最佳K值
# ==============================

import matplotlib.pyplot as plt

inertia = []

for k in range(2, 10):
    kmeans = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )
    
    kmeans.fit(X_scaled)
    
    inertia.append(kmeans.inertia_)


plt.figure(figsize=(8,5))

plt.plot(
    range(2,10),
    inertia,
    marker="o"
)

plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Inertia")
plt.savefig(
    "elbow_method.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()
# ==============================
# 第十二部分：KMeans正式聚类
# ==============================

kmeans = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

# 生成类别标签
df["cluster"] = kmeans.fit_predict(X_scaled)

print("\n=== 各类别学生数量 ===")
print(df["cluster"].value_counts())
# ==============================
# 第十三部分：分析各类消费画像
# ==============================

cluster_profile = df.groupby("cluster")[cluster_features].mean()

print("\n=== 各类学生平均消费特征 ===")
print(cluster_profile)
# 显示完整聚类画像

pd.set_option("display.max_columns", None)

print("\n=== 完整消费画像 ===")
print(cluster_profile)
# ==============================
# 第十五部分：聚类结果热力图
# ==============================

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

sns.heatmap(
    cluster_profile,
    annot=True,
    fmt=".1f",
    cmap="YlGnBu"
)

plt.title("Student Spending Pattern by Cluster")

plt.xlabel("Spending Category")
plt.ylabel("Cluster")

plt.tight_layout()
plt.savefig("cluster_heatmap.png", dpi=300, bbox_inches="tight"
)

plt.show()