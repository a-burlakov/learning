def codewars(int32: int) -> str:
    bin_line = format(int32, 'b')
    if len(bin_line) < 32:
        bin_line = '0' * (32 - len(bin_line)) + bin_line

    ip_octets = []
    for i in range(4):
        ip_octets.append(bin_line[i * 8:(i + 1) * 8])

    return '.'.join([str(int(ip, 2)) for ip in ip_octets])


print(codewars(2149583361))
print(codewars(32))
print(codewars(0))
