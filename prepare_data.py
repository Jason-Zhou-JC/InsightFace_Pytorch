from pathlib import Path
from config import get_config
from data.data_pipe import load_bin, load_mx_rec
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='for face verification')
    parser.add_argument("-r", "--rec_path", help="mxnet record file path",default='faces_webface', type=str)
    parser.add_argument("-s", "--save_path", help="save path", default='/home/jason/Datasets/InsightFace/faces_webface_112x112', type=str)
    parser.add_argument("-i", "--img_path", help="img path", default='/home/jason/Datasets/InsightFace', type=str)

    args = parser.parse_args()
    conf = get_config()
    rec_path = conf.data_path/args.rec_path
    
    # load_mx_rec(rec_path)
    save_path = Path(args.save_path)
    load_mx_rec(rec_path, save_path, 0)
    
    # bin_files = ['agedb_30', 'cfp_fp', 'lfw', 'calfw', 'cfp_ff', 'cplfw', 'vgg2_fp']
    bin_files = ['lfw', 'calfw', 'cplfw']
    img_path = Path(args.img_path)
    for i in range(len(bin_files)):
        # load_bin(rec_path/(bin_files[i]+'.bin'), rec_path/bin_files[i], conf.test_transform)
        load_bin(rec_path/(bin_files[i]+'.bin'), rec_path/bin_files[i], conf.test_transform, img_path/(bin_files[i]+'_112x112'))
