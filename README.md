# GAN


To get the dataset for training run the following commands. The data is saved in DiscoGAN/datsets folder. You will need to install the required packages as prompted.

python preprocessing/scrape_tshirts.py
pyhton preprocessing/scrape_watches.py
python preprocessing/edgeDetector.py


Alternatively, download the dataset from https://www.dropbox.com/sh/qrvxvzobemfe1sw/AACVPWddWjGyMOqTLSZhjmlza?dl=0 and https://www.dropbox.com/sh/swo1b6da9xfazh8/AAAxxa4mgm2bTaiYoNB7ejDXa?dl=0 and save it in DiscoGAN/datsets folder.

To train tshirts2watches, run
python ./discogan/image_translation.py --task_name='TshirtsToWatches' --starting_rate=0.5

