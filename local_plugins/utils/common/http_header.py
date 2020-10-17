from random import choice
from string import ascii_uppercase, digits

class Header:
    class Key:
        ACCEPT = 'Accept'
        APP_CODE = 'appCode'
        AUTHORIZATION = 'Authorization'
        AUTHORIZATION_MEDIUM = 'AUTHORIZATION_MEDIUM'
        BASIC = 'Basic '
        BEARER = 'Bearer '
        CACHE_CONTROL = 'cache-control'
        CALLER_ID = 'Caller-Id'
        COOKIE = 'cookie'
        CHANNEL = 'Channel'
        CONTENT_TYPE = 'Content-Type'
        CORRELATION_ID = 'Correlation-Id'
        DELIVERY_METHOD = 'Delivery-Method'
        DEVICE_ID = 'Device-Id'
        DEVICE_ID_WSO2_IS = 'Device_ID'
        DEVICE_INFO = 'Device-Info'
        DEVICE_OS = 'Device-OS'
        DEVICE_NAME = 'Device-Name'
        TIME_STAMP = 'Timestamp'
        USER_AGENT = 'User-Agent'
        CONNECTION = 'Connection'

    class Value:
        APPLICATION_JSON = 'application/json'
        APPLICATION_JSON_UTF8 = 'application/json;charset=UTF-8'
        APPLICATION_WWW_FORM = 'application/x-www-form-urlencoded;charset=UTF-8'
        APPLICATION_WWW_FORM_UTF8 = 'application/x-www-form-urlencoded'
        CLIENT_CREDENTIALS = 'client_credentials'
        DEFAULT_DELIVERY_METHOD = 'SMS'
        DEFAULT_SESSION_ID = '1d948834-a1de-11e7-abc4-cec278b6b50a'
        DEFAULT_CORRELATION_ID = '96dc6517-b024-4ec4-9437-fa4b00bc7a7d'
        NO_CACHE = 'no-cache'
        SMS = 'SMS'
        TEXT_PLAIN = 'text/plain'
        TEXT_XML = 'text/xml'
        DEFAULT_TIMESTAMP = '2019-12-02'
        TIMESTAMP = '1564110825220'
        KEEP_ALIVE = 'keep-alive'

        class Device:
            ID_DEVICE = ''.join(choice(ascii_uppercase + digits) for _ in range(8))

            DEFAULT_OS_ANDROID = '7.0'
            DEFAULT_ID_ANDROID = '09909'
            DEFAULT_NAME_ANDROID = 'unknown Android SDK built for x86'
            DEVICE_SMART_APP_INFO = \
                'eyJkZXZpY2VfaWQiOiJFTVVMQVRPUjMwWDBYNVgwIiwiZGV2aWNlX25hbWUiOiJ1bmtub3duIEFuZHJvaWQgU0RLIGJ1aWx0IGZvciB4O' \
                'DYiLCJkZXZpY2Vfb3MiOiJBbmRyb2lkIDYuMCIsImZpcmViYXNlX2lkIjoiNzdiMDAxZDM5MjdhMTU3ZWZkM2M4ODdlNWJiODY3NmEiLCJnZ' \
                'W9sb2NhdGlvbiI6IiIsIm1hYyI6IiIsInNpbV9pbmZvIjpbeyJpbWVpIjoiMzU4MjQwMDUxMTExMTEwIiwiaW1zaSI6IjMxMDI2MDAwMDAw' \
                'MDAwMCIsIm5ldHdvcmsiOiJBbmRyb2lkIiwic2ltX2lkIjoiODkwMTQxMDMyMTExMTg1MTA3MjAifV0sInZlcnNpb24iOiIxLjE1LjEifQ=='

            DEVICE_USSD_INFO = \
                'eyJkZXZpY2VfaWQiOiJjZTAzMTcxM2FiNWFiZDJiMDEiLCJkZXZpY2VfbmFtZSI6InNhbXN1bmcgU00tRzk1MEYiLCJkZXZpY2Vfb3MiOi' \
                'JBbmRyb2lkIDkiLCJnZW9sb2NhdGlvbiI6IjEwLjgwMDU4MzUsMTA2LjcwNjA5MTQiLCJtYWMiOiI4QzpGNTpBMzpFQjozNTpEMSIsInNp' \
                'bV9pbmZvIjpbeyJpbWVpIjoiMzU4MDYwMDgwMDg0NDM5IiwiaW1zaSI6IjQ1MjA0MDA0MDQ0OTU2OCIsIm5ldHdvcmsiOiJWaWV0dGV' \
                'sIiwic2ltX2lkIjoiODk4NDA0ODAwMDA0MDQ0OTU2ODMifV19'

            DEVICE_INFO = \
                'eyJkZXZpY2VfaWQiOiI1MTVlNDU1OCIsImRldmljZV9uYW1lIjoic2Ftc3VuZyBTTS1QNTU1IiwiZGV2aWNlX29zIjoiQW5kcm9pZCA' \
                '3LjEuMSIsImdlb2xvY2F0aW9uIjoiIiwibWFjIjoiMDI6MDA6MDA6MDA6MDA6MDAiLCJzaW1faW5mbyI6W3siaW1laSI6IjM1OTg5OT' \
                'A2MjUzNTU0OSIsImltc2kiOiIiLCJuZXR3b3JrIjoiIiwic2ltX2lkIjoiIn1dfQ=='
