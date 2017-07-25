
train_dir = '/SegNet/segnet_fmri2/train.txt'
test_dir = '/SegNet/segnet_fmri2/test.txt'

file_train = open(train_dir, 'w')
file_test = open(test_dir, 'w')

for i in range(1, 4097):

    file_train.write('/home/philex/Data/dataset/train_data/%s.png /home/philex/Data/dataset/train_label/%s.png'
                     % (str(i), str(i)))
    file_train.write('\n')

    if i < 513:
        file_test.write(r'/home/philex/Data/dataset/test_data/%s.png /home/philex/Data/dataset/test_label/%s.png'
                     % (str(i ), str(i)))
        file_test.write('\n')