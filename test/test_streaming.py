#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import commands
import shlex
import time
import threading
#2019/07/10作成．カメラをブラウザでストリーミングできるようにするテスト
#カメラ画像はhttp://ラズパイのIP/stream.htmlで見れる(fingを使え)
class stream():
	def __init__(self):
		self.camera_flag=0
	def start(self):
		#cmd = "sh start_server.sh" 
		cmd = "/usr/local/bin/mjpg_streamer -i \"input_raspicam.so -x 640 -y 480 -fps 15 -q 80\" -o \"output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www\" -b"
		#-bでバックグラウンドで実行
		#https://qiita.com/ego/items/3d23cda713f29f0dd141
		cmd = shlex.split(cmd)
		ret = subprocess.check_output(cmd)
		print(ret)
		print("ストリーミング開始")
		self.camera_flag=1
	def end(self):
		#cmd="sh end_server.sh"
		cmd2="pidof mjpg_streamer"
		cmd2 = shlex.split(cmd2)
		ret2 = subprocess.check_output(cmd2)
		print(ret2)
		cmd="kill -9 "+ret2
		cmd = shlex.split(cmd)
		ret = subprocess.check_output(cmd)
		print(ret)
		print("ストリーミングを終了します")
		self.camera_flag=0
if __name__ == '__main__':
	cmd = "python test_streaming2.py"
	#cmd = "usr/local/bin/mjpg_streamer -i \"input_raspicam.so -x 640 -y 480 -fps 15 -q 80\" -o \"output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www\" -b"
	#cmd=['/usr/local/bin/mjpg_streamer','-i','\"input_raspicam.so -x 640 -y 480 -fps 15 -q 80\"','-o','\"output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www\"','-b']
	cmd = shlex.split(cmd)
	ret = subprocess.check_output(cmd)
	print(ret)
	# t=threading.Thread(target=stream)
	# t.start()   

	print(ret)
	print("サーバー立てても動きます")
	time.sleep(1)
	print("待って！")
	stream=stream()
	CAMERA=1
	i=0
	while True:
		i +=1
		if CAMERA==True and stream.camera_flag==0:
			stream.start()
		if CAMERA==False and stream.camera_flag==1:
			stream.end()
			break
		if i>10:
			CAMERA=0
		time.sleep(1)
