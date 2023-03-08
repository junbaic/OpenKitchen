1. Run backend
Method_1: start backend at aws server
	i) cd /capstone-project-9900-w18r-sunflower/sunflower-backend
	ii) chmod 400 comp9900.pem (if your laptop is a windows system, watch this video https://www.youtube.com/watch?v=P1erVo5X3Bs)
	iii) ssh -i "comp9900.pem" ubuntu@ec2-52-194-185-52.ap-northeast-1.compute.amazonaws.com
	iv) cd 9900backend
	v) python3 app.py (use "ctrl+c" to exit the program)
hint: 
	show all process: netstat -ntlp
	kill a process: kill -9 <pid>

Method_2: start backend at localhost
	i) cd /capstone-project-9900-w18r-sunflower/sunflower-backend
	ii) pip install -r package.txt
	iii) change "ec2-52-194-185-52.ap-northeast-1.compute.amazonaws.com" in all frontend urls to "127.0.0.1"
	iv) python3 app.py

Backend API online document: https://console-docs.apipost.cn/preview/0ec675b2ca871891/4feb3cfaa7193311?target_id=ae05f5f4-86f4-4bb7-8e42-de672e391f70


2. Use mysql workbench to connect to the aws mysql database
	i) Download MySQL Workbench 8.0 CE
	ii) add connection
	iii) enter these information:
		"connection name": rds
		"Hostname":  comp9900database.cugl4hvapyl5.ap-northeast-1.rds.amazonaws.com
		"Port": 3306
		"Username": root
	iv) click "test connection"
	v) enter password: comp9900

3. Start frontend
    i) npm i 
    Install all the dependencies
    ii) npm start
    Start frontend