### env
- `python3 -m venv .dots`
- `source .dots/bin/activate`
- `pip3 install --upgrade pip`
- `pip3 install -r requirements.txt`

### how to 
- put mp4 file in `./video`
- run `run.py -f (video_name without [.mp4])`
- two mp4 file in `./output`

### notice
1920x1080では267枚がpick_flame上限  
1280x720を推奨。pick上限を600fに設定

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
