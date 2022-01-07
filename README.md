# Automatically Send Hapy Birth Day Emails
*Automate The Boring Stuff & Never Forget Someone's Birthday Again By Automatically Sending Happy Birthday Emails Using Python!*
## How to use 
- Prepare sender.py 
```python
class Sender:
  def __init__(self):
    self.email = 'your_email'
    self.password = 'your_password'
  
  def getEmail(self):
    return self.email

  def getPassword(self):
    return self.password
```
- Prepare an input excel file called `Birthdays.xlsx` with the following structure:

| Name   | Birth_day   | Birth_month | Birth_year  | Email             |
| :----- | :---------- | :---------- | :---------- |:----------------- |
| Hoa    | 1           | 5           | 2000        |example@gmail.com  |
| Hue    | 2           | 6           | 2000        |example@gmail.com  |
| Nhi    | 3           | 7           | 1999        |example@gmail.com  |
| Huy    | 4           | 8           | 1999        |example@gmail.com  |

- Recommendation : run with crontab 




 

