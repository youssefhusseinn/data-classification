from constants import *
from dataset_reader import DataReader
from factory import Factory
import numpy as np
import time
from shutil import rmtree


if __name__ == '__main__':
    try:
        rmtree(OUTPUT_PATH)
    except:
        pass
    dataset = DataReader(DATASET_PATH)
    dataset_extract = dataset.read()
    samples, labels = np.array(dataset_extract[0]), np.array(dataset_extract[1])
    factory = Factory()
    times = [time.time()]
    for classifier_name in CLASSIFIERS:
        classifier = factory.get(classifier_name, samples, labels)
        print(f'start training {classifier_name}')
        classifier.train()
        cur = time.time()
        print((cur-times[-1]))
        times.append(cur)
    print(f'total time = {(times[-1]-times[0])}')
