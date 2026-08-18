# FDE 图书读者调研报告（对应七篇框架）

基于公开网络资料的调研，逐篇拆解不同读者角色（甲方BDM/TDM/HR、乙方从业者/管理者）在阅读时最需要被回答的问题，并标注了各章节可支撑的信息线索。

------

## 认知篇（第1–2章）：FDE是什么、为什么有效

**读者的核心疑问**

- **甲方所有角色共同的第一问**："这和外包/驻场实施到底有什么本质区别？"——这是几乎所有资料反复出现的开场质疑，虎嗅报道中一个尖锐场景是客户直接质问FDE和产品定制化有什么区别，甚至有分析直言中国的FDE本质仍是乙方人力外包，只是套了AI的新壳。认知篇必须先给出一套可操作的鉴别标准，而不是停留在概念定义。
- **"卖人力→卖能力"这条主线需要回答**：乙方为什么愿意做这种投入更重的模式？答案在于重投入换来的是极高的切换成本——一旦客户的业务逻辑被固化进系统，工作流跑起来后客户几乎无法迁移，这让FDE模式的公司拥有了类似保险或公共事业公司的商业稳定性，同时兼具软件公司的毛利。
- **"飞轮"具体转的是什么？** 乙方内部真正要同时盯住两个指标：一是交付给客户的结果价值是否越来越大，二是产品杠杆是否让FDE交付这些结果变得越来越容易、越来越少代码越少时间——这两个维度同步推进，才构成真正的飞轮，而不是单纯"多接项目"。
- **甲方CXO最关心的落地问题**：到2028年，预计三分之一的企业软件应用将内置AI Agent，15%的工作决策将实现自主化——这类数字是CXO判断"要不要现在投入"的决策依据，认知篇需要给出类似的行业基准线。
- **HR总监的独特疑问**：FDE模式带来的不只是技术变革,更直接冲击组织与人——当AI Agent等"硅基劳动力"与人类员工成为同等重要的组织资产,人力资源规划需要从"人"转向"人+算力"的混合规划,这个概念本身就需要在认知篇被提前埋下,否则HR会缺席后面团队篇的讨论。

**该篇需要额外补充的维度**：甲乙双方对"结果"定义的分歧（谁来定义"做成了"）建议作为认知篇的收尾悬念，为流程篇的SOP做铺垫。

------

## 标杆篇（第3–4章）：解剖Palantir

**读者的核心疑问**

- **TDM最想知道**："Ontology到底是什么，为什么它比一般数据平台/知识图谱更强？" Ontology是一个语义层，用来连接数据与现实世界的业务对象、关系和决策流程，包含数据、逻辑、操作三大要素，且安全性贯穿其中——它的定位不是"存数据"而是表示企业中的决策本身。一个具体的可复现案例是航空制造场景：FDE把飞机机尾号、紧固件、装配工位、质检员这些业务实体固化成Ontology后，一旦某批次零件在海关被卡住，系统能像触网一样瞬间联动，直接在屏幕上标红受影响的飞机，而传统方式需要写极复杂的SQL多次JOIN才能查到血缘关系。
- **TDM会追问的关键点**：这套模式能不能被复制，还是只有Palantir能做到？研究者指出Ontology一旦建好，业务语义层就完全绑定在Palantir的Foundry平台私有形态上，数据名义上还在客户存储里，但离开Palantir就等于要重建整个语义层——这是护城河，也是客户的退出成本，国内团队复刻这套模式时应提前规划FDE经验如何沉淀为资产，否则会陷入"永远在堆人"的困局。
- **甲方会问的现实问题**："我们能不能直接买Palantir的产品？" 答案篇需要明确说明：Palantir不进中国市场，国内团队研究Palantir本质上是研究方法论,而不是研究采购选项,国内场景通常需要"国产数据平台+自建语义层+业务侧驻场团队"的组合来实现类似效果。
- **乙方经营者最想理解的商业逻辑**：Palantir创始工程师提到，Ontology最初诞生的动机是发现给每类业务对象单独建表的方式无法跨机构、跨客户复用，于是把抽象层级拉高，只在底层提供通用的对象、属性等结构，再让FDE按每个客户的具体语境去定义——这段起源故事本身就是"标杆篇"里最有说服力的方法论示范。
- **失败案例的诚实呈现**：认真的读者（尤其TDM）会对纯正面案例产生警惕，建议标杆篇主动纳入争议性案例，避免"只讲成功故事会形成幸存者偏差"的问题。

