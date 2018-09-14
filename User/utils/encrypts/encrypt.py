import base64
import time
import re
import random
import string
from apps.User.utils.exceptions import exception


"""
加密函数
"""
def createAlphStr():
    """
        获取随机字母
    :return: 字母
    """
    return random.choice(string.ascii_letters)

def createDigitStr():
    """
        获取随机数字字符串
    :return: 数字
    """
    return str(random.randint(0,9))

def createTimeStr():
    """
        获取时间戳
    :return: 时间戳
    """
    return str(time.time()).replace(".","")[6:-2]+createAlphStr()+str(time.time()).replace(".","")[2:3] + str(time.time()).replace(".","")[3:-3]

def inserStr(st,index,inserstr):
    """
    插入字符
    :param st: 原字符串
    :param index: 插入的位置
    :param inserstr: 要插入的字符串
    :return: 插入后的字符串
    """
    return st[:index] + inserstr + st[index:]

def createEncrypt(code):
    """
    随机数 + 随机数 + 时间戳[0:]( 第1个位置code[0]+随机字母 第4个位置code[1] 第5个位置code[2] 第7个位置code[3]+随机字母)

    :param code: 4位的字符串
    :return:
    """
    str1 = inserStr(createTimeStr(),1,code[0]+createAlphStr())
    str2 = inserStr(str1,5,code[1]+createAlphStr())
    str3 = inserStr(str2,7,code[2]+createAlphStr())
    str4 = inserStr(str3,10,code[3]+createAlphStr())
    strlast = createDigitStr() + createDigitStr() + str4
    encryptStr1 = str(base64.b64encode(strlast.encode('utf-8')),encoding="utf8")
    encryptStr2 = str(base64.b64encode(encryptStr1.encode('utf-8')),encoding="utf8")
    return encryptStr2



def decryptStr(code):
    """
    解密
    :param code: 密文
    :return: 验证码
    """
    if code == "": # 如果session为空,则需要重新刷新验证码
        raise exception.myException500("请刷新验证码")
    encryptedStr1 = str(base64.b64decode(code.encode('utf-8')),encoding="utf8")
    encryptedStr2 = str(base64.b64decode(encryptedStr1.encode('utf-8')),encoding="utf8")
    return encryptedStr2[3]+encryptedStr2[7]+encryptedStr2[9]+encryptedStr2[12]