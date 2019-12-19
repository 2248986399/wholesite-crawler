## wholesite-crawler

本项目的缘起是由于查询 `文化大革命时期` 中使用到的大字报及官方通告等宣传物料，于是通过 Google 发现 https://ccradb.appspot.com/ 和 [无产阶级图书馆](https://library.proletarian.me/download.php?link=books%2F58eebcc7f061d4789fb2757c1c9b964e.zip&book=%E4%B8%AD%E5%9B%BD%E6%96%87%E5%8C%96%E5%A4%A7%E9%9D%A9%E5%91%BD%E6%96%87%E5%BA%93) 分别提供全文阅览及光盘版下载，但考虑到第一个站 appspot 已被 GFW 认证，而第二个站则需要 Windows 操作系统(本人Macos)，使用和查询并不方便，于是想到了将其全站下载并开放在 Github 方便其他人查询使用。

因此诞生了本项目，如果熟悉 Python 和 Scrapy，写一个爬虫，只需要十几行代码，耗时半小时到若干小时不等，再配合 Gohugo 等静态网站生成器，可以很方便的利用 Github Pages 生成一个全新的没有被 GFW 认证的网站。


通过此工具爬取的整站目前有如下几个

欢迎各位添加新的爬虫

## 已有爬虫

1. ccradb 中国文化大革命文库 https://speechfree.github.io/cultural-revolution-database/ 
2. xys 新语丝 https://speechfree.github.io/xys/
3. letscorp 墙外楼 https://speechfree.github.io/letscorp/

## 开发

开发本项目需要安装 Docker, docker-compose 等基础工具，将项目 clone 到本地后 `make dev` 及启动 crawler 容器，然后通过 `docker exec -it crawler bash` 进入容器，运行 `scrapy crawl letscorp` 运行相应的爬虫



