#8 variant
signal = [0,0,-1,-1,-1,0,1,0,0,0,-1,0,0,0,1,1,0,0,-1,0,1,1,0,0,0,0,-1,0,0,1,0,0,-1,-1,0,1,1,1,1,1,0,0,-1,0,0,1,0,-1,1]
#Netmao
# 1 Mother
#signal = [0,0,-1,-1,-1,0,1,1,0,0,-1,0,0,1,0,-1,0,0,1,0,-1,-1,0,0,0,0,1,0,0,-1,-1,-1,-1,-1,0,1,1,1,0,0,-1,-1,0,1,0,0,0,-1,-1]
# 2 Fishka
#signal = [0,0,-1,-1,-1,-1,0,1,1,1,0,-1,-1,0,0,0,1,1,0,-1,0,0,0,1,0,0,-1,0,0,1,1,1,1,1,0,-1,-1,0,0,1,0,0,-1,0,0,0,0,0,1]


def get_ascii_word(data):
    l = len(data) // 8
    w = ''
    for i in range(l):
        n = ''
        for j in range(8):
            n += str(data[i*8+j])
        number = int(n, 2)
        w += chr(number)
    print(w)


def main():
    data = []
    for i in range(len(signal)-1):
        signal_bit = signal[i+1]
        signal_prev_bit = signal[i]
        if signal_bit == signal_prev_bit:
            data.append(0)
        else:
            data.append(1)
    print(data)
    get_ascii_word(data)




main()