﻿from math import *
from PublicReference.base import *

古灵精怪等级 = 100 + 5 

class 古灵精怪技能0(主动技能):
    名称 = '变异苍蝇拍'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据 = [0, 5722, 6301, 6884, 7464, 8045, 8625, 9206, 9785, 10367, 10947, 11529, 12109, 12690, 13270, 13852, 14431, 15010, 15591, 16173, 16754, 17333, 17915, 18495, 19076, 19656, 20238, 20818, 21400, 21978, 22559, 23140, 23721, 24301, 24883, 25463, 26043, 26623, 27204, 27784, 28364, 28947, 29526, 30107, 30688, 31268, 31848, 32430, 33011, 33591, 34172, 34753, 35332, 35912, 36493, 37073, 37655, 38235, 38816, 39396, 39978, 40557, 41139, 41720, 42301, 42880, 43461, 44041, 44622, 45202, 45784]
    CD = 6.4
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 0.1
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] *  (1 + self.TP成长 * self.TP等级) * self.倍率
    

class 古灵精怪技能1(被动技能):
    名称 = '亲和法米利尔'
    所在等级 = 15
    等级上限 = 15
    基础等级 = 5
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.02 * self.等级 , 5)


class 古灵精怪技能2(主动技能):
    名称 = '改良舒露露'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((古灵精怪等级 - (所在等级 -10)) / 学习间隔 + 1), 等级精通)
    数据 =[0, 6419, 7070, 7721, 8373, 9023, 9675, 10326, 10977, 11630, 12281, 12931, 13583, 14234, 14886, 15536, 16187, 16839, 17490, 18142, 18793, 19444, 20095, 20746, 21397, 22048, 22699, 23352, 24003, 24654, 25306, 25957, 26609, 27259, 27909, 28561, 29212, 29864, 30515, 31166, 31819, 32470, 33122, 33773, 34421, 35074, 35725, 36376, 37028, 37679, 38331, 38982, 39633, 40286, 40937, 41586, 42237, 42888, 43541, 44192, 44843, 45495, 46146, 46798, 47449, 48099, 48750, 49401, 50053, 50704, 51355]
    CD = 16.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] *  (1 + self.TP成长 * self.TP等级) * self.倍率

class 古灵精怪技能3(主动技能):
    名称 = '熔岩药瓶失败'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 3
    等级精通 = 50
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据 = [0, 6927, 8031, 9137, 10242, 11346, 12451, 13555, 14659, 15764, 16868, 17973, 19078, 20182, 21289, 22393, 23496, 24601, 25705, 26810, 27915, 29020, 30126, 31230, 32332, 33436, 34541, 35648, 36752, 37857, 38961, 40064, 41169, 42274, 43379, 44484, 45589, 46694, 47798, 48902, 50006, 51111, 52216, 53320, 54425, 55530, 56635, 57738, 58843, 59948, 61053, 62157, 63262, 64366, 65471, 66575, 67679, 68784, 69889, 70994, 72099, 73203, 74308, 75411, 76516, 77621, 78725, 79830, 80934, 82040, 83143]
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 古灵精怪技能24(主动技能):
    名称 = '熔岩药瓶成功'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 3
    等级精通 = 50
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 1884, 2187, 2488, 2785, 3083, 3383, 3687, 3988, 4290, 4590, 4889, 5191, 5492, 5792, 6094, 6393, 6691, 6992, 7294, 7594, 7895, 8198, 8498, 8798, 9101, 9399, 9698, 9998, 10301, 10601, 10902, 11204, 11502, 11803, 12106, 12406, 12704, 13002, 13307, 13605, 13906, 14208, 14508, 14809, 15112, 15412, 15715, 16008, 16311, 16612, 16912, 17215, 17515, 17813, 18116, 18416, 18718, 19020, 19317, 19616, 19916, 20218, 20520, 20823, 21123, 21422, 21725, 22026, 22324, 22623]
    攻击次数1 = 6
    数据2 = [0, 103, 120, 135, 152, 169, 184, 201, 218, 234, 250, 267, 284, 300, 316, 333, 349, 364, 382, 398, 415, 430, 446, 464, 481, 497, 512, 529, 546, 561, 578, 594, 611, 627, 644, 660, 677, 693, 709, 726, 742, 758, 775, 792, 807, 824, 841, 857, 873, 890, 906, 922, 939, 955, 972, 988, 1005, 1021, 1038, 1054, 1070, 1087, 1104, 1119, 1136, 1153, 1169, 1185, 1202, 1218, 1233]
    攻击次数2 = 10
    
    #灼烧
    数据3 = [0, 12, 14, 16, 18, 20, 22, 24, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 119, 121, 123, 125, 127, 129, 131, 133, 135, 137, 139, 141, 143, 144]
    攻击次数3 = 10
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 古灵精怪技能4(主动技能):
    名称 = '魔道酸云雨'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 3
    等级精通 = 50
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 168, 194, 220, 247, 273, 300, 327, 354, 380, 407, 434, 460, 487, 514, 541, 567, 594, 621, 647, 673, 700, 728, 753, 780, 807, 835, 860, 887, 913, 940, 967, 994, 1020, 1047, 1074, 1101, 1126, 1154, 1181, 1207, 1233, 1261, 1288, 1314, 1340, 1368, 1393, 1420, 1447, 1474, 1501, 1527, 1553, 1579, 1607, 1634, 1661, 1686, 1714, 1741, 1767, 1793, 1821, 1846, 1874, 1900, 1928, 1953, 1981, 2006]
    攻击次数1 = 37
    数据2 = [0, 994, 1153, 1310, 1471, 1631, 1787, 1947, 2105, 2263, 2423, 2579, 2740, 2900, 3058, 3217, 3375, 3534, 3692, 3851, 4009, 4166, 4325, 4486, 4646, 4801, 4962, 5121, 5278, 5439, 5595, 5756, 5915, 6073, 6232, 6389, 6547, 6708, 6867, 7024, 7182, 7341, 7503, 7661, 7817, 7977, 8134, 8293, 8451, 8610, 8769, 8931, 9089, 9246, 9405, 9566, 9724, 9881, 10040, 10197, 10355, 10518, 10676, 10835, 10992, 11150, 11311, 11467, 11624, 11785, 11946]
    攻击次数2 = 6
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率
        


