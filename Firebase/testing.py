"""
Reference:  https://pyradise.com/10%E5%88%86%E9%90%98%E8%B3%87%E6%96%99%E5%BA%AB%E6%93%8D%E4%BD%9C-%E6%96%B0%E5%A2%9E%E8%B3%87%E6%96%99-b96db385e1e4
"""
# 引用必要套件
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


Path = 'counting-app-cbad8-firebase-adminsdk-f3g4v-11df033324.json'

# 引用私密金鑰
# path/to/serviceAccount.json 請用自己存放的路徑
cred = credentials.Certificate(Path)

# 初始化firebase，注意不能重複初始化
firebase_admin.initialize_app(cred)

# 初始化firestore
db = firestore.client()

doc = {
  'name': "chieh",
  'email': "test@gmail.com"
}

import time 

username = ['A', 'B', 'C', 'D']

for i in username:
  st = time.time()
  doc_ref = db.collection("Counting").document("User-" + str(i))
  doc_ref.set(doc)
  print("Spent : {}".format(time.time()-st))


### --- Dont define the docs id
# st = time.time()
# collection_ref = db.collection("Counting")
# collection_ref.add(doc)
# print("Second way will spend : {}".format(time.time()-st))