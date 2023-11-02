# Downloading, Unzipping and Extracting the " LibriSpeech Dataset "
# URL : 'https://www.openslr.org/12/'

import requests
import tarfile
import os
from tqdm import tqdm

# Define the URLs of the files
urls = [
    'https://www.openslr.org/resources/12/train-clean-100.tar.gz',
    'https://www.openslr.org/resources/12/train-clean-360.tar.gz',
    'https://www.openslr.org/resources/12/train-other-500.tar.gz',
    'https://www.openslr.org/resources/12/test-clean.tar.gz',
    'https://www.openslr.org/resources/12/test-other.tar.gz'
]

# Define the desired filenames
desired_files = [
    'train-clean-100.tar.gz',
    'train-clean-360.tar.gz',
    'train-other-500.tar.gz',
    'test-clean.tar.gz',
    'test-other.tar.gz'
]

# Create a directory to store the downloaded files
download_dir = 'data'
os.makedirs(download_dir, exist_ok=True)

# Iterate over the URLs and desired filenames
for url, filename in zip(urls, desired_files):
    print(f'Downloading {filename}...')
    
    # Download the file
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)
    
    with open(os.path.join(download_dir, filename), 'wb') as f:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            f.write(data)
    progress_bar.close()
    
    print(f'{filename} downloaded.')

    print(f'Extracting {filename}...')
    
    # Extract the file
    with tarfile.open(os.path.join(download_dir, filename), 'r:gz') as tar:
        total_members = len(tar.getmembers())
        progress_bar = tqdm(tar.getmembers(), total=total_members)

        for member in progress_bar:
            progress_bar.set_description(f"Extracting {member.name}")
            tar.extract(member, path='./LibriSpeech')

        progress_bar.close()
        
    print(f'{filename} extracted.')

print('All files downloaded and extracted successfully.')