class 古灵精怪技能5(主动技能):
    名称 = '电鳗碰撞机'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 870, 959, 1048, 1136, 1226, 1314, 1402, 1490, 1578, 1666, 1756, 1844, 1933, 2020, 2109, 2196, 2287, 2374, 2463, 2552, 2640, 2728, 2815, 2906, 2994, 3082, 3170, 3259, 3346, 3436, 3524, 3613, 3700, 3790, 3878, 3966, 4055, 4144, 4232, 4319, 4409, 4496, 4586, 4673, 4763, 4850, 4939, 5027, 5116, 5204, 5293, 5382, 5470, 5558, 5646, 5736, 5823, 5912, 6000, 6089, 6176, 6266, 6354, 6443, 6531, 6620, 6708, 6795, 6886, 6974]
    攻击次数1 = 14
    数据2 = [0, 1370, 1509, 1648, 1787, 1928, 2067, 2205, 2345, 2484, 2623, 2762, 2901, 3040, 3179, 3318, 3457, 3596, 3736, 3874, 4013, 4153, 4292, 4430, 4569, 4709, 4849, 4988, 5127, 5266, 5405, 5545, 5683, 5822, 5961, 6099, 6238, 6378, 6518, 6657, 6795, 6935, 7074, 7213, 7352, 7491, 7630, 7770, 7910, 8047, 8186, 8326, 8464, 8603, 8743, 8882, 9020, 9160, 9300, 9439, 9578, 9717, 9856, 9995, 10135, 10273, 10412, 10552, 10691, 10831, 10971]
    攻击次数2 = 1
    #感电
    数据3 = [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 12, 12, 12, 13, 13, 14, 14, 14, 15, 15, 16, 16, 16, 17, 17, 18, 18, 18, 19, 19, 20, 20, 20, 21, 21, 22, 22, 22, 23, 23, 24, 24, 25, 25, 25, 26, 26, 27, 27, 27, 28, 28, 29, 29, 29, 30, 30, 31, 31, 31]
    攻击次数3 = 5
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    
    演出时间 = 4.8
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率
    
    是否有护石 = 1
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.27
        elif x == 1:
            self.倍率 *= 1.36


