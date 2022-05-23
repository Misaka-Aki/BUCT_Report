import json
import requests
import urllib3
import os

url = "https://eai.buct.edu.cn/ncov/wap/default/save"
users = [
    {
        'cookies': {
            'eai-sess': os.environ['EAI'],
            'UUkey': os.environ['UUKEY']
        }
    }
]

def auto_report(user):
    urllib3.disable_warnings()
    # init
    s = requests.session()
    headers = {}
    data = {
        'sfzx': '1',  # 是否在校
        'sfzgn': '1',  # 所在地点中国大陆
        'zgfxdp': '0',  # 不在中高风险地区
        'jcjgqr': '0',  # 正常，非疑似/确诊
        'sfcxtz': '0',  # 没有出现发热、乏力、干咳、呼吸困难等症状
        'sfjcbh': '0',  # 今日是否接触无症状感染/疑似/确诊人群
        'mjry': '0',  # 今日是否接触密接人员
        'csmjry': '0',  # 近14日内本人/共同居住者是否去过疫情发生场所
        'sfcyglq': '0',  # 是否处于观察期
        'szsqsfybl': '0',  # 所在社区是否有确诊病例
        'sfcxzysx': '0',  # 是否有任何与疫情相关的， 值得注意的情况
        'tw': '1',  # 体温范围（下标从 1 开始），此处是36 - 36.5
        'area': '北京市 朝阳区',  # 所在区域
        'province': '北京市',  # 所在省
        'city': '北京市',  # 所在市
        'address': '北京市朝阳区北三环东路15号北京化工大学',  # 地址
        # 'sfcyglq': '0',  # 是否处于隔离期
        # 'sfyzz': '0',  # 是否有症状
        # 'askforleave': '0',  # 是否请假外出
        'qksm': '',  # 其他情况
        'geo_api_info': {
            'type': 'complete',
            'info': 'SUCCESS',
            'status': 1,
            'Eia': 'jsonp_913580_',
            'position': {
                'O': 113.0270592,  # 经度
                'P': 22.5524345,  # 纬度
                'lng': 113.0270592,  # 经度
                'lat': 22.5524345  # 纬度
            },
            'message': 'Get+ipLocation+success.Get+address+success.',
            'location_type': 'ip',
            'accuracy': None,
            'isConverted': True,
            'addressComponent': {
                'citycode': '',
                'adcode': '',  # 行政区划代码
                'businessAreas': [],
                'neighborhoodType': '',
                'neighborhood': '',
                'building': '',
                'buildingType': '',
                'street': '',
                'streetNumber': '',
                'province': '',  # 所在省
                'city': '',  # 所在市
                'district': '',  # 所在区
                'township': ''  # 所在街道
            },
            'formattedAddress': '',  # 拼接后的地址
            'roads': [],
            'crosses': [],
            'pois': []
        },
    }

    result = s.post(url, data=data, headers=headers,
                    cookies=user['cookies'], verify=False)
    print(json.loads(result.text)['m'])
    from onepush import notify
    notify('pushplus', token=os.environ['KEY'], title='OnePush', content=json.loads(result.text)['m'])

if __name__ == '__main__':
    for item in users:
        auto_report(item)
    
