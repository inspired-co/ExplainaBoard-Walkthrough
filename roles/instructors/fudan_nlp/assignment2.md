# ExplainaBoard: 复旦大学自然语言处理课程


## 数据介绍
* [训练集](./data/conll2003/train.txt)
* [校验集](./data/conll2003/dev.txt)
* [测试集](./data/conll2003/test.txt)



## 环境设置
* 建议使用Linux和MacOS。如果您使用Windows操作系统, 可以参照[这个教程](https://github.com/inspired-co/Inspired-walkthroughs/blob/main/roles/instructors/install_helper.md#how-to-use-linux-in-windows-os)这个教程，
实现在Windows上对Linux系统的安装
* Python >= 3.9是必需的。如果您需要帮助来安装python3.9, 参照 [这个教程](https://github.com/inspired-co/Inspired-walkthroughs/blob/main/roles/instructors/install_helper.md#how-to-install-python39-in-linux).


### ExplainaBoard 安装 (注意：和作业一稍有差异)
设置好 python(>=3.9) 环境后，只需一行即可安装 ExplainaBoard Client
 
```shell script
pip install --upgrade --force-reinstall explainaboard_client==0.0.10 explainaboard_api_client==0.2.13
```

您可以使用以下命令来测试是否已成功安装在您的机器上:

```shell script
python -m explainaboard_client.__main__
```
如果输出 `ExplainaBoard CLI` , 恭喜你，你成功了!


## 通过 ExplainaBoard 提交作业二

#### 步骤1:准备模型的预测结果文件
你需要将模型在测试集(test)或者验证集(development)的预测结果组织成json 或者conll的格式，
* [json格式样例](./data/conll2003/result.json)
* [conll格式样例](./data/conll2003/result.txt)

注意：务必保证和测试样本数目严格对齐





#### 步骤2:预测结果文件提交
要通过提交您的输出，首先单击[ExplainaBoard](https://explainaboard.inspiredco.ai)网站的右
上角`登录(Log in)`，登陆后再次单击右上角查看您的API密钥 (API Key)。
然后就可以运行以下命令将您的电子邮件和API密钥保存为环境变量:

```
export EB_USERNAME="[your username]"
export EB_API_KEY="[your API key]"
```
注意: `EB_USERNAME` 是自己的注册邮箱


下面是一个上传系统名为`baseline`的模型，其[结果文件](./data/conll2003/result.json)为json格式。

```shells
python -m explainaboard_client.cli.evaluate_system \
  --task named-entity-recognition \
  --system-name fudan_studentid_baseline \
  --dataset fudan_nlp \
  --sub-dataset conll2003 \
  --split test \
  --system-output-file ./data/conll2003/result.json \
  --system-output-file-type json \
  --shared-users blzhu20@fudan.edu.cn xjhuang@fudan.edu.cn \
  --source-language eng
```
注意：
* 请把`fudan_studentid_baseline` 中的`studentid` 改为你的学生id。
* `fudan_studentid_baseline` 中的 `baseline`可以为任意名字
* 别忘记在shared-users里添加助教和授课老师的邮箱


你也可以把你的系统输出文件打印成conll格式的[结果文件](./data/conll2003/result.txt)，那么，提交命令如下：

```shells
python -m explainaboard_client.cli.evaluate_system \
  --task named-entity-recognition \
  --system-name fudan_studentid_baseline \
  --dataset fudan_nlp \
  --sub-dataset conll2003 \
  --split test \
  --system-output-file ./data/conll2003/result.txt \
  --system-output-file-type conll \
  --shared-users blzhu20@fudan.edu.cn xjhuang@fudan.edu.cn \
  --source-language eng
```


运行上述命令后，你就可以直接在[网站]((https://explainaboard.inspiredco.ai/systems))上看到你的结果 (
或者直接进入[leaderboard榜单](https://explainaboard.inspiredco.ai/leaderboards?show_mine=false&sort_dir=desc&sort_field=created_at&dataset=fudan_nlp)
)
以及更能帮助你的模型优点、不足之处的分析。
* 提示：对于校验集(validation)的测试结果，你可以利用ExplainaBoard进行case analysis （通过点击柱形图种的每一个柱子）

请结合ExplainaBoard提供的细粒度分析结果，提交简单的对模型进一步分析的报告，比如：
* 模型的擅长处理哪一类样本？
* 你的模型相对于给定的对比模型优劣势在哪？提升显著吗？


