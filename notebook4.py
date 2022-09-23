import binascii

def eval_strint(s, base):
    return int(s, base = base)
    

def eval_strfrac(s, base):
    if "." in s:
        whole, dec = s.split(".")
    else:
        return float(eval_strint(s, base = base))
    wholeb10 = eval_strint(whole, base = base)
    decb10 = 0
    for i in range(len(dec)):
        dec1 = int(dec[i], base) * base**(-1*(i+1))
        decb10 += dec1
    return float(wholeb10 + decb10)

def fp_bin(v):
    hex_s = v.hex()
    sign = hex_s[0]
    start = hex_s.find('x')+1
    end = hex_s.find('p')
    temp = hex_s[start:end].replace('.','')
    significand = bin(int(temp, 16))[2:].zfill(53)
    significand = significand[0] + '.' + significand[1:]
    exponent = int(hex_s.split('p')[1])
    
    if sign == '0':
        sign = '+'
        
    return (sign, significand, exponent)

    
def main():
    
    # s = '11.0010001111'
    # base = 2
    # whole, dec = s.split(".")
    # wholeb10 = eval_strint(whole, base = base)
    # print(dec)
   
    # decb10 = 0
    # for i in range(len(dec)):
    #     dec1 = int(dec[i]) * base**(-1*(i+1))
    #     decb10 += dec1
        
    # result = float(wholeb10 + decb10)
    # print(result)
    # print(float((16**(-2) + 1))*(2**4))
    
    v = -1280.03125
    
    # s_hex = v.hex()
    # print(s_hex)
    # s_sign,res = s_hex.split("x")
    # s_signif, v_exp = res.split("p")
    # print(s_sign, s_signif, v_exp)
    
    # if s_sign == -0:
    #     sign = "-"
    # else:
    #     sign = "+"
    # print(sign)
       
    # if v_exp[0] == "+":
    #     exp = int(v_exp[1:])
    # else:
    #     exp = -1 * int(v_exp[1:])
    # print(exp)

    # res = bin(int(s_hex, 16)).zfill(50)
    # print(res)
    
    # hex_convert = v.hex()
    # print(f"hex: {hex_convert}")
    
    # sign = hex_convert[0]
    # start = hex_convert.find('x')+1
    # end = hex_convert.find('p')
    # temp = hex_convert[start:end].replace('.','')
    # print(f"hex2: {temp}")
    
    # significand = bin(int(temp, 16))[2:].zfill(53)
    # print(f"binary: {bin(int(temp, 16))}")
    # print(f"binary2: {bin(int(temp, 16))[2:]}")
    # print(f"binary3: {significand}")
    
    # significand = significand[0] + '.' + significand[1:]
    # print(f"result: {significand}")
    # # exponent = int(hex_convert.split('p')[1])
        
    

if __name__ == "__main__":
    main()