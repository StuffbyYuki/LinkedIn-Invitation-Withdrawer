# **LinkedIn Pending Invitations Withdrawer**

Too many pending invitations on your Linkedin account? 
This simple Python script can solve that problem by automatically going through your list and delete them all within the parameter you specify.

## **Inspiration**

I encountered a situation where I couldn't send no more invitations to connect because I had a lot of pending invitations that I had sent that hadn't been accepted. And I found myself manually going through the list one by one, and I though I have my script do it for me.

## **Getting Started**

### **Prerequisites**

You need to have your Python 3.0~ and pip installed on your computer.


And install all the necessary libraries by typing the following:


```
pip install -r requirements.txt
```


**You'll need to add your config.py file that contains your LinkedIn password, username, and path to your driver, or you can directly enter them in the script.**


Refer to the following link for downloading your driver (Chrome is used in the script) - 
[Selenium documentation](https://selenium-python.readthedocs.io/installation.html)

Please change the class object's parameter to your liking. It's set as 'month' by default but you could change to '3 weeks', 'year', etc. 


### **Installing**

When everything is set up, run the following to execute the script:

```
python invitation_withdrawer.py
```


## **Author**

* **Yuki Kakegawa** - [Github](https://github.com/stuffbyyuki), [LinkedIn](https://linkedin.com/in/yukikakegawa)


## **License**

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
