# 这个东西是什么 What  
- 这些是一系列好用的工具，通常为Python/.bat文件，满足了开发中的简单需求。  
- These are a series of useful Python tools that meet simple needs during development.

# 目前有的工具  
## BuildFileTree.py
- 在总目录下运行脚本，可以输出一个文件夹目录树。用于向人工智能提问、总览项目结构。  
- 提供完整输出模式（容易输出过多）/仅输出文件夹模式（易于提问）
- 可添加到环境变量中，以在任意目录终端下使用命令行控制，例如 buildft -c, buildft -s 直接生成，无需复制脚本
- Run the script in the root directory to output a folder tree, useful for AI queries and project overview.  
- Supports full output mode (may be too verbose) / folder-only mode (better for prompting).
- Supports adding to system PATH to allow powershell's control, using command such as buildft -c, buildft -s to generate the directory_structre at any folder, no needing for copying the script

## ip.py + ip.bat  
- 配合bat文件调用，以让命令行输入如(ip 8.8.8.8)以获取目标ip的基础信息  
- Use with a .bat file so you can run commands like `ip 8.8.8.8` in terminal to get basic IP info.

## deploy.bat
- Hexo框架下配套的简单批处理脚本，用于一键推送博客、查看博客状态
- Use .bat script to simplify deploying the blog and running the website within the Hexo frame.
