import random
import time
from datetime import datetime


import pymysql
#pymysql.install_as_MySQLdb()
from pymysql.converters import escape_string

Flight_Company = ["中国东方航空公司", "中国国际航空公司", "海南航空", "深圳航空", "厦门航空", "四川航空", "山东航空", "上海航空", "天津航空", "春秋航空"]

Place = ["广州", "武汉", "南京", "西安", "沈阳", "成都", "重庆", "郑州", "苏州", "青岛", "合肥", "长春", "杭州", "宁波", "太原", "无锡",
         "济南", "长沙", "哈尔滨", "乌鲁木齐", "南昌", "南宁", "大连", "福州", "昆明", "石家庄", "贵阳", "兰州", "海口", "呼和浩特", "银川",
         "西宁", "拉萨"]

Passenger = ["passenger", "flight", "airport"]

Infect = ["N", "Y", "NY"]

Person = ["admin", "airport", "passenger", "flight"]

Task = ["security", "cleaning", "check-in"]

Flight_Type = ["pilot", "service"]

RandNum = [1, -1]

FlightIDNum = ["CA1302", "CZ1547", "MU1021", "HU1420", "ZH1012", "FM2147", "MF1478", "SC3214", "3U1454", "9C4124"]

def produce_time():
    a1 = (2021, 1, 1, 0, 0, 0, 0, 0, 0)  # 设置开始日期时间元组（2021-01-01 00：00：00）
    a2 = (2021, 12, 31, 23, 59, 59, 0, 0, 0)  # 设置结束日期时间元组（2021-12-31 23：59：59）

    start = time.mktime(a1)  # 生成开始时间戳
    end = time.mktime(a2)  # 生成结束时间戳

    # 随机生成10个日期字符串
    for i in range(10):
        t = random.randint(start, end)  # 在开始和结束时间戳中随机取出一个
        date_touple = time.localtime(t)  # 将时间戳生成时间元组
        date = time.strftime("%Y-%m-%d %H:%M", date_touple)  # 将时间元组转成格式化字符串
    return date


def produce_endTime(startTime):
    import datetime
    startTime = datetime.datetime.strptime(startTime, "%Y-%m-%d %H:%M")
    endTime = (startTime + datetime.timedelta(minutes=random.randint(1, 59))).strftime("%Y-%m-%d %H:%M")
    endTime = datetime.datetime.strptime(endTime, "%Y-%m-%d %H:%M")
    endTime = (endTime + datetime.timedelta(hours=random.randint(0, 4))).strftime("%Y-%m-%d %H:%M")
    return endTime


def produce_name():
    a1 = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
           '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦', '章',
           '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁', '柳',
           '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安', '常',
           '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧', '尹',
           '姚', '邵', '湛', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明']
    a2 = ['壮', '昱杰', '开虎', '叶行', '家越', '煜文', '家惟', '龄之', '俊有', '啸威', '浩一', '向红', '军', '建荣', '紫威', '彬', '作为',
          '博轩', '爵', '榕轩', '韦聿', '仁腾', '诏涣', '勇宁', '东阁', '泰寰', '春军', '翼帆', '诏炀', '培帆', '又淇', '谦韵', '子柏',
          '永慧', '仲泉', '恒一', '恒源', '凯', '大奇', '兴宁', '笑野', '浩峰', '宪', '伟平', '彦博', '树魏', '坚武', '梓华', '啸吟', '华繁',
          '啸宇', '健奇', '艺臣', '一同', '疾风', '伟洪', '镜敏', '政浩', '子旭', '玉轩', '子林', '延赤', '禾', '环球', '亚韬', '昊俊', '嘉汶',
          '纯德', '天宇', '盛世', '华山', '兆临', '泽光', '栗', '樯', '一辉', '闻博', '国洋', '毅杰', '建可', '惠山', '谦之', '连喜', '溪俨',
          '学江', '树鹏', '鹏', '天友', '庆宇', '本凤', '少涛', '键程', '厚霖', '泽一', '清嵘', '车亦', '新民', '志东', '剑清', '海霖', '一溪',
          '融渝', '玺剑', '超宇', '永润', '人月', '炳荣', '冰博', '季栋', '仁赫', '兰斌', '嘉伟', '军军', '鄂', '思华', '建青', '兴华', '冀川',
          '赞平', '佳汛', '万鹏', '飞平', '树隶', '子桁', '志忠', '柯茗', '佛晓', '之帆', '晟尔', '守均', '茁壮', '梁宇', '博洪', '亚军', '翼成',
          '胜轩', '子皿', '记博', '博玉', '继优', '翰琨', '均培', '敦强', '浩羽', '先登', '明津', '潇添', '燃', '章见', '本三', '仁甫', '小磊', '文福',
          '鹏云', '成虎', '家正', '来麟', '树木', '超勇', '榀荃', '博涛', '炳越', '宝全', '浩然', '明华']
    name = random.choice(a1)+random.choice(a2)
    return name


