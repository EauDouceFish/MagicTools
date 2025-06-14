import re
import sys
import requests
from urllib.parse import urlparse
from pathlib import Path


def download_image(url, save_path):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"[+] 下载成功：{url} -> {save_path}")
    except Exception as e:
        print(f"[!] 下载失败：{url}，原因：{e}")


def find_hexo_root(md_path: Path):
    cur_path = md_path.parent
    while cur_path != cur_path.parent:
        if (cur_path / "source" / "_posts").exists() and (cur_path / "public").exists():
            return cur_path
        cur_path = cur_path.parent
    return None


def process_markdown(md_path: Path):
    if not md_path.exists():
        print(f"[!] 文件不存在: {md_path}")
        return

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    pattern = r'!\[([^\]]*)\]\((https?://[^\)]+)\)'

    matches = list(re.finditer(pattern, content))
    if not matches:
        print("[*] 没有找到远程图片链接。")
        return

    category_match = re.search(r'categories:\s*\["?([\w\-]+)"?]', content)
    category = category_match.group(1) if category_match else "uncategorized"

    hexo_root = find_hexo_root(md_path)
    if not hexo_root:
        print("[!] 未找到 Hexo 根目录，确保项目包含 source/_posts 和 public 文件夹")
        return

    img_folder_name = md_path.stem
    img_save_dir = hexo_root / "source" / "img" / category / img_folder_name
    img_save_dir.mkdir(parents=True, exist_ok=True)

    img_counter = 1

    def replace_match(match):
        nonlocal img_counter
        alt_text = match.group(1)
        url = match.group(2)

        parsed = urlparse(url)
        suffix = Path(parsed.path).suffix or ".png"
        filename = f"{img_folder_name}_{img_counter:03d}{suffix}"
        img_counter += 1

        local_img_path = img_save_dir / filename
        relative_img_path = f"/img/{category}/{img_folder_name}/{filename}"

        if not local_img_path.exists():
            download_image(url, local_img_path)
        else:
            download_image(url, local_img_path)
            print(f"[✓] 已存在，覆盖下载：{local_img_path}")

        return f"![{alt_text}]({relative_img_path})"

    content = re.sub(pattern, replace_match, content)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n[✓] 已完成处理：{md_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python Yuque2Hexo.py <md文件路径>")
    else:
        md_file = Path(sys.argv[1]).resolve()
        process_markdown(md_file)
