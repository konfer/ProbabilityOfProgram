#coding:utf-8

import ExploreDataAnalyse.nsfg as nsfg

df=nsfg.ReadFemPreg()
print(df)

print(df.columns)
print(df.columns[1])
pregordr=df['pregordr']
print("---pregordr----------")
type(pregordr)
print("----type----------pregordr----------------")
print(pregordr)

print("----dataVerify----------")
print(df.outcome.value_counts().sort_index())

print(df.outcome)