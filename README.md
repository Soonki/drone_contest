# Project Drone Contest
ドローンコンテスト用プログラム

## Description

本プログラムはラズベリーパイゼロW上で動作し、Pixracerと通信する。

## Hardware
- Raspberry Pi Zero W
- Pixracer

## Requirement

- Raspbian Stretch
- Python2 or Python3
- Pymavlink
- OpenCV2


## Install

### Raspberry Pi Zero Setup

- OS Install
- Network Set Up

### Git Setup

```bash
sudo git config --global user.email "${your_email_address}"
sudo git config --global user.name "${your_name}"
```

### Clone Repository

```bash
git clone https://github.com/Soonki/drone_contest.git
```

### Dependency

```bash
pip install pymavlink
pip install opencv-python
```

## Usage

Pixracer、Raspberry Pi、LED、カメラを正しく配線した上でRaspberry Pi上で以下のコマンドを実行する。

```bash
python src/main.py
```

## Test

ユニットテストは未実装である。各クラスの機能テストのみ実装している。testフォルダ内のフォルダ及びクラスを定義しているファイルを直接実行することで機能テストを実行できる。

## Branch

`Git-flow` を採用している。