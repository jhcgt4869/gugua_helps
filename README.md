# gugua_helps
 七夕孤寡助手

<font size=4 color=red><center>七夕在即</center></font>
<font size=5 color=red><center>你还在为怎么说情话烦恼嘛？</center></font>
<font size=6 color=red><center>你还在不知道怎么样文艺表白困苦嘛？</center></font>
<font size=6 color=red><center>你还在因为分不清口红而被责备嘛？</center></font>
<font size=6 color=red><center>你还在为一个人"孤寡"烦恼嘛？</center></font>
<font size=6 color=red><center>孤寡机器人解决你的困恼！</center></font>


## 查看机器人使用指南



<iframe style="width:80%;height: 600px;"src="//player.bilibili.com/player.html?aid=632151779&bvid=BV1ab4y1z7vs&cid=384415312&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

## 内容查看

### 嗨~&&情话&&藏头诗

<img src="https://ai-studio-static-online.cdn.bcebos.com/ecd247575af9489f83248d2eee320246b9d5da87682c4a01944c1cbfbb7bd2ca" alt="image-20210703150848118" style="zoom: 50%;" />

### 口红

<img src="https://ai-studio-static-online.cdn.bcebos.com/574dcefae4ca4eee8663c02add4084cdcf5a30bf789147cf88baa801c3e6240b" alt="image-20210703150848118" style="zoom: 50%;" />

### 孤寡大礼包

<img src="https://ai-studio-static-online.cdn.bcebos.com/ea03c91f39034ec3aac92e87a1432f0868735ce678b44882981e7e95ee0c2be5" alt="image-20210703150848118" style="zoom: 50%;" />



### 总结

<font size=4>

怎么样，是不是很刺激，以后妈妈再也不担心我的……

那么到底是怎么样完成的呢？  
  让我们一起来看看


### 逻辑导图

![](https://ai-studio-static-online.cdn.bcebos.com/9dea1c38c45743988bc04db90935f90b9576629ea1874e1ab3d8153a51daede0)


### 部分代码查看

<font size=5> 自动回复部分</font>


```python
# 自动回复内容
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
            await talker.say('已经收到你的心意' + msg.text()[1:] + '，正在生产"藏头诗"~~~')
            print(msg.text()[1:])
            await talker.say(cts(msg.text()[1:]))

        if msg.text()[0] == "2":
            await talker.say('稍等片刻，小助手马上教你说"情话"~~~')
            await talker.say(qh(msg.text()[1:]))

        if msg.text() == "口红明细":
            await talker.say(khdata1)

        if msg.text() == "口红品牌":
            await talker.say(khdata2)

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
            await talker.say(kh(img_path))

        if msg.text() == "大礼包":
            await talker.say("孤寡~孤寡~孤寡~")
            time.sleep(3)
            await talker.say("祝你七夕孤寡~~~")
            time.sleep(4)
            await talker.say("你孤寡我孤寡大家一起孤寡寡\n下面是小助手送你的孤寡礼物！")
            time.sleep(3)
            for i in range(3):
                await talker.say("孤寡  孤寡  孤寡  "*50)
                time.sleep(20)
            await talker.say("七夕节快乐~~~狗粮管够~~~")
```

<font size=5> 藏头诗部分</font>


```python
def cts(data):
    long = len(data)

    if long <= 4:
        long = 4
    else:
        long = 8
    print(long)
    module = hub.Module(name="ernie_gen_acrostic_poetry", line=long, word=7)

    results = module.generate(texts=[data], use_gpu=True, beam_width=1)
    for result in results:
        print(results)
        return result[0]

```

<font size=5> 情诗部分 </font>


```python
def qh(data):
    module = hub.Module(name="ernie_gen_lover_words")
    results = module.generate(texts=[data], use_gpu=True, beam_width=1)
    for result in results:
        return result[0]
```

<font size=5> 口红分类部分 </font>


```python
# 数据处理
img = Image.open(path)  # 打开图片
img = img.convert('RGB')
img = img.resize((100, 100), Image.ANTIALIAS)  # 大小归一化
img = np.array(img).astype('float32')  # 转换成 数组
img = img.transpose((2, 0, 1))  # 读出来的图像是rgb,rgb,rbg..., 转置为 rrr...,ggg...,bbb...
img = img / 255.0  # 缩放

# 模型读取
model_state_dict = paddle.load('./resnet101.pdparams')  # 读取模型
model = resnet101()  # 实例化模型
model.set_state_dict(model_state_dict)
model.eval()

# 预测
ceshi = model(paddle.reshape(paddle.to_tensor(img), (1, 3, 100, 100)))  # 测试
return lablelist[np.argmax(ceshi.numpy())]  # 获取值
```

### 参考项目

不仅限于以下项目：　　

[[七夕特辑]如何应对灵魂发问：我的这口红是什么……](https://aistudio.baidu.com/aistudio/projectdetail/2258924)  
[星际旅行向导机器人（基于paddlehub+wechaty完成）](https://aistudio.baidu.com/aistudio/projectdetail/2248648)    
[一步一步教你用wechaty+百度云主机打造一个带你穿越星际的微信机器人](https://aistudio.baidu.com/aistudio/projectdetail/2177502)    
……

### 团队&&致谢


团队：让我们水到底！　　　　　　

成员：[三岁](https://aistudio.baidu.com/aistudio/personalcenter/thirdview/284366)、[super松](https://aistudio.baidu.com/aistudio/personalcenter/thirdview/279448)、[iterhui](https://aistudio.baidu.com/aistudio/personalcenter/thirdview/643467)、[L兮木](https://aistudio.baidu.com/aistudio/personalcenter/thirdview/891283)、[七年期限](https://aistudio.baidu.com/aistudio/personalcenter/thirdview/58637)（以上成员均是大佬，不分先后）

致谢：

感谢团队成员的各类建议和合作配合

感谢参考项目的各位大佬帮助　　

感谢积极帮助解决问题的各路大佬　　

感谢帮助参考口红类型的各位小姐姐　　

最后感谢主办方的机会和精良的活动～～～

