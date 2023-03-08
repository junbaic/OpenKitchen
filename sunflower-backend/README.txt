1. Run backend
start backend at localhost
	i) cd /OpenKitchen/sunflower-backend
	ii) pip install -r package.txt
	iii) python app.py

Backend API online document: https://console-docs.apipost.cn/preview/0ec675b2ca871891/4feb3cfaa7193311?target_id=ae05f5f4-86f4-4bb7-8e42-de672e391f70

2. Use mysql workbench to connect to the aws mysql database
	i) Download MySQL Workbench 8.0 CE
	ii) add connection
	iii) enter these information:
		"connection name": rds
		"Hostname": localhost
		"Port": 3306
		"Username": root
	iv) click "test connection"
	v) enter password: 201199

3. Start frontend
    i) npm i 
    Install all the dependencies
    ii) npm start
    Start frontend