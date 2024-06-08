# 获取前端输入数据生成模型的输入数据 应该是生成csv文件，然后encode里面去读进去
import transform
import delet
import insert
import pandas as pd
def generate(n20):
    # font 是从前端得到的N20序列
    font_n20 = n20
    # replace
    replace_transform = transform.transform(font_n20)
    # delete
    del_transform = delet.delete(font_n20)
    # insert
    insert_transform = insert.insert(font_n20)
    # merge
    final_gn20 = replace_transform + del_transform + insert_transform

    # print(after_transform)  # 转变后的list
    # for item in after_transform: #依次读到转变后的item
    #     print(item)
    # 创建字典赋值
    dic = {
        'N20': font_n20,
        'gn20': final_gn20,
        'F': 10
    }
    #  创建DataFrame 传入模型
    dt = pd.DataFrame(dic)
    # show df
    # print(dt)
    # dt.to_csv('test.csv')
    return dt
