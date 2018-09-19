import base64

import requests
# from util.time_13bit import time_13bit
import json
import os
import time
import re
from lxml import etree
import execjs
from selenium import webdriver
import time

class Soufang_Cs:
    def __init__(self):
        self.n = 5
    def img(self):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; agent_sofang_session=e2f4fc14b3a003bb838f82e5b9f957e399bb8dbf; cityid=eyJpdiI6IlZVaHdEUXFJdlwveWh4enpjVEx1cytnPT0iLCJ2YWx1ZSI6InY2aDZXZ3Z6S2Jxckdmd0pQUCs5dnc9PSIsIm1hYyI6ImU2M2JiNGM3MzBiZjlkMGU0MGE4ZWMzM2UwNGVhYjJmYmEwNzliNmRlNDE4ODA5YWZiMjEwYjBmMjMzMjFjZDgifQ%3D%3D; city=eyJpdiI6Inc2XC9scGxTdkhxMndjZG9JWVJjSDl3PT0iLCJ2YWx1ZSI6IndoK0E2bk9GbVwvNnFmeEExN002a2JzY1c4bWVkUyt2UkpDdSttV29wbUNscDNxdldqbnFrRWdFSUhwNVhLUnArRUZ3NG1EWnNUR0UwUHJjK1dsUWJQQitLY2QyaStnSU4yXC84T1JiNUdwVmVjVHoxcjRpWEswcTIxbGlHd0xYSDEzVFI5XC84YTJaVm1raDd5Vjh2VnBVZ2U1RmtHZzZ1cHVZYkZCbTNOb2xSUDlIMzNTcm9PeStTZE1FMURkS0Y2aDBBSXZHRjNueDRBZ0s3d1J2UVo0b2I5TmNQS01kM29MNVJ3OExWVDBXbDRVRjZsRnNlWlwvZ3ZlUXdNSkQwZVV5S3FGYkFERklTeVpOZVNwYm13bkcxMjFHaEFnb1pFUDFMNk85b0tlWVc0OD0iLCJtYWMiOiJlMGUwN2IyMDAxODBmNTUzZmE2Yjk2NmQ0MDcxNzIzMjkzN2VhNmUwODgwNzdkMWU3MDA0NDBmNWIxMWRhYTFkIn0%3D; citypy=eyJpdiI6InBDNWlKcVAySnlqc1NCdENSXC8xSFBRPT0iLCJ2YWx1ZSI6Imh6cWlvbkQ3TE9vSnJHdjE0ZVJcL1RBPT0iLCJtYWMiOiIxYzVkMzUwNmE5M2VjY2IzMDQ4YTViNjNlNjdjZTUwNmJkNzFjNWE2YTliMDE5YzU4MmIzNjdiZGI0MTQ3NDFlIn0%3D; XSRF-TOKEN=eyJpdiI6ImdUOVc5alBuSGtuUW1Dc2hHVFJNZkE9PSIsInZhbHVlIjoiNkxRR01oZXoyQ3VoQmVIYTc5a1o5VXdiTHBJQmpycEVqU0hXQjBVa1pTUFN0QVRjcm5CVkt3VFFZdE9SZG9iR2VBUkR5V2F6V1wvTnh1VnFTXC9HeUZrdz09IiwibWFjIjoiMDA1OWViZjBlYjMyOTc2YzNkYTE4MGVmMGZiMGI1YjIzN2QwZDUzMGMwNmZhMDE2ZWI5MTg1ZDMyMmE0MDM4YSJ9'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldsale/house',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        img_list = []
        files_name = [r'C:\Users\Admin\Pictures\Saved Pictures\text1.jpg',r'C:\Users\Admin\Pictures\Saved Pictures\text.jpg']
        for img in files_name:
            files = {'attachment_file': ('timg.jpg', open(img, 'rb'), 'image/jpeg')}
            self.res = requests.post('http://agent.sofang.com/upload/addphoto?imageType=houseSale',headers=headers_1,files=files).content.decode()
            image = {"img":self.res,"note":"","type":"10"}
            img_list.append(image)
        self.image = str(img_list).replace("'",'"')
        print(self.image)
        return self.res
    def biaoti_img(self):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; agent_sofang_session=e2f4fc14b3a003bb838f82e5b9f957e399bb8dbf; cityid=eyJpdiI6IlZVaHdEUXFJdlwveWh4enpjVEx1cytnPT0iLCJ2YWx1ZSI6InY2aDZXZ3Z6S2Jxckdmd0pQUCs5dnc9PSIsIm1hYyI6ImU2M2JiNGM3MzBiZjlkMGU0MGE4ZWMzM2UwNGVhYjJmYmEwNzliNmRlNDE4ODA5YWZiMjEwYjBmMjMzMjFjZDgifQ%3D%3D; city=eyJpdiI6Inc2XC9scGxTdkhxMndjZG9JWVJjSDl3PT0iLCJ2YWx1ZSI6IndoK0E2bk9GbVwvNnFmeEExN002a2JzY1c4bWVkUyt2UkpDdSttV29wbUNscDNxdldqbnFrRWdFSUhwNVhLUnArRUZ3NG1EWnNUR0UwUHJjK1dsUWJQQitLY2QyaStnSU4yXC84T1JiNUdwVmVjVHoxcjRpWEswcTIxbGlHd0xYSDEzVFI5XC84YTJaVm1raDd5Vjh2VnBVZ2U1RmtHZzZ1cHVZYkZCbTNOb2xSUDlIMzNTcm9PeStTZE1FMURkS0Y2aDBBSXZHRjNueDRBZ0s3d1J2UVo0b2I5TmNQS01kM29MNVJ3OExWVDBXbDRVRjZsRnNlWlwvZ3ZlUXdNSkQwZVV5S3FGYkFERklTeVpOZVNwYm13bkcxMjFHaEFnb1pFUDFMNk85b0tlWVc0OD0iLCJtYWMiOiJlMGUwN2IyMDAxODBmNTUzZmE2Yjk2NmQ0MDcxNzIzMjkzN2VhNmUwODgwNzdkMWU3MDA0NDBmNWIxMWRhYTFkIn0%3D; citypy=eyJpdiI6InBDNWlKcVAySnlqc1NCdENSXC8xSFBRPT0iLCJ2YWx1ZSI6Imh6cWlvbkQ3TE9vSnJHdjE0ZVJcL1RBPT0iLCJtYWMiOiIxYzVkMzUwNmE5M2VjY2IzMDQ4YTViNjNlNjdjZTUwNmJkNzFjNWE2YTliMDE5YzU4MmIzNjdiZGI0MTQ3NDFlIn0%3D; XSRF-TOKEN=eyJpdiI6ImdUOVc5alBuSGtuUW1Dc2hHVFJNZkE9PSIsInZhbHVlIjoiNkxRR01oZXoyQ3VoQmVIYTc5a1o5VXdiTHBJQmpycEVqU0hXQjBVa1pTUFN0QVRjcm5CVkt3VFFZdE9SZG9iR2VBUkR5V2F6V1wvTnh1VnFTXC9HeUZrdz09IiwibWFjIjoiMDA1OWViZjBlYjMyOTc2YzNkYTE4MGVmMGZiMGI1YjIzN2QwZDUzMGMwNmZhMDE2ZWI5MTg1ZDMyMmE0MDM4YSJ9'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldsale/house',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        data_1 = {
                     'path':self.res
        }

        response = requests.post('http://agent.sofang.com/upload/addphoto?imageType=houseSale&title=1',headers=headers_1,data=data_1).content.decode()
        image = {"img":response,"type":"9","note":"","tag":"2"}
        img_list=[image]
        self.image1 = str(img_list).replace("'",'"')
        print(self.image1)

    def roomStr(self, item):
        self.roomStr = item["shi"] + '_' + item["ting"] + '_' + item["wei"] + '_' + item["chufang"]
        return self.roomStr

    def put(self, ):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; agent_sofang_session=e2f4fc14b3a003bb838f82e5b9f957e399bb8dbf; cityid=eyJpdiI6IlZVaHdEUXFJdlwveWh4enpjVEx1cytnPT0iLCJ2YWx1ZSI6InY2aDZXZ3Z6S2Jxckdmd0pQUCs5dnc9PSIsIm1hYyI6ImU2M2JiNGM3MzBiZjlkMGU0MGE4ZWMzM2UwNGVhYjJmYmEwNzliNmRlNDE4ODA5YWZiMjEwYjBmMjMzMjFjZDgifQ%3D%3D; city=eyJpdiI6Inc2XC9scGxTdkhxMndjZG9JWVJjSDl3PT0iLCJ2YWx1ZSI6IndoK0E2bk9GbVwvNnFmeEExN002a2JzY1c4bWVkUyt2UkpDdSttV29wbUNscDNxdldqbnFrRWdFSUhwNVhLUnArRUZ3NG1EWnNUR0UwUHJjK1dsUWJQQitLY2QyaStnSU4yXC84T1JiNUdwVmVjVHoxcjRpWEswcTIxbGlHd0xYSDEzVFI5XC84YTJaVm1raDd5Vjh2VnBVZ2U1RmtHZzZ1cHVZYkZCbTNOb2xSUDlIMzNTcm9PeStTZE1FMURkS0Y2aDBBSXZHRjNueDRBZ0s3d1J2UVo0b2I5TmNQS01kM29MNVJ3OExWVDBXbDRVRjZsRnNlWlwvZ3ZlUXdNSkQwZVV5S3FGYkFERklTeVpOZVNwYm13bkcxMjFHaEFnb1pFUDFMNk85b0tlWVc0OD0iLCJtYWMiOiJlMGUwN2IyMDAxODBmNTUzZmE2Yjk2NmQ0MDcxNzIzMjkzN2VhNmUwODgwNzdkMWU3MDA0NDBmNWIxMWRhYTFkIn0%3D; citypy=eyJpdiI6InBDNWlKcVAySnlqc1NCdENSXC8xSFBRPT0iLCJ2YWx1ZSI6Imh6cWlvbkQ3TE9vSnJHdjE0ZVJcL1RBPT0iLCJtYWMiOiIxYzVkMzUwNmE5M2VjY2IzMDQ4YTViNjNlNjdjZTUwNmJkNzFjNWE2YTliMDE5YzU4MmIzNjdiZGI0MTQ3NDFlIn0%3D; XSRF-TOKEN=eyJpdiI6ImdUOVc5alBuSGtuUW1Dc2hHVFJNZkE9PSIsInZhbHVlIjoiNkxRR01oZXoyQ3VoQmVIYTc5a1o5VXdiTHBJQmpycEVqU0hXQjBVa1pTUFN0QVRjcm5CVkt3VFFZdE9SZG9iR2VBUkR5V2F6V1wvTnh1VnFTXC9HeUZrdz09IiwibWFjIjoiMDA1OWViZjBlYjMyOTc2YzNkYTE4MGVmMGZiMGI1YjIzN2QwZDUzMGMwNmZhMDE2ZWI5MTg1ZDMyMmE0MDM4YSJ9'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldrent/house',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        data = {
            '_token': item["token"],                                #token
            'houseType1': item["houseType1"],                       #房屋类型（houseType1）
            'rentType': item["rentType"],                           #出租类型（rentType）
            'cityId': item["cityId"],                               #市(cityId)
            'cityareaId': item["cityareaId"],                       #区(cityareaId)
            'name': item["name"],                                   #小区(name)
            'communityId': item["communityId"],                     # 小区id（communityId）
            'address': item["address"],                             #地址(address)
            'fitment': item["fitment"],                             #装修状况（fitment）
            'roomStr': self.roomStr ,                               #室厅卫厨(roomStr)
            "price": item["price"],                                 #出租价格 (price)
            'priceUnit': item["priceUnit"],                         #价格单位（priceUnit）
            'paymentType': item["paymentType"],                     #付款类型（paymentType）
            "area": item["area"],                                   #面积(area)
            "currentFloor": item["currentFloor"],                   #楼层(currentFloor)
            "totalFloor": item["totalFloor"],                       #总楼层(totalFloor)
            # 'houseType2': item["houseType2"],                       #物业类型(houseType2)
            'faceTo': item["faceTo"],                               #房屋朝向（faceTo）
            "title": item["title"],                                 #标题(title)
            'describe': item["describe"],                           #描述(describe)
            'indoor':self.image,                                    #室内图（indoor）
            'titleimg':self.image1,                                 #标题图（titleimg）
            "linkman": item["linkman"],                             #联系人(linkman)
            "linkmobile": item["linkmobile"]                        #电话(linkmobile)
        }
        print(data)
        print("*" * 80)
        res = requests.post('http://agent.sofang.com/submitrent', headers=headers_1, data=data).content.decode()
        print(res)
        msg_list = re.findall('''"result":(.*?),"message":"(.*?)"''', res)[0]
        if 'false' in msg_list:
            print(msg_list[1])
        else:
            print('待发布成功')
            self.id = re.findall('"message":"rent-(.*?)"', res)[0]
            print(self.id)

    def chuzu_fabu(self):
        cookie = 'uniqueName=904fef156334c3a26e3f72e2a199d3dd; UM_distinctid=165833588ca580-09fc49592708fd-47e1039-1fa400-165833588cb78c; agent_sofang_session=e2f4fc14b3a003bb838f82e5b9f957e399bb8dbf; cityid=eyJpdiI6IlZVaHdEUXFJdlwveWh4enpjVEx1cytnPT0iLCJ2YWx1ZSI6InY2aDZXZ3Z6S2Jxckdmd0pQUCs5dnc9PSIsIm1hYyI6ImU2M2JiNGM3MzBiZjlkMGU0MGE4ZWMzM2UwNGVhYjJmYmEwNzliNmRlNDE4ODA5YWZiMjEwYjBmMjMzMjFjZDgifQ%3D%3D; city=eyJpdiI6Inc2XC9scGxTdkhxMndjZG9JWVJjSDl3PT0iLCJ2YWx1ZSI6IndoK0E2bk9GbVwvNnFmeEExN002a2JzY1c4bWVkUyt2UkpDdSttV29wbUNscDNxdldqbnFrRWdFSUhwNVhLUnArRUZ3NG1EWnNUR0UwUHJjK1dsUWJQQitLY2QyaStnSU4yXC84T1JiNUdwVmVjVHoxcjRpWEswcTIxbGlHd0xYSDEzVFI5XC84YTJaVm1raDd5Vjh2VnBVZ2U1RmtHZzZ1cHVZYkZCbTNOb2xSUDlIMzNTcm9PeStTZE1FMURkS0Y2aDBBSXZHRjNueDRBZ0s3d1J2UVo0b2I5TmNQS01kM29MNVJ3OExWVDBXbDRVRjZsRnNlWlwvZ3ZlUXdNSkQwZVV5S3FGYkFERklTeVpOZVNwYm13bkcxMjFHaEFnb1pFUDFMNk85b0tlWVc0OD0iLCJtYWMiOiJlMGUwN2IyMDAxODBmNTUzZmE2Yjk2NmQ0MDcxNzIzMjkzN2VhNmUwODgwNzdkMWU3MDA0NDBmNWIxMWRhYTFkIn0%3D; citypy=eyJpdiI6InBDNWlKcVAySnlqc1NCdENSXC8xSFBRPT0iLCJ2YWx1ZSI6Imh6cWlvbkQ3TE9vSnJHdjE0ZVJcL1RBPT0iLCJtYWMiOiIxYzVkMzUwNmE5M2VjY2IzMDQ4YTViNjNlNjdjZTUwNmJkNzFjNWE2YTliMDE5YzU4MmIzNjdiZGI0MTQ3NDFlIn0%3D; XSRF-TOKEN=eyJpdiI6IlB3M3JqcGxudGFta3lYb21IMnEyZnc9PSIsInZhbHVlIjoiVVhudU1mbGdlK2txbkRRN2N3aHRURjZQeVdCWVpZZXluZHpZRUF3VUdsTDBxeDVhcVNUQ1VjRWQ2VWlNcmVpOTQ3UWh3RVkraFFNbTBzUHhrY2NyXC9nPT0iLCJtYWMiOiIxZTU1NjIxZTFkMzc1N2MxNzIxN2I0Yzc1OWMyZTZhOWZkNWU0ZWQxODhhNWRkYWM3YTEzMmI2YWYzMmViNDI5In0%3D'
        headers_1 = {
            'host': 'agent.sofang.com',
            'Referer': 'http://agent.sofang.com/oldrentmanage/shops/releaseed',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie': cookie,

        }
        data_1 = {
            'id': self.id
        }
        url = 'http://agent.sofang.com/statusrent/release?id={}'.format(self.id)
        response = requests.get(url, headers=headers_1, data=data_1).content.decode()
        print(response)
        if response == "1":
            print("正式发布成功")
        elif response == "5":
            print("您当天免费发布套数已用完！")
        else:
            print("正式发布失败")
