import DBServer
import DataGenerators
import MQServer
import random
from datetime import datetime
import time
from django.contrib.auth.hashers import make_password, check_password

def main():
    print("Program start ....")

    # 连接mysql数据库
    ds = DBServer.DBServer()

    # 连接MQ
    mq_host = "47.98.214.197"
    mq_port = 61613
    mq_username = "admin"
    mq_passwd = "admin"
    ms = MQServer.MyActiveMq(mq_host, mq_port, mq_username, mq_passwd)
    ms.mq_conn()

    # 监听
    ms.read_data('/topic/alarmindect')

    # # 创建感染警示检测设备
    # infect_alarm = DataGenerators.InfectArarmDevice("0", "Infect_alarm")
    #
    # # 创建感染风险预警检测设备
    infect_risk = DataGenerators.InfectRiskDevice("1", "Infect_risk")
    #
    # # 创建航班表检测设备
    # flight_flight = DataGenerators.FlightDevice("2", "flight_flight")
    #
    # 创建飞机搭乘信息检测设备
    # take_flight = DataGenerators.TakeFlightDevice("3", "take_flight")

    # # 创建监测点位置表检测设备
    # position = DataGenerators.PositionDevice("4", "position")
    # #
    # # # 创建检测数据检测设备
    position_data = DataGenerators.PositonDataDevice("5", "position_data")

    # # 创建出勤任务检测设备
    # task = DataGenerators.TaskDevice("6", "task")
    #
    # # 创建出勤任务执行信息表检测设备
    # task_finish = DataGenerators.TaskFinishDevice("7", "task_finish")
    #
    # # 创建用户信息表检测设备
    # user = DataGenerators.UserInfoDevice("8", "user")

    while True:
    #     infectalarm_info = infect_alarm.get_info()
    #     print(infectalarm_info)
    #     print(infect_alarm.get_sql_cmd(infectalarm_info["data"]))
    #     ds.execute(infect_alarm.get_sql_cmd(infectalarm_info["data"]))
    #     ms.send_data("infectalarm_info", infectalarm_info)
    #

        # infectrisk_info = infect_risk.get_info()
        #
        # print(infectrisk_info)
        # print(infect_risk.get_sql_cmd(infectrisk_info["data"]))
        # ds.execute(infect_risk.get_sql_cmd(infectrisk_info["data"]))
        # ms.send_data("infectrisk_info", infectrisk_info)
    #
        # flight_info = flight_flight.get_info()
        # print(flight_info)
        # print(flight_flight.get_sql_cmd(flight_info["data"]))
        # ds.execute(flight_flight.get_sql_cmd(flight_info["data"]))
        # ms.send_data("flight_info", flight_info)

        # takeflight_info = take_flight.get_info()
        # print(takeflight_info)
        # print(take_flight.get_sql_cmd(takeflight_info["data"]))
        # ds.execute(take_flight.get_sql_cmd(takeflight_info["data"]))
        # ms.send_data("takeflight_info", takeflight_info)
    #
    #     position_info = position.get_info()
    #     print(position_info)
    #     print(position.get_sql_cmd(position_info["data"]))
    #     ds.execute(position.get_sql_cmd(position_info["data"]))
    #     ms.send_data("position_info", position_info)
    #
        # positiondata_info = position_data.get_info()
        # print(positiondata_info)
        # print(position_data.get_sql_cmd(positiondata_info["data"]))
        # ds.execute(position_data.get_sql_cmd(positiondata_info["data"]))
       # ms.send_data("positiondata_info", positiondata_info)
    #
    #     task_info = task.get_info()
    #     print(task_info)
    #     print(task.get_sql_cmd(task_info["data"]))
    #     ds.execute(task.get_sql_cmd(task_info["data"]))
    #     ms.send_data("task_info", task_info)
    #
    #     taskfinish_info = task_finish.get_info()
    #     print(taskfinish_info)
    #     print(task_finish.get_sql_cmd(taskfinish_info["data"]))
    #     ds.execute(task_finish.get_sql_cmd(taskfinish_info["data"]))
    #     ms.send_data("taskfinish_info", taskfinish_info)
    #
    #     user_info = user.get_info()
    #     print(user_info)
    #     print(user.get_sql_cmd(user_info["data"]))
    #     ds.execute(user.get_sql_cmd(user_info["data"]))
    #     ms.send_data("user_info", user_info)


        for i in range(1, 21):
            x = "INSERT INTO alarm_infectrisk(infect_level, time, monitor_id_id) VALUES ('{LEVEL}', '{TIME}', '{MONITOR}')"
            infectriskinfo = {}
            level = random.randint(1, 3)
            risktime = datetime.now()
            infectriskinfo["infect_level"] = level
            infectriskinfo["time"] = risktime
            infectriskinfo["monitor_id_id"] = i
            x = x.format(LEVEL=random.randint(1, 3), TIME=datetime.now(), MONITOR=i)
            print(x)
            ds.execute(x)
            json.dumps(infectriskinfo)
            ms.send_data("infectriskinfo", infectriskinfo)
        #
        time.sleep(5)







    # # 创建温度设备
    # td = DataGenerator.TemperDevive("1", "Temp1")
    #
    # while True:
    #     # 产生温度数据
    #     tempInfo = td.get_info()
    #     print(tempInfo)
    #     # 将数据存储到mysql
    #    # ds.execute(td.get_sql_cmd(tempInfo["data"]))
    #     # 将数据存储到消息队列
    #    # ms.send_data("Temper", tempInfo)
    #     time.sleep(5)
    #     print("secceed...")


if __name__ == '__main__':
    main()