------

## 流程篇（第5–9章）：四阶段SOP与能力回注方法论

**读者的核心疑问（这是全书最实操、读者期待最高的部分）**

- **通用四阶段落地路径**，TDM和项目经理最需要的骨架：选型评估平台的安全性与扩展性→选定1-2个核心场景做POC（业务人员提供领域知识、技术人员负责流程编排）→制定评估指标（准确率、处理时效、人力节省工时）→试点成功后逐步向其他部门横向扩展，同时建立"数字员工管理机制"。
- **甲方最常问的"能不能不做全套"**：93%的AI Agent项目卡在从POC到生产的跨越,核心失败原因之一是技术部门推着AI上、业务部门却不知道要解决什么问题——流程篇需要明确指出正确的起点应该是"这个Agent消灭了哪个岗位的哪类重复工作"，而不是"我们能用AI做什么"。
- **能力回注具体怎么做，这是乙方和TDM共同关心的机制问题**：行业实践给出了明确的分层标准——如果做完项目只留给客户一个系统，那是外包；带回一些经验但无法复用，是项目制交付；只有严格去掉客户信息、把行业通用经验沉淀为可复用的Skill、模板和产品能力，才是真正的FDE，沉淀后应该能显著降低下一个同类客户的交付成本。
- **验收节奏的问题（甲方最痛的点）**：如果交付模式是"闷头做三个月再上线"，项目大概率死在第六周——甲方看不到阶段性成果就会开始怀疑、抽调资源、砍预算，流程篇应该给出具体的短周期冲刺节奏建议。
- **风险与权限治理如何嵌入SOP（TDM高度关注）**：全链路监控与审计要建立不可篡改的行为日志，记录Agent调用了什么API、用了哪些数据、返回了什么结果；同时遵循最小权限原则，每个Agent只获得完成任务所需的最小工具和数据访问权限，禁止直接访问数据库或文件系统——这些应该作为SOP中每个阶段的标准检查项，而不是事后补救。
- **评估体系怎么建（TDM深层疑问）**：Agent与传统软件有本质不同——具有非确定性、Prompt即源代码、依赖会自己动，因此传统QA框架系统性失效，需要一套新的开发生命周期，其中"定义'好'"要排在动手构建之前。

------

## 团队篇（第10–12章）：五大角色体系、协作机制、人才培养

**读者的核心疑问**

- **甲方HR和TDM共同关心**："这个团队应该长什么样，我们自己有没有可能建？" Palantir工程师约25%的时间在客户端工作，医疗AI公司Commure的FDE驻场比例甚至高达50%——团队篇需要给出不同驻场强度对应的团队配置模型，供甲方判断自建还是外部合作。
- **前后方协作机制（乙方管理者最关心）**：前方FDE负责现场探索，后方PDE负责把FDE拿回来的模式抽象成产品能力，这种双轮驱动架构解决了传统软件公司的顽疾——研发不知道用户要什么，销售答应了用户但研发做不出来。
- **人才培养的现实挑战（乙方HR/管理者关心）**：FDE的核心能力从来不是写代码，而是要把"我想用AI降本增效"这类模糊诉求拆解成可落地的技术路径，业内共识是这种能力极度依赖行业经验，物流行业的落地方法放到赛车行业完全不适用，不存在通用课程体系能速成培养。
- **知识管理与复用机制（TDM/乙方管理者）**：一个可借鉴的做法是每个定制项目完成后，必须抽象出至少两个可复用的业务组件，通过低代码平台、行业组件库等形式沉淀为可复用的能力中台。
- **驻场团队的组织政治问题（HR和甲方对接人的隐藏疑问）**：对接FDE的甲方员工往往是被要求投入更多时间的人，同时也可能是流程自动化后最先被替代的岗位——这不是技术问题，是组织政治问题，团队篇需要正视这个张力，而不是回避。
- **薪酬与激励现实**：字节"FDE专家"月薪开到3万元至5万元、15薪，普遍高于同级别研发，出现薪资倒挂现象，这类数据对HR总监设计岗位体系、说服管理层批预算有直接参考价值。

------

## 中国实践篇（第13–14章）：云厂商图谱、案例锚点、乙方转型挑战与合规清单

**读者的核心疑问**

