# import pandas as pd
# import re
# from ckipnlp.pipeline import CkipPipeline, CkipDocument

# stop_pos = ['COLONCATEGORY','COMMACATEGORY','DASHCATEGORY','DOTCATEGORY','ETCCATEGORY','EXCLAMATIONCATEGORY','PARENTHESISCATEGORY','PAUSECATEGORY','PERIODCATEGORY','QUESTIONCATEGORY','SEMICOLONCATEGORY','SPCHANGECATEGORY','FW']
# text = "◾花生餅（$15）：餅皮帶著淡淡的麵粉香，口感上比較紮實，花生口味的內陷讓人驚艷，花生很濃郁，可以微微吃到沙沙的口感，也因為餅皮比較紮實，讓整體的甜度中和了不少，整體來說滿推薦的！是路過可以買的小點心，吃了會心情很好🤩🫶(蔥花)，原本以為是青蔥，結果不是，是油蔥，一點點鹹味也不錯吃。是一家難得的超值饅頭店！必買！"

# pipeline = CkipPipeline()
# doc = CkipDocument(raw=text)
# pipeline.get_ws(doc)
# pipeline.get_pos(doc)



# ws = doc.ws.to_text()[0].split('\u3000')
# pos = doc.pos.to_text()[0].split('\u3000')

# xxxxxx = doc.ws[0].to_text()
# print(xxxxxx)
# print(type(xxxxxx))

# # for i,j in zip(ws,pos):
# #   print('('+i,j+')',end='')
# # print('')

# for x in range(len(pos)-1,-1,-1):
#   if pos[x] in stop_pos :
#     # print(ws.pop(x),end = ' ')
#     # print(pos.pop(x))
#     ws.pop(x)
#     pos.pop(x)


# # for i,j in zip(ws,pos):
# #   print('('+i,j+')',end='')
# # print('')

# clearnws = ''
# clearnpos = ''
# for i,j in zip(ws,pos):
#   clearnws = clearnws + '\u3000' + i
#   # clearnpos.append(j)

import pandas as pd
import re
from ckipnlp.pipeline import CkipPipeline, CkipDocument

datanum = 1
pipeline = CkipPipeline()
pattern = r'\bDfa\s+VK|D\s+VC|VH|VHC|VI\b'
rows = pd.read_csv(r'D:\vscode\python\reviews_rating\CSV\訓練集\data45.csv')
stop_pos = ['COLONCATEGORY','COMMACATEGORY','DASHCATEGORY','DOTCATEGORY','ETCCATEGORY','EXCLAMATIONCATEGORY','PARENTHESISCATEGORY','PAUSECATEGORY','PERIODCATEGORY','QUESTIONCATEGORY','SEMICOLONCATEGORY','SPCHANGECATEGORY','FW']

for index, row in rows.iterrows():
    review = row['Reviews']
    doc = CkipDocument(raw=review)
    pipeline.get_ws(doc)
    pipeline.get_pos(doc)

    # 預處理
    ws = doc.ws.to_text()[0].split('\u3000')
    pos = doc.pos.to_text()[0].split('\u3000')
    clearnws = ''
    clearnpos = ''
    for x in range(len(pos)-1,-1,-1):
      if pos[x] in stop_pos :
        ws.pop(x)
        pos.pop(x)
    for i,j in zip(ws,pos):
      clearnws = clearnws + '\u3000' + i
      clearnpos = clearnpos + '\u3000' + j
    clearnws = clearnws[1:]
    clearnpos = clearnpos[1:]
    
    #算字數
    chinese_chars = re.findall(u"[\u4e00-\u9fff]", clearnws)
    chars = len(chinese_chars)

    #算形容次數
    matches = re.findall(pattern, clearnpos)
    count = len(matches)

    if chars >= 24:
        if count <= 8:
            chat_score = count * 1
        elif count > 8:
            chat_score = 8 * 1
    elif chars < 24:
        if count <= 8:
            chat_score = count * 0.8     
    total = chat_score

    nws = clearnws.replace('\u3000', '|')
    rows.loc[index,['ckipnlp','score']] = [nws,total]
    datanum+=1

    if datanum%100 == 0:
        print("已分析{}筆".format(datanum))
rows.to_csv(r"D:\vscode\python\reviews_rating\CSV\訓練集\data45.csv", index=False)
print("處理了{}筆資料".format(datanum-1))
