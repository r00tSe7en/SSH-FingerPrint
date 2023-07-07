import subprocess
import argparse
import re
import base64
import binascii

def decode_base64_and_hex(input_str):
    # Base64解码
    decoded_str = base64.b64decode(input_str)
    # 将解码后的二进制转换为十六进制
    hex_str = binascii.hexlify(decoded_str).decode()
    return(hex_str)

def extract_key(output):
    pattern = r"SHA256:(\S+)\s"
    match = re.search(pattern, output)
    if match:
        key = match.group(1)
        return(key)

def ssh_keyscan(port,ip_address):
    command1 = f"ssh-keyscan -t ECDSA -p {port} {ip_address}"
    command2 = "ssh-keygen -E sha256 -lf -"
    try:
        # 执行第一个命令并将其输出作为第二个命令的输入
        process1 = subprocess.Popen(command1.split(), stdout=subprocess.PIPE)
        process2 = subprocess.Popen(command2.split(), stdin=process1.stdout, stdout=subprocess.PIPE)
        process1.stdout.close()
        # 获取第二个命令的输出
        output = process2.communicate()[0]
        # 调用函数来提取关键部分
        base64str = extract_key(output.decode())+'='
        print(ip_address + ' services.ssh.server_host_key.fingerprint_sha256='+decode_base64_and_hex(base64str))
    except:
        print(ip_address + ' Probably not the ssh port')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip_address", dest="ip_address", help="ip_address")
    parser.add_argument("-p", "--port", dest="port", help="port")
    args = parser.parse_args()
    ip_address = args.ip_address
    if args.port:
        port = args.port
    else:
        port = 22
    if (ip_address):
        ssh_keyscan(port,ip_address)
    else:
        print("please enter parameters -i 8.8.8.8 -p 22")
