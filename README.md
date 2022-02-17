### env
- `python3 -m venv .dots`
- `source .dots/bin/activate`
- `pip3 install --upgrade pip`
- `pip3 install -r requirements.txt`

### how to 
- put mp4 file in `./video`  
    ex. `./video/sample.mp4`
- run `run.py`  
    ex. `python3 run.py -f sample`
- three mp4 file in `./output`  

### notice
`./video`直下のmp4ファイルをすべて取得し、600fのドット動画に変換する。  
1920x1080では267imagesがmake_dots処理上限のため、1280x720を推奨。  
先頭600f以降のデータは棄却される。  
### dir
```
make_dot_videos
├── README.md
├── requirements.txt
│
├── run.py
├── utils/
│   ├── pick_flame.py
│   ├── make_dots.py
│   ├── connect_pict.py
│   └── eraser.py
│
├── video/
├── output/
└── images/
    ├── normal_image/
    └── dot_image/
```
