print(str('居中').center(20))
print(str('左对齐').ljust(20))
print(str('居右').rjust(20))
print(str('居中两边补齐').center(20,'*'))

print('{0:^20}'.format('居中'))
print('{0:<20}'.format('居左'))
print('{0:>20}'.format('居右'))
print('{0:*^20}'.format('居中补齐'))

print('多参数示例：{0:^10} = {1:<10}*{2:>10}'.format(8,2,4))

#进制转化，b o d x 分别表示二、八、十、十六进制
print('{:b}'.format(250))
print('{:o}'.format(250))
print('{:d}'.format(250))
print('{:x}'.format(250))

print('f精度:')
print('{:.1f}'.format(4.234324525254))
print('{:.4f}'.format(4.1))

#千分位分隔符，这种情况只针对与数字
print('{:,}'.format(1234567890))
print('{:,}'.format(567890.278634))

#精度/分隔符/居右
print('{:>18,.2f}'.format(1234567890))
print('{:>18,.2f}'.format(567890.278634))