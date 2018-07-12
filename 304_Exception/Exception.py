#例外に関する情報の利用
try:
    a = 10 / 0
    print("{0}".format(a))
except ZeroDivisionError as e:
    print("type:{0}".format(type(e)))
    print("args:{0}".format(e.args))
#    print("message:{0}".format(e.message))
    print("{0}".format(e))


#複数パターンの例外
try:
    f = open(file_name,'w')
    data = dict_input['data']
    f.write(data)
    f.close()
except KeyError:
    print('キーが見つかりませんでした')
except (FileNotFoundError, TypeError) :
    print('ファイルが開けませんでした')
except:
    print('何らかのエラーが発生')


#else/finally
try:
    a = 10 / 0
#    a = 10 / 1
    print("{0}".format(a))
except ZeroDivisionError as e:
    print("ZeroDivisionError!!")
else:
    print("else statement")
finally:
    print("finally statement")

#故意に例外を発生
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
