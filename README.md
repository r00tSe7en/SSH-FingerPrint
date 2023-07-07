# SSH-FingerPrint

SSH指纹与信息收集 - https://mp.weixin.qq.com/s/joZfpe2x0rDJAb8Vd_inEw

生成Censys.io (https://search.censys.io/data) 支持的 Sha256 Hash [services.ssh.server_host_key.fingerprint_sha256] 检索
# 依赖
```
python3
Linux：ssh-keyscan、ssh-keygen
```
# 使用方法

```
> python3 SSH-FingerPrint.py -h
usage: SSH-FingerPrint.py [-h] [-i IP_ADDRESS] [-p PORT]

options:
  -h, --help            show this help message and exit
  -i IP_ADDRESS, --ip_address IP_ADDRESS
                        ip_address
  -p PORT, --port PORT  port                           
```


