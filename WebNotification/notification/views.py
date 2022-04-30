from django.http.request import HttpHeaders
from django.shortcuts import render

from django.http import HttpResponse
import requests
import json



def send_notification(registration_ids , message_title , message_desc):
    fcm_api = "AAAAh3gYfpE:APA91bGi3O-53aqP7drgFpvYRbvNhejTVjU4QlEZUcDJuE2nWkvKBZ0uUK7knd5W8350LKdSRHmsamnK3PO53_cNMqJtH1Ft3KPBK6I19jsjKGr0Q_-npTFMb3EFsR57d1CVDDGqhoVy"
    url = "https://fcm.googleapis.com/fcm/send"
    
    headers = {
    "Content-Type":"application/json",
    "Authorization": 'key='+fcm_api}
    print(registration_ids,message_desc,message_title)
    payload = {
        "registration_ids" :registration_ids,
        "priority" : "high",
        "notification" : {
            "body" : message_desc,
            "title" : message_title,
            "image" : "https://media-exp1.licdn.com/dms/image/C5603AQEBWGSDtxwgdg/profile-displayphoto-shrink_200_200/0/1628446066965?e=1656547200&v=beta&t=kKp6WMBDuFoh4u4ImKXWfpkqY-CD8-YBQnTyV2Zj-uI",
            "icon": "https://yt3.ggpht.com/ytc/AKedOLSMvoy4DeAVkMSAuiuaBdIGKC7a5Ib75bKzKO3jHg=s900-c-k-c0x00ffffff-no-rj",
            
        }
    }

    result = requests.post(url,  data=json.dumps(payload), headers=headers )
    print(result)
    print(result.json())







def index(request):
    return render(request , 'index.html')

def send(request):
    resgistration  = ['eLdkIhe7B2yzq0skf42vsd:APA91bEMS-tq9je_7koCehDLYv26yG20HPAKtkn-lOcP5ETR5Wqs_dN9eVXRyuEj6LM4XZpgGOGewJkhycG8bY-fvQfX-cBROEtE7b9GC5Sva7D7Bl4bCm4Cl1TVdP3t5rhXcNdCNjM-']
    send_notification(resgistration , 'Code Keen added a new video' , 'Code Keen new video alert')
    return HttpResponse("sent")




def showFirebaseJS(request):
    data='importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-app.js");' \
         'importScripts("https://www.gstatic.com/firebasejs/8.2.0/firebase-messaging.js"); ' \
         'var firebaseConfig = {' \
         '        apiKey: "AIzaSyCJD0-w89XcoKXIS5RKCJjFGwdiYvLF9UQ",' \
         '        authDomain: "web-noti-ffa7c.firebaseapp.com",' \
         '        databaseURL: "",' \
         '        projectId: "web-noti-ffa7c",' \
         '        storageBucket: "web-noti-ffa7c.appspot.com",' \
         '        messagingSenderId: "581835456145",' \
         '        appId: "1:581835456145:web:40046e026a6f16e5e54930",' \
         '        measurementId: "G-DFX484N9LS"' \
         ' };' \
         'firebase.initializeApp(firebaseConfig);' \
         'const messaging=firebase.messaging();' \
         'messaging.setBackgroundMessageHandler(function (payload) {' \
         '    console.log(payload);' \
         '    const notification=JSON.parse(payload);' \
         '    const notificationOption={' \
         '        body:notification.body,' \
         '        icon:notification.icon' \
         '    };' \
         '    return self.registration.showNotification(payload.notification.title,notificationOption);' \
         '});'

    return HttpResponse(data,content_type="text/javascript")
