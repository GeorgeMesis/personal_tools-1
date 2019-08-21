import re
import requests
def getHTMLText(url):
    try:
        kv = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE','cookie':'thw=cn; tracknick=%5Cu9A84%5Cu50B2%5Cu4F60%5Cu662F%5Cu732A; lgc=%5Cu9A84%5Cu50B2%5Cu4F60%5Cu662F%5Cu732A; tg=0; enc=J3UIu%2BvdqbulFUMg1IQQGClJgKaPXOCaX%2FZiq%2F1OhmquQA9et%2BfoklDAcgDWjFKMtCMz6JjJrBypR03RSoG8aw%3D%3D; __guid=154677242.1068028679480357600.1541823694750.0984; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; UM_distinctid=167014a1b0c2a8-0fa1c951b73263-3c604504-1fa400-167014a1b0d3d0; miid=48670442091275730; t=609874792120ecc5482f52ebe24c9ff1; cna=8ZykFCSzfGICAXdW61L2ER4F; v=0; cookie2=3b6eaf4e692349fa0c856c0f35009d36; _tb_token_=e77b686fbdb36; alitrackid=www.taobao.com; swfstore=10456; unb=2977420000; sg=%E7%8C%AA02; _l_g_=Ug%3D%3D; skt=ccc8b880ba32a024; cookie1=BxSt%2FxlLcxvPoZ3NoHfLCY9hX7ub2SlLtUaqwE3Hb2w%3D; csg=892eccf2; uc3=vt3=F8dByRIu7cUe6VLghaI%3D&id2=UUGlSWS47N8T4Q%3D%3D&nk2=3ujrKzmXjow29A%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTU0NjY5NDUxMA%3D%3D; _cc_=UtASsssmfA%3D%3D; dnk=%5Cu9A84%5Cu50B2%5Cu4F60%5Cu662F%5Cu732A; _nk_=%5Cu9A84%5Cu50B2%5Cu4F60%5Cu662F%5Cu732A; cookie17=UUGlSWS47N8T4Q%3D%3D; mt=ci=13_1; _uab_collina=154669616853847360029803; x5sec=7b227365617263686170703b32223a2265353763343363333636666665306462353735333333363031353963643333614350507277754546454a53772b72797471662b716e514561444449354e7a63304d6a41774d4441374d513d3d227d; lastalitrackid=i.taobao.com; uc1=cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=WqG3DMC9Fb5mPLIQo9kR&cookie15=V32FPkk%2Fw0dUvg%3D%3D&existShop=false&pas=0&cookie14=UoTYMD22GDuSkw%3D%3D&tag=8&lng=zh_CN; JSESSIONID=B2B32949C5DEE03BD765C4CA83BF9897; monitor_count=15; whl=-1%260%260%261546697164904; l=aBCvANE5yHa0dHCXzMaiiXqP51MtQkBPiTJW1MaL-TwfDZITZ2r99jno-VwW2_qC55Ly_K-5F; isg=BMrKo7qIojXJYi60KpuKXIuSG7Ab7asZ_b7bPFQDdp2oB2rBPEueJRB3EzN-98at'}
        r = requests.get(url,timeout=30,headers=kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def parsePage(ilt,html):
     try:
         plt = re.findall(r'"view_price":"[\d.]*"',html)#原生字符串不转义
         tlt = re.findall(r'"raw_title":".*?"',html)
         
         for i in range(len(plt)):
             price = eval(plt[i].split(':')[1])
             title = eval(tlt[i].split(':')[1])
             ilt.append([price,title])
             
     except:
        print("1111")
def printGoodsList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号","价格","商品名称"))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count,g[0],g[1]))
 
def main():
    print('输入所需查找的物品名称：\r')
    goods = input()
    depth = 2
    start_url = 'https://s.taobao.com/search?q='+goods
    infoList = []
    for i in range(depth):
        try:
            if i==0:
                url = start_url
            else:
                url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue

    printGoodsList(infoList)
    
main()
