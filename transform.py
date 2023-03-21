# n20的mis match 变换
def transform(seq):
    base = "ATCG"
    seq = seq
    after_seq = []
    # 添加本身序列到列表中
    after_seq.append(seq)
    for idx, letter in list(enumerate(seq)):
        if idx>=1 and idx<=8:
            seq_list = list(seq)
            for j in  base:
                if letter != j:
                    seq_list[idx] = j
                    z = ''.join(seq_list)
                    after_seq.append(z)
    # print(len(after_seq))
    return after_seq


