#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 必要なライブラリをインポート
import sys
import pickle
import numpy as np
import matplotlib.pyplot as plt
import load_dataset
import os
import sys
sys.path.append(os.path.abspath("../gakusyu_library"))
from network import TwoLayerNetwork


# データセットを読み込む
dataset = load_dataset.load_dataset()
# 訓練画像を取り出す
train_image = dataset['train_image']
# 訓練画像のラベルを取り出す
train_label = dataset['train_label']

# 定義したネットワークをインスタンス化
network = TwoLayerNetwork(10)

# 保存されたパラメータを読み込む
with open('tegaki.weights', 'rb') as web:
    params = pickle.load(web)
# パラメータをモデルに適用する
network.load_parameter(params)

# ランダムに訓練データを1枚を選択
mask = np.random.choice(train_image.shape[0], 1)
image_batch = train_image[mask]
label_batch = train_label[mask]

def key_press(event):
    """
    キー入力されたとき、予測を開始する関数
    """

    # wキーを押したとき、予測を開始する
    if event.key == "w":
        # 選択した訓練データに対して予測
        predict_label = network.predict_label(image_batch)
        print("---------------------")
        for i in range(10):
            print("数字{0}:　{1:.0f}%".format(i,predict_label[0][i]*100))
        print("---------------------")
        print("予測結果: {0}".format(np.argmax(predict_label, axis=1)[0]))
        print("入力画像の正解ラベル: {0}".format(np.argmax(label_batch, axis=1)[0]))


# 入力画像を表示
print("入力画像を表示します.")
print("キーを入力してください.")
print("w: 予測開始, q: 終了")
plt.imshow(image_batch.reshape(28,28), cmap='gray')
plt.xticks(color="None")
plt.yticks(color="None")
plt.tick_params(length=0)
plt.connect('key_press_event',key_press)
plt.show()