- **甲方最想知道的行业格局全景**：谷歌、OpenAI、Anthropic、Meta等AI与云巨头近半年大力设立FDE岗或专项公司，总投入已超过数百亿人民币；国内的阿里、字节、腾讯等大模型兼云大厂，也在同期密集拉起"驻场铁军"。具体到细分领域：腾讯云在游戏云领域连续四年市场份额全国第一，华为云则在政企市场以23.3%的份额排名第一——这类差异化定位信息可以帮甲方判断该找哪家。
- **乙方转型的五大挑战需要正面回应**（这条line最贴近"转型阵痛"的真实叙事）：优秀工程师职业首选是互联网大厂，即使进入2B软件行业也优先选产品研发而非驻场开发；传统2B公司晋升机制往往让最有经验的人离开一线转做管理，恰恰背离FDE模式的初衷；国内公司普遍缺乏Palantir式的产品抽象能力，容易陷入"一次性定制开发"的陷阱。
- **合规清单是甲方TDM和乙方共同的刚需**，需要按行业细分：
  - 金融：大模型调用金融数据时面临多级隔离限制（数据不出域管控），导致"数据→模型→业务"链路被层层管控切断
  - 政务/国企：数据在内网闭环流转，结合精细化的桌面控制与权限隔离机制，确保敏感信息不出"围墙"；通过成熟的审计系统，AI智能体每一次点击、每一条决策链路均可回溯，符合国家对关键信息基础设施的监管标准
- **本土化叙事对比（读者最容易共情的部分）**：美国大企业的ERP、CRM体系经过多年沉淀相对完善，AI更像是在精密机器上加装智能大脑；而国内大量企业更像"对话驱动"，需求以非结构化方式提出，流程常常写在默契和人情里而不是系统里——这既增加落地难度，也带来跳过传统信息化阶段直接上AI的"跳级机会"。
- **付费习惯的核心矛盾（甲方BDM和乙方经营者都要面对）**：Palantir的早期客户是CIA、NSA等情报机构，单个合同动辄数千万美元，客户关注价值而非成本；反观国内客户经常要求"买一送三"，人天单价十年未涨甚至下降，这种环境下深度定制的经济模型难以成立——这是中国实践篇必须诚实面对、而非回避的结构性差异。

**三大行业的差异化锚点（建议按行业拆分小节）**

| 行业          | 核心关切               | 关键信息                                                     |
| ------------- | ---------------------- | ------------------------------------------------------------ |
| 金融          | 合规红线优先于效果     | 银行基本要求大模型私有化部署，通过统一平台管理算力、私域数据与模型能力 |
| 制造业        | 零容错场景下的责任机制 | "责任留痕"机制——操作员勾选"采纳"，系统自动生成事后复核记录，做到每一步可追溯可审计 |
| 政务/公共事业 | 自主可控是一票否决项   | 硬指标是信创适配认证，必须支持私有化部署确保敏感数据不出内网，且很多政务系统开发年代久远无法提供API，需要额外的视觉识别操作能力 |

------

## AI篇（第15–16章）：Echo视角谈成项目 vs Delta视角做成项目

**读者的核心疑问**

- **Echo（业务/商务侧）视角——甲乙共识与成熟度评估**：核心疑问是"怎么判断客户/自己是否已经到了能做FDE项目的成熟度"。一个可参考的判断标准是：如果客户是自助型、技术不复杂的买家，不需要深度定制集成，就还不需要专职FDE；如果还在验证产品是否成立的阶段，也不适合现在投入部署专项人才——这个判断框架可以直接改写成甲方自评清单。
- **Echo最需要的谈判/共识工具**：价值定价模式下，甲方在效果未出来的初期投入成本较小，乙方却很被动，只有真正产生可衡量价值才能获利——这一矛盾需要在合同条款设计层面给出具体解法，而不是停留在原则陈述。
- **Delta（技术侧）视角——技术栈与场景选择的问题**：国内主流企业Agent平台已形成多类技术路线，各有侧重，Delta篇需要给出选型对照表；同时要明确回答"我们公司规模不大，也适合用Agent吗"这类高频疑问。
- **SOP层面的具体最佳实践（Delta最实操的部分）**：蚂蚁集团采用PEER模式（计划、执行、表达、评价四个Agent协作）完成投研分析任务；平安壹钱包设计规划者、观察者、决策者三个Agent自动执行信贷审批，效率提升约40%，差错率下降超过60%；某制造业设备监测平台引入Workflow架构，将故障响应时间由平均2小时缩短至15分钟——这类具体到工作流拆解粒度的案例最贴近"SOP 9"这类实操清单的定位。
- **AI辅助FDE本身工作方式的变化（TDM和乙方都关心的元问题）**：过去FDE需要花三天时间写代码、调界面，现在AI辅助下可能只需要三十分钟做"逻辑调优"，AI负责底层复杂性，FDE只需要负责定义问题和最后确认——这是AI篇最能体现"为什么现在做FDE比五年前门槛更低、但要求也更高"的核心论点。

