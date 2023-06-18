![alt text](Flask.png)





# Android Client/Flask Server :+1:

> Read the full article from here: https://medium.com/analytics-vidhya/how-to-make-client-android-application-with-flask-for-server-side-8b1d5c55446e.

### An Android app with a Flask server backend. This open-source project provides a seamless integration of Flask web framework in the server-side and Android app development in the client-side. By following the steps below, you can quickly get started with building your own Android-Flask web app.

## Server-Side Setup (Flask)
### Step 1 - Install Flask Framework
Open your terminal and execute the following command:

      $ pip3 install Flask

### Step 2 - Coding
Start developing your Flask web app by leveraging the extensive capabilities of the Flask framework. With its simplicity and flexibility, Flask allows you to build robust and scalable web applications effortlessly.
Note: you will find the python code inside the src folder.

## Client-Side Setup (Android App)
### Step 1 - Environment Configuration
Configure your development environment by installing the necessary tools and libraries. Ensure that you have Android Studio properly set up for Android app development.

### Step 2 - Coding
Leverage the power of OkHttp/Retrofit library and the versatility of Java/Kotlin to develop a feature-rich Android app. Utilize the Android Studio IDE to streamline your development process and create stunning user interfaces.

## Tips for Seamless Integration
### Manifest Configuration
Don't forget to add the following line to your Android manifest file to enable sending clear text to the server:
xml

      <application
          android:usesCleartextTraffic="true"
          ...
      >
          ...
      </application>

### Emulator Default Localhost
When running the Android app on an emulator, you can access the Flask server using the default localhost IP:

      http://10.0.2.2:PortNumber/
      
This allows the emulator to connect to the Flask server running on your local machine.

Feel free to explore and contribute to this project. Let's build amazing mobile/web apps together!

## License
This project is licensed under the MIT License.
     
  