class 古灵精怪技能6(主动技能):
    名称 = '反重力装置'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据 = [0, 12258, 13502, 14745, 15989, 17233, 18475, 19719, 20963, 22207, 23451, 24694, 25937, 27181, 28424, 29668, 30912, 32155, 33399, 34642, 35886, 37130, 38373, 39617, 40861, 42105, 43347, 44591, 45834, 47078, 48322, 49566, 50810, 52052, 53296, 54540, 55784, 57027, 58271, 59515, 60757, 62001, 63245, 64489, 65733, 66977, 68221, 69463, 70707, 71950, 73194, 74438, 75681, 76925, 78168, 79412, 80656, 81900, 83143, 84387, 85631, 86873, 88117, 89360, 90604, 91848, 93092, 94336, 95579, 96822, 98066]
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.1
    
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] *  (1 + self.TP成长 * self.TP等级) * self.倍率


class 古灵精怪技能7(主动技能):
    名称 = '暴炎加热炉失败'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据 = [0, 918, 1010, 1105, 1198, 1291, 1384, 1478, 1571, 1665, 1758, 1851, 1943, 2036, 2130, 2222, 2316, 2409, 2504, 2596, 2689, 2782, 2875, 2969, 3062, 3156, 3248, 3342, 3435, 3528, 3622, 3715, 3807, 3900, 3994, 4087, 4179, 4273, 4366, 4461, 4553, 4647, 4739, 4833, 4927, 5020, 5113, 5205, 5299, 5393, 5487, 5579, 5673, 5764, 5858, 5951, 6044, 6138, 6230, 6325, 6418, 6511, 6604, 6696, 6790, 6884, 6977, 7070, 7164, 7256, 7351]
    攻击次数 = 13
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 2.0
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
    
    是否有护石 = 1
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2768
        elif x == 1:
            self.倍率 *= 1.3566

class 古灵精怪技能8(主动技能):
    名称 = '冰霜钻孔车失败'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 922, 1016, 1109, 1203, 1297, 1391, 1483, 1577, 1672, 1765, 1858, 1952, 2046, 2140, 2233, 2327, 2421, 2514, 2608, 2702, 2795, 2889, 2983, 3076, 3170, 3264, 3358, 3451, 3544, 3639, 3733, 3825, 3919, 4013, 4106, 4199, 4293, 4387, 4481, 4573, 4668, 4762, 4855, 4948, 5042, 5137, 5230, 5323, 5417, 5511, 5604, 5699, 5792, 5885, 5979, 6073, 6167, 6260, 6354, 6448, 6541, 6635, 6729, 6823, 6915, 7009, 7103, 7198, 7289, 7383]
    攻击次数1 = 9
    数据2 = [0, 8306, 9150, 9992, 10836, 11677, 12521, 13363, 14207, 15050, 15891, 16735, 17578, 18420, 19263, 20107, 20947, 21791, 22634, 23477, 24320, 25162, 26005, 26848, 27691, 28533, 29377, 30219, 31061, 31904, 32748, 33591, 34433, 35276, 36118, 36961, 37804, 38647, 39489, 40332, 41175, 42018, 42862, 43704, 44546, 45389, 46233, 47074, 47918, 48762, 49602, 50445, 51289, 52132, 52974, 53817, 54659, 55503, 56345, 57188, 58032, 58874, 59715, 60559, 61403, 62244, 63087, 63930, 64773, 65615, 66459]
    攻击次数2 = 1
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
   
    演出时间 = 2.0
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率
    
    是否有护石 = 1
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.32
        
class 古灵精怪技能9(主动技能):
    名称 = '超级苍蝇拍'
    所在等级 = 60
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据 = [27391,30171,32948,35726,38504,41284,44063,46842,49621,52400,55178,57958,60737,63516,66294,69074,71852,74631,77411,80190,82968,85748,88525,91304,94082,96862]
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    
    演出时间 = 0.1
    护石选项 = ['魔界', '圣痕']
    
    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] *  (1 + self.TP成长 * self.TP等级) * self.倍率
    
    是否有护石 = 1
    def 装备护石(self, x):
        if x == 0: 
            self.倍率 *= 1.15
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.24
            self.CD *= 0.9
        
class 古灵精怪技能10(被动技能):
    名称 = '成功预感'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1 + round(16 + 1.5 * (self.等级 - 16), 1) / 100