def produce_username():
    name = produce_name()
    name = name + ''.join(random.sample('qwertyuiiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM', random.randint(2, 6)))
    name = name + ''.join(random.sample('0123456789', random.randint(2, 6)))
    return name


def produce_password():
    x = random.sample('abcdefghijklmnopqrstuvwxyz!@#$%^&*=', 8)
    temp = ""
    for i in x:
        temp += i
    return temp


def produce_email( emailType=None, rang=None):
    __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]
    # 如果没有指定邮箱类型，默认在 __emailtype中随机一个
    if emailType == None:
        __randomEmail = random.choice(__emailtype)
    else:
        __randomEmail = emailType
    # 如果没有指定邮箱长度，默认在4-10之间随机
    if rang == None:
        __rang = random.randint(4, 10)
    else:
        __rang = int(rang)
    __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
    _email = __randomNumber + __randomEmail
    return _email


def produce_phone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
               "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))


def produce_generator():
    import datetime
    # 身份证号的前两位，省份代号
    sheng = ('11', '12', '13', '14', '15', '21', '22', '23', '31', '32', '33', '34', '35', '36', '37', '41', '42', '43', '44', '45', '46', '50', '51', '52', '53', '54', '61', '62', '63', '64', '65', '66')

    # 随机选择距离今天在7000到25000的日期作为出生日期（没有特殊要求我就随便设置的，有特殊要求的此处可以完善下）
    birthdate = (datetime.datetime.today() - datetime.timedelta(random.randint(7000, 25000)))

    # 拼接出身份证号的前17位（第3-第6位为市和区的代码，中国太大此处就偷懒了写了定值，有要求的可以做个随机来完善下；第15-第17位为出生的顺序码，随机在100到199中选择）
    ident = sheng[random.randint(0, 31)] + '0101' + birthdate.strftime("%Y%m%d") + str(random.randint(100, 199))

    # 前17位每位需要乘上的系数，用字典表示，比如第一位需要乘上7，最后一位需要乘上2
    coe = {1: 7, 2: 9, 3: 10, 4: 5, 5: 8, 6: 4, 7: 2, 8: 1, 9: 6, 10: 3, 11:7, 12: 9, 13: 10, 14: 5, 15: 8, 16: 4, 17: 2}
    summation = 0

    # for循环计算前17位每位乘上系数之后的和
    for i in range(17):
        summation = summation + int(ident[i:i + 1]) * coe[i+1]#ident[i:i+1]使用的是python的切片获得每位数字

    # 前17位每位乘上系数之后的和除以11得到的余数对照表，比如余数是0，那第18位就是1
    key = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}

    # 拼接得到完整的18位身份证号
    return ident + key[summation % 11]


def produce_positon():
    Position = ["东", "南", "西", "北"]
    Direction = ["一", "二", "三", "四"]
    return ''.join(random.sample(Position, 1) + random.sample(Direction, 1))


class Item(object):
    Name = ""


