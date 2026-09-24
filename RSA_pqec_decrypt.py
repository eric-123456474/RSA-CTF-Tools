#!/usr/bin/env python3
"""
RSA Decryptor for CTF challenges

This script decrypts RSA ciphertext when given p, q, e, and c.
Usage: python rsa_decryptor.py <p> <q> <e> <c>

Or run interactively to input values manually.
"""

import sys

def modinv(a, m):
    """计算模逆元"""
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None
    else:
        return x % m

def extended_gcd(a, b):
    """扩展欧几里得算法"""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def rsa_decrypt(c, d, n):
    """RSA解密"""
    return pow(c, d, n)

def int_to_str(num):
    """将整数转换为字符串"""
    try:
        # 尝试直接转换
        return bytes.fromhex(hex(num)[2:]).decode('utf-8')
    except:
        # 尝试其他可能的编码
        try:
            # 移除前导零并转换
            hex_str = hex(num)[2:]
            if len(hex_str) % 2 != 0:
                hex_str = '0' + hex_str
            return bytes.fromhex(hex_str).decode('utf-8', errors='ignore')
        except:
            return f"[无法转换为字符串] {num}"

def main():
    """主函数"""
    print("RSA Decryptor for CTF challenges")
    print("=" * 50)
    
    # 检查命令行参数
    if len(sys.argv) == 5:
        # 从命令行获取参数
        p = int(sys.argv[1])
        q = int(sys.argv[2])
        e = int(sys.argv[3])
        c = int(sys.argv[4])
    else:
        # 交互式输入
        print("请输入以下参数：")
        p = int(input("p: "))
        q = int(input("q: "))
        e = int(input("e: "))
        c = int(input("c: "))
    
    print("\n计算中...")
    
    # 计算n
    n = p * q
    print(f"n = {n}")
    
    # 计算欧拉函数φ(n)
    phi_n = (p - 1) * (q - 1)
    print(f"φ(n) = {phi_n}")
    
    # 计算私钥d
    d = modinv(e, phi_n)
    if d is None:
        print("错误：无法计算模逆元，e和φ(n)不互质")
        return
    print(f"d = {d}")
    
    # 解密密文
    m = rsa_decrypt(c, d, n)
    print(f"m = {m}")
    
    # 将数字转换为字符串
    flag = int_to_str(m)
    print(f"\nFlag: {flag}")
    
    # 保存结果到文件
    with open('decryption_result.txt', 'w', encoding='utf-8') as f:
        f.write(f"p = {p}\n")
        f.write(f"q = {q}\n")
        f.write(f"e = {e}\n")
        f.write(f"c = {c}\n")
        f.write(f"n = {n}\n")
        f.write(f"φ(n) = {phi_n}\n")
        f.write(f"d = {d}\n")
        f.write(f"m = {m}\n")
        f.write(f"Flag = {flag}\n")
    print("\n结果已保存到 decryption_result.txt")

if __name__ == "__main__":
    main()