class 古灵精怪技能11(主动技能):
    名称 = '技艺融合'
    所在等级 = 50
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 1632, 2011, 2390, 2771, 3148, 3528, 3906, 4285, 4664, 5043, 5421, 5801, 6179, 6558, 6936, 7316, 7693, 8073, 8451, 8830, 9209, 9588, 9967, 10346, 10724, 11103, 11483, 11859, 12240, 12619, 12996, 13375, 13755, 14132, 14512, 14891, 15269, 15648, 16028, 16405, 16785, 17164, 17543, 17922, 18302, 18678, 19059, 19436, 19815, 20194, 20573, 20951, 21331, 21709, 22088, 22467, 22846, 23224, 23604, 23981, 24361, 24741, 25118, 25497, 25876, 26255, 26633, 27013, 27391, 27770]
    攻击次数1 = 22
    数据2 = [0, 44353, 54637, 64922, 75206, 85490, 95777, 106061, 116346, 126630, 136914, 147199, 157485, 167768, 178054, 188338, 198623, 208908, 219192, 229477, 239761, 250047, 260332, 270616, 280902, 291185, 301470, 311755, 322039, 332326, 342610, 352894, 363179, 373463, 383748, 394032, 404318, 414603, 424887, 435172, 445456, 455740, 466026, 476311, 486596, 496880, 507164, 517449, 527735, 538019, 548304, 558588, 568873, 579159, 589443, 599727, 610011, 620296, 630583, 640867, 651152, 661435, 671720, 682005, 692289, 702576, 712860, 723144, 733429, 743713, 753998]
    攻击次数2 = 1
    CD = 145.0
    
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 *1.1) * (1 + self.TP成长 * self.TP等级) * self.倍率
    
    
   
class 古灵精怪技能12(主动技能):
    名称 = '光电兔'
    所在等级 = 70
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 9439, 10397, 11355, 12312, 13270, 14227, 15186, 16142, 17100, 18058, 19016, 19974, 20931, 21889, 22847, 23805, 24762, 25719, 26677, 27635, 28593, 29550, 30507, 31466, 32423, 33381, 34338, 35296, 36254, 37212, 38169, 39126, 40085, 41042, 42001, 42957, 43914, 44873, 45830, 46788, 47745, 48704, 49661, 50620, 51576, 52534, 53492, 54449, 55407, 56364, 57323, 58280, 59239, 60195, 61153, 62111, 63068, 64025, 64983, 65941, 66899, 67857, 68814, 69772, 70730, 71688, 72644, 73602, 74560, 75518]
    攻击次数1 = 4
    数据2 = [0, 5524, 6085, 6645, 7205, 7766, 8327, 8887, 9447, 10008, 10568, 11128, 11689, 12250, 12810, 13370, 13931, 14491, 15051, 15612, 16173, 16733, 17293, 17854, 18414, 18975, 19535, 20097, 20656, 21216, 21778, 22338, 22899, 23458, 24020, 24580, 25140, 25701, 26261, 26822, 27383, 27943, 28503, 29063, 29624, 30184, 30745, 31306, 31866, 32426, 32986, 33547, 34107, 34668, 35229, 35789, 36349, 36909, 37470, 38030, 38591, 39153, 39712, 40272, 40832, 41394, 41954, 42514, 43076, 43636, 44196]
    攻击次数2 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    
    演出时间 = 4
    护石选项 = ['魔界', '圣痕']
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率
   
    是否有护石 = 1
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.15
        elif x == 1:
            self.倍率 *= 1.23

class 古灵精怪技能13(主动技能):
    名称 = '雪人刨冰'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 2100, 2312, 2525, 2737, 2951, 3165, 3378, 3591, 3803, 4017, 4230, 4442, 4656, 4869, 5082, 5295, 5508, 5722, 5933, 6147, 6362, 6573, 6789, 7000, 7214, 7427, 7640, 7853, 8066, 8279, 8492, 8705, 8919, 9131, 9345, 9556, 9770, 9984, 10197, 10410, 10622, 10836, 11049, 11262, 11475, 11688, 11901, 12113, 12327, 12541]
    攻击次数1 = 18
    
    数据2 = [0, 1294, 1426, 1558, 1688, 1820, 1950, 2082, 2215, 2346, 2477, 2607, 2739, 2870, 3003, 3134, 3266, 3396, 3527, 3658, 3792, 3923, 4054, 4186, 4317, 4449, 4580, 4711, 4842, 4974, 5105, 5237, 5369, 5499, 5631, 5761, 5893, 6024, 6157, 6288, 6419, 6550, 6682, 6812, 6945, 7077, 7207, 7338, 7469, 7601, 7733]
    攻击次数2 = 13
    
    数据3 = [0, 17810, 19615, 21421, 23229, 25035, 26842, 28649, 30455, 32261, 34069, 35875, 37682, 39488, 41295, 43101, 44909, 46715, 48524, 50329, 52136, 53944, 55750, 57556, 59364, 61169, 62976, 64783, 66590, 68396, 70203, 72009, 73816, 75623, 77430, 79235, 81043, 82849, 84656, 86463, 88270, 90076, 91884, 93690, 95497, 97305, 99111, 100916, 102724, 104530, 106337]
    攻击次数3 = 1
   
    CD = 40.0
    演出时间 = 4
    
    是否有护石 = 1
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率 *= 1.3

