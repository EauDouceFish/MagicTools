import requests
import argparse


# 查询IP信息的函数（使用ipinfo.io）
def get_ip_info_from_ipinfo(ip_address):
    try:
        response = requests.get(f"http://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error querying ipinfo.io: {e}")
        return None


# 查询IP信息的函数（使用ip-api.com 作为备用）
def get_ip_info_from_ipapi(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception as e:
        print(f"Error querying ip-api.com: {e}")
        return None


# 主函数，用于从命令行获取IP并返回查询信息
def main():
    # 使用 argparse 解析命令行参数
    parser = argparse.ArgumentParser(description="Query IP address information.")
    parser.add_argument("ip_address", help="The IP address to query")
    args = parser.parse_args()

    ip_address = args.ip_address

    # 尝试通过 ipinfo.io 获取 IP 信息
    ip_info = get_ip_info_from_ipinfo(ip_address)

    # 如果 ipinfo.io 查询失败，使用 ip-api.com 作为备用
    if ip_info is None:
        print("ipinfo.io query failed, trying ip-api.com...")
        ip_info = get_ip_info_from_ipapi(ip_address)

    # 如果还没有结果，返回错误信息
    if ip_info:
        print("\nIP Information:")
        for key, value in ip_info.items():
            print(f"{key}: {value}")
    else:
        print(f"Unable to retrieve information for IP {ip_address}")


if __name__ == "__main__":
    main()