class DataItem(Item):
    """
        数据项的的基类
    """
    Type = "Bool" # Bool Int Float 数据值类型
    Unit = "Unit" # 单位
    Range = { #  数据范围
        "Min": 0,
        "Max": 1
    }

    def get_value(self):
        if self.Type == "Bool":
            return True if random.randint(0, 1) == 0 else False
        elif self.Type == "Int":
            return random.randint(self.Range["Min"], self.Range["Max"])
        elif self.Type == "Float":
            return round(self.Range["Min"] + random.random() * (self.Range["Max"] - self.Range["Min"]),2)
        elif self.Type == "Char":
            return chr(random.randint(self.Range["Min"], self.Range["Max"]))
        elif self.Type == "Company":
            return Flight_Company[random.randint(self.Range["Min"], self.Range["Max"])]
        elif self.Type == "Time":
            return produce_time()
        elif self.Type == "Passenger":
            return Passenger[random.randint(self.Range["Min"], self.Range["Max"])]
        elif self.Type == "Name":
            return produce_name()
        elif self.Type == "Position":
            return produce_positon()
        elif self.Type == "Place":
            return Place[random.randint(self.Range["Min"], self.Range["Max"])]
        elif self.Type == "Infect":
            return Infect[random.randint(self.Range["Min"], self.Range["Max"])]
        elif self.Type == 'Password':
            return produce_password()
        elif self.Type == 'Email':
            return produce_email()
        elif self.Type == 'Phone':
            return produce_phone()
        elif self.Type == 'Card':
            return produce_generator()
        elif self.Type == 'FlightId':
            return FlightIDNum[random.randint(self.Range["Min"], self.Range["Max"])]
        elif self.Type == 'PersonType':
            return Person[random.randint(self.Range["Min"], self.Range["Max"])]
        elif self.Type == 'Avatar':
            return "avatar/" + "".join(random.sample('123456789', 1)) + ".jpg"
        elif self.Type == 'TaskType':
            return Task[random.randint(self.Range["Min"], self.Range["Max"])]
        elif self.Type == 'Flighttype':
            return Flight_Type[random.randint(self.Range["Min"], self.Range["Max"])]
        elif self.Type == 'UserName':
            return produce_username()


class Device(object):
    def __init__(self, id_: object, name: object) -> object:
        self.id_ = id_
        self.name = name

    def get_id(self):
        return self.id_

    def get_all_data(self):
        all_data = {}
        for data_type in self.get_data_type_list():
            data = data_type()
            all_data[data.Name] = data.get_value()
        return all_data

    def control(self, CMD_Type):
        if CMD_Type in self.get_contorl_type():
            print(self.name, CMD_Type.Command)

    def get_device_typename(self):
        return self.__class__.__name__

    def get_data_type_list(self):
        return []

    def get_contorl_type(self):
        return []

    def get_sql_format(self):
        return ""

    def get_sql_cmd(self, data):
        return ""

    def get_info(self):
        return {
            "id" : self.id_,
            "name": self.name,
            "data": self.get_all_data(),
        }


# 感染警示等级 alarm_level  感染风险等级 infect_level
class LevelItem(DataItem):
    Name = "level"
    Type = "Int"
    Unit = ""
    Range = {
        "Min": 1,
        "Max": 3
    }


# 感染风险预警编号 risk_id_id
class Risk_ID_Item(DataItem):
    Name = "Risk_ID"
    Type = "Char"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 10
    }


# 机场管理人员编号 staff_id_id
class Staff_ID_Item(DataItem):
    Name = "Staff_ID"
    Type = "Char"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 10000
    }


# 监测点编号 monitor_id_id
class Monitor_ID_Item(DataItem):
    Name = "Monitor_ID"
    Type = "Int"
    Unit = ""
    Range = {
        "Min": 1,
        "Max": 20
    }


# 飞机编号
class Flight_ID_Item(DataItem):
    Name = "flight_ID"
    Type = "FlightId"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 9
    }


