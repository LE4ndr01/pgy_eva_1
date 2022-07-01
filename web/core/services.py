from django_otp import devices_for_user
from django_otp.plugins.otp_totp.models import TOTPDevice

class UtilsOTP:
    @classmethod
    def get_user_totp_device(cls,user,confirmed=None):
        devices = devices_for_user(user,confirmed=confirmed)
        for device in devices:
            if isinstance (device,TOTPDevice):
                return device