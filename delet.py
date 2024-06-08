# base delete

# 进来一个n20 seq:
def delete(seq):
    # 依次读到序列的每一个位置信息idx
    remove_list = []
    seq_list = list(seq)
    # print(seq_list) #  ['C', 'C', 'A','G'] 这样子的样子的
    for i in range(len(seq)):
        if i>=1 and i<=8:
            seq_list[i] = ""
            z = ''.join(seq_list)
            remove_list.append(z)
            # 重置一下seq
            seq_list = list(seq)
    return remove_list

# 测试
if __name__ == '__main__':
    seq = "CCAAGTAGGCATTCCAGGAG"
    i = delete(seq)
    print(i)
    print(len(i))
