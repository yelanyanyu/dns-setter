# dns-setter

[yelanyanyu/dns-setter (github.com)](https://github.com/yelanyanyu/dns-setter)

# 基本介绍

一个简易的 dns 设置的小工具，免除 dns 设置的烦恼。

# 未来更新计划

- [ ] 支持命令行参数设置指定网络的 dns 服务器（全部网络一键覆盖，指定单一、多个网络设置）。如果不指定该参数，则进行默认设置；
- [ ] 支持命令行参数的 dns 服务器优选，优先选择国内延迟最小的 dns 服务器，然后保存在 json 中。

# 基本使用
## 下载
下载最新的 [Releases · yelanyanyu/dns-setter (github.com)](https://github.com/yelanyanyu/dns-setter/releases/) 中的 `dns-setter.zip`，然后解压在任意目录。
文件的目录结构为：
```text
dns-setter-v1.0.0
    ├─bin
    │      dns-setter.exe
    │      
    └─config
            dns_server.json
            settings.json
```

点击 `dns-setter.exe` 即可运行程序。

## 配置
### dns 服务器
用户可以在 config 目录的 `dns-server.json` 配置自定义的 dns 服务器。

```json
{
  "primary": "223.5.5.5",
  "secondary": "10.1.1.9",
  "others": [
    "223.6.6.6"
  ]
}
```

其中，`primary` 是第一地址，`secondary` 是第二地址，以此类推。

### 配置默认生效的网络
用户可以在 config 目录下的 `settings.json`  中进行配置。

```json
{  
  "default_interfaces_name": [  
    "以太网",  
    "WLAN"  
  ]  
}
```

在以上配置中，我们在 `dns-server.json` 中配置的 dns 服务器将在网络名称 `以太网`、`WLAN` 的网络生效。