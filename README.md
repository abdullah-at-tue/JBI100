## Local installation
1. Requirements: 
   * Python 3.12
   * Required modules installed
     * Do that by running `python -m pip -r requirements.txt`
2. Add the dataset to `./main/dataset` with the name `dataset.csv`
   * You can find meaning of the dataset attributes in `./main/dataset/case_detail_data_dictionary.pdf`
   * There is a jupyter notebook in `./main/dataset` to get familiarized with the dataset we are using
3. Run `dev.py` with `python dev.py` to run the web application

## Dataset
- Processed (301MB): https://dev-icp.s3.eu-central-1.amazonaws.com/VIS/dataset_processed.csv
- Unprocessed (264MB): https://dev-icp.s3.eu-central-1.amazonaws.com/VIS/dataset_unprocessed.csv

## Production
If you just want to take a look without running it locally, you can have a look at https://jbi100.abdullahalhariri.com 
