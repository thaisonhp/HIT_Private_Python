def dao_ma_tran(matrix):
    """Hàm này dùng để đảo ma trận cách 1 :
     đọc hơi khó hình dung nên không recommed"""
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def dao_ma_tran_v2(matrix):
     """Hàm này cũng để đảo ma trận nhưng ngắn hơn
        cũng dễ hiểu hơn nữa"""
     return [list(row) for row in zip(*matrix)]
# do em đã thử nhưng chưa pip được numpy nên em comment lại đã còn em chạy trên colab thì ok rồi ạ .
# import numpy as np

# def dao_ma_tran_v3(matrix):
#      """Cách ngắn nhất em nghĩ được để đảo ma trận """
#      return np.transpose(matrix)

hang, cot =  map(int, input().split())
ma_tran = [list(map(int, input().split())) for i in range(hang)]
ma_tran_dao_v1 = dao_ma_tran(ma_tran)
for i in ma_tran_dao_v1:
    for j in i : 
          print(j, end = " ")
    print()
