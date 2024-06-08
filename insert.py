# base insert

# 进来一个n20 seq:
def insert(seq):
    # 依次读到序列的每一个位置信息idx
    insert_list = []
    seq_list = list(seq)
    base = "ATCG"
    # print(seq_list)  # ['C', 'C', 'A','G'] 这样子的样子的
    for i in range(1, len(seq)):
        # print(i) # 1-19 用来标记在第几位之前插入
        if i >=1 and i<=8:
            for j in base:
                seq_list.insert(i, j)
                s = "".join(map(str, seq_list))
                insert_list.append(s)
                # 重置一下seq
                seq_list = list(seq)

    return insert_list


if __name__ == '__main__':
    seq = "CCAAGTAGGCATTCCAGGAG"
    ins = insert(seq)
    print(ins)
    print(len(ins))