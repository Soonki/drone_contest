#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
import commands
import shlex
import time
import threading
#2019/07/10作成．カメラをブラウザでストリーミングできるようにするテスト

def stream():
    cmd = "sh start_server.sh" 
    #cmd = "usr/local/bin/mjpg_streamer -i \"input_raspicam.so -x 640 -y 480 -fps 15 -q 80\" -o \"output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www\" -b"
    #-bでバックグラウンドで実行
    #https://qiita.com/ego/items/3d23cda713f29f0dd141
    cmd = shlex.split(cmd)
    ret = subprocess.check_output(cmd)
    print(ret)
    time.sleep(3)
    print("OK")
    #cmd="sh end_server.sh"
    cmd2="pidof mjpg_streamer"
    cmd2 = shlex.split(cmd2)
    ret2 = subprocess.check_output(cmd2)
    print(ret2)
    cmd="kill -9 "+ret2
    cmd = shlex.split(cmd)
    ret = subprocess.check_output(cmd)
    print(ret)
    print("END")
if __name__ == '__main__':
    cmd = ['python', 'test_streaming2.py']
    #cmd = shlex.split(cmd)
    ret = subprocess.check_output(cmd)
    print(ret)
   # t=threading.Thread(target=stream)
   # t.start()   

    print(ret)
    print("サーバー立てても動きます")
    time.sleep(1)
    print("待って！")
    stream()