item={
'token': 'fclJwFfxdWQbWAuQE3b08xdYjePJMsvpQJr5JjzW' ,       # 在house?rentType=1里面
"rentType":"1",                                             #（1整租2合租。这里把1写死，合租暂时不涉及）
'houseType1': '3',                                          #(3住宅2写字楼1商铺)
"cityId":"332","cityareaId":"2985",
"price":'3456',"priceUnit":"1",                             #（1住宅2商铺写字楼）
"area":'123',"paymentType":"1",                            #(1押一付一)
"name":'月亮湾浦发广场',"address":'普陀中山北路1655弄10支弄','communityId': 306030,
"fitment":'3',                                            #（1毛坯2简装3中装修4精装修5豪华装修）
"shi":"3",
"ting":"2",
"wei":"1",
"chufang":"1",
"faceTo":"1" ,                                              #（1东2南3西4北5南北6东南7西南8东北9西北10东西）
"currentFloor":"4","totalFloor":"25",
# "houseType2":"101" ,                                        #(302经济适用房303商住楼304别墅305豪宅306平房307四合院，301住在201写字楼101商铺)
"title":"haha你据斤上taS=N较斤f市计较斤斤计较",
"describe":"水水水水水水d水时间还哈工水哦拉卡拉的手机发水水法的实施",
"linkman":"鱼","linkmobile":"15629185662",
}
if __name__ == '__main__':
    soufang = Soufang_Cs()
    soufang.img()
    soufang.biaoti_img()
    soufang.roomStr(item)
    soufang.put()
    time.sleep(5)#这里必须有等待时间，不然成功率不高
    soufang.chuzu_fabu()


# 1 发布数量没有限制，但是title相同的不能重复发，
# 2 信息有预发布和已发布两个步骤
# 3 不同账号改token和cookie值
# 4 住宅商铺写字楼只用换2个字段（houseType1，priceUnit）
# 5 除了市（cityId）区（cityareaId）其他字段可随便填