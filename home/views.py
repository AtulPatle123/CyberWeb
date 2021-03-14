from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from blog.models import Post
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
data = pd.read_csv('Train_data.csv')
data1 = pd.read_csv('new.csv')
# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'home/home.html' , context)

# def about1(request):
#     return render(request, 'home/about1.html')

def about1(request):
    return render(request, 'home/about1.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "please fill the form correctly")
        else:
            contact = Contact(name=name,email=email,phone=phone, content=content)
            contact.save()
            messages.success(request,"Your message has been successfully sent")

    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    if len(query)>78:
        allPosts = Post.object.none()
    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent)
    if allPosts.count == 0:
            messages.warning(request, "No search result found. please refine your query")
    params = {'allPosts': allPosts, 'query':query}
    return render(request, 'home/search.html',params)

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "your accound has been successfully created")
        return redirect('home')
    else:
        return HttpResponse('404 - Not found')

def handleLogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request,"successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials, please try again")
            return redirect('home')

    return HttpResponse('404- Not Found')

def handleLogout(request):
        logout(request)
        messages.success(request,"successfully logout")
        return redirect('home')

def check(request):
    if request.method=='POST':
        value1 = request.POST['value1']
        value2 = request.POST['value2']
        value3 = request.POST['value3']
        value4 = request.POST['value4']
        value5 = request.POST['value5']
        value6 = request.POST['value6']
        print(value1)
        print(type(value1))
        print(value2)
        print(type(value2))
        print(value3)
        type(value3)
        print(value4)
        type(value4)
        print(value5)
        type(value5)
        print(value6)
        type(value6)
        value1=int(value1)
        r=['udp','tcp','icmp']
        r1=['aol', 'auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime', 'discard', 'domain', 'domain_u', 'echo', 'eco_i', 'ecr_i', 'efs', 'exec', 'finger', 'ftp', 'ftp_data', 'gopher', 'harvest', 'hostnames', 'http', 'http_2784', 'http_443', 'http_8001', 'imap4', 'IRC', 'iso_tsap', 'klogin', 'kshell', 'ldap', 'link', 'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns', 'netbios_ssn', 'netstat', 'nnsp', 'nntp', 'ntp_u', 'other', 'pm_dump', 'pop_2', 'pop_3', 'printer', 'private', 'red_i', 'remote_job', 'rje', 'shell', 'smtp', 'sql_net', 'ssh', 'sunrpc', 'supdup', 'systat', 'telnet', 'tftp_u', 'tim_i', 'time', 'urh_i', 'urp_i', 'uucp', 'uucp_path', 'vmnet', 'whois', 'X11', 'Z39_50']
        r2=['SF', 'S0', 'REJ', 'RSTR', 'RSTO', 'S1', 'SH', 'S2', 'RSTOS0', 'S3', 'OTH']
        if value2 not in r:
            a={'a':'1','a1':'this is not valid'}
            return render(request, 'home/home.html' , a)
            print('home')
        if value3 not in r1:
            a1={'a1':'1','a12':'this is not valid'}
            return render(request, 'home/home.html' , a1) 
        if value4 not in r2:
            a2={'a2':'1','a21':'this is not valid'}
            return render(request, 'home/home.html' , a1)
        value1='udp'
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
        protocol_type = {'tcp': 0, 'udp': 1, 'icmp': 2}
        protocol_type.items()
        kdd_train_clean.protocol_type = [protocol_type[item] for item in kdd_train_clean.protocol_type]
        kdd_train_clean.head(20)
        if value1=="udp":
            kdd_data1.protocol_type=0
        elif value1=="tcp":
            kdd_data1.protocol_type=1
        elif value1=="icmp":
            kdd_data1.protocol_type=2
        else:
            pass
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

        #Creating features and labelskdd
        X_train = kdd_train_clean.iloc[:,:-1].values
        y_train = kdd_train_clean.iloc[:, -1].values
        X_test = kdd_test_clean.iloc[:,:-1].values
        y_test = kdd_test_clean.iloc[:,-1].values
        kdd_data1.train=kdd_data1.iloc[:,:-1].values
        kdd_data1.test=kdd_data1.iloc[:, -1].values
        classifier_LR = LogisticRegression()
        classifier_LR.fit(X_train, y_train)
        y_pred_LR = classifier_LR.predict(X_test)
        cm_LR = confusion_matrix(y_test, y_pred_LR)
        accuracy_LR = metrics.accuracy_score(y_test, y_pred_LR)
        dic_LR = {'s':str(cm_LR), 's1':str(accuracy_LR)}
        print(dic_LR)
        y_this=classifier_LR.predict(kdd_data1.train)
        cm_data1=confusion_matrix(kdd_data1.test, y_this)
        accuracy_LR_data1 = metrics.accuracy_score(kdd_data1.test, y_this)
        dic_LR1 = {'s':str(cm_LR), 's1':str(accuracy_LR),'s2':str(cm_data1), 's3':str(accuracy_LR_data1)}
        print(y_this)
        print(dic_LR1)
        # val1 = int(value1)
        # val2 = int(value2)
        # val3 = int(value3)
        # val4 = int(value4)
        # val5 = int(value5)
        # val6 = int(value6)


        
        # if (val1 > 0 and val2 > 0 and val3 > 0 and val4 > 0 and val5 > 0 and val6 > 0):

        context = {'value1': value1, 'value2': value2, 'value3':value3, 'value4':value4, 'value5':value5,'value6':value6,'s2':str(cm_data1), 's3':str(accuracy_LR_data1)}

        return render(request, 'home/check.html' , context)
    else:

        return redirect('home')

    # elif (value1 > 0 and value2 > 0 and value3 > 0 and value4 > 0 and value5 > 0 and value6 > 0):
    #     context = {'value1': value1, 'value2': value2, 'value3':value3, 'value4':value4, 'value5':value5,'value6':value6}
    #     print(value1 , value2 , value3 , value4 , value5 , value6)

    #     return render(request, 'home/check.html' , context=RequestContext(request))

    # else:
    #     messages.error(request,"Please Enter valid details")
    #     return redirect('home')