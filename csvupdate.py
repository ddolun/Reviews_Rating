import pandas as pd
import re
from ckipnlp.pipeline import CkipPipeline, CkipDocument

i = 1
pipeline = CkipPipeline()
pattern = r'\bDfa\s+VK|D\s+VC|VH|VHC|VI\b'
rows = pd.read_csv('new_data.csv')

for index, row in rows.iterrows():
    review = row['Reviews']
    doc = CkipDocument(raw=review)
    pipeline.get_ws(doc)
    pipeline.get_pos(doc)
    
    chinese_chars = re.findall(u"[\u4e00-\u9fff]", doc.ws[0].to_text())
    chars = len(chinese_chars)
    # print("{}字".format(chars))

    matches = re.findall(pattern, doc.pos[0].to_text())
    count = len(matches)
    # print("有{}個形容詞".format(count))

    if chars >= 24:
        if count <= 8:
            chat_score = count * 1
        elif count > 8:
            chat_score = 8 * 1
    elif chars < 24:
        if count <= 8:
            chat_score = count * 0.8     
    # print("文字分數為{}".format(chat_score))

    total = chat_score
    # print("總分數為{}".format(total))

    nws =''
    for word in doc.ws[0]:
        nws = nws +'|'+ word
    nws = nws[1:]

    rows.loc[index,['ckipnlp','score']] = [nws,total]
    i+=1
    if i%10 == 0:
        print("已分析{}筆".format(i))
# rows.to_csv("new_data.csv", index=False)
print("處理了{}筆資料".format(i-1))