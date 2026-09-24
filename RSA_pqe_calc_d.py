def extended_gcd(a, b):
    """扩展欧几里得算法，返回 (gcd, x, y)，其中 ax + by = gcd"""
    if b == 0:
        return (a, 1, 0)
    else:
        g, x, y = extended_gcd(b, a % b)
        return (g, y, x - (a // b) * y)

def mod_inverse(e, phi):
    """计算e在模phi下的乘法逆元d"""
    g, x, y = extended_gcd(e, phi)
    if g != 1:
        raise Exception('e和phi不互质，无法计算逆元')
    else:
        return x % phi

def calculate_d(p, q, e):
    """已知p、q、e，计算私钥d"""
    # 计算欧拉函数φ(n)
    phi = (p - 1) * (q - 1)
    
    # 验证e是否与phi互质
    g, _, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception(f"e={e}与phi={phi}不互质，请选择其他e值")
    
    # 计算d
    d = mod_inverse(e, phi)
    
    # 验证d是否正确
    if (e * d) % phi != 1:
        raise Exception("计算错误，d验证失败")
    
    return d

def main():
    print("RSA私钥d计算器")
    print("-----------------")
    
    try:
        # 输入参数
        p = int(input("请输入质数p: "))
        q = int(input("请输入质数q: "))
        e = int(input("请输入公钥e: "))
        
        # 计算d
        d = calculate_d(p, q, e)
        
        # 输出结果
        print("\n计算结果:")
        print(f"p = {p}")
        print(f"q = {q}")
        print(f"e = {e}")
        print(f"n = p * q = {p * q}")
        print(f"φ(n) = (p-1) * (q-1) = {(p-1) * (q-1)}")
        print(f"d = {d}")
        print(f"验证: e * d mod φ(n) = {(e * d) % ((p-1) * (q-1))}")
        print("\n成功计算出私钥d！")
        
    except ValueError:
        print("错误: 请输入有效的整数")
    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    main()