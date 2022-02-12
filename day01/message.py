print("\n", "=" * 10, "蚂蚁庄园动态", "=" * 10)
'''with open('message.txt','w')as file:
    pass
file.write("黑发不知勤学早，白首方悔读书迟")
print("\n即将显示.....\n")
#file.close()'''
file = open("../message.txt", "w")
file.write("黑发不知勤学早，白首方悔读书迟,你使用了一张加速卡，小鸡撸起袖子开始吃饲料，进食速度大大加快\n")
print("\n即将显示.....\n")
file.close()