# 飞机从属航空公司
class Flight_Company_Item(DataItem):
    Name = "Flight_Company"
    Type = "Company"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 8
    }


# 始发地
class Flight_Start_Place(DataItem):
    Name = "Flight_Start_Place"
    Type = "Place"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 32
    }


# 目的地
class Flight_End_Place(DataItem):
    Name = "Flight_End_Place"
    Type = "Place"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 32
    }


# 起飞时间
class Flight_Time(DataItem):
    Name = "Flight_Time"
    Type = "Time"
    Unit = ""
    Range = {
    }


# 机场人员管理编号
class Flight_People(DataItem):
    Name = "Flight_people"
    Type = "Int"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 1000000
    }


# 乘客类型 passenger_type  [旅客/机组人员]
class Passenger_Type(DataItem):
    Name = "Passenger_Type"
    Type = "Passenger"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 1
    }


# 乘客编号 passenger_id
class Passenger_Id(DataItem):
    Name = "Passenger_Id"
    Type = "Int"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 1000000
    }


# 乘客姓名 passenger_name
class Passenger_Name(DataItem):
    Name = "Passenger_Name"
    Type = "Name"
    Unit = ""
    Range = {
    }


# 乘客是否乘机 is_take
class Is_Take(DataItem):
    Name = "Is_take"
    Type = "Infect"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 1
    }


# 飞机座位号 seat
class SeatItem(DataItem):
    Name = "Seat"
    Type = "Int"
    Unit = ""
    Range = {
        "Min": 1,
        "Max": 100
    }


# 检测点位置 position
class PositionItem(DataItem):
    Name = "position"
    Type = "Position"
    Unit = ""
    Range = {
    }


# 检测人员类型
class Inspector_Type(DataItem):
    Name = "Inspector_Type"
    Type = "Passenger"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 2
    }


# 检测人员编号 person_id
class Inspector_Id(DataItem):
    Name = "Inspector_Id"
    Type = "Int"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 1000000
    }


# 检测人员体温 person_temperature
class Temperature(DataItem):
    Name = "Temperature"
    Type = "Float"
    Unit = ""
    Range = {
        "Min": 35,
        "Max": 39
    }


# 检测人员受感染状态 person_infect
class PersonInfect(DataItem):
    Name = "PersonInfect"
    Type = "Infect"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 2
    }


# 出勤人员是否道勤
class Attendance(DataItem):
    Name = "Attendance"
    Type = "Infect"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 1
    }


# 密码 password
class PasswordItem(DataItem):
    Name = "Password"
    Type = "Password"
    Unit = ""
    Range = {

    }


# 是否超级用户 is_superuser
class SuperItem(DataItem):
    Name = "SuperMan"
    Type = "Int"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 1
    }


# 机组管理人员姓名 username
class MangeName(DataItem):
    Name = "MangeName"
    Type = "UserName"
    Unit = ""
    Range = {
    }


# 机场工作人员姓名 username
class FirstName(DataItem):
    Name = "FirstName"
    Type = "Name"
    Unit = ""
    Range = {
    }


# 机组人员姓名 username
class SecondName(DataItem):
    Name = "SecondName"
    Type = "Name"
    Unit = ""
    Range = {
    }


# 邮箱 email
class EmailItem(DataItem):
    Name = "Emailer"
    Type = "Email"
    Unit = ""
    Range = {
    }


# is_staff
class IsStaff(DataItem):
    Name = "IsStaff"
    Type = "Int"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 1
    }


# is_active
class IsActive(DataItem):
    Name = "IsActive"
    Type = "Int"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 1
    }


# 年龄 age
class AgeItem(DataItem):
    Name = "Age"
    Type = "Int"
    Unit = ""
    Range = {
        "Min": 20,
        "Max": 50
    }


# 身份证号   card_id
class CardItem(DataItem):
    Name = "CradId"
    Type = "Card"
    Unit = ""
    Range = {
    }