class 古灵精怪技能14(被动技能):
    名称 = '贤者之石'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['魔道酸云雨','电鳗碰撞机','反重力装置','熔岩药瓶成功']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)          


class 古灵精怪技能15(被动技能):
    名称 = '魔道学助手'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['变异苍蝇拍','超级苍蝇拍','改良舒露露','技艺融合','超级棒棒糖','光电兔','雪人刨冰','乌洛波洛斯之环']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.17 + 0.02 * self.等级, 5)           

  
class 古灵精怪技能16(被动技能):
    名称 = '魔道学助手+苦涩棒棒糖'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['冰霜钻孔车失败','暴炎加热炉失败','熔岩药瓶失败']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.88 + 0.02 * self.等级, 5)      

class 古灵精怪技能17(主动技能):
    名称 = '超级棒棒糖'
    所在等级 = 80
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 51168, 56357, 61549, 66738, 71930, 77120, 82313, 87503, 92695, 97884, 103076, 108266, 113458, 118648, 123839, 129029, 134222, 139412, 144603, 149793, 154984, 160174, 165367, 170557, 175748, 180939, 186129, 191319, 196512, 201701, 206893, 212083, 217275, 222466, 227658, 232846, 238038, 243228, 248420, 253611, 258803, 263992, 269183, 274373, 279566, 284756, 289947, 295139, 300329, 305522, 310711, 315903, 321092, 326284, 331474, 336666, 341857, 347048, 352237, 357428, 362619, 367811, 373002, 378193, 383382, 388573, 393765, 398956, 404146, 409338]
    攻击次数1 = 1
    数据2 = [0, 32713, 36032, 39351, 42670, 45988, 49307, 52626, 55944, 59262, 62582, 65900, 69219, 72536, 75857, 79174, 82493, 85811, 89131, 92452, 95770, 99090, 102407, 105727, 109044, 112365, 115681, 119000, 122319, 125638, 128955, 132275, 135593, 138913, 142230, 145550, 148868, 152187, 155507, 158825, 162146, 165463, 168783, 172101, 175420, 178738, 182058, 185376, 188695, 192013, 195332, 198651, 201969, 205288, 208607, 211925, 215244, 218564, 221882, 225201, 228519, 231840, 235157, 238477, 241795, 245115, 248432, 251752, 255070, 258390, 261707]
    攻击次数2 = 1
    是否有护石 = 1
    
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率
    
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        self.倍率 *= 1.32
        self.CD *= 0.9
        
    CD = 45.0
    演出时间 = 0.5
    

