# ExplainaBoard for Fudan NLP Class



## ExplainaBoard Submission for Homework1

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
* `--dataset` the dataset name (sst/cfimdb).
* `--split` the split (dev/test).
* `--output` the system output you're uploading.
* `--public` if you want your output listed on the public site so people in the class
  can compare and contrast with it add this flag. But it is off by default (and has no
  effect on your grade).

Here is an example of uploading all of the datasets with a system name of `baseline`.

```
python upload_results.py --system_name baseline --dataset sst --split dev --output sst-dev-output.txt
python upload_results.py --system_name baseline --dataset sst --split test --output sst-test-output.txt
```

You can then go to the ExplainaBoard systems page to confirm that the results are
uploaded properly.



## ExplainaBoard Submission for Homework2