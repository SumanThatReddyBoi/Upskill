import time
import pyotp as otp
import qrcode as code

secret_key = otp.random_base32()
temp_otp_auth=otp.totp.TOTP(secret_key).provisioning_uri(
    name='Suman Reddy',
    issuer_name='Personal Authenticator Project'
)

print(temp_otp_auth)

#QR Code Generated (Only needed for initialization)
#code.make(temp_otp_auth).save("otp.png") 


code = otp.TOTP(secret_key)

while True:
    print(code.verify(input("Enter the Code: ")))