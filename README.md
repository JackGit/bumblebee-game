An chat game that llm responses like bumblebee


GPT prompt
> 我们玩个游戏，请用文件里的英文内容回答我的问题，不要更改内容，直接引用内容回答我的问题。
> 比如我问：“你生那么大的气干嘛”
> 而文件中有一个“你先冷静冷静”，正好可以回答这个问题，就使用这个内容进行回答。
> 回答同时给出所在 json 数组对象的完整信息作为参考


测试飞驰人生2的 asr 内容时，发现 gpt：
1. 只能识别到不到 1500 行（格式化后的 json 文件），还不到 1/10 的内容；
2. 同时发现一个有点，gpt 会自己做语句合并，自动合并计算起始时间。


弹幕：
1. https://www.bilibili.com/read/cv5187469/ xml 文件解释

## todo
- [ ] 对于电影内容，从弹幕中分析高潮部分，只提取高潮部分的对话
- [ ] 一些有名的电影：后会无期、西虹市首付、夏洛特烦恼、飞驰人生
- [ ] 用这些内容讲一个小故事
- [ ] 直接从必剪的梗视频作为数据源
- [ ] 用小品相声作为数据源
- [ ] 接入 GPT
- [ ] 接入语音助手
- [ ] 添加波形图