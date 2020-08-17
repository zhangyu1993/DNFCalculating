from PublicReference.base import *

class 机械之灵技能0(被动技能):
    名称 = '机械原理'
    所在等级=15
    等级上限=11
    基础等级=1
    
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.085+0.015*self.等级,3)

class 机械之灵技能1(主动技能):
    名称 = 'G1科罗纳'
    所在等级=20
    等级上限=60
    基础等级=43  
    基础=99.84/0.20
    成长=11.52/0.20
    CD=1.0
    TP成长=0.10
    TP上限 = 5
   
    def 等效CD(self, 武器类型):
        return round(1.0,1)
    
    def G系加成倍率(self):
        if self.等级==0:
            return 0.0
        else:
            return round(0.59+0.01*self.等级,3)
    
class 机械之灵技能2(主动技能):
    名称='G2旋雷者'
    所在等级=25
    等级上限=60
    基础等级=41  
    基础=1786
    成长=202
    CD=6.0
    TP成长=0.10
    TP上限 = 5
    
    def 等效CD(self, 武器类型):
        return round(6.0,1)

    def G系加成倍率(self):
        if self.等级==0:
            return 0.0
        else:
            return round(0.50+0.01*self.等级,3)

class 机械之灵技能3(主动技能):
    名称='毒蛇炮'
    所在等级=25
    等级上限=60
    基础等级=41  
    基础=1856
    成长=197.25
    CD=2.975
    TP成长=0.10
    TP上限 = 5
    

class 机械之灵技能4(被动技能):
    名称='电能转换'
    所在等级=25
    等级上限=20
    基础等级=10
    关联技能=['毒蛇炮', '自爆狂风', '空战机械：狂风', '空投支援', '拦截机工厂', '光反应能量模块', 'G0战争领主', 'HS12等离子体', 'G4雷行者', 'GSP猎鹰科罗纳形态', 'GSP猎鹰旋雷者形态', 'GSP猎鹰捕食者形态', '高压电磁场', '终结者：博尔特MX', '空中射击']
    
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.10+0.02*self.等级,3)

class 机械之灵技能5(主动技能):
    名称='G3捕食者'
    所在等级=30
    等级上限=60
    基础等级=38
    基础=718.92
    成长=81.08
    CD=1
    TP成长=0.10
    TP上限 = 5
    
    def 等效CD(self, 武器类型):
        return round(1.0,1)

    def G系加成倍率(self):
        if self.等级==0:
            return 0.0
        else:
            return round(0.50+0.017*self.等级,3)

class 机械之灵技能6(主动技能):
    名称='G1磁力弹'
    所在等级=30
    等级上限=70
    基础等级=43  
    CD=12.75
   
class 机械之灵技能7(主动技能):
    名称='自爆狂风'
    所在等级=35
    等级上限=60
    基础等级=36  
    基础=1978.589
    成长=223.41
    CD=24.48
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.4
    
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=8.79

        elif x == 1:
            self.倍率*=9.24
            

class 机械之灵技能8(主动技能):
    名称='空战机械：狂风'
    所在等级=35
    等级上限=60
    基础等级=36  
    基础=3129.09/3
    成长=353.91/3
    CD=1.0
    TP成长=0.10
    TP上限 = 5

    def 等效CD(self, 武器类型):
        return round(1.0,1)

class 机械之灵技能9(主动技能):
    名称='空投支援'
    所在等级=40
    等级上限=60
    基础等级=33  
    基础=14841.875
    成长=1678.125
    CD=34.0
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3.5

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.242
            self.CD*=0.9
        elif x == 1:
            self.倍率*=1.334
            self.CD*=0.9
class 机械之灵技能10(主动技能):
    名称='拦截机工厂'
    所在等级=45
    等级上限=60
    基础等级=31  
    基础=21171.87
    成长=2398.13
    CD=38.25
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4.9

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.17

        elif x == 1:
            self.倍率*=1.25

class 机械之灵技能11(主动技能):
    名称='光反应能量模块'
    所在等级=45
    等级上限=60
    基础等级=31  
    基础=17480.4
    成长=1973.63
    CD=38.25
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.7

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.14

        elif x == 1:
            self.倍率*=1.22

class 机械之灵技能12(被动技能):
    名称='G系扩张'
    所在等级=48
    等级上限=40
    基础等级=20
    
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        else:
            return round(1.025+0.02*self.等级,3)

class 机械之灵技能13(主动技能):
    名称='G0战争领主'
    所在等级=50
    等级上限=40
    基础等级=12  
    基础=46219.33
    成长=13966.67
    CD=145.0
    演出时间 = 7.1

class 机械之灵技能14(主动技能):
    名称='HS12等离子体'
    所在等级=60
    等级上限=40
    基础等级=23  
    基础=15145
    成长=1710
    CD=25.5
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.9

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.12

        elif x == 1:
            self.倍率*=1.21

class 机械之灵技能15(主动技能):
    名称='G4雷行者'
    所在等级=70
    等级上限=40
    基础等级=18  
    基础=24396.94
    成长=2753.04
    CD=38.25
    TP成长=0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 7.3
    
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率*=1.12
            self.CD*=0.9
   
        elif x == 1:
            self.倍率*=1.20
            self.CD*=0.9

