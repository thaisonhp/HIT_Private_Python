# n = int(input("n = "))
# k = int(input("k = "))
# while n < k : 
#     print("Lỗi mời nhập lại sao cho n > k!")
#     n = int(input("n = "))
#     k = int(input("k = "))

# def nhap_n_k():
#     n1 = int(input("n1 = "))
#     k1 = int(input("k1 = "))
#     n2 = int(input("n2 = "))
#     k2 = int(input("k2 = "))
#     while n < k : 
#         print("Lỗi mời nhập lại sao cho n > k!")
#         n = int(input("n = "))
#         k = int(input("k = "))
#         n2 = int(input("n2 = "))
#         k2 = int(input("k2 = "))

person1_sroce = 0 
person2_sroce = 0 
person1_opinion = "YES" 
person2_opinion = "YES"
index_round = 1
person_1_mistake = 0 
person_2_mistake = 0 
list_round_win_1 = [] 
list_round_win_2 = []
while person1_opinion == "YES" and person2_opinion == "YES" : 
    print("Bắt đầu vòng thứ ", index_round)
    n1 = int(input("n1 = "))
    k1 = int(input("k1 = "))
    n2 = int(input("n2 = "))
    k2 = int(input("k2 = "))
    while n1 < k1 : 
        person_1_mistake += 1
        print("Lỗi mời người chơi 1 nhập lại sao cho n > k!")
        n1 = int(input("n1 = "))
        k1 = int(input("k1 = "))
    while n2  < k2 : 
        person_2_mistake += 1
        print("Lỗi mời người chơi thứ hai nhập lại sao cho n2 > k2")
        n2 = int(input("n2 = "))
        k2 = int(input("k2 = "))
    # bắt đầu các turn 
    index_turn = 0 
    while n1 > 0 and n2 > 0 : 
        # nguoi choi 1 
        if index_turn % 2 == 0: 
            print("Đến lượt của người chơi thứ nhất!")
            gioi_han = min(n1,k1)
            x = int(input(f'Mời bạn nhập 1 số trong khoảng [1,{gioi_han}]:'))
            while x not in list(i for i in range(gioi_han+1)):
                x = int(input("Mời người chơi một nhập lại số :"))
            n1 -= x 
            index_turn += 1
        else:
            print("Đến lượt của người chơi thứ hai!")
            gioi_han = min(n2,k2)
            x = int(input(f'Mời bạn nhập 1 số trong khoảng [1,{gioi_han}]:'))
            while x not in list(i for i in range(gioi_han+1)):
                x = int(input("Mời người chơi hai nhập lại số :"))
            n2 -= x 
            index_turn += 1
    if n1 > 0 :
        person1_sroce += 1
        print(f'Round {index_round} người chơi 1 thắng' )
        list_round_win_1.append(index_round)
    if n2 > 0 : 
        person2_sroce += 1
        print(f'Round {index_round} người chơi 2 thắng' )
        list_round_win_2.append(index_round)
    print("Bạn có muốn chơi nữa không ?")
    print("Người chơi thứ nhất:")
    person1_opinion = input("Soạn YES nếu bạn muốn chơi tiếp không thì soạn NO!")
    person2_opinion = input("Soạn YES nếu bạn muốn chơi tiếp không thì soạn NO!")
    if person1_opinion == "YES" and person2_opinion == "YES": index_round += 1
# tong ket chung cuoc 
winner = 1
if person1_sroce > person2_sroce : 
    winner = 1
elif person1_sroce > person2_sroce : 
    print("Người chơi thứ hai thắng chung cuộc!")
    winner = 2
else: 
    if person_1_mistake > person_2_mistake: 
        winner = 1
    elif  person_1_mistake < person_2_mistake:
        winner = 2
    else: 
        print("Hai người hoà nhau")
# show thong tin cac tran cua nguoi thang 
if winner == 1 : 
    print("Người chơi thứ nhất thắng chung cuộc!")
    print("Các round mà người chơi thứ nhất win là: ", end = " ")
    for i in list_round_win_1:
        print(i, end=" ")
else: 
    print("Người chơi thứ hai thắng chung cuộc!")
    print("Các round mà người chơi thứ hai win là: ", end = " ")
    for i in list_round_win_2:
        print(i, end=" ")