class 古灵精怪技能18(主动技能):
    名称 = '乌洛波洛斯之环'
    所在等级 = 85
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((古灵精怪等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 2806, 3457, 4107, 4758, 5409, 6060, 6712, 7362, 8013, 8664, 9315, 9966, 10616, 11266, 11918, 12568, 13218, 13871, 14521, 15173, 15823, 16473, 17124, 17775, 18426, 19077, 19727, 20378, 21030, 21680, 22331, 22982, 23633, 24284, 24934, 25585, 26236, 26887, 27537, 28189, 28840, 29491, 30140, 30792, 31442, 32093, 32744, 33394, 34046, 34696, 35348, 35999, 36649, 37301, 37951, 38601, 39253, 39903, 40555, 41205, 41854, 42508, 43158, 43809, 44460, 45109, 45762, 46411, 47062, 47713]
    攻击次数1 = 21
    数据2 = [0, 2282, 2810, 3338, 3868, 4396, 4925, 5454, 5982, 6511, 7041, 7569, 8097, 8628, 9158, 9685, 10214, 10744, 11273, 11800, 12330, 12859, 13387, 13916, 14446, 14976, 15504, 16032, 16562, 17090, 17619, 18149, 18676, 19205, 19735, 20264, 20793, 21322, 21851, 22380, 22908, 23437, 23967, 24495, 25023, 25553, 26081, 26612, 27140, 27670, 28198, 28727, 29256, 29784, 30313, 30843, 31371, 31899, 32429, 32959, 33487, 34016, 34545, 35075, 35602, 36131, 36661, 37189, 37717, 38247, 38778]
    攻击次数2 = 20
    数据3 = [0, 71074, 87557, 104038, 120520, 137001, 153481, 169962, 186444, 202925, 219408, 235889, 252370, 268852, 285333, 301815, 318296, 334778, 351258, 367740, 384220, 400702, 417183, 433665, 450146, 466628, 483109, 499591, 516072, 532553, 549033, 565515, 581996, 598479, 614959, 631441, 647922, 664404, 680885, 697367, 713848, 730329, 746810, 763292, 779772, 796254, 812735, 829218, 845699, 862180, 878661, 895143, 911624, 928104, 944585, 961068, 977549, 994031, 1010512, 1026993, 1043475, 1059956, 1076439, 1092919, 1109400, 1125881, 1142363, 1158844, 1175325, 1191806, 1208289]
    攻击次数3 = 1
    
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2+self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    CD = 180.0


class 古灵精怪技能19(主动技能):
    名称 = '魔法秀'
    所在等级 = 20
    等级上限 = 15
    基础等级 = 10
    是否有伤害 = 0
    冷却关联技能 = ['改良舒露露','熔岩药瓶失败','魔道酸云雨','电鳗碰撞机','暴炎加热炉失败','冰霜钻孔车失败','反重力装置','熔岩药瓶成功','光电兔','雪人刨冰']

    魔法秀数值 = [0, 22, 43, 65, 86, 108, 130, 151, 173, 194, 216, 238, 259, 281, 302, 324, 346, 367, 389, 410, 432]
    def CD缩减倍率(self, 武器类型):
            if self.等级 == 0:
               return 1.0
            else:
               return round(1 - 0.001*self.魔法秀数值[self.等级] , 3)

class 古灵精怪技能20(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 古灵精怪技能21(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 古灵精怪技能22(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

class 古灵精怪技能23(被动技能):
    名称 = '幸运棒棒糖'
    所在等级 = 25
    等级上限 = 15
    基础等级 = 5
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.07 + 0.01 * self.等级 , 5)


古灵精怪技能列表 = []
i = 0
while i >= 0:
    try:
        exec('古灵精怪技能列表.append(古灵精怪技能'+str(i)+'())')
        i += 1
    except:
        i = -1

古灵精怪技能序号 = dict()
for i in range(len(古灵精怪技能列表)):
    古灵精怪技能序号[古灵精怪技能列表[i].名称] = i

古灵精怪一觉序号 = 0
古灵精怪二觉序号 = 0
古灵精怪三觉序号 = 0
for i in 古灵精怪技能列表:
    if i.所在等级 == 50:
        古灵精怪一觉序号 = 古灵精怪技能序号[i.名称]
    if i.所在等级 == 85:
        古灵精怪二觉序号 = 古灵精怪技能序号[i.名称]
    if i.所在等级 == 100:
        古灵精怪三觉序号 = 古灵精怪技能序号[i.名称]

古灵精怪护石选项 = ['无']
for i in 古灵精怪技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        古灵精怪护石选项.append(i.名称)

古灵精怪符文选项 = ['无']
for i in 古灵精怪技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        古灵精怪符文选项.append(i.名称)

class 古灵精怪角色属性(角色属性):

    实际名称 = '古灵精怪'
    角色 = '魔法师(女)'
    职业 = '魔道学者'

    武器选项 = ['魔杖','法杖','棍棒','矛','扫把']
    
    伤害类型选择 = ['魔法固伤']
    
    伤害类型 = '魔法固伤'
    防具类型 = '皮甲'
    防具精通属性 = ['智力']

    主BUFF = 1.92
   
    远古记忆 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(古灵精怪技能列表)
        self.技能序号= deepcopy(古灵精怪技能序号)
    
class 古灵精怪(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 古灵精怪角色属性()
        self.角色属性A = 古灵精怪角色属性()
        self.角色属性B = 古灵精怪角色属性()
        self.一觉序号 = 古灵精怪一觉序号
        self.二觉序号 = 古灵精怪二觉序号
        self.三觉序号 = 古灵精怪三觉序号
        self.护石选项 = deepcopy(古灵精怪护石选项)
        self.符文选项 = deepcopy(古灵精怪符文选项)