class 机械之灵技能16(被动技能):
    名称='GX主宰者'
    所在等级=75
    等级上限=40
    基础等级=11
    
    def 加成倍率(self, 武器类型):
        if self.等级==0:
            return 1.0
        if self.等级 in [1,2]:
            return round(1.08+0.02*self.等级,3)
        if self.等级==3:
            return round(1.15,3)    
        if self.等级==4:
            return round(1.20,3) 
        if self.等级>=5:
            return round(1.12+0.02*self.等级,3)


class 机械之灵技能17(主动技能):
    名称='GSP猎鹰科罗纳形态'
    所在等级=75
    等级上限=40
    基础等级=16
    基础=14018.25
    成长=1582.75
    CD=12.75
    基础释放次数=2
    演出时间 = 1.3
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35
            self.CD*=0.9

    def 等效CD(self, 武器类型):
        return round(self.CD,1)            

class 机械之灵技能18(主动技能):
    名称='GSP猎鹰旋雷者形态'
    所在等级=75
    等级上限=40
    基础等级=16
    基础=14370.375
    成长=1622.625
    CD=12.75
    基础释放次数=2
    演出时间 = 1.6
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.34
            self.CD*=0.9
    
    def 等效CD(self, 武器类型):
        return round(self.CD,1)


class 机械之灵技能19(主动技能):
    名称='GSP猎鹰捕食者形态'
    所在等级=75
    等级上限=40
    基础等级=16
    基础=15184.375
    成长=1715.625
    CD=12.75
    基础释放次数=2
    演出时间 = 2.8

    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.314
            self.CD*=0.9

    def 等效CD(self, 武器类型):
        return round(self.CD,1)

class 机械之灵技能20(主动技能):
    名称='高压电磁场'
    所在等级=80
    等级上限=40
    基础等级=13  
    基础=49465
    成长=5585
    CD=42.5
    演出时间 = 3.5
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.30
            self.CD*=0.9

class 机械之灵技能21(主动技能):
    名称='终结者：博尔特MX'
    所在等级=85
    等级上限=40
    基础等级=5  
    基础=93293.571
    成长=28170.429
    CD=180
    演出时间 = 7.1

class 机械之灵技能22(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 机械之灵技能23(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 机械之灵技能24(被动技能):
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

class 机械之灵技能25(主动技能):
    名称='空中射击'
    备注='(TP为基础精通)'
    所在等级=15
    等级上限=20
    基础等级=10
    基础=6726.4215
    成长=134.518125
    CD=1
    TP成长=0.10
    TP上限 = 3
    

    def 等效CD(self, 武器类型):
        return round(1.0,1)        

机械之灵技能列表 = []
i = 0
while i >= 0:
    try:
        exec('机械之灵技能列表.append(机械之灵技能'+str(i)+'())')
        i += 1
    except:
        i = -1

机械之灵技能序号 = dict()
for i in range(len(机械之灵技能列表)):
    机械之灵技能序号[机械之灵技能列表[i].名称] = i

机械之灵一觉序号 = 0
机械之灵二觉序号 = 0
机械之灵三觉序号 = 0
for i in 机械之灵技能列表:
    if i.所在等级 == 50:
        机械之灵一觉序号 = 机械之灵技能序号[i.名称]
    if i.所在等级 == 85:
        机械之灵二觉序号 = 机械之灵技能序号[i.名称]
    if i.所在等级 == 100:
        机械之灵三觉序号 = 机械之灵技能序号[i.名称]

机械之灵护石选项 = ['无']
for i in 机械之灵技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        机械之灵护石选项.append(i.名称)

机械之灵符文选项 = ['无']
for i in 机械之灵技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        机械之灵符文选项.append(i.名称)

class 机械之灵角色属性(角色属性):

    实际名称 = '机械之灵'
    角色 = '神枪手(女)'
    职业 = '机械师'

    武器选项 = ['自动手枪']
    
    伤害类型选择 = ['魔法百分比']
    
    伤害类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.850
   
    远古记忆 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(机械之灵技能列表)
        self.技能序号= deepcopy(机械之灵技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['G1科罗纳']].被动倍率 *= 1+self.技能栏[self.技能序号['G2旋雷者']].G系加成倍率()+self.技能栏[self.技能序号['G3捕食者']].G系加成倍率()
        self.技能栏[self.技能序号['G2旋雷者']].被动倍率 *= 1+self.技能栏[self.技能序号['G1科罗纳']].G系加成倍率()+self.技能栏[self.技能序号['G3捕食者']].G系加成倍率()
        self.技能栏[self.技能序号['G3捕食者']].被动倍率 *= 1+self.技能栏[self.技能序号['G1科罗纳']].G系加成倍率()+self.技能栏[self.技能序号['G2旋雷者']].G系加成倍率()
        self.技能栏[self.技能序号['G1磁力弹']].基础 = self.技能栏[self.技能序号['G1科罗纳']].等效百分比(self.武器类型)*0.21*1.72*10
        self.技能栏[self.技能序号['G1磁力弹']].被动倍率 = self.技能栏[self.技能序号['G1科罗纳']].被动倍率
        self.技能栏[self.技能序号['G1磁力弹']].等级 = self.技能栏[self.技能序号['G1科罗纳']].等级

class 机械之灵(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 机械之灵角色属性()
        self.角色属性A = 机械之灵角色属性()
        self.角色属性B = 机械之灵角色属性()
        self.一觉序号 = 机械之灵一觉序号
        self.二觉序号 = 机械之灵二觉序号
        self.三觉序号 = 机械之灵三觉序号
        self.护石选项 = deepcopy(机械之灵护石选项)
        self.符文选项 = deepcopy(机械之灵符文选项)