# 手机号码 tel
class TelPhone(DataItem):
    Name = "Tel"
    Type = "Phone"
    Unit = ""
    Range = {
    }


# person_type
class PersonType(DataItem):
    Name = "PersonType"
    Type = "PersonType"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 3
    }


# IsDeteItem
class IsDeteItem(DataItem):
    Name = "IsDeteItem"
    Type = "Int"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 1
    }


# 头像 avatar
class AvatarItem(DataItem):
    Name = "Avatar"
    Type = "Avatar"
    Unit = ""
    Range = {
    }


# task_type
class TaskType(DataItem):
    Name = "Task"
    Type = "TaskType"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 2
    }


# flight_type
class FlightType(DataItem):
    Name = "FlightType"
    Type = "Flighttype"
    Unit = ""
    Range = {
        "Min": 0,
        "Max": 1
    }



# 感染警示表 alarm_infectalarm
class InfectArarmDevice(Device):
    def get_data_type_list(self):
        return [LevelItem]

    def get_sql_format(self):
        return "INSERT INTO alarm_infectalarm(alarm_level, time) " \
               "VALUES ('{LEVEL}', '{TIME}')"

    def get_sql_cmd(self, data):
        return self.get_sql_format().format(LEVEL=data[LevelItem.Name], TIME=datetime.now())


# 感染风险预警表 alarm_infectrisk
class InfectRiskDevice(Device):
    def get_data_type_list(self):
        return [LevelItem, Monitor_ID_Item]

    def get_sql_format(self):
        return "INSERT INTO alarm_infectrisk(infect_level, time, monitor_id_id) VALUES ('{LEVEL}', '{TIME}', '{MONITOR}')"

    def get_sql_cmd(self, data):
        return self.get_sql_format().format(LEVEL=data[LevelItem.Name], TIME=datetime.now(), MONITOR=data[Monitor_ID_Item.Name])


# 航班表 flight_flight
class FlightDevice(Device):
    def get_data_type_list(self):
        return [Flight_ID_Item, Flight_Company_Item, Flight_Start_Place, Flight_End_Place, Flight_Time, Flight_People]

    def get_sql_format(self):
        return "INSERT INTO flight_flight(flight_id, flight_company, departure, destination, begin_time, end_time) " \
               "VALUES ('{FLIGHT_ID}', '{COMPANY}', '{DEPARTURE}', '{DESTINATION}', '{BEGIN_TIME}', '{END_TIME}')"

    def get_sql_cmd(self, data):
        print(data[Flight_Time.Name])
        return self.get_sql_format().format(FLIGHT_ID=data[Flight_ID_Item.Name], COMPANY=data[Flight_Company_Item.Name], DEPARTURE=data[Flight_Start_Place.Name],
                                     DESTINATION=data[Flight_End_Place.Name], BEGIN_TIME=data[Flight_Time.Name], END_TIME=produce_endTime(data[Flight_Time.Name]))


# 飞机搭乘信息表 flight_takeflight
class TakeFlightDevice(Device):
    def get_data_type_list(self):
        return [Passenger_Type, Passenger_Id, Passenger_Name, Is_Take, SeatItem]

    def get_sql_format(self):
        return "INSERT INTO flight_takeflight(passenger_type, passenger_id, passenger_name, is_take, seat) VALUES " \
            "('{TYPE}', '{ID}', '{NAME}', '{TAKE}', '{SEAT}')"

    def get_sql_cmd(self, data):
        return self.get_sql_format().format(TYPE=data[Passenger_Type.Name], ID=data[Passenger_Id.Name], NAME=data[Passenger_Name.Name],
                                     TAKE=(data[Is_Take.Name]), SEAT=data[SeatItem.Name])


# 监测点位置表 monitor_monitor
class PositionDevice(Device):
    def get_data_type_list(self):
        return [PositionItem]

    def get_sql_format(self):
        return "INSERT INTO monitor_monitor(position) VALUES ('{POSITION}')"

    def get_sql_cmd(self, data):
        return self.get_sql_format().format(POSITION=data[PositionItem.Name])