------

## 附录（A–G）：官方来源、技术栈清单、术语表、研讨题

这部分本身不太需要单独的读者疑问调研，但从前面各篇高频出现的分歧点来看，建议附录额外覆盖：

- **一份"甲乙方术语对照表"**：同一个词在甲方和乙方语境里含义经常不同（比如"结果""交付""驻场"），这是贯穿全书的高频摩擦点，值得单独列一张对照表而不是散落在各章。
- **合规速查表按行业分列**（金融/制造/政务三行业各自的红线条款），方便TDM和合规负责人直接查阅而不必翻正文。
- **课后研讨题建议按角色设计**：比如"如果你是HR总监，你会如何设计FDE团队进场后的组织沟通机制"，让不同角色读者都能在附录找到属于自己的思考题，而不是所有角色共用一套通用问题。

------

## 七篇框架之外，建议额外补充的维度

调研中发现几类问题反复出现、但不太适合塞进现有任何一篇，建议单独考虑：

1. **甲乙方视角对照——建议作为贯穿全书的"专栏"而非独立章节**：每篇结尾加一个"同一个问题，甲方怎么问、乙方怎么答"的对照小节，因为中国FDE实践中，组织内部的权责博弈往往比技术方案本身更复杂，这种张力在每一篇里都会以不同形式出现（认知篇是"什么是FDE"，流程篇是"谁验收"，团队篇是"谁的岗位会被替代"）。
2. **失败案例专题**：目前七篇框架里没有明确位置放"失败复盘"，但这恰恰是读者信任度最高的内容类型。一位一线FDE口述了一个千万级大单因迟迟无法验收陷入瘫痪的真实案例，这类"反高潮"叙事比纯正面案例更有说服力，建议在流程篇或中国实践篇之间插入一个独立的失败案例小节。
3. **"真假FDE"鉴别工具**：如何区分真正的forward deployed engineer和"换了个牌子的人力外包"是贯穿标杆篇、团队篇、中国实践篇的一条暗线，建议提炼成一份可复用的鉴别清单，单独放在认知篇末尾或作为附录的独立条目。
4. **HR专属章节的必要性**：目前团队篇把HR并入"人才培养"讨论，但从调研看，HR总监的关切点（组织设计、员工心理、绩效体系重构）和TDM的关切点（技术团队搭建）差异很大，如果书的目标读者明确包含HR总监，建议团队篇内部至少分出一个独立小节而不是合并论述。

如果需要，我可以针对某一篇（比如流程篇的SOP细节，或中国实践篇的三行业合规清单）再做一轮更深的定向调研，产出可以直接用于写作的素材包。



# FDE 图书调研 —— 引用资料链接汇总

> 按调研报告中出现的顺序 / 主题分组整理，供教材编写组核对信源、扩展阅读使用。 所有链接均为公开网络资料，抓取时间为 2026 年 8 月。

------

## 一、FDE 概念背景 / 全球趋势

1. Forbes Council《Beyond The Proof Of Concept: How Forward Deployed Engineering Accelerates Enterprise AI Adoption》 https://www.forbes.com/councils/forbestechcouncil/2026/02/10/beyond-the-proof-of-concept-how-forward-deployed-engineering-accelerates-enterprise-ai-adoption/
2. Deloitte《Forward Deployed Engineering》官方服务页 https://www.deloitte.com/us/en/services/consulting/services/forward-deployed-engineering.html
3. Tredence《Forward Deployed Engineers: Enterprise AI's New Front Line》 https://www.tredence.com/blog/forward-deployment-engineers-the-new-front-line-of-enterprise-ai
4. Hatchworks《What Is a Forward Deployed Engineer? The Model Getting Enterprise AI Into Production》 https://hatchworks.com/blog/fde/forward-deployed-engineer/
5. FDE Academy 官网 https://fde.academy/
6. FDE Academy《Why Every AI Startup Needs a Forward Deployed Engineer (FDE)》 https://fde.academy/blog/why-every-ai-startup-needs-a-forward-deployed-engineer
7. techscoop（Substack）《Why Forward Deployed Engineers Are Becoming the Delivery Layer for Enterprise AI》 https://techscoop.substack.com/p/why-forward-deployed-engineers-are

