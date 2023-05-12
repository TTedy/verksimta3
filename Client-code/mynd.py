import asyncio
import imgbbpy
import requests


async def main():
    client = imgbbpy.AsyncClient('cf4ef37cff62db61d6fb5bd95d46630a')
    image = await client.upload(file='l')
    thecard =image.url
    return thecard

def paste(thecard):
    api_dev_key = "YFC16kpR5u9tTJ2DOI52pyMcTANvV3b0"
    api_user_key = "d7d1bc50a9f63e7e91349f69fdc27dbcY"
    api_paste_key = "https://pastebin.com/6u3TheGv"
    data = {
        "api_option": "paste",
        "api_dev_key": api_dev_key,
        "api_user_key": api_user_key,
        "api_paste_key": api_paste_key,
        "api_paste_code": thecard
    }

    # Send the request to update the paste
    response = requests.post("https://pastebin.com/api/api_post.php", data=data)

    # Check the response status
    if response.status_code == requests.codes.ok:
        print("The paste was successfully updated!")
    else:
        print("An error occurred while updating the paste.")

cards = asyncio.run(main())
paste(cards)

