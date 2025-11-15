import time
import pyotp as otp
import qrcode as code

secret_key = otp.random_base32()
temp_otp_auth=otp.totp.TOTP(secret_key).provisioning_uri(
    name='Suman Reddy',
    issuer_name='Programming Authority'
)

print(temp_otp_auth)

code.make(temp_otp_auth).save("otp.png")
qr = otp.TOTP(secret_key)

code = otp.TOTP(secret_key)

while True:
    print(code.verify(input("Enter the Code: ")))