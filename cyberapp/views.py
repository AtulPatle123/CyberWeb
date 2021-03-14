from django.shortcuts import render

# Create your views here.
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

#importing the dataset
data = pd.read_csv('cyberapp/Train_data.csv')
data1 = pd.read_csv('cyberapp/new.csv')
#Splitting the data into training ans testing test set
kdd_train,kdd_test = train_test_split(data, test_size= 0.2)

kdd_train_clean = kdd_train.drop(
    ['wrong_fragment', 'urgent', 'num_failed_logins', 'num_file_creations', 'num_shells',
     'num_outbound_cmds'], axis=1)
kdd_test_clean = kdd_test.drop(
    ['wrong_fragment', 'urgent', 'num_failed_logins', 'num_file_creations', 'num_shells',
     'num_outbound_cmds'], axis=1)
kdd_data1= data1.drop(
    ['wrong_fragment', 'urgent', 'num_failed_logins', 'num_file_creations', 'num_shells',
     'num_outbound_cmds'], axis=1)
kdd_train_clean.head()
kdd_test_clean.head()
kdd_data1.head()
kdd_train_clean.info()
kdd_test_clean.info()
kdd_data1.info()
kdd_train_clean.describe()
kdd_test_clean.describe()
kdd_data1.describe()

kdd_train_clean['protocol_type'].value_counts()
kdd_test_clean['protocol_type'].value_counts()
kdd_train_clean['service'].value_counts()
kdd_test_clean['service'].value_counts()
kdd_train_clean['flag'].value_counts()
kdd_test_clean['flag'].value_counts()

#converting categorical data to numerical data
protocol_type = {'tcp': 0, 'udp': 1, 'icmp': 2}
protocol_type.items()
kdd_train_clean.protocol_type = [protocol_type[item] for item in kdd_train_clean.protocol_type]
kdd_train_clean.head(20)
kdd_data1.protocol_type=0
protocol_type = {'tcp': 0, 'udp': 1, 'icmp': 2}
protocol_type.items()
kdd_test_clean.protocol_type = [protocol_type[item] for item in kdd_test_clean.protocol_type]
kdd_test_clean.head(20)

duration = kdd_train_clean['duration']

kdd_train_clean['duration'] = np.where((kdd_train_clean.duration <= 2), 0, 1)
kdd_train_clean.head(20)

duration = kdd_test_clean['duration']

kdd_test_clean['duration'] = np.where((kdd_test_clean.duration <= 2), 0, 1)
kdd_test_clean.head(20)

service = {'aol': 1, 'auth': 2, 'bgp': 3, 'courier': 4, 'csnet_ns': 5, 'ctf': 6, 'daytime': 7, 'discard': 8,
                 'domain': 9, 'domain_u': 10, 'echo': 11, 'eco_i': 12, 'ecr_i': 13, 'efs': 14, 'exec': 15,
                 'finger': 16, 'ftp': 17, 'ftp_data': 18, 'gopher': 19, 'harvest': 20, 'hostnames': 21, 'http': 22,
                 'http_2784': 23, 'http_443': 24, 'http_8001': 25, 'imap4': 26, 'IRC': 27, 'iso_tsap': 28,
                 'klogin': 29, 'kshell': 30, 'ldap': 31, 'link': 32, 'login': 33, 'mtp': 34, 'name': 35,
                 'netbios_dgm': 36, 'netbios_ns': 37, 'netbios_ssn': 38, 'netstat': 39, 'nnsp': 40, 'nntp': 41,
                 'ntp_u': 42, 'other': 43, 'pm_dump': 44, 'pop_2': 45, 'pop_3': 46, 'printer': 47, 'private': 48,
                 'red_i': 49, 'remote_job': 50, 'rje': 51, 'shell': 52, 'smtp': 53, 'sql_net': 54, 'ssh': 55,
                 'sunrpc': 56, 'supdup': 57, 'systat': 58, 'telnet': 59, 'tftp_u': 60, 'tim_i': 61, 'time': 62,
                 'urh_i': 63, 'urp_i': 64, 'uucp': 65, 'uucp_path': 66, 'vmnet': 67, 'whois': 68, 'X11': 69,
                 'Z39_50': 70}
service.items()
kdd_train_clean.service = [service[item] for item in kdd_train_clean.service]
kdd_train_clean.head(20)
kdd_data1.service=[service[item] for item in kdd_data1.service]
kdd_data1.service=18

kdd_test_clean.service = [service[item] for item in kdd_test_clean.service]
kdd_test_clean.head(20)


flag = {'SF': 0, 'S0': 1, 'REJ': 2, 'RSTR': 3, 'RSTO': 4, 'S1': 5, 'SH': 6, 'S2': 7, 'RSTOS0': 8, 'S3': 9,
              'OTH': 10}
flag.items()
kdd_train_clean.flag = [flag[item] for item in kdd_train_clean.flag]
kdd_train_clean.head(20)

kdd_test_clean.flag = [flag[item] for item in kdd_test_clean.flag]
kdd_test_clean.head(20)
kdd_data1.flag=[flag[item] for item in kdd_data1.flag]

#Creating features and labels
X_train = kdd_train_clean.iloc[:,:-1].values
y_train = kdd_train_clean.iloc[:, -1].values
X_test = kdd_test_clean.iloc[:,:-1].values
y_test = kdd_test_clean.iloc[:,-1].values
kdd_data1.train=kdd_data1.iloc[:,:-1].values
kdd_data1.test=kdd_data1.iloc[:, -1].values


def home(request):
    return render(request, 'cyberapp/cyberHome.html')



#Logistic Regression
def Logistic(request):


    classifier_LR = LogisticRegression()
    classifier_LR.fit(X_train, y_train)
    y_pred_LR = classifier_LR.predict(X_test)
    cm_LR = confusion_matrix(y_test, y_pred_LR)
    accuracy_LR = metrics.accuracy_score(y_test, y_pred_LR)
    y_this=classifier_LR.predict(kdd_data1.train)
    cm_data1=confusion_matrix(kdd_data1.test, y_this)
    accuracy_LR_data1 = metrics.accuracy_score(kdd_data1.test, y_this)
    print(y_this)
    dic_LR = {'s':str(cm_LR), 's1':str(accuracy_LR),'s2':str(cm_data1), 's4':str(accuracy_LR_data1)}
    return render(request, 'cyberapp/logistic.html',dic_LR)



#Random forest algorithm
def random(request):
    classifier_RF = RandomForestClassifier(n_estimators = 100, random_state=101)
    classifier_RF.fit(X_train,y_train)
    y_pred_RF = classifier_RF.predict(X_test)
    cm_RF = confusion_matrix(y_test,y_pred_RF)
    accuracy_RF = metrics.accuracy_score(y_test,y_pred_RF)
    dic_RF = {'s': cm_RF, 's1': accuracy_RF}
    return render(request,'cyberapp/random.html',dic_RF)