------

## 二、企业AI决策者关切（BDM/TDM 通用）

1. Forbes Council《Why Enterprise AI Agent Adoption Is A Socio-Technical Challenge》 https://www.forbes.com/councils/forbesbusinesscouncil/2026/07/24/why-enterprise-ai-agent-adoption-is-a-socio-technical-challenge/
2. World Economic Forum《Here's how to pick the right AI agent for your organization》 https://www.weforum.org/stories/2025/05/ai-agents-select-the-right-agent/
3. National CIO Review《Why Navigating Agentic AI Adoption Is Now a Decision Leadership Test for CIOs》 https://nationalcioreview.com/articles-insights/why-navigating-agentic-ai-adoption-is-now-a-decision-leadership-test-for-cios/
4. HackerNoon《Why AI Agents Fail in Enterprise Decision-Making》 https://hackernoon.com/why-ai-agents-fail-in-enterprise-decision-making
5. CIO.com《How AI agents are turning enterprise apps into decision systems》 https://www.cio.com/article/4187315/how-ai-agents-are-turning-enterprise-apps-into-decision-systems.html
6. TechIntelPro《AI in Decision-Making: What It Means for Enterprise Leaders》 https://techintelpro.com/articles/ai-in-decision-making-what-it-means-for-enterprise-leaders
7. iianalytics《The Enterprise AI Adoption Gap》 https://iianalytics.com/community/blog/the-enterprise-ai-adoption-gap-why-adoption-fails-before-training-begins
8. arXiv《Domain Adaptable Prescriptive AI Agent for Enterprise》 https://arxiv.org/pdf/2407.20447
9. arXiv《A Conceptual Model for AI Adoption in Financial Decision-Making...SMEs》 https://arxiv.org/pdf/2512.04339

------

## 三、中国 FDE 市场概览 / 政策信号

