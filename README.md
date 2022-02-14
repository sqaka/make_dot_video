### env
- `python3 -m venv .dots`
- `source .dots/bin/activate`
- `pip3 install --upgrade pip`
- `pip3 install -r requirements.txt`

### how to 
- put mp4 file in `./video`
    ex. `./video/sample.mp4`
- run `run.py -f [video_name without(.mp4)]`
    ex. `python3 run.py -f sample`
- two mp4 file in `./output`
    ex. `./output/sample_k4.mp4` and `./output/sample_k16.mp4`

### notice
1920x1080では267枚がpick_flame上限  
1280x720を推奨。先頭600f以降は棄却

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
