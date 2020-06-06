.PHONY: all clean test

TRAIN_URL = 'https://s3.ap-south-1.amazonaws.com/datahack-prod/train_file/Train_UWu5bXk.csv

TEST_URL = 'https://s3.ap-south-1.amazonaws.com/datahack-prod/test_file/Test_u94Q5KV.csv'

all: reports/figures/exploratory.png models/random_forest.model

clean:
	rm -f data/raw/*.csv
	rm -f data/processed/*.pickle
	rm -f data/processed/*.xlsx
	rm -f reports/figures/*.png
	rm -f models/*.model

data/raw/train.csv:
	python src/data/download.py $(TRAIN_URL) $@

data/raw/test.csv:
	python src/data/download.py $(TEST_URL) $@	
	
data/processed/processed.pickle: data/raw/iris.csv
		python src/data/preprocess.py $< $@ --excel data/processed/processed.xlsx
	
reports/figures/exploratory.png: data/processed/processed.pickle
	python src/visualization/exploratory.py $< $@


test: all
	pytest src

models/random_forest.model: data/processed/processed.pickle
	python src/models/train_model.py $< $@