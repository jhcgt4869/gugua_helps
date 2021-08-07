import os
import asyncio
import paddle
import paddlehub as hub
from wechaty import (
    Contact,
    FileBox,
    Message,
    Wechaty,
    ScanStatus,
)
from PIL import Image
import paddle.nn
import numpy as np

os.environ['WECHATY_PUPPET_SERVICE_TOKEN'] = 'puppet_padlocal_xxxxxx'

# reply自动回复话术合集
reply = [
    '''嗨~\n你好啊这里是“高质量”七夕孤寡小助手,很高兴为你服务。
小助手为你准备了以下3个高质量服务
1、很直很直的表白藏头诗— —回复[藏头诗]参与
2、“骚话语录”小助手教你说情话— —回复[情话]参与
3、女友死亡问答“我的口红是什么……”之口红种类识别— —回复[口红]参与
回复[帮助]即可获得小助手教学指南~~~''',
    '欢迎使用~七夕藏头诗板块\n直接回复你要的藏的内容即可~~~\n格式如下：1+回复内容\n例如：回复“我喜欢你”就输入1我喜欢你\n（目前支持4-8个字如果超'
    '出会自动截断）',
    '哈喽！欢迎你找到宝藏内容，请开一个开头，小助手教你说情话~~~\n格式如下：2+回复内容\n例如：回复“我喜欢你”就输入2我喜欢你',
    '''嗷呜~~~\n你还在为女友的灵魂发问而烦恼嘛？你还在为不知道女友口红是什么而烦恼嘛？小助手祝你一臂之力！
    把女友口红照片发给小助手,小助手帮你识别女友的口红类型！\n回复— —[口红品牌]对目前支持查询的口红品牌进行查看\n回复— —[口红明细]查看具体的口红''']

helptxt = '''博客地址：https://blog.csdn.net/weixin_45623093/article/details/119484889
AI Stduio地址：https://aistudio.baidu.com/aistudio/projectdetail/2263052
B站（哔哩哔哩）地址：'''

khdata1 = '''古驰倾色柔纱润唇膏
古驰倾色丝润唇膏
古驰倾色琉光唇膏
古驰倾色华缎唇膏
古驰倾色绒雾唇膏
古驰倾色星辉唇膏
爱马仕唇妆系列缎光唇膏
阿玛尼「红管」臻致丝传奇绒哑光唇釉
阿玛尼「红黑管」哑光唇膏
阿玛尼「小胖丁」持色凝彩哑光染唇液
阿玛尼「5G」黑管
阿玛尼「黑」漆光迷情唇釉
迪奥烈艳蓝金唇膏
Dior「红管」花芯唇膏
DIOR迪奥魅惑釉唇膏
烈艳蓝金锁色唇釉
圣罗兰纯口红
圣罗兰细管纯口红（小金条）
圣罗兰莹亮纯魅唇膏
圣罗兰细管纯口红（小黑条）
娇兰臻彩宝石唇膏
娇兰亲亲唇膏
娇兰唇蜜
CHILI 小辣椒
魅可清新漆光唇釉
完美日记小细跟口红
完美日记唇彩  
完美日记口红
兰蔻唇釉
兰蔻唇膏
娇韵诗丰盈唇膏
香奈儿可可小姐唇膏
CL路铂廷女王权杖（萝卜丁口红）
CL路铂廷女王权杖黑管（萝卜丁口红）
纪梵希小羊皮
纪梵希羊皮唇釉
纪梵希禁忌之吻星云唇膏
3CE细管唇膏
3CE哑光口红
3CE唇泥
3CE三熹玉云朵唇釉
UNNY唇泥
UNNY雾面雪雾花园唇釉
植村秀小黑方唇膏口红
植村秀无色限方管漆光唇釉口红
TOM FORD唇膏
雅诗兰黛口红金管
橘朵哑光唇釉
橘朵小花管唇膏
稚优泉口红
稚优泉无惧幻想绒雾唇釉
稚优泉琉光之镜水光唇釉
稚优泉 绒情迷雾哑光唇釉'''

khdata2 = '''Gucci（古驰）
爱马仕
阿玛尼（Armani）
Dior（奥迪）
YSL（圣罗兰）杨树林
GUerlain（娇兰）
mac（魅可）
完美日记
兰蔻（Lancome）
娇韵诗（clarins）
香奈儿（Chanel）
胡萝卜丁（christianlouboutin）
Givenhy（纪梵希）
3CE
unny
植村秀
Tom Ford （TF）
雅诗兰黛（Estee Lauder）
橘朵（JudydoLL）
稚优泉'''


class MyBot(Wechaty):
    async def on_message(self, msg: Message):
        talker = msg.talker()
        await talker.ready()
        if msg.text() == "嗨~":
            await talker.say(reply[0])

        if msg.text() == "藏头诗":
            await talker.say(reply[1])

        if msg.text() == "情话":
            await talker.say(reply[2])

        if msg.text() == "口红":
            await talker.say(reply[3])

        if msg.text() == "帮助":
            await talker.say(helptxt)

        if msg.text()[0] == "1":
            await talker.say('已经收到你的心意，正在生产"藏头诗"~~~')
            await talker.say(cst(msg.text()[1:]))

        if msg.text()[0] == "2":
            await talker.say('稍等片刻，小助手马上教你说"情话"~~~')
            await talker.say(qh(msg.text()[1:]))

        if msg.text() == "口红明细":
            await talker.say(khdata1)

        if msg.text() == "口红品牌":
            await  talker.say(khdata2)

        if msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
            await talker.say('已收到图像，开始验证')
            # 将Message转换为FileBox
            file_box_user_image = await msg.to_file_box()
            # 获取图片名
            img_name = file_box_user_image.name
            # 图片保存的路径
            img_path = './image/' + img_name

            # 将图片保存为本地文件
            await file_box_user_image.to_file(file_path=img_path)



def cts(data):
    long = len(data)
    if long <= 4:
        long = 4
    else:
        long = 8
    module = hub.Module(name="ernie_gen_acrostic_poetry", line=long, word=7)

    results = module.generate(texts=data, use_gpu=True, beam_width=1)
    for result in results:
        return result[0]


def qh(data):
    module = hub.Module(name="ernie_gen_lover_words")
    results = module.generate(texts=data, use_gpu=True, beam_width=1)
    for result in results:
        return result[0]


def kh(path):
    img = Image.open(path)  # 打开图片
    img = img.resize((100, 100), Image.ANTIALIAS)  # 大小归一化
    img = np.array(img).astype('float32')  # 转换成 数组
    img = img.transpose((2, 0, 1))  # 读出来的图像是rgb,rgb,rbg..., 转置为 rrr...,ggg...,bbb...
    img = img / 255.0  # 缩放
    model_state_dict = paddle.load('./data/resnet101.pdparams')  # 读取模型
    model = resnet101()  # 实例化模型
    model.set_state_dict(model_state_dict)
    model.eval()

    # print(paddle.to_tensor(img).shape)
    ceshi = model(paddle.reshape(paddle.to_tensor(img), (1, 3, 100, 100)))  # 测试
    return lablelist[np.argmax(ceshi.numpy())]  # 获取值



async def main():
    bot = MyBot()
    await bot.start()


asyncio.run(main())
