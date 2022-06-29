import os, shutil

def makedir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
def select_txt(
                          labels_dir,
                          labels_train_dir,
                          labels_valid_dir,
                          labels_test_dir,
                          name_train,
                          name_valid,
                          name_test):
    makedir(labels_train_dir)
    makedir(labels_valid_dir)
    makedir(labels_test_dir)
    with open(name_train, "r") as f1:
        for line in f1:
            shutil.copy(os.path.join(labels_dir, line[:-1] + ".txt"),
                        os.path.join(labels_train_dir, line[:-1] + ".txt"))
    with open(name_valid, "r") as f2:
        for line in f2:
            shutil.copy(os.path.join(labels_dir, line[:-1] + ".txt"),
                        os.path.join(labels_valid_dir, line[:-1] + ".txt"))

    with open(name_test, "r") as f3:
        for line in f3:
            shutil.copy(os.path.join(labels_dir, line[:-1] + ".txt"),
                        os.path.join(labels_test_dir, line[:-1] + ".txt"))
    return
if __name__ == "__main__":

    dir_label = r"E:\cats_dogs\kaggle_Dog&Cat\labels\train1"

    dir1_train = r"E:\cats_dogs\kaggle_Dog&Cat\labels\train2"
    dir1_val = r"E:\yolov3_pytorch_last\yolov3_pytorch5\mask_detection\labels\val"



    main_train = r"E:\cats_dogs\kaggle_Dog&Cat\images//train1_name.txt"
    main_val = r"E:\yolov3_pytorch_last\yolov3_pytorch5\mask_detection//val_name.txt"

    select_txt(
        labels_dir,
        labels_train_dir,
        labels_valid_dir,
        labels_test_dir,
        name_train,
        name_valid,
        name_test)

