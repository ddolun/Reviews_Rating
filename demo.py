from ckipnlp.pipeline import CkipPipeline, CkipDocument
import pickle
pipeline = CkipPipeline()
doc = CkipDocument(raw='啟動中')
pipeline.get_ws(doc)
sentences =[]
with open(r'D:\vscode\python\reviews_rating\CSV\modelV3_5\117KstopwsSVMmodel.pkl', 'rb') as f:
    model = pickle.load(f)
with open(r'D:\vscode\python\reviews_rating\CSV\modelV3_5\117Kstopwsvectorizer.pkl', 'rb') as f:
    vector = pickle.load(f)


i = 0
while i<10 :
    theinput = input("請輸入評論:")
    doc = CkipDocument(raw=theinput)
    pipeline.get_ws(doc)
    ws = '|'.join(doc.ws[0])
    sentences = [ws]
    X = vector.transform(sentences)
    pred = round(model.predict(X)[0],1)
    print("具體度為{}分".format(pred))
    i+=1
#今天送餐很快，東西又好吃，推薦大家來吃
#店員態度很好，上菜速度快，特別是他們家的漢堡很好吃，而且價格不貴，推推推!!!
# 吃過那麼多燒肉店，第一次遇到不用服務費 服務還那麼好的，也很主動換烤網
# 這輩子再也不會再來了，沒有餐點是值得的，貴又難吃，一份炒泡麵要賣360，以為是什麼神級美食，結果是餐飲業的詐騙集團，有看到我的評論的請相信我，給一星都嫌多了
# 魚肉炸的很紮實，羹湯還不錯，雞腿普通，炸豆腐好吃
# 一人199烤蚵吃到飽🦪🦪🦪加點炒螺肉150也好吃👍🏻👍🏻👍🏻
# 一人199烤蚵吃到飽，加點炒螺肉150也好吃
# 小籠包現包現蒸，尺寸比外面的大一些，內餡足、湯汁多，皮蠻薄的，不建議外帶（內用與外帶口感差異頗大）
# 每次經過了這裏，都想找時間來吃看看這裏的平價丼飯 以及很多特色的大碗肉多多丼飯，這裏的價格非常的親民，一份不到2百元的套餐，除了主食還提供了幫助你消化的果醋，甜點豆花，還有無限暢飲的麥茶，熱湯等等覺得吃的不過癮，這裏也有其他單點的餐品客可供選擇。而且這裏的用餐空間雖然不大，但提供的座位都還蠻舒適的，假日來用餐都是坐無虛席，建議選擇平日用餐才不會等太久喔。另外這裏也提供外帶和food外送! 喜歡日式平價餐點的人可以來試試。