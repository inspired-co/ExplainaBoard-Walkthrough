# ExplainaBoard for Fudan NLP Class



### Environment Setup
* Linux and MacOS are encouraged to use. If you use Windows OS, see [how to work as linux
in Windows](https://github.com/inspired-co/ExplainaBoard-Walkthrough/blob/main/roles/instructors/install_helper.md#how-to-use-linux-in-windows-os)
* Python >= 3.9 is required. If you need help to install python3.9, see this [doc](https://github.com/inspired-co/ExplainaBoard-Walkthrough/blob/main/roles/instructors/install_helper.md#how-to-install-python39-in-linux).


### ExplainaBoard Install
Once you have set up an python (>=3.9) environment, one line to install ExplainaBoard Client
 
```shell script
pip install explainaboard_client
```

You can use the following command to test whether the package has been successfully installed in your
machine:

```shell script
python -m explainaboard_client.__main__
```
If `ExplainaBoard CLI` is printed, congratulation, you make it!


## ExplainaBoard Submission for Homework1

#### Step 1: System output Preparation
You need organize the predicted results (e.g., positive or negative) from your system
 on test or validation into a text file, where
 * each row represent a predicted label
 * the number of rows should equals the number of samples in test or validation set.

Here is one [example output file](./data/baseline_predictions.txt) of a baseline system.


#### Step 2: System submission
To submit your outputs via [ExplainaBoard](https://explainaboard.inspiredco.ai), first
click the top-right of the site to log in, and then again click the top-right to view
your API key. Run the following to save your email and API key to environmental
variables:

```
export EB_EMAIL=your_email_used_for_explainaboard
export EB_API_KEY=your_api_key_for_explainaboard
export EB_STUDENT_ID=your_student_id
```

Now you can upload the outputs of your model with the `upload_results.py` script. There
are the following options.

* `--system_name` a name that you can choose for your system. Your final system name
  will be `anlp_{studentid}_{system_name}`.
* `--dataset` the dataset name (e.g., mr).
* `--split` the split (validation/test).
* `--output` the system output you're uploading.
* `--public` if you want your output listed on the public site so people in the class
  can compare and contrast with it add this flag. But it is off by default (and has no
  effect on your grade).

Here is an example of uploading all of the datasets with a system name of `baseline`.

```
python upload_results.py --system_name baseline --dataset mr --split validation --output mr-dev-output.txt
python upload_results.py --system_name baseline --dataset mr --split test --output mr-test-output.txt
```

You can then go to the ExplainaBoard [systems page](https://explainaboard.inspiredco.ai/systems) to confirm
that the results are uploaded properly.

