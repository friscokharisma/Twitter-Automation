# Twitter-Automation

This automation was written on August 17, 2021, with the possibility of xpath changes in the future. This automation contains test case login, post tweet, and post image.

Requirement :
- Mozzila Firefox
- Python v2.7 : https://www.python.org/downloads
- Selenium    : https://selenium-python.readthedocs.io/installation.html

Note :
- Login used handler to anticipate twitter security system that does not allow to use email for login continuously, it is necessary to change with username and there is also a handler to overcome bots which are given login with different layouts
- Twitter posts cannot be the same, so unique value is needed in the form of decimal numbers.
- This code run for Windows operating system, a little bit change will be necessary for Mac os and Linux in the image path. Because this script will create an image containing a screenshoot in the same place as the script is located

How to use
- Download this repository
- Extract the downloaded file
- Run CMD
- Move to Downloads\Twitter-Automation-main
- Type : python codemi_test_qa_engineer.py and hit enter. As a result, you will get a tweet and an image post

Additional information

You can make account changes by changing the email variables and passwords in the script, you can also make content post changes to variable text_to_tweet
