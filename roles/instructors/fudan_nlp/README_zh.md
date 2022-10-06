# ExplainaBoard: 复旦大学自然语言处理课程 [[English]](README.md)



### 环境设置
* 建议使用Linux和MacOS。如果您使用Windows操作系统, 可以参照[这个教程](https://github.com/inspired-co/ExplainaBoard-Walkthrough/blob/main/roles/instructors/install_helper.md#how-to-use-linux-in-windows-os)这个教程，
实现在Windows上对Linux系统的安装
* Python >= 3.9是必需的。如果您需要帮助来安装python3.9, 参照 [这个教程](https://github.com/inspired-co/ExplainaBoard-Walkthrough/blob/main/roles/instructors/install_helper.md#how-to-install-python39-in-linux).


### ExplainaBoard 安装
设置好 python(>=3.9) 环境后，只需一行即可安装 ExplainaBoard Client
 
```shell script
pip install explainaboard_client
```

您可以使用以下命令来测试是否已成功安装在您的机器上:

```shell script
python -m explainaboard_client.__main__
```
如果输出 `ExplainaBoard CLI` , 恭喜你，你成功了!


## 通过 ExplainaBoard 提交作业一

#### 步骤1:准备模型的预测结果文件
你需要将模型在测试集(test)或者验证集(development)的预测结果组织成如下格式的文件：
* 每一行代表一个预测标签(positive 或者 negative)
* 行数应等于测试或验证集中的样本数。

这里有个[样例]((./data/mr-test-baseline.txt))。



#### 步骤2:预测结果文件提交
要通过提交您的输出，首先单击[ExplainaBoard](https://explainaboard.inspiredco.ai)网站的右
上角`登录(Log in)`，登陆后再次单击右上角查看您的API密钥 (API Key)。
然后就可以运行以下命令将您的电子邮件和API密钥保存为环境变量:

```
export EB_EMAIL=your_email_used_for_explainaboard
export EB_API_KEY=your_api_key_for_explainaboard
export EB_STUDENT_ID=your_student_id
```

现在您可以使用`upload_results.py`脚本上传模型的输出。有以下选项。
* `--system_name` 模型的名字。最终的模型名称为：`fudan_nlp_ {studentid} _ {system_name}`。
* `--dataset` 数据集名称(作业一里应为：`mr`)。
* `--split` 拆分(验证/测试)。
* `--output` 你上传的模型预测结果文件。
* `--public` 如果你想让你的结果为公开可见，这样班上的人可以与它进行比较和对比，就添加这个标志。但是默认情况下它是关闭的(并且没有
影响你的成绩)。




下面是一个上传系统名为`baseline`的模型预测结果文件示例。

```
python upload_results.py --system_name baseline --dataset mr --split validation --output mr-dev-output.txt
python upload_results.py --system_name baseline --dataset mr --split test --output mr-test-output.txt
```
运行上述命令后，你就可以直接在[网站]((https://explainaboard.inspiredco.ai/systems))上看到你的结果，
以及更能帮助你的模型优点、不足之处的分析。

请结合ExplainaBoard提供的细粒度分析结果，提交简单的对模型进一步分析的报告，比如：
* 模型的擅长处理哪一类样本？
* 你的模型相对于给定的对比模型优劣势在哪？提升显著吗？


