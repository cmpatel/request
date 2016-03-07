import requests

url = "https://sj-dmz-test"
cookie = {
    "__RequestVerificationToken": "Hy5EzUYwr-M6eb8282Jne8oEZlsopVF3AEG1-hHiXIg7bN3G58CJnhr39M87W2mN0t7hBGXP0Abp-nziPG3QCqW7G9fVPx8_BF1jFW0Wy2I1"}

r1 = requests.post("https://sj-dmz-test/Account/Login?ReturnUrl=%2F", cookies=cookie, verify=False,
                  auth=('superadmin', '@Dm1n4aCp'))
r2 = requests.post("https://sj-dmz-test/Account/Notification?returnUrl=%2F", cookies=r1.cookies, verify=False,
                  auth=('superadmin', '@Dm1n4aCp'))
r3 = requests.get("https://sj-dmz-test/", cookies=r2.cookies, verify=False, auth=('superadmin', '@Dm1n4aCp'))
