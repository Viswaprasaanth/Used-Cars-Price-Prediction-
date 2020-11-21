#READ DATA
import pandas as pd
data=pd.read_csv("cars_price.csv")
data.head()

#DATA PRE-PROCESSING
data.describe()
data.isnull()
data.boxplot()

#RELATION AMONG RICESUSD, MILEAGE, YEAR
df=pd.DataFrame(data, columns=["priceUSD", "year", "mileage(kilometers)"])
df.corr()

#RELATION BETWEEN SEGMENT, PRICEUSD
data=data.dropna(subset=["segment"], axis=0)
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())
q1 = """SELECT segment,priceUSD 
FROM data GROUP BY segment ORDER BY priceUSD DESC;"""
query1 = pysqldf(q1)
x=query1["segment"]
y=query1["priceUSD"]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(x,y)
plt.xlabel("segment")
plt.ylabel("priceUSD")
plt.show()

#QUERIES
#DISPLAYING MAKE, PRICEUSD GROUP BY MAKE ORDER BY PRICEUSD#DISPLAYING MAKE, PRICEUSD GROUP BY PRICEUSD
q1 = """SELECT make, priceUSD
FROM data
GROUP BY make ORDER BY priceUSD DESC LIMIT 10;"""
query1 = pysqldf(q1)
x=query1["make"]
y=query1["priceUSD"]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(x,y)
#plt.title("GT Compressor decay state coefficient")
plt.xlabel("Make")
plt.ylabel("priceUSD")
plt.show()

#DISPLAYING MODEL FOR A PARTICULAR COMPANY GROUP BY MODEL
q1 = """SELECT model, priceUSD
FROM data where make='bentley'
GROUP BY model ORDER BY priceUSD DESC LIMIT 10;"""
query1 = pysqldf(q1)
print(query1)
import matplotlib
matplotlib.axes.Axes.pie
matplotlib.pyplot.pie
x=query1["model"]
y=query1["priceUSD"]
fig1, ax1 = plt.subplots()
ax1.pie(y, labels=x, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
plt.show()

#DISPLAYING YEAR, MAKE, PRICEUSD GROUP BY YEAR ORDER BY PRICEUSD (DESCNDING)
q1 = """SELECT year, make, priceUSD
FROM data GROUP BY year ORDER BY priceUSD DESC LIMIT 10;"""
query1 = pysqldf(q1)
print(query1)

#DISPLAYING MODEL, MAKE, PRICEUSD GROUP BY MAKE, MODEL ORDER BY PRICEUSD (DESCNDING)
q1 = """SELECT make,model, priceUSD
FROM data GROUP BY make, model ORDER BY priceUSD DESC LIMIT 10;"""
query1 = pysqldf(q1)
print(query1)

#DISPLAYING YEAR, MODEL, PRICEUSD GROUP BY YEAR, MODEL ORDER BY PRICEUSD (DESCNDING)
q1 = """SELECT year, model, priceUSD 
FROM data GROUP BY year, model ORDER BY year, priceUSD DESC LIMIT 10;"""
query1 = pysqldf(q1)
print(query1)

#TREND IN DATA
q1 = """SELECT year, priceUSD
FROM data
GROUP BY year;"""
query1 = pysqldf(q1)
x=query1["year"]
y=query1["priceUSD"]
import matplotlib.pyplot as plt
plt.plot(x,y)
plt.xlabel("year")
plt.ylabel("PriceUSD")

#t-TEST
import numpy as np
from scipy import stats
N =len(data)
a = test["mileage(kilometers)"]
b = test["volume(cm3)"]
var_a = a.var(ddof=1)
var_b = b.var(ddof=1)
#std deviation
s = np.sqrt((var_a + var_b)/2)
t = (a.mean() - b.mean())/(s*np.sqrt(2/N))
df = 2*N - 2
p = 1 - stats.t.cdf(t,df=df)
print("t = " + str(t))
print("p = " + str(2*p))

#CHI-SQUARE TEST 
#CHI-SQUARE TESTFOR FUELTYPE, TRANSMISSION
a=test[["fuel_type1", "transmission1"]]
from scipy.stats import chi2_contingency 
stat, p, dof, expected = chi2_contingency(a) 
alpha = 0.05
print("p value is " + str(p)) 

#CHI-SQUARE TEST FOR TRANSMISSION, DRIVE_UNIT
a=test[["transmission1", "drive_unit2"]]
from scipy.stats import chi2_contingency 
stat, p, dof, expected = chi2_contingency(a) 
alpha = 0.05
print("p value is " + str(p))


#CHI-SQUARE TEST FOR TRANSMISSION, DRIVE_UNIT
a=test[["fuel_type1", "drive_unit2"]]
from scipy.stats import chi2_contingency 
stat, p, dof, expected = chi2_contingency(a) 
alpha = 0.05
print("p value is " + str(p))



