from time import perf_counter
import Sqlite

class CF:

    def __init__(self, points, k=20, n=10):
        self.points = points
        # 相邻用户个数
        self.k = k
        # 推荐元素个数
        self.n = n
        # 用户对元素的交互数
        # 数据格式{UserID:[(ElementID, Points)]}
        self.userDict = {}
        # 对某元素交互的用户
        # 数据格式：{ElementID：[UserID]}
        # {'1',[1,2,3..],...}
        self.ItemUser = {}
        # 相邻用户的信息
        self.neighbors = []
        # 推荐列表
        self.recommandList = []
        self.cost = 0.0

    # 基于用户的推荐
    # 根据对元素的交互计算用户之间的相似度
    def recommendByUser(self, userId):
        self.format()
        self.n = 8
        self.getNearestNeighbor(userId)
        self.getrecommandList(userId)
        self.getPrecision(userId)

    # 获取推荐列表
    def getrecommandList(self, userId):
        self.recommandList = []
        # 建立推荐字典
        recommandDict = {}
        a=0
        for neighbor in self.neighbors:
            a+=neighbor[0]
            elements = self.userDict[neighbor[1]]
            for element in elements:
                if element[0] in recommandDict:
                    recommandDict[element[0]] += neighbor[0]*element[1]
                else:
                    recommandDict[element[0]] = neighbor[0]*element[1]
            for element in self.ItemUser:
                if element not in recommandDict:
                    recommandDict[element] = 0.0
                

        # 建立推荐列表
        for key in recommandDict:
            self.recommandList.append([key, recommandDict[key]/a])
        self.recommandList.sort(reverse=False)
        self.recommandList = self.recommandList[:self.n]


    def format(self):
        self.userDict = {}
        self.ItemUser = {}
        for i in self.points:
            for a in range(1,len(self.points[0])):
                if i[a] !=0:
                    if  i[0] in self.userDict:
                        self.userDict[i[0]].append((a,i[a]))
                    else:
                        self.userDict[i[0]]=[(a,i[a])]
                    if a in self.ItemUser:
                        self.ItemUser[a].append(i[0])
                    else:
                        self.ItemUser[a]=[i[0]]


    # 找到某用户的相邻用户
    def getNearestNeighbor(self, userId):
        neighbors = []
        # 获取userId点击的元素都有哪些用户也点击过
        for i in self.userDict[userId]:
            for j in self.ItemUser[i[0]]:
                if(j != userId and j not in neighbors):
                    neighbors.append(j)
        # 计算这些用户与userId的相似度并排序
        for i in neighbors:
            dist = self.getCost(userId, i)
            self.neighbors.append([dist, i])
        # 排序默认是升序，reverse=True表示降序
        self.neighbors.sort(reverse=True)
        self.neighbors = self.neighbors[:self.k]


    # 格式化userDict数据
    def formatuserDict(self, userId, l):
        user = {}
        for i in self.userDict[userId]:
            user[i[0]] = [i[1], 0]
        for j in self.userDict[l]:
            if(j[0] not in user):
                user[j[0]] = [0, j[1]]
            else:
                user[j[0]][1] = j[1]
        return user

    # 计算余弦距离
    def getCost(self, userId, l):
        # 获取用户userId和l点击元素的并集
        # {'ElementID'：[userId的点击数，l的点击数]} 没有点击为0
        user = self.formatuserDict(userId, l)
        x = 0.0
        y = 0.0
        z = 0.0
        for k, v in user.items():
            x += float(v[0]) * float(v[0])
            y += float(v[1]) * float(v[1])
            z += float(v[0]) * float(v[1])
        if(z == 0.0):
            return 0
        return z / (x * y)**0.5

    # 推荐的准确率
    def getPrecision(self, userId):
        
        user=[]
        recommand=[]
        cost=0.0

        for i in range(1,5):
            user.append(self.points[userId-1][i]/12)
            for a in self.recommandList:
                if i==a[0]:
                    recommand.append(a[1]/12)
        for i in range(0,4):
            cost+=(user[i]-recommand[i])**2
        self.cost=1-cost**0.5

def run(filepath):
    start = perf_counter()
    points = Sqlite.getData(filepath)
    demo = CF(points, k=200)
    demo.recommendByUser(len(demo.points))

    Sqlite.returnData(filepath,demo.recommandList)

    print("处理的数据为%d条" % (len(demo.points)))
    print("准确率： %.2f %%" % (demo.cost * 100))
    end = perf_counter()
    print("耗费时间： %f s" % (end - start))
