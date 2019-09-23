import random

#https://blog.csdn.net/u010786109/article/details/45244103

# 函数一:参数为当前棋盘布局状态，根据布局判断当前八皇后布局存在冲突的皇后对数
def get_numof_conflict(status):
    num = 0

    for i in range(len(status)):
        for j in range(i + 1, len(status)):

            if status[i] == status[j]:#这一行表示如果有的话表示status[j]和status[i]在同一行
                num += 1
            offset = j - i
            if abs(status[i] - status[j]) == offset:#好牛逼的逻辑：这个绝对值表示两列之间检查点相差的格数，
                # 如果相等，表示是在两个45度角的方向上所以应该num+1
                num += 1
    return num


# 函数二：参数为当前棋盘布局状态，利用爬山法思想选择邻居状态最好的布局并返回
#这个函数的目的：比如一开始是[0,1,2,3,4,5,6,7],针对每一个数字除了他自己循环:比如变为[1,1,2,3,4,5,6,7],下一个[2,1,2,3,4,5,6,7]
#找出所有的组合中conflict次数最小的组合放到一个叫answer中，有可能有好几个所以随意取一个。
def hill_climbing(status):
    convert = {}
    length = len(status)
    for col in range(length):
        # best_move = status[col]
        for row in range(length):#这里循环这么多不要怕，不管循环，直接把row和col当做两个数。
            if status[col] == row:#跳过自己,就是[7,6,0,3,4,5,1,2]左侧数第四位数是3，循环是这样开始的[7,6,0,0,4,5,1,2],
                #[7, 6, 0, 1, 4, 5, 1, 2][7,6,0,2,4,5,1,2][7,6,0,4,4,5,1,2]这样循环
                continue
            status_copy = list(status)#好！这一步就是前者和后者不refer同一个地址，也就是说status怎么变，不影响它的copy。
            # python3可以用deepcopy包。这里原status不变，变的是status_copy。
            status_copy[col] = row#每次碰到循环只需要看看row和col是怎么变的，这里就是固定一列，row从0到length，也就是说固定一列，
            # row从上到下循环，然后再下一列，row再从上到下循环。每一次的col循环，代表这个list的某一个数字在变动。
            # 比如就是[7,6,0,3,4,5,1,2]左侧数第四位数是3，循环是这样开始的[7,6,0,0,4,5,1,2],
            # #[7, 6, 0, 1, 4, 5, 1, 2][7,6,0,2,4,5,1,2][7,6,0,4,4,5,1,2]这样循环
            convert[(col, row)] = get_numof_conflict(status_copy)#收集所有的组合以及他的conflict次数放在convert这个dictionary

    answers = []  # 最佳后继集合
    conflict_now = get_numof_conflict(status)  # 当前皇后冲突对数

    # 遍历存储所有可能后继的字典，找出最佳后继
    for key, value in convert.items():
        if value < conflict_now:
            conflict_now = value#找到conflict_now最小值
    for key, value in convert.items():
        if value == conflict_now:
            answers.append(key)#提取最小值的时候的所有的key放到answers中

    # 如果最佳后继集合元素大于一个 随机选择一个
    if len(answers) > 0:
        x = random.randint(0, len(answers) - 1)
        col = answers[x][0]
        row = answers[x][1]
        status[col] = row#在所有最好的中，随意选出一个真的将这个status的list的某个位置给替换然后return

    return status
#一上所有做的只是改变status所有数字中的某一个数字，下面这个函数是通过while循环一点点改变status的某些数字直到为0

# 函数三：求得八皇后满足冲突数为0的一个解，循环输出每一步的后继集合 直到不存在冲>突为止
def Queens():
    status = [0, 1, 2, 3, 4, 5, 6, 7]  # 初始状态所有皇后都在对角线

    # 当存在冲突的个数大于0时 循环求解最佳后继 直到找到八皇后解
    while get_numof_conflict(status) > 0:
        status = hill_climbing(status)
        print(status)
        print(get_numof_conflict(status))
    print("the answer is")
    print()
    print(status)


if __name__ == '__main__':
    Queens()

