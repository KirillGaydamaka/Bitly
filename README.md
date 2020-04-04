# Bitly url shorterer

Tool for using bit.ly from console.

### How to install

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Code example

Geven any link starting with "http" returns bitlink: 
```
main.py http://ya.ru
Битлинк bit.ly/2X0XnmP
```
Geven any link starting with "bit.ly" returns clicks count: 
```
main.py bit.ly/2X0XnmP
Кликов 2
```



### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).