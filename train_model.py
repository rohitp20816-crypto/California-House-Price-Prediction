from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
import numpy as np

california_df=fetch_california_housing(as_frame=True).frame
cols=['MedInc', 'HouseAge', 'AveRooms', 'Population', 'AveOccup',
       'Latitude', 'MedHouseVal']
df=california_df[cols]

X=df.drop('MedHouseVal',axis=1)
y=df['MedHouseVal']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=1234)

lr=LinearRegression()
lr.fit(X_train,y_train)
y_pred=lr.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

import pickle
info={'Model':lr,'n_columns':6,'columns':X_train.columns}

file_name='california_info.joblib'
with open(file_name,'wb') as file:
    pickle.dump(info,file)