# 检测数据表 monitor_monitordata
class PositonDataDevice(Device):
    def get_data_type_list(self):
        return [Inspector_Type, Inspector_Id, Passenger_Name, Temperature, PersonInfect, Monitor_ID_Item]

    def get_sql_format(self):
        return "INSERT INTO monitor_monitordata(time, person_type, person_id, person_name, person_temperature, person_infect, monitor_id_id, pre_monitor_id) VALUES " \
               "('{TIME}', '{PERSON_TYPE}', '{ID}', '{NAME}', '{TEMP}', '{INFECT}', '{MONITOR}', '{PREMONITOR}')"

    def get_sql_cmd(self, data):
        return self.get_sql_format().format(TIME=datetime.now(), PERSON_TYPE=data[Inspector_Type.Name], ID=data[Inspector_Id.Name],
                                     NAME=data[Passenger_Name.Name], TEMP=data[Temperature.Name], INFECT=2,
                                    MONITOR=data[Monitor_ID_Item.Name], PREMONITOR=data[Monitor_ID_Item.Name]+random.choice(RandNum))


# 出勤任务表 task_task
class TaskDevice(Device):
    def get_data_type_list(self):
        return []

    def get_sql_format(self):
        return "INSERT INTO task_task(time) VALUES ('{TIME}')"

    def get_sql_cmd(self, data):
        return self.get_sql_format().format(TIME=datetime.now())


# 出勤任务执行信息表 task_taskfinish
class TaskFinishDevice(Device):
    def get_data_type_list(self):
        return [Attendance]

    def get_sql_format(self):
        return "INSERT INTO task_taskfinish(is_finish) VALUES ('{Attend}')"

    def get_sql_cmd(self, data):
        return self.get_sql_format().format(Attend=data[Attendance.Name])


# 用户信息表 users_userinfo
# 包括机场管理人员表、机场工作人员表、机组人员表和旅客人员表，靠属性区分
class UserInfoDevice(Device):
    def get_data_type_list(self):
        return [PasswordItem, SuperItem, MangeName, FirstName, SecondName, EmailItem, IsStaff, IsActive, AgeItem,
                CardItem, TelPhone, PersonType, LevelItem, IsDeteItem, AvatarItem, TaskType, FlightType]

    def get_sql_format(self):
        return "INSERT INTO users_userinfo(password, last_login, is_superuser, username, first_name, last_name, email, " \
               "is_staff, is_active, date_joined, age, card_id, tel, person_type, infect_level, isDelete, avatar, task_type, flight_type) " \
               "VALUES ('{PASSWORD}', '{LOGIN}', '{SUPER}', '{USER}', '{FIRST}', '{SECOND}', '{EMAIL}', '{STAFF}', '{ACTIVE}'," \
               "'{DATE}', '{AGE}', '{CARD}', '{TEL}', '{PERSON}', '{INFECT}', '{IsDete}', '{AVATAR}', '{TASK}', '{FLIGHT}')"

    def get_sql_cmd(self, data):
        return self.get_sql_format().format(PASSWORD=data[PasswordItem.Name], LOGIN=datetime.now(), SUPER=data[SuperItem.Name],
                   USER=data[MangeName.Name], FIRST=data[FirstName.Name], SECOND=data[SecondName.Name], EMAIL=data[EmailItem.Name],
                   STAFF=data[IsStaff.Name], ACTIVE=data[IsActive.Name], DATE=datetime.now(), AGE=data[AgeItem.Name],
                   CARD=data[CardItem.Name], TEL=data[TelPhone.Name], PERSON=data[PersonType.Name], INFECT=data[LevelItem.Name],
                   IsDete=data[IsDeteItem.Name], AVATAR=data[AvatarItem.Name],  TASK=data[TaskType.Name], FLIGHT=data[FlightType.Name])