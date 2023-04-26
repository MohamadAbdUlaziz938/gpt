import time

import openai
import yaml
from upload_data import upload_data_set
from custom_completion import custom_completion
from fine_tuning import fine_tuning
from langchain import *
from llama_index import *


if __name__ == "__main__":
    with open('../cred.yaml') as f:
        data = yaml.load(f, Loader=yaml.SafeLoader)

    openai.api_key = data["OPENAI_API_KEY"]
    # dataset_response=upload_data_set()
    # print(f'data set response: {dataset_response}' )

    dataset_response = {
        "bytes": 622,
        "created_at": 1681761712,
        "filename": "file",
        "id": "file-pRgiGZTS6ICXcMhQOwfBpW2F",
        "object": "file",
        "purpose": "fine-tune",
        "status": "uploaded",
        "status_details": None
    }

    #fine_tuning_response = fine_tuning(data_set_id=dataset_response["id"])
    #print(f'fine tuning response: {fine_tuning_response}')
    '''
    fine tuning response: {
  "created_at": 1681761925,
  "events": [
    {
      "created_at": 1681761925,
      "level": "info",
      "message": "Created fine-tune: ft-S0DSvD8plQAycDK4XlYjfWmH",
      "object": "fine-tune-event"
    }
  ],
  "fine_tuned_model": null,
  "hyperparams": {
    "batch_size": 1024,
    "learning_rate_multiplier": null,
    "n_epochs": 1000,
    "prompt_loss_weight": 0.01
  },
  "id": "ft-S0DSvD8plQAycDK4XlYjfWmH",
  "model": "davinci",
  "object": "fine-tune",
  "organization_id": "org-KT5o4mJuDaMgXHxbMlwRbeIa",
  "result_files": [],
  "status": "pending",
  "training_files": [
    {
      "bytes": 622,
      "created_at": 1681761712,
      "filename": "file",
      "id": "file-pRgiGZTS6ICXcMhQOwfBpW2F",
      "object": "file",
      "purpose": "fine-tune",
      "status": "processed",
      "status_details": null
    }
  ],
  "updated_at": 1681761925,
  "validation_files": []
}
    '''
    # check status
    '''
    while True:
        fine_tuning_status = openai.FineTune.retrieve(
            fine_tuning_response["id"])
        print(f"Status: {fine_tuning_status['status']}")

        if fine_tuning_status["status"] in ["succeeded", "failed"]:
            break

    time.sleep(60)  # Poll every 60 seconds
    print(f'fine tuning status : {fine_tuning_status}')
    '''
    # response of success fine tuning
    '''
    fine tuning status : {
  "created_at": 1681761925,
  "events": [
    {
      "created_at": 1681761925,
      "level": "info",
      "message": "Created fine-tune: ft-S0DSvD8plQAycDK4XlYjfWmH",
      "object": "fine-tune-event"
    },
    {
      "created_at": 1681762340,
      "level": "info",
      "message": "Fine-tune costs $3.54",
      "object": "fine-tune-event"
    },
    {
      "created_at": 1681762340,
      "level": "info",
      "message": "Fine-tune enqueued. Queue number: 0",
      "object": "fine-tune-event"
    },
    {
      "created_at": 1681762343,
      "level": "info",
      "message": "Fine-tune started",
      "object": "fine-tune-event"
    },
    {
      "created_at": 1681762515,
      "level": "info",
      "message": "Completed epoch 256/1000",
      "object": "fine-tune-event"
    },
    {
      "created_at": 1681762525,
      "level": "info",
      "message": "Completed epoch 512/1000",
      "object": "fine-tune-event"
    },
    {
      "created_at": 1681762537,
      "level": "info",
      "message": "Completed epoch 768/1000",
      "object": "fine-tune-event"
    },
    {
      "created_at": 1681762589,
      "level": "info",
      "message": "Uploaded model: davinci:ft-personal-2023-04-17-20-16-28",
      "object": "fine-tune-event"
    },
    {
      "created_at": 1681762590,
      "level": "info",
      "message": "Uploaded result file: file-yuQyvGwN2OPG0Yo6fFlJr41r",
      "object": "fine-tune-event"
    },
    {
      "created_at": 1681762590,
      "level": "info",
      "message": "Fine-tune succeeded",
      "object": "fine-tune-event"
    }
  ],
  "fine_tuned_model": "davinci:ft-personal-2023-04-17-20-16-28",
  "hyperparams": {
    "batch_size": 1024,
    "learning_rate_multiplier": 0.2,
    "n_epochs": 1000,
    "prompt_loss_weight": 0.01
  },
  "id": "ft-S0DSvD8plQAycDK4XlYjfWmH",
  "model": "davinci",
  "object": "fine-tune",
  "organization_id": "org-KT5o4mJuDaMgXHxbMlwRbeIa",
  "result_files": [
    {
      "bytes": 374,
      "created_at": 1681762590,
      "filename": "compiled_results.csv",
      "id": "file-yuQyvGwN2OPG0Yo6fFlJr41r",
      "object": "file",
      "purpose": "fine-tune-results",
      "status": "uploaded",
      "status_details": null
    }
  ],
  "status": "succeeded",
  "training_files": [
    {
      "bytes": 622,
      "created_at": 1681761712,
      "filename": "file",
      "id": "file-pRgiGZTS6ICXcMhQOwfBpW2F",
      "object": "file",
      "purpose": "fine-tune",
      "status": "processed",
      "status_details": null
    }
  ],
  "updated_at": 1681762590,
  "validation_files": []
}
    '''
    fine_tuning_status = openai.FineTune.retrieve(
            "ft-S0DSvD8plQAycDK4XlYjfWmH")
    print(fine_tuning_status)
    custom_completion(prompt="What is a variable in programming?", model_name="davinci:ft-personal-2023-04-17-20-16-28")
    #custom_completion(prompt="How do you create a function in Python?", model_name="davinci:ft-personal-2023-04-17-20-16-28")
