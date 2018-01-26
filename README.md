# tideking-
下面是车次信息网站
  url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018'
如  ：网页上 @bjb|北京北|VAP|beijingbei|bjb|0@bjd|北京东|BOP|beijingdong|bjd|1     编译器上：u'\u961c\u5357': u'FNH'
将上列信息转换为字典 如｛北京北：bjb,北京东：bjd.....｝
# 法1： 用re正则选出站名和大写编码               |                # 法2：根据信息分割提取
 pattern = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'     |                   data = r.text     ;      data = data.split('@')
 result = re.findall(pattern, r.text)          |                   sta = {}   for i in data: 
 station = dict(result)                        |                                 if '|' in i:
                                               |                                      i = i.split('|')  ;  sta[i[1]] = i[2]
结果字典：sta={u'\u961c\u5357': u'FNH', u'\u4e09\u660e\u5317': u'SHS', u'\u9ed1\u6c34': u'HOT'........}
将station.py输入命令行：station.py>sta.py
