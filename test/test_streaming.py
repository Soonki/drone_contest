import subprocess
import shlex

#2019/07/10作成．カメラをブラウザでストリーミングできるようにするテスト
#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    cmd = "python test_streaming2.py"
    cmd = shlex.split(cmd)
    ret = subprocess.check_output(cmd)
    print(ret)