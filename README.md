# robosys_ROS

# ライセンス概要

This repository is licensed under the BSD-3-Clause license, see LICENSE.

# 課題概要

講義で利用したプログラムになります。<br>
Tera Termを3つのウィンドウで開き,<br>

$rosrun mypkg count.py <br>

$rourun mypkg twice.py <br>

$rostopic echo /twice <br>

以上の3種類のコマンドをすべて別々のウィンドウで実行すると,　<br>
$rostopic echo /twice を実行したウィンドウで<br>
count_upから出された値を2倍したものをどんどん足し合わせて表示します。<br>

# ファイルの位置

$/catkin_ws/src/mypkg/scripts/count.py <br>
$/catkin_ws/src/mypkg/scripts/twice.py <br>

# 操作方法

$ roscore & <br>
$ cd catkin/catkin_ws/src/mypkg/scripts/
$ sudo chmod 766 count.py <br>
$ sudo chmod 766 twice.py <br>
$ rosrun mypkg count.py <br>
$ rosrun mypkg twice.py <br>
$ rostopic echo /twice <br>
 
最後の三行はすべて別々のウィンドウのTera Termで実行 <br>

# 動画URL
https://twitter.com/owner_king_74/status/1221388605546885120?s=20 <br>