1. 新浪科技（同 IDC）《FDE在中国火了，Agent实施服务的真正考验在哪儿？》 https://finance.sina.com.cn/tech/roll/2026-08-06/doc-inimksmi0612418.shtml
2. 百度百科《前沿部署工程师(FDE)》 [https://baike.baidu.com/item/%E5%89%8D%E6%B2%BF%E9%83%A8%E7%BD%B2%E5%B7%A5%E7%A8%8B%E5%B8%88(FDE)/67210101](https://baike.baidu.com/item/前沿部署工程师(FDE)/67210101)
3. 中华网《FDE 如何帮助企业 AI 落地》 https://tech.china.com/articles/20260811/202608111938351.html
4. IDC 官方博客《FDE 在中国火了，Agent 实施服务的真正考验在哪儿？》 [https://www.idc.com/resource-center/blog/fde-%E5%9C%A8%E4%B8%AD%E5%9B%BD%E7%81%AB%E4%BA%86%EF%BC%8Cagent-%E5%AE%9E%E6%96%BD%E6%9C%8D%E5%8A%A1%E7%9A%84%E7%9C%9F%E6%AD%A3%E8%80%83%E9%AA%8C%E5%9C%A8%E5%93%AA%E5%84%BF%EF%BC%9F/](https://www.idc.com/resource-center/blog/fde-在中国火了，agent-实施服务的真正考验在哪儿？/)
5. FDE百科《什么是 FDE...定义、能力模型与中国落地指南》 https://fdebaike.com/what-is-fde/
6. 于德辉（网站）《中国AI现场部署服务（FDE）行业白皮书》 https://yudehui.cn/
7. 钱拓科技官网（FDE 金融 AI 服务商案例） https://www.aioai.cc/

------

## 四、甲方/乙方视角差异

1. 阿里云帮助中心《阿里云FDE大模型技术服务》 https://help.aliyun.com/zh/document_detail/3030376.html
2. 知乎《硅谷兴起 FDE 模式：AI 能力狂飙却部署迟缓...》 https://zhuanlan.zhihu.com/p/1948843698046625735
3. 智源社区（BAAI）《AI-Native 组织落地和 FDE 到底怎么做，我们跟五位一线创业者聊了聊》 https://hub.baai.ac.cn/view/56554
4. CSDN《实战分享：某纺织制造企业智能制造平台架构的ROI提升案例》 https://blog.csdn.net/2502_92631100/article/details/151798887
5. 知乎《最近硅谷爆火的岗位 FDE 到底是什么？一文带你搞懂它》 https://zhuanlan.zhihu.com/p/2042658306733372164
6. CSDN《【干货收藏】企业智能体从0到1：15个关键成功要素指南！》 https://blog.csdn.net/2401_85390073/article/details/151820286
7. CSDN（智能体开发者社区）《AI Agent可以做哪些工作，企业级智能体如何重塑业务流与生产力？》 https://adg.csdn.net/6a6b72e1662f9a54cb966123.html
8. 腾讯云开发者社区《FDE 模式：硅谷新热潮，在国内水土不服吗？》 https://cloud.tencent.com/developer/article/2618954
9. 知乎《FDE不是"高级外包"——AI时代，客户成功的终局是知识蒸馏》 https://zhuanlan.zhihu.com/p/2044730994671014468
10. 知乎《驻场：FDE的工作方法》 https://zhuanlan.zhihu.com/p/2067513588160452478
11. 36氪《前线共创，双向赋能：FDE 模式行业观察与实践报告》 https://www.36kr.com/p/3926404419910018
12. 知乎《信任工程：FDE如何进入制造业的零容错世界》 https://zhuanlan.zhihu.com/p/2066413546297102618
13. 虎嗅《中国FDE真实图景：AI落地遭遇组织权责博弈与用户习惯困境》 https://www.huxiu.com/article/4873792.html
14. 虎嗅《FDE岗位概念在中国AI落地中再度兴起，面临市场认知与预算挑战》 https://www.huxiu.com/article/4869111.html
15. 知乎《从写代码到翻译业务：IT人员的FDE转型自我诊断框架》 https://zhuanlan.zhihu.com/p/2069359808193598626
16. 证券时报（网）《大厂正在花百万年薪抢人，FDE到底是什么？》 https://www.stcn.com/article/detail/3994532.html
17. NewMax《FDE企业落地方法论：从专家知识到SOP》 https://newmax.cc/share/fde-enterprise-implementation-guide

------

## 五、HR / 组织变革相关

1. 知乎《HR进入AI时代，这3个关键动作，决定组织AI HR转型能走多远》 https://zhuanlan.zhihu.com/p/1976293429060330671
2. CSDN《AI 重塑人力资源：HR 职能的进化与实践》 https://blog.csdn.net/2501_93602066/article/details/155777496
3. Microsoft Copilot《适用于 HR 的 AI：一种变革性方法》 https://www.microsoft.com/zh-cn/microsoft-copilot/copilot-101/ai-for-hr
4. 知乎《大咖谈：生成式AI在人力资源各个不同场景的应用及对HR高管的重要性》 https://zhuanlan.zhihu.com/p/654154286
5. 易路《HR应该如何推进AI在企业人力资源的落地应用》 https://www.ersoft.com/news-GxU1Nwkl6.html
6. peoplus（易路）《从"想做好"到"做得好"企业HR 应如何推进AI应用在企业的落地？》 https://newws.peoplus.cn/news-d1uevIJyO.html

------

## 六、行业案例：金融

1. 53AI《国内银行业大模型应用落地调研》 https://www.53ai.com/news/qianyanjishu/191.html
2. 电子工程专辑《金融信创70个典型案例集》 https://www.eet-china.com/mp/a159475.html
3. 新浪财经《近9万字，覆盖全行业，金融信创白皮书重磅发布！》 https://finance.sina.com.cn/roll/2024-10-29/doc-incuetki4731391.shtml
4. 深信服《四川天府银行携手深信服打造安全数字化办公空间》 https://www.sangfor.com.cn/case/1680146333488
5. 广州鼎甲《案例合集｜赋能金融行业，金融信创灾备首选鼎甲》 https://www.scutech.com/?p=15943
6. 发现报告《2025年数字金融信创研究报告》 https://www.fxbaogao.com/detail/5117123
7. IDC《AI原生开启金融智能新未来——金融行业大模型应用落地白皮书》（PDF） [https://aigc.idigital.com.cn/djyanbao/%E3%80%90IDC%E3%80%91%E9%87%91%E8%9E%8D%E8%A1%8C%E4%B8%9A%E5%A4%A7%E6%A8%A1%E5%9E%8B%E5%BA%94%E7%94%A8%E8%90%BD%E5%9C%B0%E7%99%BD%E7%9A%AE%E4%B9%A6%EF%BC%9AAI%E5%8E%9F%E7%94%9F%E5%BC%80%E5%90%AF%E9%87%91%E8%9E%8D%E6%99%BA%E8%83%BD%E6%96%B0%E6%9C%AA%E6%9D%A5-2025-09-02.pdf](https://aigc.idigital.com.cn/djyanbao/【IDC】金融行业大模型应用落地白皮书：AI原生开启金融智能新未来-2025-09-02.pdf)

------

## 七、行业案例：政府 / 公共事业

1. 安恒信息《政府_客户案例》 https://www.dbappsecurity.com.cn/case/list208_233.html
2. 搜狐《2026 国产化 AI Agent 平台选购避坑指南》 https://www.sohu.com/a/1028144523_122743141
3. 实在智能《政务智能体平台哪家强？2026政务Agent选型指南》 https://www.ai-indeed.com/encyclopedia/15331.html
4. 实在智能《国企/政务单位能引入AI智能体吗？合规性有保障吗？》 https://www.ai-indeed.com/encyclopedia/18552.html
5. CSDN《AI大模型应用：政务大模型落地案例分析》 https://blog.csdn.net/m0_59164304/article/details/143634015
6. 东方财富证券研究报告《AI+政务：最具执行力的AI 应用落地方向》（PDF） https://pdf.dfcfw.com/pdf/H3_AP202504261662908517_1.pdf
7. Kingsware《DeepSeek热潮下，探索智慧政务的N种可能》 https://www.kingsware.cn/hangyezixunBZJ/191

------

## 八、Palantir / Ontology 标杆研究

1. 《Palantir AIP Ontology 深析》 https://wwwweeia.github.io/palantir-aip-study/01-palantir-aip-ontology.html
2. 博客园《Ontology 如何构建企业数字世界：Palantir 技术原理》 https://www.cnblogs.com/jarryli/p/20036215
3. 腾讯新闻《从Palantir到FDE热潮，AI如何真正进入企业组织》 https://news.qq.com/rain/a/20260518A0004300
4. 知乎《为什么 Palantir 十几年前就在用的 FDE 模式，现在才被整个行业重新重视？》 https://www.zhihu.com/question/2047820512374657595
5. 知乎《Palantir 创始工程师深度分享：FDE 模式是 Agent 时代的 PMF 范式》 https://zhuanlan.zhihu.com/p/1961540910274842935
6. 知乎《什么是Ontology本体论数据结构？Palantir 技术原理解析》 https://zhuanlan.zhihu.com/p/2038007854565675689
7. 知乎《Palantir 学习笔记：2.1.12 FDE -- 深度解读》 https://zhuanlan.zhihu.com/p/2036373013927555310
8. 知乎《AI时代的大数据底层结构：Palantir Ontology深度解析》 https://zhuanlan.zhihu.com/p/2035489195578405285
9. 工业智能算网《深度拆解 Palantir 的 FDE 模式：为何"重服务"才是 AI 时代高毛利的终极路径？》 https://gyznsw.cn/2026/04/24/palantir-fde-model-services-as-software-20260424/

------

## 九、中国云厂商格局

1. 国际电子商情《2025年第一季度，中国云基础设施市场加速增长...》 https://www.esmchina.com/marketnews/54374.html
2. OFweek云计算网《云计算盘点：阿里云、腾讯云、字节云》 https://cloud.ofweek.com/news/2023-04/ART-178801-8500-30593145.html
3. 21经济网《阿里字节，谁是"云"第一？》 https://www.21jingji.com/article/20251029/herald/45de7f0edef0da619ec6279c539d248e.html
4. 数据观《"东数西算"强势爆发！腾讯、华为、阿里等巨头披露布局》 https://www.cbdio.com/BigData/2022-02/21/content_6167822.htm
5. 国信证券经济研究所《海内外云厂商发展与现状（一）》（PDF） https://pdf.dfcfw.com/pdf/H3_AP202502171643158494_1.pdf
6. 中国信息化周报《中国"云"出海 赢在新思路》 https://www.cio360.net/show-611-103619-1.html
7. letschuhai《国产"三朵云"出海，一场迫在眉睫的突围战？》 https://letschuhai.com/tencent-alibaba-huawei-cloud-aws-global

------

## 十、FDE 岗位热度 / 大厂招聘数据

1. 腾讯云开发者社区《FDE火了：AI落地最后一公里的人，一半是新岗位，一半是旧驻场》 https://cloud.tencent.com.cn/developer/article/2695346
2. 腾讯云开发者社区《FDE（前沿部署工程师）深度解析：AI时代最火爆的新型技术人才》 https://cloud.tencent.com/developer/article/2674646
3. 雷峰网《独家解读丨花百亿建「FDE团队」：AWS 们在走 BAT 云「定制化」老路吗？》 https://www.leiphone.com/category/industrycloud/AC2Hfio9HDh57dBk.html
4. 同花顺（财经）《大厂抢人、薪资倒挂：FDE为何成为AI落地时代的新贵？》 https://field.10jqka.com.cn/20260812/c678892815.shtml
5. 潮新闻《观智潮｜大厂抢人、薪资倒挂：FDE为何成为AI落地时代的新贵？》 https://tidenews.com.cn/news.html?id=3527834
6. 知乎《2026深度解析｜FDE前沿部署工程师：AI智能体落地时代的核心稀缺人才》 https://zhuanlan.zhihu.com/p/2055693660948264124
7. 知乎《当腾讯云开始招"前线部署工程师"：FDE 是 AI 时代的特种兵，还是高级版驻场？》 https://zhuanlan.zhihu.com/p/2052343182436963047
8. 络石智能（cnfde.com.cn）《大厂正在花百万年薪抢人，FDE到底是什么？》 https://www.cnfde.com.cn/en/knowledge/hang-ye-dong-tai/da-chang-zheng-zai-hua-bai-wan--2ritsr

------

## 十一、企业 Agent 落地流程 / SOP / 评估方法论

1. 博客园（七牛云）《2026年企业AI Agent落地实战指南：从选型到上线的完整路径》 https://www.cnblogs.com/qiniushanghai/p/19981425
2. CSDN《AI Agent技术演进与企业落地实践指南》 https://bbs.csdn.net/weixin_29061041/article/details/100233245
3. 亚马逊AWS官方博客《Agentic AI 基础设施实践经验系列（一）：Agent 应用开发与落地实践思考》 https://aws.amazon.com/cn/blogs/china/agentive-ai-infrastructure-practice-series-1/
4. 亚马逊AWS官方博客《企业级 Agentic AI 架构设计》 https://aws.amazon.com/cn/blogs/china/enterprise-level-agentic-ai-architecture-design/
5. 知乎《企业落地 AI Agent 的四大关键实践，少走90%弯路!》 https://zhuanlan.zhihu.com/p/1969433865039898472
6. 实在智能《AIAgent落地企业详细步骤》 https://www.ai-indeed.com/encyclopedia/17925.html
7. 亚马逊AWS官方博客《评估企业级智能体：从原型验证到生产就绪》 https://aws.amazon.com/cn/blogs/china/part-2-enterprise-intelligent-validation/

------

## 十二、FDE 人才培养 / 知识管理 / 能力模型

1. （同80）腾讯云开发者社区《FDE（前沿部署工程师）深度解析》 https://cloud.tencent.com/developer/article/2674646
2. 搜狐（CPDA）《FDE 火了，企业真正需要什么样的数据分析人才？》 https://www.sohu.com/a/1053394963_121124379
3. 知乎《FDE：AI时代崛起的核心技术新岗位》 https://zhuanlan.zhihu.com/p/2045083600299849053
4. 新浪新闻《FDE为何成为AI落地时代的新贵？解读落地价值与爆发逻辑》 https://k.sina.com.cn/article_7879996023_1d5af327706801lo1q.html?from=tech
5. 极客时间（geekbang）《Demo 能跑，项目却落不了地：企业真正缺的是 FDE 能力》 https://b.geekbang.org/news/1ff1de774005f8da13f42943881c655f
6. 搜狐《前线共创，双向赋能：FDE 模式行业观察与实践报告》 https://m.sohu.com/a/1059144862_455313/?pvid=000115_3w_a&scm=10001.325_13-325_13.0.0-0-0-0-0.5_1334

------

## 使用提示

- 部分链接指向知乎/搜狐/腾讯云开发者社区等平台的个人或机构专栏文章，观点性较强，建议编写组交叉核实后再引用为教材正文内容，尤其是涉及具体数字（招聘增速、薪资水平、项目金额等）的表述，最好能找到原始数据源（如 Indeed、LinkedIn 报告原文）二次核验。
- 带有 PDF 后缀的链接为研究报告类文档，部分需要下载后查看完整内容。
- 中国实践篇引用的多篇虎嗅/知乎文章包含一线从业者口述内容，人物为化名或代称，教材使用时建议注明"据受访者口述整理"等字样，避免误认为官方数据