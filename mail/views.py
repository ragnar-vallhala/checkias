from rest_framework import status, views
from rest_framework.response import Response
from .models import OTP
from .serializers import OTPSerializer
import smtplib, random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email account credentials
smtp_server = 'smtp.gmail.com'
smtp_port = 587
username = ''  # fill sender code
password = ''  # fill sender passcode
sender_email = ''

def generate_new_otp(length=4):
    """Generate a new OTP with a specified length."""
    digits = '0123456789'
    otp = ''.join(random.choice(digits) for _ in range(length))
    return otp

def sendmail(receiver_email, body):
    try:
        # Create the email message
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = receiver_email
        message['Subject'] = 'Your OTP Code'
        message.attach(MIMEText(body, 'plain'))
        
        # Connect to the server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(username, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            
    except Exception as e:
        print(f"Error sending email: {e}")
        return "not-sent"
    return "sent"

class CreateOTPView(views.APIView):
    def post(self, request, *args, **kwargs):
        # [Ashu] python debug support
        import pdb; pdb.set_trace()
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        email = email.lower()  # Ensure email is lowercase

        # Mark any existing OTP as deleted
        OTP.objects.filter(email=email, is_deleted=False).update(is_deleted=True)
        
        # Generate and save new OTP
        otp = generate_new_otp()
        otp_instance = OTP.objects.create(email=email, otp=otp)
        
        # Send OTP email
        email_body = f'Your OTP code is {otp}. It is valid for 10 minutes.'
        # [Ashu] commented bottom line to avoid sending mail
        print(email_body)
        #sendmail(receiver_email=email, body=email_body)
        
        return Response({'message': 'OTP sent successfully'}, status=status.HTTP_200_OK)

class ValidateOTPView(views.APIView):
    def post(self, request, *args, **kwargs):
        # [Ashu] python debug support
        import pdb; pdb.set_trace()
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            # [Ashu] checking validation status
            print("[ValidateOTPView]:",email,otp)
            
            try:
                otp_instance = OTP.objects.get(email=email, otp=otp, is_deleted=False)
                if otp_instance.is_valid():
                    return Response({'message': 'OTP is valid'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'OTP has expired'}, status=status.HTTP_400_BAD_REQUEST)
            except OTP.DoesNotExist:
                return Response({'error': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
