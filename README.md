## SimpleOCR

### 项目简介

A Simple OCR Project

### 项目文件

~~~
├── Dockerfile	# Dockerfile
├── Procfile	# Deploy to Heroku Config
├── README.md	#
├── UnitTest	# UnitTest
│   ├── __init__.py
│   ├── resources	# Test images
│   ├── test_dao.py	# Test Dao
│   └── test_ocr.py	# Test OCR
├── manager.py	#
├── requirements.txt	# requirement
├── resources	# Images
├── simple_ocr	# Core
│   ├── __init__.py
│   ├── config
│   	├── __init__.py	# Config File Here
│   ├── constants.py	# Project Constants
│   ├── dao	# Dao
│   ├── main.py	# Core Entry
│   ├── models.py	# models
│   └── ocr	# ocr module
~~~

### 项目启动

- Docker

  ```
  docker build -t simple-ocr .	# build
  docker run  -p 5000:5000  simple-ocr	# run
  ```

### 项目部署

项目目前暂时部署在了heroku的免费资源上：https://simple-ocr-demo.herokuapp.com/docs