# MyLove - An Alexa Skill for Personalized Love Notes
MyLove is an Amazon Alexa skills app, designed to be run only within the Alexa family of products. You can download the [latest version](https://skills-store.amazon.com/deeplink/dp/B079WNPNSB) to your Alexa system by visting the Amazon Skills store.

MyLove gives you a great way to create a list of personalized messages that can later be randomly read back whenever your partner feels the need.

This app demonstrates three attributes of the Alexa eco-system:

* Working with lists
* Managing user controlled permissions
* Making REST calls to Alexa

To use this application as a starting point for your Alexa project, you will need to incorporate the following modules into your Amazon Lambda container, as it does not provide this in it's Python environent.

* **[PYOWM](https://github.com/csparpa/pyowm)** - A fantastic weather API (Github)
* **certifi** - Validates SSL certs (_pip install certifi_)
* **[chardet](https://github.com/chardet/chardet)** - Character encoding detector (Github)
* **idna** - Domain name handler (_pip install idna_)
* **[requests](https://github.com/requests/requests)** - HTTP requests REST package (Github)
* **urllib3** - HTTP client (_pip install urllib3_)

Commenting is done in pydocs format utilizing the popular NumPy format. You will need to provie your own Alexa skill id in globals.py to make this a functioning app. 

I chose not to bring in the logging libraries that are much better suited to debugging. I was trying to keep the footprint of the code as small as possible and opted to simply use if DEBUG statements. Shame on me.

Note: if you are not familiar with the Alexa development environment, A Cloud Guru has a great free [introductory course](https://acloud.guru/course/intro-alexa-free/dashboard) that is fantastic.