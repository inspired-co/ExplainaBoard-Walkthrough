from __future__ import annotations
import argparse
import json
import os

from explainaboard_api_client.model.system import System
from explainaboard_api_client.model.system_create_props import SystemCreateProps
from explainaboard_api_client.model.system_metadata import SystemMetadata
from explainaboard_api_client.model.system_output_props import SystemOutputProps
from explainaboard_client import Config, ExplainaboardClient
from explainaboard_client.tasks import TaskType
from explainaboard_client.utils import generate_dataset_id



def main():

    # Parse arguments
    parser = argparse.ArgumentParser(
        description="A command-line tool to upload movie review results "
        "to the ExplainaBoard web interface."
    )
    parser.add_argument(
        "--system_name",
        type=str,
        required=True,
        help="The name of the system",
    )
    parser.add_argument(
        "--output",
        type=str,
        required=True,
        help="Path to the system output file",
    )
    parser.add_argument(
        "--dataset", type=str, help="A dataset name from DataLab"
    )
    parser.add_argument(
        "--split",
        type=str,
        required=False,
        default="test",
        help="The name of the dataset split to process",
    )
    parser.add_argument(
        "--public", action="store_true", help="Make the uploaded system public"
    )
    args = parser.parse_args()

    # Get environmental variables
    for k in ["EB_API_KEY", "EB_EMAIL", "EB_STUDENT_ID"]:
        if k not in os.environ:
            raise ValueError(f"{k} is not set")
    api_key = os.environ["EB_API_KEY"]
    email = os.environ["EB_EMAIL"]
    student_id = os.environ["EB_STUDENT_ID"]


    # Preset values by Instructor
    course_name = "fudan_nlp"
    shared_users = ['neubig@gmail.com']

    # Preset values
    task = TaskType.text_classification
    metric_names = ['Accuracy']
    source_language = 'eng'
    target_language = 'eng'
    system_name = f'{course_name}_{student_id}_{args.system_name}'
    online_split = 'validation' if args.split == 'dev' else args.split

    # Convert file
    new_file = convert_file(args.output, label_mapping)

    # Do upload
    system_output = SystemOutputProps(
        data=new_file,
        file_type='text',
    )
    metadata = SystemMetadata(
        task=task,
        is_private=not args.public,
        system_name=system_name,
        metric_names=metric_names,
        source_language=source_language,
        target_language=target_language,
        dataset_split=online_split,
        shared_users=shared_users,
        system_details={},
    )
    metadata.dataset_metadata_id = generate_dataset_id(course_name, args.dataset)
    create_props = SystemCreateProps(metadata=metadata, system_output=system_output)
    client_config = Config(
        email,
        api_key,
        environment='main',
    )
    client = ExplainaboardClient(client_config)

    result: System = client.systems_post(create_props)
    try:
        sys_id = result.system_id
        client.systems_get_by_id(sys_id)
        print(f"successfully posted system {system_name} with ID {sys_id}\n"
              f"view the result at https://explainaboard.inspiredco.ai/systems")
    except Exception:
        print(f"failed to post system {system_name}")

    # delete new_file
    os.remove(new_file)

if __name__ == "__main__":
    main()