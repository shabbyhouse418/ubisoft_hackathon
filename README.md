# 这是一个简要的项目介绍

## 概要

这个简单的“小游戏”有两个场景，我们预计对用户场景一的表现，即点击偏好进行处理，给用户的场景二进行偏好上的推荐。

## 背景

1. 开放、半开放的游戏场景中可交互的互动元素非常多
2. 用户对某些可交互的互动元素有特定的偏好
3. 单人脱机游戏

## 算法

目标：基于用户的协同过滤

用户数据集通过模拟2500位用户行为产生



# Leslie Shang 文件夹

recommendation.py 推荐算法代码

Sqlite.py 连接Sqlite数据库,对数据文件进行读写操作

main.py 主运行程序(watchdog监控文件目录变化,若数据库文件变化则进行推荐更新,并写入数据库文件)

# unity 文件夹

Prototype.unitypackage 仅包含游戏原型项目的所有内容，不包含数据处理内容

使用方法：

1、使用Unity3D将所有文件导入

2、将Test_DATA、SampleScene、SampleScene_null三个场景添加进Build Settings...

3、使用16:9的分辨率运行以达到最好效果

# unity/GameCode_12.15.2019 文件夹

GameManager.cs 游戏主要逻辑循环的实现，生成游戏的主场景（Test_DATA）

click.cs/click1.cs/click2.cs/click3.cs 不同点击事件逻辑的处理

GM_END.cs 控制游戏的SampleScene场景的逻辑和场景物品的初始化生成

GM_INI.cs 控制游戏的SampleScene_null场景的逻辑和场景物品的初始化生成
