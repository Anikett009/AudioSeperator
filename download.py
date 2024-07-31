import os
import random
import numpy as np

def mir1k_train_test_split(mir1k_dir, train_valid_test_ratio=[0.8, 0.1, 0.1], random_seed=0):
    assert len(train_valid_test_ratio) == 3
    assert np.sum(train_valid_test_ratio) == 1

    random.seed(random_seed)

    wavs_dir = os.path.join(mir1k_dir, 'UndividedWavfile')

    wav_filenames = []
    for file in os.listdir(wavs_dir):
        if file.endswith('.wav'):
            wav_filenames.append(os.path.join(wavs_dir, file))

    random.shuffle(wav_filenames)
    num_samples = len(wav_filenames)
    train_split = int(num_samples * train_valid_test_ratio[0])
    valid_split = train_split + int(num_samples * train_valid_test_ratio[1])

    train_path = os.path.join(mir1k_dir, 'train.txt')
    valid_path = os.path.join(mir1k_dir, 'valid.txt')
    test_path = os.path.join(mir1k_dir, 'test.txt')

    with open(train_path, 'w') as text_file:
        for i in range(0, train_split):
            text_file.write(wav_filenames[i] + '\n')

    with open(valid_path, 'w') as text_file:
        for i in range(train_split, valid_split):
            text_file.write(wav_filenames[i] + '\n')

    with open(test_path, 'w') as text_file:
        for i in range(valid_split, num_samples):
            text_file.write(wav_filenames[i] + '\n')

    return train_path, valid_path, test_path

if __name__ == '__main__':
    # Update this path to the root directory of your MIR-1K dataset
    mir1k_dir = r'MIR-1K'
    
    train_path, valid_path, test_path = mir1k_train_test_split(
        mir1k_dir=mir1k_dir, 
        train_valid_test_ratio=[0.8, 0.1, 0.1], 
        random_seed=0
    )
    
    print(f"Train file created at: {train_path}")
    print(f"Validation file created at: {valid_path}")
    print(f"Test file created at: {test_path}")