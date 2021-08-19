# IIR新生訓練Django_HW
## 建置 Django - docker
* Dockerfile ：
```
FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN pip install pip -U

ADD requirements.txt /code/

RUN pip install -r requirements.txt

ADD . /code/
```
* docker-compose.yaml ：
```
web:
  build: .
  environment:
    MYENV: EXAMPLE
  volumes:
    - .:/code
web_migrate:
  extends:
    service: web
  command: python manage.py migrate
web_run:
  extends:
    service: web
  command: python manage.py runserver 0.0.0.0:8000
  ports:
    - "8000:8000"
```
* requirement ：
```
django==2.2
pandas==1.1.5
```
## docker使用流程
### 1. 於終端機輸入
```
git clone https://github.com/Chei-YuanChi/Django_HW.git
cd Django_hw
docker-compose up -d --build
```
### 2. 連線至 ( http://localhost:8000/recommender/index/ )
### 3. remove container
```
docker-compose down
```
### 4. model weight 儲存於 movie_recommender.h5

## 網頁使用說明
### 1. 主頁( Home ) ：
#### * 顯示各分頁可以做的事：
![](https://i.imgur.com/RPLG8Pd.png)
#### * 左側點擊可進入各分頁
![](https://i.imgur.com/hjuyheJ.png)
#### * Toggle Menu ： 顯示或隱藏左側按鈕
#### *Home ： 回到主頁面
### 2. Get list ： 輸入欲 insert 至資料庫之資料數量 並 output 所有在資料庫中的資料(若欲輸入之資料已在資料庫中則跳過)
### 3. Delete ： 輸入 userId 以及 movieId 若在資料庫中則刪除
### 4. Watched movies ： 輸入指定 userId 並 output 其在資料庫中看過的電影
### 5. Modify ： 輸入 userId, movieId, rating 若 userId 及 movieId 在資料庫中則修改其對應的 rating 為輸入之 rating 值
### 6. Recommend ： 輸入指定 userId 並為其推薦 2 部電影
