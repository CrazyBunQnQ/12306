# -*- coding: utf8 -*-

import requests

__author__ = 'MR.wen'
import TickerConfig


def sendIFTTT(msg):
    """
    IFTTT 通知
    :param msg: 提醒内容
    :return:
    """
    try:
        # The payload that will be sent to IFTTT service
        data = {'value1': '恭喜，您已订票成功', 'value2': msg, 'value3': ''}
        # inserts our desired event
        ifttt_event_url = TickerConfig.IFTTT_CONF['webhooks_url']
        # Sends a HTTP POST request to the webhook URL
        requests.post(ifttt_event_url, json=data)
        print(u"已发送 IFTTT 消息提醒, 请查收")
    except Exception as e:
        print(u"IFTTT 配置有误{}".format(e))


if __name__ == '__main__':
    sendIFTTT(1)
