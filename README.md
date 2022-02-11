### env
- `python3 -m venv .dots`
- `source .dots/bin/activate`
- `pip3 install --upgrade pip`
- `pip3 install -r requirements.txt`

### how to 
- put mp4 file in `./video`
- run `pick_flame.py (-f video_name)` to make normal_images
- run `make_dots.py (-f video_name)` to make dot_images
- run `connect_pict.py (-f video_name)` to make dot_movie

### notice
1920x1080では267枚がpick_flame上限  
面倒なので、1280x720を参照

### dir
```
make_dot_videos
├── README.md
├── requirements.txt
│
├── pick_flame.py
├── make_dots.py
├── connect_pict.py
├── eraser.py
│
├── video
├── output
└── images
    ├── normal_image
    └── dot_image
```
