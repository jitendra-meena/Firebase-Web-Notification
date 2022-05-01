# Firebase-Web-Notification
This Project were We can get Live Web Notifications Using Firebase 

# Basic Setup

1. Create your virtual environment
2. Create a Django project
3. git clone remote url

# Install Dependencies
  ```bash
  pip install -r requirements.txt
  ```


# FireBase Cloud Messaging
The FCM JavaScript API lets you receive notification messages in web apps running in browsers that support the Push API. 

# Add and initialize the FCM SDK :
import { initializeApp } from "firebase/app";
import { getMessaging } from "firebase/messaging";

// TODO: Replace the following with your app's Firebase project configuration
// See: https://firebase.google.com/docs/web/learn-more#config-object
const firebaseConfig = {
  // ...
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


// Initialize Firebase Cloud Messaging and get a reference to the service
const messaging = getMessaging(app);


# Configure Web credentials in your app
The method getToken(): Promise allows FCM to use the VAPID key credential when sending message requests to different push services. Using the key you generated or imported according to the instructions in Configure Web Credentials with FCM, add it in your code after the messaging object is retrieved

  ```bash
 // Add the public key generated from the console here.
messaging.getToken({vapidKey: "BKagOny0KF_2pCJQ3m....moL0ewzQ8rZu"});
  ```


# Access the registration token
When you need to retrieve the current registration token for an app instance, call getToken. If notification permission has not been granted, this method will ask the user for notification permissions. Otherwise, it returns a token or rejects the promise due to an error.

FCM requires a firebase-messaging-sw.js file. Unless you already have a firebase-messaging-sw.js file, create an empty file with that name and place it in the root of your domain before retrieving a token. You can add meaningful content to the file later in the client setup process

```bash
import { getMessaging, getToken } from "firebase/messaging";

// Get registration token. Initially this makes a network call, once retrieved
// subsequent calls to getToken will return from cache.
const messaging = getMessaging();
getToken(messaging, { vapidKey: '<YOUR_PUBLIC_VAPID_KEY_HERE>' }).then((currentToken) => {
  if (currentToken) {
    // Send the token to your server and update the UI if necessary
    // ...
  } else {
    // Show permission request UI
    console.log('No registration token available. Request permission to generate one.');
    // ...
  }
}).catch((err) => {
  console.log('An error occurred while retrieving token. ', err);
  // ...
});
```

# Configurations in views.py 
Create Notifications Functions define FCM Server Key and Urls and set notification message and description and other like logo and image also. 

```bash
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
            "icon": "https://png.pngtree.com/png-clipart/20190906/original/pngtree-c4d-cool-black-red-gold-three-dimensional-letter-j-decoration-png-image_4572647.jpg",
            
        }
    }
```

# Register User For Live Web notifications

![GitHub Logo](./images/reg.png)


```bash


```
![GitHub Light](https://github.com/github-light.png#gh-dark-mode-only)

# Thank You Team

