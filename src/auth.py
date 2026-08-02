import requests
from config import CLIENT_ID, CLIENT_SECRET, CHANNEL_NAME

TOKEN_URL = "https://id.kick.com/oauth/token"

def get_access_token():
    data = {
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    try:
        response = requests.post(TOKEN_URL, data=data, headers=headers)

        if response.status_code == 200:
            token = response.json()["access_token"]
            print("✅ Access Token تم الحصول عليه بنجاح")
            return token

        print("❌ فشل الحصول على Access Token")
        print(response.status_code)
        print(response.text)
        return None

    except Exception as e:
        print(f"❌ خطأ: {e}")
        return None


def get_channel_info():
    url = f"https://kick.com/api/v1/channels/{CHANNEL_NAME}"

    try:
        response = requests.get(url)

        if response.status_code != 200:
            print("❌ فشل في جلب بيانات القناة")
            print(response.status_code)
            print(response.text)
            return None

        data = response.json()

        return {
            "channel_id": data["id"],
            "chatroom_id": data["chatroom"]["id"],
            "username": data["user"]["username"]
        }

    except Exception as e:
        print(f"❌ خطأ أثناء جلب بيانات القناة: {e}")
        return None