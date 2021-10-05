#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image
import os
import shutil
import random

dataset_name = "tegaki_dataset"
dirnames = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
original_dirname = "original_images"
train_dirname = "train_dataset"
test_dirname = "test_dataset"

train_choice = ["001", "002", "003", "005", "007", "008", "009", "010"]
test_choice = ["004", "006"]

# 水増しする枚数を指定
mizumashi_num = 50

def resize_mizumashi(img):
    rotated_img = img.convert('RGBA').rotate(random.randint(-10, 10))
    kasamashi_img = Image.new('RGBA', rotated_img.size, (255,) * 4)
    kasamashi_img = Image.composite(rotated_img, kasamashi_img, rotated_img)
    kasamashi_img = kasamashi_img.convert(img.mode)
    kasamashi_img = kasamashi_img.resize((28, 28))
    return kasamashi_img

# ディレクトリ作成
if(os.path.exists(dataset_name)):
    shutil.rmtree(dataset_name)
os.makedirs("{}".format(dataset_name))

# 学習用画像
print("学習用データセットを作成中")
os.makedirs("{}/{}/".format(dataset_name, train_dirname))
for dirname in dirnames:
    print("  「{}」ディレクトリからデータ作成中".format(dirname))
    files = os.listdir("{}/{}/".format(original_dirname, dirname))
    os.makedirs("{}/{}/{}".format(dataset_name, train_dirname, dirname))
    for file in files:
        img = Image.open("{}/{}/{}".format(original_dirname, dirname, file))
        if(os.path.splitext(os.path.basename(file))[0] in train_choice):
            for i in range(mizumashi_num):
                kasamashi_img = resize_mizumashi(img)
                kasamashi_img.save("{}/{}/{}/M{}_{}".format(dataset_name, train_dirname, dirname, str(i), file))

# テスト用画像
print("テスト用データセットを作成中")
os.makedirs("{}/{}/".format(dataset_name, test_dirname))
for dirname in dirnames:
    print("  「{}」ディレクトリからデータ作成中".format(dirname))
    files = os.listdir("{}/{}/".format(original_dirname, dirname))
    os.makedirs("{}/{}/{}".format(dataset_name, test_dirname, dirname))
    for file in files:
        img = Image.open("{}/{}/{}".format(original_dirname, dirname, file))
        if(os.path.splitext(os.path.basename(file))[0] in test_choice):
            for i in range(mizumashi_num):
                kasamashi_img = resize_mizumashi(img)
                kasamashi_img.save("{}/{}/{}/M{}_{}".format(dataset_name, test_dirname, dirname, str(i), file))
print("データセットの作成が完了しました。")