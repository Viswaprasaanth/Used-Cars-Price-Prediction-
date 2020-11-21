#READ DATA
import pandas as pd
data=pd.read_csv("cars_price.csv")
data.head()

#LABEL ENCODING THE DATA
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
le.fit(data["make"])
list(le.classes_)
data["make1"]=le.transform(data["make"])
le.fit(data["model"])
list(le.classes_)
data["model1"]=le.transform(data["model"])
le.fit(data["condition"])
list(le.classes_)
data["condition1"]=le.transform(data["condition"])
le.fit(data["fuel_type"])
list(le.classes_)
data["fuel_type1"]=le.transform(data["fuel_type"])
le.fit(data["color"])
list(le.classes_)
data["color1"]=le.transform(data["color"])
le.fit(data["transmission"])
list(le.classes_)
data["transmission1"]=le.transform(data["transmission"])
le.fit(data["segment1"])
list(le.classes_)
data["segment2"]=le.transform(data["segment1"])
data["drive_unit1"]=data["drive_unit1"].astype(str)
le.fit(data["drive_unit1"])
list(le.classes_)
data["drive_unit2"]=le.transform(data["drive_unit1"])

#DATA PRE-PROCESSING
data.describe()
data.isnull()
data.boxplot()

#TREATING NULL VALUES
df["volume(cm3)"]=df["volume(cm3)"].fillna(df["volume(cm3)"].median())

#SPLITING THE DATA INTO TRANING AND TESTING SETS
x= dt.iloc[:,[1,2,4,5,6,7,8,9,10,11]].values 
y=dt["priceUSD"]
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test= train_test_split(x, y, test_size=0.3)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#LINEAR REGRESSION
import numpy as np
from sklearn import linear_model
regr = linear_model.LinearRegression()
regr.fit(X_train, y_train)
pred = regr.predict(X_test)
print(regr.score(X_test,pred))
mse=np.square(np.subtract(y_test,pred)).mean()
print ("MSE: ",mse)

#DECISION TREE REGRESSOR
from sklearn.tree import DecisionTreeRegressor 
regressor = DecisionTreeRegressor(random_state = 0) 
regressor.fit(X_train, y_train) 
y_pred = regressor.predict(X_test) 
print(regressor.score(X_test,y_pred))
import numpy as np
mse=np.square(np.subtract(y_test,y_pred)).mean()
print ("MSE: ",mse)

#RANDOM FOREST REGRESSOR
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
regr = RandomForestRegressor(max_depth=2, random_state=0)
regr.fit(X_train, y_train)
y_pred1 = regr.predict(X_test) 
print(regr.score(X_test,y_pred1))
mse=np.square(np.subtract(y_test,y_pred1)).mean()
print ("MSE: ",mse)

#rbf SUPPORT VECTOR REGRESSOR
from sklearn.svm import SVR
from sklearn.metrics import r2_score
regressor=SVR(kernel='rbf',epsilon=1.0)
regressor.fit(X_train,y_train)
pred=regressor.predict(X_test)
print(regressor.score(X_test,pred))
mse=np.square(np.subtract(y_test,pred)).mean()
print ("MSE: ",mse)

#LINEAR SUPPORT VECOR REGRESSOR FOR GT Turbine decay state coefficient
from sklearn.svm import SVR
regressor=SVR(kernel='linear',degree=1)
from sklearn.model_selection import train_test_split
regressor.fit(X_train,y_train)
pred=regressor.predict(X_test)
print(regressor.score(X_test,pred))
mse=np.square(np.subtract(y_test,pred)).mean()
print ("MSE: ",mse)

#PLOTTING THE MSE VALUES
import matplotlib.pyplot as plt
x=["LR", "DT", "RF", "SVRL", "SVRrbf"]
y=[5.323899858513796e-23, 3273.967833333333, 9456773.989658201, 0.025258557124269897, 64191967.14013864 ]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(x,y)
#plt.title("GT Turbine decay state coefficient")
plt.xlabel("MODELS")
plt.ylabel("MEAN SQUARE ERROR")
plt.show()
