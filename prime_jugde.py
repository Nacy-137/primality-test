n = int(input('素数判定したい整数を入力してください:'))
p = 0
i = 1

while(p<3 and i<n+1):   
    if n%i==0:
        p += 1
    i += 1

if p==2:
    print(f'{n}は素数です')
else:
    print(f'{n}は素数ではありません')
