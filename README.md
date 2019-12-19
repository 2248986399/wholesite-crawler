## wholesite-crawler

本工具主要是用于一些网站的快速抓取及备份，将页面存储撑 markdown 文档，然后利用 Gohugo 等静态页面生成器快速在 Github pages 建立其备份网站。

## 已有爬虫

1. ccradb 中国文化大革命文库
2. xys 新语丝
3. letscorp 墙外楼

## 开发

开发本项目需要安装 Docker, docker-compose 等基础工具，将项目 clone 到本地后 `make dev` 及启动 crawler 容器，然后通过 `docker exec -it crawler bash` 进入容器，运行 `scrapy crawl letscorp` 运行相应的爬虫



