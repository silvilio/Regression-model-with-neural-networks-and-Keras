#!/usr/bin/env python


{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<a>\n",
    "  <img src='titulillo.png' width=\"1150\">\n",
    "</a>\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "\n",
    "# A. Build a baseline model\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# We import libraries\n",
    "import pandas as pd\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Cement</th>\n",
       "      <th>Blast Furnace Slag</th>\n",
       "      <th>Fly Ash</th>\n",
       "      <th>Water</th>\n",
       "      <th>Superplasticizer</th>\n",
       "      <th>Coarse Aggregate</th>\n",
       "      <th>Fine Aggregate</th>\n",
       "      <th>Age</th>\n",
       "      <th>Strength</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>540.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>162.0</td>\n",
       "      <td>2.5</td>\n",
       "      <td>1040.0</td>\n",
       "      <td>676.0</td>\n",
       "      <td>28</td>\n",
       "      <td>79.99</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>540.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>162.0</td>\n",
       "      <td>2.5</td>\n",
       "      <td>1055.0</td>\n",
       "      <td>676.0</td>\n",
       "      <td>28</td>\n",
       "      <td>61.89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>332.5</td>\n",
       "      <td>142.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>228.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>932.0</td>\n",
       "      <td>594.0</td>\n",
       "      <td>270</td>\n",
       "      <td>40.27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>332.5</td>\n",
       "      <td>142.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>228.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>932.0</td>\n",
       "      <td>594.0</td>\n",
       "      <td>365</td>\n",
       "      <td>41.05</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>198.6</td>\n",
       "      <td>132.4</td>\n",
       "      <td>0.0</td>\n",
       "      <td>192.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>978.4</td>\n",
       "      <td>825.5</td>\n",
       "      <td>360</td>\n",
       "      <td>44.30</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Cement  Blast Furnace Slag  Fly Ash  Water  Superplasticizer  \\\n",
       "0   540.0                 0.0      0.0  162.0               2.5   \n",
       "1   540.0                 0.0      0.0  162.0               2.5   \n",
       "2   332.5               142.5      0.0  228.0               0.0   \n",
       "3   332.5               142.5      0.0  228.0               0.0   \n",
       "4   198.6               132.4      0.0  192.0               0.0   \n",
       "\n",
       "   Coarse Aggregate  Fine Aggregate  Age  Strength  \n",
       "0            1040.0           676.0   28     79.99  \n",
       "1            1055.0           676.0   28     61.89  \n",
       "2             932.0           594.0  270     40.27  \n",
       "3             932.0           594.0  365     41.05  \n",
       "4             978.4           825.5  360     44.30  "
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# We create the dataframe with the data obtained from the url dataset\n",
    "df = pd.read_csv('concrete_data.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1030 entries, 0 to 1029\n",
      "Data columns (total 9 columns):\n",
      " #   Column              Non-Null Count  Dtype  \n",
      "---  ------              --------------  -----  \n",
      " 0   Cement              1030 non-null   float64\n",
      " 1   Blast Furnace Slag  1030 non-null   float64\n",
      " 2   Fly Ash             1030 non-null   float64\n",
      " 3   Water               1030 non-null   float64\n",
      " 4   Superplasticizer    1030 non-null   float64\n",
      " 5   Coarse Aggregate    1030 non-null   float64\n",
      " 6   Fine Aggregate      1030 non-null   float64\n",
      " 7   Age                 1030 non-null   int64  \n",
      " 8   Strength            1030 non-null   float64\n",
      "dtypes: float64(8), int64(1)\n",
      "memory usage: 72.5 KB\n"
     ]
    }
   ],
   "source": [
    "# We get a general idea of ​​what the dataframe contains\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1030, 9)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# # Observe the size of the dataset\n",
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Cement                0\n",
       "Blast Furnace Slag    0\n",
       "Fly Ash               0\n",
       "Water                 0\n",
       "Superplasticizer      0\n",
       "Coarse Aggregate      0\n",
       "Fine Aggregate        0\n",
       "Age                   0\n",
       "Strength              0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# # Check if the dataframe contains null values\n",
    "df.isnull().sum()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The target variable in this problem is the concrete sample strength. Therefore, our predictors will be all the other columns.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_columns = df.columns\n",
    "\n",
    "predictors = df[df_columns[df_columns != 'Strength']] # all columns except Strength\n",
    "target = df['Strength']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Cement</th>\n",
       "      <th>Blast Furnace Slag</th>\n",
       "      <th>Fly Ash</th>\n",
       "      <th>Water</th>\n",
       "      <th>Superplasticizer</th>\n",
       "      <th>Coarse Aggregate</th>\n",
       "      <th>Fine Aggregate</th>\n",
       "      <th>Age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>540.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>162.0</td>\n",
       "      <td>2.5</td>\n",
       "      <td>1040.0</td>\n",
       "      <td>676.0</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>540.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>162.0</td>\n",
       "      <td>2.5</td>\n",
       "      <td>1055.0</td>\n",
       "      <td>676.0</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>332.5</td>\n",
       "      <td>142.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>228.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>932.0</td>\n",
       "      <td>594.0</td>\n",
       "      <td>270</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>332.5</td>\n",
       "      <td>142.5</td>\n",
       "      <td>0.0</td>\n",
       "      <td>228.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>932.0</td>\n",
       "      <td>594.0</td>\n",
       "      <td>365</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>198.6</td>\n",
       "      <td>132.4</td>\n",
       "      <td>0.0</td>\n",
       "      <td>192.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>978.4</td>\n",
       "      <td>825.5</td>\n",
       "      <td>360</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Cement  Blast Furnace Slag  Fly Ash  Water  Superplasticizer  \\\n",
       "0   540.0                 0.0      0.0  162.0               2.5   \n",
       "1   540.0                 0.0      0.0  162.0               2.5   \n",
       "2   332.5               142.5      0.0  228.0               0.0   \n",
       "3   332.5               142.5      0.0  228.0               0.0   \n",
       "4   198.6               132.4      0.0  192.0               0.0   \n",
       "\n",
       "   Coarse Aggregate  Fine Aggregate  Age  \n",
       "0            1040.0           676.0   28  \n",
       "1            1055.0           676.0   28  \n",
       "2             932.0           594.0  270  \n",
       "3             932.0           594.0  365  \n",
       "4             978.4           825.5  360  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# We check that it has separated well\n",
    "predictors.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    79.99\n",
       "1    61.89\n",
       "2    40.27\n",
       "3    41.05\n",
       "4    44.30\n",
       "Name: Strength, dtype: float64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# In the same way with the target\n",
    "target.head()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We store the number of predictors in the variable n_cols. Since we will use it as input to our neural network"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "8"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "n_cols = predictors.shape[1]\n",
    "n_cols"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "\n",
    "## Build a Neural Network \n",
    "### Let's import keras\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# We import the Keras library. In turn the functions of Sequential and Dense\n",
    "import keras\n",
    "from keras.models import Sequential\n",
    "from keras.layers import Dense\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import mean_squared_error\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Create a function that defines our regression model for us so that we can conveniently call it to create our model:\n",
    "\n",
    "- One hidden layer of 10 nodes, and a ReLU activation function\n",
    "- Use the adam optimizer and the mean squared error as the loss function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#num of inputs = num of predictors colums\n",
    "def regression_model():\n",
    "    model = Sequential()\n",
    "    model.add(Dense(10, activation='relu', input_shape=(n_cols,)))\n",
    "    model.add(Dense(1))\n",
    "    \n",
    "    # compile model\n",
    "    model.compile(optimizer='adam', loss='mean_squared_error')\n",
    "    return model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Build the model\n",
    "model = regression_model()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Randomly split the data into a training set (70%) and a test set (30%):  \n",
    "X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Next, we will train and test the model at the same time using the *fit* method. We will train the model for 50 epochs.\n",
    "reg = model.fit(X_train, y_train, epochs=50, verbose=0, validation_data=(X_test, y_test))"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "We evaluate the model on the test data and calculate the root mean square error between the predicted concrete strength and the actual concrete strength. We use the mean_squared_error function from Scikit-learn."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10/10 [==============================] - 0s 869us/step\n",
      "1405.0685347664228\n"
     ]
    }
   ],
   "source": [
    "#Find mean_squared_error as last value in history.\n",
    "y_pred = model.predict(X_test)\n",
    "mse = mean_squared_error(y_test, y_pred)\n",
    "print(mse)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Here, an empty list called mse_list is created to store the root mean square errors. Then a for loop is used to repeat steps 1 through 3 50 times. Inside the loop, the data is randomly divided into a training set and a test set, the model is trained and evaluated on the test data. Each root mean square error is stored in the mse_list. Finally, we use Numpy's np.mean function to calculate the mean of the mean squared errors and the np.std function to calculate the standard deviation."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10/10 [==============================] - 0s 773us/step\n",
      "Mean Squared Error in epoch  0  is:  156.4518062900823\n",
      "10/10 [==============================] - 0s 664us/step\n",
      "Mean Squared Error in epoch  1  is:  116.13129995967574\n",
      "10/10 [==============================] - 0s 659us/step\n",
      "Mean Squared Error in epoch  2  is:  93.34491563895372\n",
      "10/10 [==============================] - 0s 663us/step\n",
      "Mean Squared Error in epoch  3  is:  102.67750390213826\n",
      "10/10 [==============================] - 0s 636us/step\n",
      "Mean Squared Error in epoch  4  is:  87.84534045267755\n",
      "10/10 [==============================] - 0s 556us/step\n",
      "Mean Squared Error in epoch  5  is:  91.3539964377937\n",
      "10/10 [==============================] - 0s 721us/step\n",
      "Mean Squared Error in epoch  6  is:  78.98367173087979\n",
      "10/10 [==============================] - 0s 723us/step\n",
      "Mean Squared Error in epoch  7  is:  85.28051788341159\n",
      "10/10 [==============================] - 0s 706us/step\n",
      "Mean Squared Error in epoch  8  is:  106.94380122870335\n",
      "10/10 [==============================] - 0s 696us/step\n",
      "Mean Squared Error in epoch  9  is:  72.21134833573788\n",
      "10/10 [==============================] - 0s 834us/step\n",
      "Mean Squared Error in epoch  10  is:  81.2030407232727\n",
      "10/10 [==============================] - 0s 704us/step\n",
      "Mean Squared Error in epoch  11  is:  68.23815237778534\n",
      "10/10 [==============================] - 0s 776us/step\n",
      "Mean Squared Error in epoch  12  is:  59.65312541340476\n",
      "10/10 [==============================] - 0s 672us/step\n",
      "Mean Squared Error in epoch  13  is:  54.332621621669716\n",
      "10/10 [==============================] - 0s 730us/step\n",
      "Mean Squared Error in epoch  14  is:  52.205648990359\n",
      "10/10 [==============================] - 0s 665us/step\n",
      "Mean Squared Error in epoch  15  is:  54.802629648707\n",
      "10/10 [==============================] - 0s 699us/step\n",
      "Mean Squared Error in epoch  16  is:  53.26745210405882\n",
      "10/10 [==============================] - 0s 791us/step\n",
      "Mean Squared Error in epoch  17  is:  55.61610980054707\n",
      "10/10 [==============================] - 0s 691us/step\n",
      "Mean Squared Error in epoch  18  is:  50.21184755630525\n",
      "10/10 [==============================] - 0s 774us/step\n",
      "Mean Squared Error in epoch  19  is:  49.33214902568856\n",
      "10/10 [==============================] - 0s 695us/step\n",
      "Mean Squared Error in epoch  20  is:  47.04513571082426\n",
      "10/10 [==============================] - 0s 666us/step\n",
      "Mean Squared Error in epoch  21  is:  54.005363431372764\n",
      "10/10 [==============================] - 0s 695us/step\n",
      "Mean Squared Error in epoch  22  is:  51.76971119243079\n",
      "10/10 [==============================] - 0s 790us/step\n",
      "Mean Squared Error in epoch  23  is:  46.40137783654161\n",
      "10/10 [==============================] - 0s 867us/step\n",
      "Mean Squared Error in epoch  24  is:  47.320948842083844\n",
      "10/10 [==============================] - 0s 738us/step\n",
      "Mean Squared Error in epoch  25  is:  48.24349655120721\n",
      "10/10 [==============================] - 0s 704us/step\n",
      "Mean Squared Error in epoch  26  is:  52.7936030132314\n",
      "10/10 [==============================] - 0s 864us/step\n",
      "Mean Squared Error in epoch  27  is:  46.53401481307223\n",
      "10/10 [==============================] - 0s 802us/step\n",
      "Mean Squared Error in epoch  28  is:  65.69543766545493\n",
      "10/10 [==============================] - 0s 616us/step\n",
      "Mean Squared Error in epoch  29  is:  49.75790428410603\n",
      "10/10 [==============================] - 0s 789us/step\n",
      "Mean Squared Error in epoch  30  is:  48.13869637929474\n",
      "10/10 [==============================] - 0s 747us/step\n",
      "Mean Squared Error in epoch  31  is:  46.88088530213473\n",
      "10/10 [==============================] - 0s 750us/step\n",
      "Mean Squared Error in epoch  32  is:  49.61512736590691\n",
      "10/10 [==============================] - 0s 639us/step\n",
      "Mean Squared Error in epoch  33  is:  57.71868576677902\n",
      "10/10 [==============================] - 0s 695us/step\n",
      "Mean Squared Error in epoch  34  is:  54.13881310318268\n",
      "10/10 [==============================] - 0s 554us/step\n",
      "Mean Squared Error in epoch  35  is:  48.1125331021868\n",
      "10/10 [==============================] - 0s 716us/step\n",
      "Mean Squared Error in epoch  36  is:  43.44204554955413\n",
      "10/10 [==============================] - 0s 665us/step\n",
      "Mean Squared Error in epoch  37  is:  54.10521253837315\n",
      "10/10 [==============================] - 0s 671us/step\n",
      "Mean Squared Error in epoch  38  is:  53.458371692605155\n",
      "10/10 [==============================] - 0s 665us/step\n",
      "Mean Squared Error in epoch  39  is:  61.79985169118292\n",
      "10/10 [==============================] - 0s 628us/step\n",
      "Mean Squared Error in epoch  40  is:  50.3862726916888\n",
      "10/10 [==============================] - 0s 592us/step\n",
      "Mean Squared Error in epoch  41  is:  51.237234957579794\n",
      "10/10 [==============================] - 0s 680us/step\n",
      "Mean Squared Error in epoch  42  is:  53.08123557505395\n",
      "10/10 [==============================] - 0s 669us/step\n",
      "Mean Squared Error in epoch  43  is:  46.3829153921415\n",
      "10/10 [==============================] - 0s 681us/step\n",
      "Mean Squared Error in epoch  44  is:  57.39121737781628\n",
      "10/10 [==============================] - 0s 710us/step\n",
      "Mean Squared Error in epoch  45  is:  48.31676645111568\n",
      "10/10 [==============================] - 0s 659us/step\n",
      "Mean Squared Error in epoch  46  is:  52.320024375224804\n",
      "10/10 [==============================] - 0s 654us/step\n",
      "Mean Squared Error in epoch  47  is:  49.73347875181353\n",
      "10/10 [==============================] - 0s 630us/step\n",
      "Mean Squared Error in epoch  48  is:  50.442007077960895\n",
      "10/10 [==============================] - 0s 665us/step\n",
      "Mean Squared Error in epoch  49  is:  55.358158322160165\n",
      "Mean of the mean squared errors:  62.23427011851866\n",
      "Standard deviation of the mean squared errors:  21.938660691702605\n"
     ]
    }
   ],
   "source": [
    "mse_list = []\n",
    "\n",
    "for i in range(50):\n",
    "    X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.3)\n",
    "\n",
    "    # Training the model\n",
    "    reg = model.fit(X_train, y_train, epochs=50, verbose=0, validation_data=(X_test, y_test))\n",
    "\n",
    "    # Prediction on test data\n",
    "    y_pred = model.predict(X_test)\n",
    "\n",
    "    # Calculation of root mean square error\n",
    "    mse = mean_squared_error(y_test, y_pred)\n",
    "    mse_list.append(mse)\n",
    "    print(\"Mean Squared Error in epoch \", i, \" is: \", mse)\n",
    "\n",
    "mean_mse = np.mean(mse_list)\n",
    "std_mse = np.std(mse_list)\n",
    "\n",
    "print(\"Mean of the mean squared errors: \", mean_mse)\n",
    "print(\"Standard deviation of the mean squared errors: \", std_mse)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean of the mean squared errors:  62.23427011851866\n",
      "Standard deviation of the mean squared errors:  21.938660691702605\n"
     ]
    }
   ],
   "source": [
    "print(\"Mean of the mean squared errors: \", mean_mse)\n",
    "print(\"Standard deviation of the mean squared errors: \", std_mse)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "# B. Normalize the data\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Now we need to normalize the data. We'll do this by subtracting the mean and dividing by the standard deviation.\n",
    "predictors_norm = (predictors - predictors.mean()) / predictors.std()\n",
    "predictors_norm.head()\n",
    "n_cols = predictors_norm.shape[1]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "def regression_model2():\n",
    "    model2 = Sequential()\n",
    "    model2.add(Dense(10, activation='relu', input_shape=(n_cols,)))\n",
    "    model2.add(Dense(1))\n",
    "    \n",
    "    # compile model\n",
    "    model2.compile(optimizer='adam', loss='mean_squared_error')\n",
    "    return model2\n",
    "model2 = regression_model2()"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Train and test the model at the same time using the fit-method. We will leave out 30% of the data for validation and we will train the model for 50 epochs. And use predictors_norm instead of predictors."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10/10 [==============================] - 0s 691us/step\n",
      "Mean Squared Error in epoch  0  is:  152.84085781294618\n",
      "10/10 [==============================] - 0s 683us/step\n",
      "Mean Squared Error in epoch  1  is:  112.34366141084911\n",
      "10/10 [==============================] - 0s 555us/step\n",
      "Mean Squared Error in epoch  2  is:  114.863909763286\n",
      "10/10 [==============================] - 0s 772us/step\n",
      "Mean Squared Error in epoch  3  is:  105.18250725634856\n",
      "10/10 [==============================] - 0s 647us/step\n",
      "Mean Squared Error in epoch  4  is:  117.46409185284789\n",
      "10/10 [==============================] - 0s 766us/step\n",
      "Mean Squared Error in epoch  5  is:  109.06680067157387\n",
      "10/10 [==============================] - 0s 715us/step\n",
      "Mean Squared Error in epoch  6  is:  108.67521821490871\n",
      "10/10 [==============================] - 0s 620us/step\n",
      "Mean Squared Error in epoch  7  is:  110.49828021652212\n",
      "10/10 [==============================] - 0s 665us/step\n",
      "Mean Squared Error in epoch  8  is:  117.50454587685498\n",
      "10/10 [==============================] - 0s 554us/step\n",
      "Mean Squared Error in epoch  9  is:  114.07755244740737\n",
      "10/10 [==============================] - 0s 665us/step\n",
      "Mean Squared Error in epoch  10  is:  107.36601869533916\n",
      "10/10 [==============================] - 0s 762us/step\n",
      "Mean Squared Error in epoch  11  is:  98.66660845093422\n",
      "10/10 [==============================] - 0s 776us/step\n",
      "Mean Squared Error in epoch  12  is:  130.3868067659021\n",
      "10/10 [==============================] - 0s 795us/step\n",
      "Mean Squared Error in epoch  13  is:  125.7129614466891\n",
      "10/10 [==============================] - 0s 711us/step\n",
      "Mean Squared Error in epoch  14  is:  104.43560939371571\n",
      "10/10 [==============================] - 0s 681us/step\n",
      "Mean Squared Error in epoch  15  is:  115.03765725362716\n",
      "10/10 [==============================] - 0s 602us/step\n",
      "Mean Squared Error in epoch  16  is:  118.68866554906019\n",
      "10/10 [==============================] - 0s 708us/step\n",
      "Mean Squared Error in epoch  17  is:  117.19267425513975\n",
      "10/10 [==============================] - 0s 665us/step\n",
      "Mean Squared Error in epoch  18  is:  116.78053943102925\n",
      "10/10 [==============================] - 0s 765us/step\n",
      "Mean Squared Error in epoch  19  is:  132.31331402667655\n",
      "10/10 [==============================] - 0s 757us/step\n",
      "Mean Squared Error in epoch  20  is:  117.24219622807068\n",
      "10/10 [==============================] - 0s 667us/step\n",
      "Mean Squared Error in epoch  21  is:  110.01051099935546\n",
      "10/10 [==============================] - 0s 667us/step\n",
      "Mean Squared Error in epoch  22  is:  107.15972773372015\n",
      "10/10 [==============================] - 0s 559us/step\n",
      "Mean Squared Error in epoch  23  is:  111.55736428170962\n",
      "10/10 [==============================] - 0s 743us/step\n",
      "Mean Squared Error in epoch  24  is:  132.92364120474454\n",
      "10/10 [==============================] - 0s 735us/step\n",
      "Mean Squared Error in epoch  25  is:  106.94187310284751\n",
      "10/10 [==============================] - 0s 775us/step\n",
      "Mean Squared Error in epoch  26  is:  102.13642537018123\n",
      "10/10 [==============================] - 0s 723us/step\n",
      "Mean Squared Error in epoch  27  is:  105.04387767560853\n",
      "10/10 [==============================] - 0s 717us/step\n",
      "Mean Squared Error in epoch  28  is:  104.32872775607235\n",
      "10/10 [==============================] - 0s 668us/step\n",
      "Mean Squared Error in epoch  29  is:  132.8416208302197\n",
      "10/10 [==============================] - 0s 558us/step\n",
      "Mean Squared Error in epoch  30  is:  109.58298865743492\n",
      "10/10 [==============================] - 0s 636us/step\n",
      "Mean Squared Error in epoch  31  is:  126.33794466863692\n",
      "10/10 [==============================] - 0s 741us/step\n",
      "Mean Squared Error in epoch  32  is:  116.33299706532334\n",
      "10/10 [==============================] - 0s 1ms/step\n",
      "Mean Squared Error in epoch  33  is:  117.21381536418089\n",
      "10/10 [==============================] - 0s 981us/step\n",
      "Mean Squared Error in epoch  34  is:  105.17991334597369\n",
      "10/10 [==============================] - 0s 688us/step\n",
      "Mean Squared Error in epoch  35  is:  130.90223506646228\n",
      "10/10 [==============================] - 0s 891us/step\n",
      "Mean Squared Error in epoch  36  is:  127.76450841811759\n",
      "10/10 [==============================] - 0s 838us/step\n",
      "Mean Squared Error in epoch  37  is:  113.03048474808526\n",
      "10/10 [==============================] - 0s 872us/step\n",
      "Mean Squared Error in epoch  38  is:  119.2023619715279\n",
      "10/10 [==============================] - 0s 826us/step\n",
      "Mean Squared Error in epoch  39  is:  117.17757497531288\n",
      "10/10 [==============================] - 0s 554us/step\n",
      "Mean Squared Error in epoch  40  is:  142.82214108402803\n",
      "10/10 [==============================] - 0s 664us/step\n",
      "Mean Squared Error in epoch  41  is:  100.99618311828577\n",
      "10/10 [==============================] - 0s 786us/step\n",
      "Mean Squared Error in epoch  42  is:  94.68213755407007\n",
      "10/10 [==============================] - 0s 570us/step\n",
      "Mean Squared Error in epoch  43  is:  109.55297677465896\n",
      "10/10 [==============================] - 0s 665us/step\n",
      "Mean Squared Error in epoch  44  is:  117.22446609659005\n",
      "10/10 [==============================] - 0s 740us/step\n",
      "Mean Squared Error in epoch  45  is:  112.51977836066956\n",
      "10/10 [==============================] - 0s 835us/step\n",
      "Mean Squared Error in epoch  46  is:  100.3616803980363\n",
      "10/10 [==============================] - 0s 858us/step\n",
      "Mean Squared Error in epoch  47  is:  114.16244289856606\n",
      "10/10 [==============================] - 0s 2ms/step\n",
      "Mean Squared Error in epoch  48  is:  114.7813283320429\n",
      "10/10 [==============================] - 0s 690us/step\n",
      "Mean Squared Error in epoch  49  is:  128.5515811110025\n",
      "Mean of the mean squared errors:  115.55327571966389\n",
      "Standard deviation of the mean squared errors:  11.357851008862163\n"
     ]
    }
   ],
   "source": [
    "mse_list = []\n",
    "\n",
    "for i in range(50):\n",
    "    X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.3)\n",
    "\n",
    "    # Training the model\n",
    "    reg = model2.fit(X_train, y_train, epochs=50, verbose=0, validation_data=(X_test, y_test))\n",
    "\n",
    "    # Prediction on test data\n",
    "    y_pred = model2.predict(X_test)\n",
    "\n",
    "    # Calculation of root mean square error\n",
    "    mse = mean_squared_error(y_test, y_pred)\n",
    "    mse_list.append(mse)\n",
    "    print(\"Mean Squared Error in epoch \", i, \" is: \", mse)\n",
    "\n",
    "mean_mse = np.mean(mse_list)\n",
    "std_mse = np.std(mse_list)\n",
    "\n",
    "print(\"Mean of the mean squared errors: \", mean_mse)\n",
    "print(\"Standard deviation of the mean squared errors: \", std_mse)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean of the mean squared errors:  115.55327571966389\n",
      "Standard deviation of the mean squared errors:  11.357851008862163\n"
     ]
    }
   ],
   "source": [
    "print(\"Mean of the mean squared errors: \", mean_mse)\n",
    "print(\"Standard deviation of the mean squared errors: \", std_mse)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### How does the mean of the mean squared errors compare to that from Step A?"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Conclusions: <br>\n",
    "We found that normalizing the data did not work too well. Both the mean and the standard deviation of the errors have been larger than in test one. Likewise, the difference has not been much and very large errors are handled."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "# C. Increate the number of epochs \n",
    "\n",
    "\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "This time I will repeat Part B but I will use 100 epochs for training. I will continue to use the normalized data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "def regression_model3():\n",
    "    model3 = Sequential()\n",
    "    model3.add(Dense(10, activation='relu', input_shape=(n_cols,)))\n",
    "    model3.add(Dense(1))\n",
    "    \n",
    "    # compile model\n",
    "    model3.compile(optimizer='adam', loss='mean_squared_error')\n",
    "    return model3\n",
    "model3 = regression_model3()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10/10 [==============================] - 0s 617us/step\n",
      "Mean Squared Error in epoch  0  is:  160.48142988718405\n",
      "10/10 [==============================] - 0s 759us/step\n",
      "Mean Squared Error in epoch  1  is:  110.27403360097689\n",
      "10/10 [==============================] - 0s 605us/step\n",
      "Mean Squared Error in epoch  2  is:  101.13419954761574\n",
      "10/10 [==============================] - 0s 904us/step\n",
      "Mean Squared Error in epoch  3  is:  111.98366140438955\n",
      "10/10 [==============================] - 0s 723us/step\n",
      "Mean Squared Error in epoch  4  is:  99.79857672644756\n",
      "10/10 [==============================] - 0s 776us/step\n",
      "Mean Squared Error in epoch  5  is:  119.69931538629947\n",
      "10/10 [==============================] - 0s 871us/step\n",
      "Mean Squared Error in epoch  6  is:  117.62072280707787\n",
      "10/10 [==============================] - 0s 843us/step\n",
      "Mean Squared Error in epoch  7  is:  114.03399140174018\n",
      "10/10 [==============================] - 0s 724us/step\n",
      "Mean Squared Error in epoch  8  is:  107.75120577073389\n",
      "10/10 [==============================] - 0s 812us/step\n",
      "Mean Squared Error in epoch  9  is:  103.49937281815818\n",
      "10/10 [==============================] - 0s 662us/step\n",
      "Mean Squared Error in epoch  10  is:  110.83761200703154\n",
      "10/10 [==============================] - 0s 628us/step\n",
      "Mean Squared Error in epoch  11  is:  120.78305053038625\n",
      "10/10 [==============================] - 0s 886us/step\n",
      "Mean Squared Error in epoch  12  is:  104.11796481470704\n",
      "10/10 [==============================] - 0s 796us/step\n",
      "Mean Squared Error in epoch  13  is:  121.77264248502483\n",
      "10/10 [==============================] - 0s 877us/step\n",
      "Mean Squared Error in epoch  14  is:  111.98107577505404\n",
      "10/10 [==============================] - 0s 653us/step\n",
      "Mean Squared Error in epoch  15  is:  114.78623617777478\n",
      "10/10 [==============================] - 0s 665us/step\n",
      "Mean Squared Error in epoch  16  is:  110.34114338691154\n",
      "10/10 [==============================] - 0s 866us/step\n",
      "Mean Squared Error in epoch  17  is:  110.32274674506456\n",
      "10/10 [==============================] - 0s 777us/step\n",
      "Mean Squared Error in epoch  18  is:  107.7464748107024\n",
      "10/10 [==============================] - 0s 750us/step\n",
      "Mean Squared Error in epoch  19  is:  118.3921297931188\n",
      "10/10 [==============================] - 0s 554us/step\n",
      "Mean Squared Error in epoch  20  is:  122.25610417555697\n",
      "10/10 [==============================] - 0s 805us/step\n",
      "Mean Squared Error in epoch  21  is:  122.80952889457183\n",
      "10/10 [==============================] - 0s 997us/step\n",
      "Mean Squared Error in epoch  22  is:  120.412357183589\n",
      "10/10 [==============================] - 0s 652us/step\n",
      "Mean Squared Error in epoch  23  is:  113.71147071222858\n",
      "10/10 [==============================] - 0s 701us/step\n",
      "Mean Squared Error in epoch  24  is:  116.36375450180402\n",
      "10/10 [==============================] - 0s 624us/step\n",
      "Mean Squared Error in epoch  25  is:  125.46039443960984\n",
      "10/10 [==============================] - 0s 706us/step\n",
      "Mean Squared Error in epoch  26  is:  115.10835962800012\n",
      "10/10 [==============================] - 0s 612us/step\n",
      "Mean Squared Error in epoch  27  is:  102.97891556762241\n",
      "10/10 [==============================] - 0s 972us/step\n",
      "Mean Squared Error in epoch  28  is:  115.03339728139382\n",
      "10/10 [==============================] - 0s 937us/step\n",
      "Mean Squared Error in epoch  29  is:  108.19594582068004\n",
      "10/10 [==============================] - 0s 776us/step\n",
      "Mean Squared Error in epoch  30  is:  109.5466833505131\n",
      "10/10 [==============================] - 0s 661us/step\n",
      "Mean Squared Error in epoch  31  is:  109.7199044316874\n",
      "10/10 [==============================] - 0s 734us/step\n",
      "Mean Squared Error in epoch  32  is:  108.36177395807815\n",
      "10/10 [==============================] - 0s 669us/step\n",
      "Mean Squared Error in epoch  33  is:  99.98839793539085\n",
      "10/10 [==============================] - 0s 952us/step\n",
      "Mean Squared Error in epoch  34  is:  106.9829241852612\n",
      "10/10 [==============================] - 0s 838us/step\n",
      "Mean Squared Error in epoch  35  is:  106.44336591991294\n",
      "10/10 [==============================] - 0s 935us/step\n",
      "Mean Squared Error in epoch  36  is:  115.40079199196082\n",
      "10/10 [==============================] - 0s 914us/step\n",
      "Mean Squared Error in epoch  37  is:  68.97564974135824\n",
      "10/10 [==============================] - 0s 843us/step\n",
      "Mean Squared Error in epoch  38  is:  63.944380863698086\n",
      "10/10 [==============================] - 0s 784us/step\n",
      "Mean Squared Error in epoch  39  is:  60.18278123929514\n",
      "10/10 [==============================] - 0s 838us/step\n",
      "Mean Squared Error in epoch  40  is:  62.38499705909124\n",
      "10/10 [==============================] - 0s 933us/step\n",
      "Mean Squared Error in epoch  41  is:  50.41609726972746\n",
      "10/10 [==============================] - 0s 1ms/step\n",
      "Mean Squared Error in epoch  42  is:  47.77718680097015\n",
      "10/10 [==============================] - 0s 901us/step\n",
      "Mean Squared Error in epoch  43  is:  54.30702464102933\n",
      "10/10 [==============================] - 0s 659us/step\n",
      "Mean Squared Error in epoch  44  is:  50.701767233592705\n",
      "10/10 [==============================] - 0s 785us/step\n",
      "Mean Squared Error in epoch  45  is:  51.323580867806285\n",
      "10/10 [==============================] - 0s 887us/step\n",
      "Mean Squared Error in epoch  46  is:  47.96219321594689\n",
      "10/10 [==============================] - 0s 981us/step\n",
      "Mean Squared Error in epoch  47  is:  47.269230285607456\n",
      "10/10 [==============================] - 0s 780us/step\n",
      "Mean Squared Error in epoch  48  is:  48.409389537432276\n",
      "10/10 [==============================] - 0s 922us/step\n",
      "Mean Squared Error in epoch  49  is:  53.16240438762856\n",
      "\n",
      "Mean of the mean squared errors:  98.05896677994889\n",
      "Standard deviation of the mean squared errors:  27.57965495000192\n"
     ]
    }
   ],
   "source": [
    "mse_list = []\n",
    "\n",
    "for i in range(50):\n",
    "    X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.3)\n",
    "\n",
    "    # Training the model\n",
    "    reg = model3.fit(X_train, y_train, epochs=100, verbose=0, validation_data=(X_test, y_test))\n",
    "\n",
    "    # Prediction on test data\n",
    "    y_pred = model3.predict(X_test)\n",
    "\n",
    "    # Calculation of root mean square error\n",
    "    mse = mean_squared_error(y_test, y_pred)\n",
    "    mse_list.append(mse)\n",
    "    print(\"Mean Squared Error in epoch \", i, \" is: \", mse)\n",
    "\n",
    "mean_mse = np.mean(mse_list)\n",
    "std_mse = np.std(mse_list)\n",
    "\n",
    "print(\"\")\n",
    "print(\"Mean of the mean squared errors: \", mean_mse)\n",
    "print(\"Standard deviation of the mean squared errors: \", std_mse)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "How does the mean of the mean squared errors compare to that from Step B?"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Conclusions:** <br>\n",
    "Here the results have improved considerably. It can be said that the more epochs the better result. Even so, it is not a small error either. the standard deviation of the root mean square of the error has been quite low compared to previous cases."
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "---"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "# D. Increase the number of hidden layers\n",
    "\n"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Repeat part B but use a neural network with the following instead:\n",
    "\n",
    "- Three hidden layers, each of 10 nodes and ReLU activation function."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "def regression_model4():\n",
    "    model4 = Sequential()\n",
    "    model4.add(Dense(10, activation='relu', input_shape=(n_cols,)))\n",
    "    model4.add(Dense(10, activation='relu'))\n",
    "    model4.add(Dense(10, activation='relu'))\n",
    "    model4.add(Dense(1))\n",
    "    \n",
    "    # compile model\n",
    "    model4.compile(optimizer='adam', loss='mean_squared_error')\n",
    "    return model4\n",
    "model4 = regression_model4()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10/10 [==============================] - 0s 741us/step\n",
      "Mean Squared Error in epoch  0  is:  108.0608692856171\n",
      "10/10 [==============================] - 0s 928us/step\n",
      "Mean Squared Error in epoch  1  is:  54.704863153619\n",
      "10/10 [==============================] - 0s 822us/step\n",
      "Mean Squared Error in epoch  2  is:  62.72714058941757\n",
      "10/10 [==============================] - 0s 924us/step\n",
      "Mean Squared Error in epoch  3  is:  52.122600596185535\n",
      "10/10 [==============================] - 0s 905us/step\n",
      "Mean Squared Error in epoch  4  is:  57.5921584766869\n",
      "10/10 [==============================] - 0s 709us/step\n",
      "Mean Squared Error in epoch  5  is:  43.84366247044178\n",
      "10/10 [==============================] - 0s 709us/step\n",
      "Mean Squared Error in epoch  6  is:  45.46559327578457\n",
      "10/10 [==============================] - 0s 1ms/step\n",
      "Mean Squared Error in epoch  7  is:  46.265972972693056\n",
      "10/10 [==============================] - 0s 856us/step\n",
      "Mean Squared Error in epoch  8  is:  48.568420950880494\n",
      "10/10 [==============================] - 0s 693us/step\n",
      "Mean Squared Error in epoch  9  is:  49.19031437202601\n",
      "10/10 [==============================] - 0s 555us/step\n",
      "Mean Squared Error in epoch  10  is:  46.58144354189668\n",
      "10/10 [==============================] - 0s 832us/step\n",
      "Mean Squared Error in epoch  11  is:  52.84597596300285\n",
      "10/10 [==============================] - 0s 679us/step\n",
      "Mean Squared Error in epoch  12  is:  49.51969209332703\n",
      "10/10 [==============================] - 0s 665us/step\n",
      "Mean Squared Error in epoch  13  is:  64.20209712062395\n",
      "10/10 [==============================] - 0s 775us/step\n",
      "Mean Squared Error in epoch  14  is:  50.45589175083448\n",
      "10/10 [==============================] - 0s 691us/step\n",
      "Mean Squared Error in epoch  15  is:  48.28216206623831\n",
      "10/10 [==============================] - 0s 766us/step\n",
      "Mean Squared Error in epoch  16  is:  47.94720177216017\n",
      "10/10 [==============================] - 0s 685us/step\n",
      "Mean Squared Error in epoch  17  is:  57.8692380886732\n",
      "10/10 [==============================] - 0s 679us/step\n",
      "Mean Squared Error in epoch  18  is:  42.829934505510565\n",
      "10/10 [==============================] - 0s 894us/step\n",
      "Mean Squared Error in epoch  19  is:  48.973578377929655\n",
      "10/10 [==============================] - 0s 730us/step\n",
      "Mean Squared Error in epoch  20  is:  45.538248989991615\n",
      "10/10 [==============================] - 0s 775us/step\n",
      "Mean Squared Error in epoch  21  is:  43.813458443724265\n",
      "10/10 [==============================] - 0s 2ms/step\n",
      "Mean Squared Error in epoch  22  is:  40.458873620408646\n",
      "10/10 [==============================] - 0s 1ms/step\n",
      "Mean Squared Error in epoch  23  is:  48.46307354902895\n",
      "10/10 [==============================] - 0s 776us/step\n",
      "Mean Squared Error in epoch  24  is:  38.61331293052257\n",
      "10/10 [==============================] - 0s 702us/step\n",
      "Mean Squared Error in epoch  25  is:  43.87441127326316\n",
      "10/10 [==============================] - 0s 938us/step\n",
      "Mean Squared Error in epoch  26  is:  38.429588118692855\n",
      "10/10 [==============================] - 0s 601us/step\n",
      "Mean Squared Error in epoch  27  is:  39.49855597897249\n",
      "10/10 [==============================] - 0s 767us/step\n",
      "Mean Squared Error in epoch  28  is:  36.52961093178331\n",
      "10/10 [==============================] - 0s 745us/step\n",
      "Mean Squared Error in epoch  29  is:  35.68231833876267\n",
      "10/10 [==============================] - 0s 697us/step\n",
      "Mean Squared Error in epoch  30  is:  44.092813051830646\n",
      "10/10 [==============================] - 0s 724us/step\n",
      "Mean Squared Error in epoch  31  is:  48.108810045008184\n",
      "10/10 [==============================] - 0s 754us/step\n",
      "Mean Squared Error in epoch  32  is:  44.05418115864954\n",
      "10/10 [==============================] - 0s 869us/step\n",
      "Mean Squared Error in epoch  33  is:  47.4958780571687\n",
      "10/10 [==============================] - 0s 818us/step\n",
      "Mean Squared Error in epoch  34  is:  43.181775729228846\n",
      "10/10 [==============================] - 0s 879us/step\n",
      "Mean Squared Error in epoch  35  is:  44.333759219169735\n",
      "10/10 [==============================] - 0s 705us/step\n",
      "Mean Squared Error in epoch  36  is:  37.70140521478047\n",
      "10/10 [==============================] - 0s 751us/step\n",
      "Mean Squared Error in epoch  37  is:  36.98895816258533\n",
      "10/10 [==============================] - 0s 809us/step\n",
      "Mean Squared Error in epoch  38  is:  38.048612371471876\n",
      "10/10 [==============================] - 0s 619us/step\n",
      "Mean Squared Error in epoch  39  is:  36.11155711680713\n",
      "10/10 [==============================] - 0s 712us/step\n",
      "Mean Squared Error in epoch  40  is:  39.8015719705749\n",
      "10/10 [==============================] - 0s 776us/step\n",
      "Mean Squared Error in epoch  41  is:  44.657905397522576\n",
      "10/10 [==============================] - 0s 665us/step\n",
      "Mean Squared Error in epoch  42  is:  35.40626303356544\n",
      "10/10 [==============================] - 0s 665us/step\n",
      "Mean Squared Error in epoch  43  is:  41.45868872487076\n",
      "10/10 [==============================] - 0s 674us/step\n",
      "Mean Squared Error in epoch  44  is:  35.766440597915\n",
      "10/10 [==============================] - 0s 772us/step\n",
      "Mean Squared Error in epoch  45  is:  42.323889060160475\n",
      "10/10 [==============================] - 0s 673us/step\n",
      "Mean Squared Error in epoch  46  is:  47.33412452674402\n",
      "10/10 [==============================] - 0s 712us/step\n",
      "Mean Squared Error in epoch  47  is:  39.918947034449886\n",
      "10/10 [==============================] - 0s 666us/step\n",
      "Mean Squared Error in epoch  48  is:  38.17230512862065\n",
      "10/10 [==============================] - 0s 793us/step\n",
      "Mean Squared Error in epoch  49  is:  44.96095354189456\n",
      "\n",
      "Mean of the mean squared errors:  46.37738205483437\n",
      "Standard deviation of the mean squared errors:  11.043617231548984\n"
     ]
    }
   ],
   "source": [
    "mse_list = []\n",
    "\n",
    "for i in range(50):\n",
    "    X_train, X_test, y_train, y_test = train_test_split(predictors, target, test_size=0.3)\n",
    "\n",
    "    # Training the model\n",
    "    reg = model4.fit(X_train, y_train, epochs=50, verbose=0, validation_data=(X_test, y_test))\n",
    "\n",
    "    # Prediction on test data\n",
    "    y_pred = model4.predict(X_test)\n",
    "\n",
    "    # Calculation of root mean square error\n",
    "    mse = mean_squared_error(y_test, y_pred)\n",
    "    mse_list.append(mse)\n",
    "    print(\"Mean Squared Error in epoch \", i, \" is: \", mse)\n",
    "\n",
    "mean_mse = np.mean(mse_list)\n",
    "std_mse = np.std(mse_list)\n",
    "\n",
    "print(\"\")\n",
    "print(\"Mean of the mean squared errors: \", mean_mse)\n",
    "print(\"Standard deviation of the mean squared errors: \", std_mse)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Conclusions:** <br>\n",
    "In this case the standard deviation of the root mean square of the error has has remained the same. <br>\n",
    "What has improved is the mean squared error, dropping to 37. We are beginning to handle acceptable values ​​for the model.\n",
    "<br>\n",
    "<br>\n",
    "In conclusion, test 4 has been the one that has yielded the best data. According to the study of regressive neural networks, it can be said that the most important parameter of training in a neural network has not been the treatment of the data at the beginning, nor the epochs. What has really made the difference has been adding hidden layers to give consistency to the neural network. Thank you!"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv_analytics",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "b69e841faa10be29ec1a7378b9ef0bf394b18c3d1a642c200938909c70064bb9"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
