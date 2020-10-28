# **LinkedIn Pending Invitations Withdrawer**

Too many pending invitations on your Linkedin account? 
This python script can solve that problem by automatically going through your list and delete them all within the parameter you specify.

<br>

## **Inspiration**

I encountered a situation where I couldn't send no more invitations to connect because I had a lot of pending invitations that I had sent that hadn't been accepted. And I found myself manually going through the list one by one, and I though I have my script do it for me.

<br>

## **Getting Started**

<br>

### **Prerequisites**

You need to have your Python 3.0~ and pip installed on your computer.


And install all the necessary libraries by typing the following:


```
pip install -r requirements.txt
```


**You'll need to add your config.py file that contains your LinkedIn password, username, and path to your driver, or you can directly enter them in the script.**


Refer to the following link for downloading your driver (Chrome is used in the script) - 
[Selenium documentation](https://selenium-python.readthedocs.io/installation.html)

<b>Please change the class object's parameter to your liking. You can either directly set it in the script or add an argument when you run the script on command line. </b>It's set as 'month' by default but you could change to '3 weeks', 'year', etc. If you specify the wait length with a number like '3 weeks', then you're just deleting those invitations that you've been waiting on for that specific length of time. But when specifying without a number, like 'month'/'week', this means deleting invitations with more than a month/week wait. 

<br>

### **Installing**

When everything is set up, run the following to execute the script:

```
python invitation_withdrawer.py
```

Or you add an argument for specifying how long you've been waiting on the invitations. The script will delete the invitations wih the specified length of wait.

```
python invitation_withdrawer.py '2 weeks'
```

<br>

## **Author**

* **Yuki Kakegawa** - [Github](https://github.com/stuffbyyuki), [LinkedIn](https://linkedin.com/in/yukikakegawa)

<br>

## **License**

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
