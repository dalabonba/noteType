
#------------定義類別-----------
class Bank():#類別名稱首字母必大寫
    title="taipei bank"#定義屬性
    def motto(self):#定義方法
        return "以客為尊"

userbank=Bank()
print("目前銀行:",userbank.title)
print("銀行的服務理念:",userbank.motto())
#-------------------------------


#-------類別建構元 初始化類別--------
# class Bank():
#     def __init__(self,username,money):#初始化 (銀行開戶)
#         self.title="taipei bank"
#         self.name=username
#         self.balance=money
        
#     def getBalance(self):
#         return self.balance

# userbank001=Bank("小明",10)
# print("目前銀行:",userbank001.title)
# print(f"{userbank001.name} 的存款餘額是 {userbank001.getBalance()}")
#-------------------------------------


#-------新增提款存款-----------------
# class Bank():
#     def __init__(self,username,money):#初始化
#         self.title="taipei bank"
#         self.name=username
#         self.balance=money
        
#     def getBalance(self):
#         return self.balance
    
#     def saveMoney(self,money):
#         self.balance+=money
#         print(f"{self.name}存了{money}元")
        
#     def withdrawMoney(self,money):
#         self.balance-=money
#         print(f"{self.name}領了{money}元")

# userbank001=Bank("小明",10)
# print("目前銀行:",userbank001.title)
# print(f"{userbank001.name}的存款餘額是{userbank001.getBalance()}")
# userbank001.saveMoney(40)
# print(f"{userbank001.name}的存款餘額是{userbank001.getBalance()}")

# print("----------------------")

# userbank002=Bank("小華",100)
# print("目前銀行:",userbank002.title)
# print(f"{userbank002.name}的存款餘額是{userbank002.getBalance()}")
# userbank002.withdrawMoney(90)#提款
# print(f"{userbank002.name}的存款餘額是{userbank002.getBalance()}")

# # print("----------------------")
# # userbank001.balance=10000000000000
# # print(f"{userbank001.name}的存款餘額是{userbank001.getBalance()}")
#---------------------------------------


#-------私有屬性 私有方法 封裝------------
# class Banks():
    
#     def __init__(self,uname):
#         self.__title="雲林銀行"
#         self.name=uname
#         self.__balance=0
#         self.__rate=30
#         self.__serviceCharge=0.01#手續費率1%
        
#     def saveMoney(self,money):
#         self.__balance+=money
#         print(f"成功存款{money}元")
        
#     def withDrawMoney(self,money):
#         self.__balance-=money
#         print(f"成功提款{money}元")
        
#     def getBalance(self):
#         print(f"{self.name}目前的餘額有{self.__balance}")
        
#     def __calRate(self,usaDoller):
#         return int(usaDoller*self.__rate*(1-self.__serviceCharge))#要換的美金*匯率*(1-手續費率)=可換得金額
        
#     def usaToTwd(self,usaDoller):
#         self.result=self.__calRate(usaDoller)
#         return self.result
    
# userBank=Banks("小明")

# userBank.saveMoney(100)

# userBank.getBalance()

# userBank.withDrawMoney(75)

# userBank.getBalance()

# usaDoller=2
# print(userBank.name,"的",usaDoller,"美金可換",userBank.usaToTwd(usaDoller),"台幣")
#---------------------------------------------