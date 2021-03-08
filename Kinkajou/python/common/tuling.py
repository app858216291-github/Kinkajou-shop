# -*- coding: utf-8 -*-
import json
import re
import requests
import setting
unit_token=setting.Tuling.unit_token
unit_lanhua_botId=setting.Tuling.unit_lanhua_botId

def post(url, body):
    headers = {'content-type': 'application/json'}
    response = requests.post(url, json=body)
    return response.text

def get(url, body="", headers=""):
    headers = {'content-type': "application/json", 'Authorization': 'APP appid = 4abf1a,token = 9480295ab2e2eddb8'}
    response = requests.get(url, "", headers=headers)
    return response.text


def get_unit_token():
    result=get(setting.Tuling.unit_url)
    result=json.loads(result)
    return result["access_token"]

def getIntendId():
    bot_id = str(unit_lanhua_botId)
    access_token = unit_token
    print(access_token)

    data = '{"bot_session":"","intentId":"FAQ_LANHUA","intentType":"faq","log_id":"7758521","skillId":0,"pageNo":1,"pageSize":50,"botId":"' + bot_id + '","version":"2.0"}'
    data = json.loads(data)
    answer = post("https://aip.baidubce.com/rpc/2.0/unit/intent/list?access_token=" + access_token + "", data)
    print(answer)
    resul = json.loads(answer)
    intentId = resul['result']['intents'][0]['intentId']
    return intentId
unit_token=get_unit_token()




###机器人库
class TuLing:
    #百度unit
    @staticmethod
    def getUnit(text):
        bot_id=str(unit_lanhua_botId)
        access_token =unit_token
        data = '{"bot_session":"","log_id":"7758521","request":{"bernard_level":1,"client_session":"123","query":"'+text+'","query_info":{"asr_candidates":[],"source":"KEYBOARD","type":"TEXT"},"updates":"","user_id":"88888"},"bot_id":"'+bot_id+'","version":"2.0"}'
        data = json.loads(data)
        answer = post("https://aip.baidubce.com/rpc/2.0/unit/bot/chat?access_token="+access_token+"", data)
        resul = json.loads(answer)
        resul = resul['result']
        response = resul['response']
        say = response['action_list'][0]['say']
        actionId = response['action_list'][0]['action_id']

        if actionId == u'faq_select_guide':
            # say = response['action_list'][0]['say']
            ques = resul['bot_session']
            ques = ques.encode('utf-8')
            ques = json.loads(ques)
            ques = ques['bot_views']
            ques = ques['bernard_res'][0]
            ques = ques['qu_res']
            candidates = ques['candidates']
            for question in candidates:
                say = say + '\n' + question['match_info']
            return say
        elif actionId == u'fail_action':
            say = "你好，你的问题我不还不知道怎么回答，已经反馈给我主人，你明天再试试就能找到答案了。"
            return say
        elif actionId == u'faq_lanhua_satisfy':
            return say
        else:
            return say

    @staticmethod
    def getList(pageNo=1,pageSize=50):
        bot_id=str(unit_lanhua_botId)
        access_token =unit_token
        data = '{"intentId":"36940","skillId":0,"pageNo":'+str(pageNo)+',"pageSize":'+str(pageSize)+',"botId":"' + bot_id + '"}'
        data = json.loads(data)
        answer = post("https://aip.baidubce.com/rpc/2.0/unit/faq/list?access_token="+access_token+"", data)
        print(answer)
        resul = json.loads(answer)
        resul = resul['result']
        # faqList=resul['faqList']
        return resul

    @staticmethod
    def add(answer,question):
        bot_id=str(unit_lanhua_botId)
        access_token =unit_token
        data = '{"intentId":"36940","skillId":0,"botId":"' + bot_id + '","faqAnswers": [{"answer":"'+answer+'"}],"faqQuestions":[{"question": "'+question+'"}]}'
        data = json.loads(data)
        answer = post("https://aip.baidubce.com/rpc/2.0/unit/faq/add?access_token="+access_token+"", data)
        print(answer)
        resul = json.loads(answer)
        resul = resul['result']
        # faqList=resul['faqList']
        return resul

    @staticmethod
    def delete(faqId=2609186):
        bot_id=str(unit_lanhua_botId)
        access_token =unit_token
        data = '{"intentId":"36940","skillId":0,"faqId": '+faqId+',"botId":"' + bot_id + '"}'
        data = json.loads(data)
        answer = post("https://aip.baidubce.com/rpc/2.0/unit/faq/delete?access_token="+access_token+"", data)
        print(answer)
        resul = json.loads(answer)
        # resul = resul['result']
        # faqList=resul['faqList']
        return resul

    @staticmethod
    def update(faqId=2609186):
        bot_id = str(unit_lanhua_botId)
        access_token = unit_token
        data = '{"intentId":"36940","skillId":0,"botId":"' + bot_id + '","faqAnswers": [{"answer":"新增答案1"}],"faqQuestions":[{"question": "新增问题1"}],"faqId": 2609186}'
        data = json.loads(data)
        answer = post("https://aip.baidubce.com/rpc/2.0/unit/faq/add?access_token=" + access_token + "", data)
        print(answer)
        resul = json.loads(answer)
        resul = resul['result']
        # faqList=resul['faqList']
        return resul

    @staticmethod
    def info(text):
        bot_id=str(unit_lanhua_botId)
        access_token =unit_token
        data = '{"bot_session":"","log_id":"7758521","skillId":15442,"pageNo":1,"pageSize":50,"faqId":1553082,"request":{"skillId":15442,"pageNo":1,"pageSize":50,"bernard_level":1,"client_session":"123","query":"'+text+'","query_info":{"asr_candidates":[],"source":"KEYBOARD","type":"TEXT"},"updates":"","user_id":"88888"},"bot_id":"'+bot_id+'","version":"2.0"}'
        data = json.loads(data)
        answer = post("https://aip.baidubce.com/rpc/2.0/unit/v3/faqskill/faqPair/info?access_token="+access_token+"", data)
        resul = json.loads(answer)
        resul = resul['result']
        response = resul['response']
        say = response['action_list'][0]['say']
        actionId = response['action_list'][0]['action_id']

        if actionId == u'faq_select_guide':
            # say = response['action_list'][0]['say']
            ques = resul['bot_session']
            ques = ques.encode('utf-8')
            ques = json.loads(ques)
            ques = ques['bot_views']
            ques = ques['bernard_res'][0]
            ques = ques['qu_res']
            candidates = ques['candidates']
            for question in candidates:
                say = say + '\n' + question['match_info']
            return say
        elif actionId == u'fail_action':
            say = "你好，你的问题我不还不知道怎么回答，已经反馈给我主人，你明天再试试就能找到答案了。"
            return say
        elif actionId == u'faq_lanhua_satisfy':
            return say
        else:
            return say





